"""Workflow operations built on the local-first operating kernel."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from kernel import KernelError, OperatingKernel


HANDOFF_STATUSES = {"prepared", "acknowledged", "accepted", "returned", "closed"}


def create_work_package(
    kernel: OperatingKernel,
    project_id: str,
    *,
    objective: str,
    question: str,
    inputs: list[str],
    exclusions: list[str],
    evidence_contract: str,
    acceptance: str,
    owner: str,
    reviewer: str,
    actor: str = "system",
) -> dict[str, Any]:
    return kernel.create(
        "work_package",
        {
            "project_id": project_id,
            "objective": objective,
            "question": question,
            "inputs": inputs,
            "exclusions": exclusions,
            "evidence_contract": evidence_contract,
            "acceptance": acceptance,
            "owner": owner,
            "reviewer": reviewer,
            "status": "proposed",
        },
        actor=actor,
    )


def assign_work_package(
    kernel: OperatingKernel,
    work_package_id: str,
    *,
    owner: str,
    actor: str = "system",
) -> dict[str, Any]:
    work = kernel.get("work_package", work_package_id)
    if not work:
        raise KernelError("Work package does not exist")
    status = work.get("status", "proposed")
    if status == "proposed":
        kernel.update("work_package", work_package_id, {"status": "scoped"}, actor=actor)
        status = "scoped"
    if status != "scoped":
        raise KernelError(f"Work package cannot be assigned from {status}")
    return kernel.update("work_package", work_package_id, {"status": "assigned", "owner": owner}, actor=actor)


def start_work_package(kernel: OperatingKernel, work_package_id: str, *, actor: str = "system") -> dict[str, Any]:
    work = kernel.get("work_package", work_package_id)
    if not work or work.get("status") != "assigned":
        raise KernelError("Only an assigned work package can start")
    return kernel.update("work_package", work_package_id, {"status": "in_progress"}, actor=actor)


def submit_work_package(
    kernel: OperatingKernel,
    work_package_id: str,
    *,
    output_ids: list[str],
    deviations: list[str] | None = None,
    actor: str = "system",
) -> dict[str, Any]:
    work = kernel.get("work_package", work_package_id)
    if not work or work.get("status") != "in_progress":
        raise KernelError("Only an in-progress work package can be submitted")
    return kernel.update(
        "work_package",
        work_package_id,
        {"status": "submitted", "output_ids": output_ids, "deviations": deviations or []},
        actor=actor,
    )


def review_work_package(
    kernel: OperatingKernel,
    work_package_id: str,
    *,
    accepted: bool,
    findings: list[str],
    reviewer: str,
    actor: str = "system",
) -> dict[str, Any]:
    work = kernel.get("work_package", work_package_id)
    if not work or work.get("status") != "submitted":
        raise KernelError("Only a submitted work package can be reviewed")
    reviewed = kernel.update(
        "work_package",
        work_package_id,
        {"status": "reviewed", "reviewer": reviewer, "review_findings": findings},
        actor=actor,
    )
    final_status = "accepted" if accepted else "returned"
    return kernel.update("work_package", work_package_id, {"status": final_status}, actor=actor)


def create_handoff(
    kernel: OperatingKernel,
    project_id: str,
    *,
    sender: str,
    receiver: str,
    work_package_id: str,
    context: str,
    objective: str,
    inputs: list[str],
    exclusions: list[str],
    evidence_contract: str,
    expected_output: str,
    acceptance: str,
    authority: str,
    actor: str = "system",
) -> dict[str, Any]:
    work = kernel.get("work_package", work_package_id)
    if not work or work.get("project_id") != project_id:
        raise KernelError("Handoff work package must exist in the same project")
    handoff = kernel.create(
        "handoff",
        {
            "project_id": project_id,
            "sender": sender,
            "receiver": receiver,
            "work_package_id": work_package_id,
            "context": context,
            "objective": objective,
            "inputs": inputs,
            "exclusions": exclusions,
            "evidence_contract": evidence_contract,
            "expected_output": expected_output,
            "acceptance": acceptance,
            "authority": authority,
            "status": "prepared",
        },
        actor=actor,
    )
    kernel.link(project_id, "handoff", handoff["id"], "addresses", "work_package", work_package_id, actor=actor)
    return handoff


def acknowledge_handoff(
    kernel: OperatingKernel,
    handoff_id: str,
    *,
    accepted: bool,
    acknowledgement: str,
    actor: str = "system",
) -> dict[str, Any]:
    handoff = kernel.get("handoff", handoff_id)
    if not handoff:
        raise KernelError("Handoff does not exist")
    if handoff.get("status") not in {"prepared", "returned"}:
        raise KernelError(f"Handoff cannot be acknowledged from {handoff.get('status')}")
    status = "acknowledged" if accepted else "returned"
    return kernel.update(
        "handoff",
        handoff_id,
        {"status": status, "acknowledgement": acknowledgement},
        actor=actor,
    )


def prepare_gate(
    kernel: OperatingKernel,
    project_id: str,
    *,
    phase: str,
    criteria: list[str],
    evidence_packet: list[str],
    unresolved_conditions: list[str] | None = None,
    actor: str = "system",
) -> dict[str, Any]:
    return kernel.create(
        "gate",
        {
            "project_id": project_id,
            "phase": phase,
            "criteria": criteria,
            "evidence_packet": evidence_packet,
            "unresolved_conditions": unresolved_conditions or [],
            "status": "not_ready",
        },
        actor=actor,
    )


def close_accepted_work_package(
    kernel: OperatingKernel,
    work_package_id: str,
    *,
    actor: str = "system",
) -> dict[str, Any]:
    work = kernel.get("work_package", work_package_id)
    if not work or work.get("status") != "accepted":
        raise KernelError("Only an accepted work package can close")
    return kernel.update("work_package", work_package_id, {"status": "closed"}, actor=actor)


def save_continuation(
    kernel: OperatingKernel,
    project_id: str,
    out_dir: str | Path,
) -> tuple[Path, Path]:
    return kernel.export_continuation(project_id, out_dir)
