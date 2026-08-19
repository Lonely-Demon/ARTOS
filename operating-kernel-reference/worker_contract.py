"""Typed task-package and worker-result contracts for future adapters.

The contract is intentionally transport-neutral. An adapter may use a subprocess,
HTTP, MCP, ACP, message queue, or another protocol, but the kernel-facing shape
remains stable.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


class WorkerContractError(ValueError):
    pass


@dataclass(frozen=True)
class TaskPackage:
    project_id: str
    work_package_id: str
    objective: str
    context: str
    inputs: list[str] = field(default_factory=list)
    exclusions: list[str] = field(default_factory=list)
    evidence_contract: str = ""
    allowed_tools: list[str] = field(default_factory=list)
    allowed_paths: list[str] = field(default_factory=list)
    side_effect_budget: dict[str, Any] = field(default_factory=dict)
    deadline: str | None = None
    acceptance_criteria: list[str] = field(default_factory=list)
    return_format: str = "typed_result_v1"
    authority: str = "worker_only"
    schema_version: str = "task_package_v1"

    def validate(self) -> None:
        required = {
            "project_id": self.project_id,
            "work_package_id": self.work_package_id,
            "objective": self.objective,
            "context": self.context,
            "evidence_contract": self.evidence_contract,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            raise WorkerContractError(f"Task package missing required fields: {', '.join(missing)}")
        if self.authority != "worker_only":
            raise WorkerContractError("Workers cannot receive approval or certification authority")
        if not self.allowed_paths:
            raise WorkerContractError("Task package must state allowed_paths explicitly")
        if not self.side_effect_budget:
            raise WorkerContractError("Task package must state side_effect_budget explicitly")
        if "network" not in self.side_effect_budget:
            raise WorkerContractError("side_effect_budget must state network policy")
        if "external_write" not in self.side_effect_budget:
            raise WorkerContractError("side_effect_budget must state external_write policy")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)


@dataclass(frozen=True)
class WorkerResult:
    project_id: str
    work_package_id: str
    status: str
    summary: str
    artefact_refs: list[str] = field(default_factory=list)
    evidence_refs: list[str] = field(default_factory=list)
    execution_trace_ref: str | None = None
    deviations: list[str] = field(default_factory=list)
    unresolved_risks: list[str] = field(default_factory=list)
    reproducibility: dict[str, Any] = field(default_factory=dict)
    requested_claim_upgrades: list[str] = field(default_factory=list)
    external_side_effects: list[str] = field(default_factory=list)
    schema_version: str = "worker_result_v1"

    def validate(self) -> None:
        if self.status not in {"succeeded", "partial", "failed", "blocked", "cancelled"}:
            raise WorkerContractError(f"Unsupported worker result status: {self.status}")
        if not self.project_id or not self.work_package_id or not self.summary:
            raise WorkerContractError("Worker result requires project_id, work_package_id, and summary")
        if self.requested_claim_upgrades:
            raise WorkerContractError(
                "Workers may report requested claim upgrades, but the adapter must not admit them directly"
            )
        if self.external_side_effects:
            raise WorkerContractError(
                "Unexpected external side effects must be escalated rather than silently accepted"
            )
        if not self.reproducibility:
            raise WorkerContractError("Worker result must include reproducibility metadata")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)


def validate_worker_return(task: TaskPackage, result: WorkerResult) -> dict[str, Any]:
    task.validate()
    result.validate()
    if task.project_id != result.project_id or task.work_package_id != result.work_package_id:
        raise WorkerContractError("Worker result does not match the task package")
    return {
        "task": task.to_dict(),
        "result": result.to_dict(),
        "admission": {
            "canonical_state_write": False,
            "claim_upgrade": False,
            "approval": False,
            "external_side_effect": False,
            "requires_review": True,
        },
    }
