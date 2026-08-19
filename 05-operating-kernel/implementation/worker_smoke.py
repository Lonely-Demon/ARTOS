from __future__ import annotations

import json
from pathlib import Path

from worker_contract import TaskPackage, WorkerContractError, WorkerResult, validate_worker_return


OUT = Path(__file__).parent / "worker-smoke-report.json"


def build_task() -> TaskPackage:
    return TaskPackage(
        project_id="prj_smoke",
        work_package_id="wp_smoke",
        objective="Return a bounded research note.",
        context="Synthetic adapter-boundary smoke test; no external tools or claims.",
        inputs=["local context only"],
        exclusions=["No network", "No repository writes", "No claim upgrades"],
        evidence_contract="Return provenance and limitations.",
        allowed_tools=[],
        allowed_paths=["/workspace/smoke"],
        side_effect_budget={"network": "deny", "external_write": "deny", "filesystem": "scoped"},
        acceptance_criteria=["Typed result returned", "Review required"],
    )


def run() -> dict:
    task = build_task()
    successful = WorkerResult(
        project_id=task.project_id,
        work_package_id=task.work_package_id,
        status="succeeded",
        summary="The bounded worker task completed in the smoke harness.",
        artefact_refs=["local://smoke/result.md"],
        evidence_refs=["local://smoke/trace.json"],
        execution_trace_ref="local://smoke/trace.json",
        reproducibility={"runner": "deterministic-smoke", "input_hash": "fixed", "network": "denied"},
    )
    accepted = validate_worker_return(task, successful)
    rejection_cases = {}
    cases = {
        "claim_upgrade": WorkerResult(
            project_id=task.project_id,
            work_package_id=task.work_package_id,
            status="succeeded",
            summary="Attempts to upgrade a claim.",
            requested_claim_upgrades=["claim_unsafe"],
            reproducibility={"runner": "smoke"},
        ),
        "external_side_effect": WorkerResult(
            project_id=task.project_id,
            work_package_id=task.work_package_id,
            status="succeeded",
            summary="Reports an unapproved side effect.",
            external_side_effects=["sent message"],
            reproducibility={"runner": "smoke"},
        ),
        "identity_mismatch": WorkerResult(
            project_id="other_project",
            work_package_id=task.work_package_id,
            status="succeeded",
            summary="Wrong project result.",
            reproducibility={"runner": "smoke"},
        ),
        "missing_reproducibility": WorkerResult(
            project_id=task.project_id,
            work_package_id=task.work_package_id,
            status="succeeded",
            summary="Missing execution conditions.",
        ),
    }
    for name, result in cases.items():
        try:
            validate_worker_return(task, result)
        except WorkerContractError as exc:
            rejection_cases[name] = {"rejected": True, "reason": str(exc)}
        else:
            rejection_cases[name] = {"rejected": False, "reason": "Unexpected acceptance"}
    report = {
        "test_type": "synthetic worker-contract smoke test",
        "evidence_state": "measured_locally",
        "warning": "This does not execute DeerFlow, OpenHands, Hermes, OpenClaw, or OpenManus and does not measure worker quality.",
        "successful_return_admission": accepted["admission"],
        "rejection_cases": rejection_cases,
        "all_malicious_cases_rejected": all(item["rejected"] for item in rejection_cases.values()),
        "canonical_state_write": accepted["admission"]["canonical_state_write"],
        "claim_upgrade": accepted["admission"]["claim_upgrade"],
        "approval": accepted["admission"]["approval"],
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
