from __future__ import annotations

import json
import sys
from pathlib import Path

IMPLEMENTATION_DIR = Path(__file__).resolve().parents[2] / "implementation"
if str(IMPLEMENTATION_DIR) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION_DIR))

from kernel import OperatingKernel
from workflow import (
    acknowledge_handoff,
    assign_work_package,
    create_handoff,
    create_work_package,
    prepare_gate,
    review_work_package,
    start_work_package,
    submit_work_package,
)

OUT = Path(__file__).parent / "outputs"
DB = OUT / "tabvolt-retrospective.sqlite3"


def create_record() -> tuple[OperatingKernel, str]:
    OUT.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    kernel = OperatingKernel(DB)
    project = kernel.create_project(
        "TabVolt retrospective calibration",
        "Design and build a low-resource browser tab/app energy-optimization capability under a 24-hour offline hackathon constraint.",
        owner="historical-project-record",
        scope="Retrospective mapping of the SSN Vortex 2.0 TabVolt conversation into the Universal Enterprise operating contract.",
        constraints=[
            "24-hour offline hackathon with internet available at venue",
            "Low-spec Windows hardware: Acer Pentium 4GB and Lenovo i3",
            "Phase 1 review before full implementation",
            "Do not present estimated energy or carbon as measured fact",
            "Core should degrade gracefully when optional AI/companion layers fail",
        ],
        actor="calibration",
    )
    project_id = project["id"]
    kernel.update("project", project_id, {"status": "active"}, actor="calibration")

    objective = kernel.create(
        "objective",
        {
            "project_id": project_id,
            "statement": "Produce a polished, working, resource-aware tab optimizer that is defensible under hackathon evaluation.",
            "success_condition": "A bounded demo identifies actionable tab states, performs safe actions, remains usable under constrained hardware, and clearly distinguishes measured behaviour from estimates.",
            "priority": "high",
            "status": "open",
        },
        actor="calibration",
    )

    factors = []
    factor_specs = [
        ("Hardware/resource constraint", "constraint", "High runtime overhead undermines the product’s low-resource positioning.", "must_address", "measured_locally"),
        ("Offline core requirement", "operational", "Cloud-only storage or AI would fail when network access is unreliable.", "must_address", "design_inference"),
        ("Browser API availability", "technical", "chrome.processes was not available on stable channels, overturning the initial exact attribution approach.", "must_address", "measured_locally"),
        ("Energy attribution validity", "epistemic", "Heuristic tab scores are not direct per-tab energy measurements and can be misinterpreted.", "must_acknowledge", "open"),
        ("Unsafe automated action", "safety", "Suspending active, pinned, or audible tabs could disrupt user work or media playback.", "must_address", "measured_locally"),
        ("AI suggestion reliability", "agentic", "A language model may suggest nonexistent, active, or audible tabs unless candidates are structurally constrained.", "must_address", "measured_locally"),
        ("Service-worker lifecycle", "technical", "MV3 background workers may stop or fail during load, making polling and state handling fragile.", "must_address", "measured_locally"),
        ("Competitor and claim boundary", "product", "Existing browser sleeping-tab features make differentiation and evidence boundaries material.", "must_acknowledge", "design_inference"),
    ]
    for statement, category, consequence, treatment, evidence_state in factor_specs:
        factors.append(
            kernel.create(
                "factor",
                {
                    "project_id": project_id,
                    "statement": statement,
                    "category": category,
                    "consequence": consequence,
                    "treatment": treatment,
                    "evidence_state": evidence_state,
                    "status": "open" if evidence_state == "open" else "treated",
                },
                actor="calibration",
            )
        )

    evidence = []
    evidence_specs = [
        {
            "proposition": "Phase 1 tab suspension functioned and a slight CPU/RAM dip was observed by the project participant.",
            "source": "Historical TabVolt conversation, Phase 1 feedback, lines 3111-3114",
            "method": "Participant-observed local test",
            "conditions": "Microsoft Edge, project participant’s machine, historical hackathon context",
            "evidence_state": "measured_locally",
            "limitations": "Single informal observation; no controlled baseline, sample size, instrumentation, or independent replication.",
        },
        {
            "proposition": "chrome.processes was unavailable on stable Chrome/Edge paths used by the project, requiring heuristic estimation.",
            "source": "Historical TabVolt iteration log, lines 3489-3498 and 3560-3564",
            "method": "Observed implementation failure and architectural revision",
            "conditions": "Stable browser channel used in the project",
            "evidence_state": "measured_locally",
            "limitations": "The calibration records the project’s reported environment; current browser support must be rechecked for a new implementation.",
        },
        {
            "proposition": "Filtering active, pinned, and audible tabs before AI prompting reduced unsafe candidate suggestions.",
            "source": "Historical TabVolt iteration log, lines 3518-3526",
            "method": "Implementation design and observed behaviour in the project record",
            "conditions": "Gemini suggestion path with deterministic fallback",
            "evidence_state": "measured_locally",
            "limitations": "No adversarial benchmark or independent review of the safety improvement.",
        },
        {
            "proposition": "The core extension can operate without a companion backend using browser APIs and IndexedDB.",
            "source": "Historical TabVolt architecture decisions, lines 507-521 and 1988-2016",
            "method": "Architecture decision and implementation plan",
            "conditions": "Browser extension-only Phase 1",
            "evidence_state": "design_inference",
            "limitations": "Does not establish cross-browser compatibility, battery benefit, or production reliability.",
        },
        {
            "proposition": "Estimated EnergyScore and carbon conversions must not be presented as direct measured energy or carbon savings.",
            "source": "Historical TabVolt R&D and revision record, lines 1598-1625 and 1845",
            "method": "Feasibility and claim-boundary review",
            "conditions": "Heuristic score and first-principles estimate",
            "evidence_state": "design_inference",
            "limitations": "The claim boundary itself requires validation in a new controlled experiment.",
        },
    ]
    for spec in evidence_specs:
        evidence.append(kernel.create("evidence", {"project_id": project_id, **spec}, actor="calibration"))

    decisions = []
    decision_specs = [
        {
            "question": "What should be the initial product boundary?",
            "options": ["Pure browser extension", "Extension plus Python backend", "Desktop application"],
            "selected_option": "Pure browser extension first, with optional companion later",
            "rationale": "Lowest deployment and resource burden; retains offline core and fastest calibration path.",
            "rejected_alternatives": ["Python backend: higher footprint and extra failure surface for the constrained first slice.", "Desktop app: more scope and less immediate browser demonstration."],
            "authority": "historical project decision",
            "status": "accepted",
        },
        {
            "question": "How should per-tab consumption be represented after exact process attribution fails?",
            "options": ["Claim exact measurement", "Remove all intelligence", "Use heuristic estimation with explicit limits"],
            "selected_option": "Heuristic estimation with explicit limitations",
            "rationale": "Preserves useful prioritisation without misrepresenting estimates as measurement.",
            "rejected_alternatives": ["Exact per-tab energy claim: unsupported after stable-channel API limitation."],
            "authority": "historical project revision",
            "status": "accepted",
        },
        {
            "question": "How should AI actions be constrained?",
            "options": ["Prompt-only exclusions", "Structural candidate filtering plus deterministic fallback", "No AI"],
            "selected_option": "Structural candidate filtering plus deterministic fallback",
            "rationale": "Prevents active, pinned, and audible tabs from entering the action candidate set.",
            "rejected_alternatives": ["Prompt-only exclusions: weaker because the model still receives ambiguous action space."],
            "authority": "historical project revision",
            "status": "accepted",
        },
        {
            "question": "How should tab state be modelled?",
            "options": ["One generic sleep action", "Separate suspended and sleeping states with protected audio/active handling"],
            "selected_option": "Separate suspended and sleeping states with explicit safe targeting",
            "rationale": "Matches different mechanisms and reduces accidental disruption.",
            "rejected_alternatives": ["Generic action: caused ambiguity and unsafe targeting in the early iteration."],
            "authority": "historical project revision",
            "status": "accepted",
        },
    ]
    for spec in decision_specs:
        decisions.append(kernel.create("decision", {"project_id": project_id, **spec}, actor="calibration"))

    risks = []
    risk_specs = [
        ("Heuristic scores may not correlate with actual energy consumption.", "Unavailable exact attribution and changing browser internals.", "Users or judges may infer false precision.", "high", "high", "Label scores as relative estimates; avoid direct savings claims; define calibration experiment.", "open"),
        ("AI may recommend an unsafe tab action.", "Model output or stale tab state.", "Active work or audio may be interrupted.", "medium", "high", "Filter candidates structurally; preserve active/pinned/audible exclusions; deterministic fallback; require review before automated action.", "mitigated"),
        ("Service worker lifecycle may interrupt polling.", "MV3 worker suspension or runtime error.", "Stale UI and missing measurements.", "medium", "medium", "Alarms, immediate boot, lifecycle handlers, session state, and graceful degradation.", "mitigated"),
        ("Resource monitor itself may consume material resources.", "Heavy runtime, polling, rendering, or dependency footprint.", "Contradicts product positioning.", "medium", "medium", "Pure extension first; measure extension footprint locally; optional companion only for unavailable metrics.", "open"),
    ]
    for statement, cause, consequence, likelihood, severity, mitigation, status in risk_specs:
        risks.append(
            kernel.create(
                "risk",
                {
                    "project_id": project_id,
                    "statement": statement,
                    "cause": cause,
                    "consequence": consequence,
                    "likelihood": likelihood,
                    "severity": severity,
                    "mitigation": mitigation,
                    "residual_state": status,
                    "status": status,
                },
                actor="calibration",
            )
        )

    claim_specs = [
        {
            "statement": "The historical Phase 1 implementation demonstrated local tab suspension and a reported CPU/RAM decrease under the tested conditions.",
            "scope": "Historical participant-observed test only",
            "evidence_state": "measured_locally",
            "permitted_wording": "In the recorded local test, TabVolt suspended a tab and the participant observed a slight CPU/RAM decrease.",
            "limitations": "Not a controlled energy study, not independently replicated, and not evidence of general battery savings.",
            "status": "open",
        },
        {
            "statement": "TabVolt measures exact per-tab energy consumption.",
            "scope": "Any public product claim",
            "evidence_state": "excluded",
            "permitted_wording": "Do not make this claim; use relative heuristic estimates unless independently calibrated.",
            "limitations": "Stable browser API limitations and lack of calibrated energy instrumentation.",
            "status": "open",
        },
        {
            "statement": "The AI action path is safer when candidate tabs are structurally filtered before prompting.",
            "scope": "Historical implementation design",
            "evidence_state": "design_inference",
            "permitted_wording": "The design reduces the action space by excluding active, pinned, and audible tabs before prompting.",
            "limitations": "Reduction in risk is not quantified; further adversarial testing is needed.",
            "status": "open",
        },
    ]
    claims = [kernel.create("claim", {"project_id": project_id, **spec}, actor="calibration") for spec in claim_specs]

    for f in factors:
        kernel.link(project_id, "objective", objective["id"], "addresses", "factor", f["id"], actor="calibration")
    for ev in evidence:
        for claim in claims:
            if ("suspension" in claim["statement"].lower() and "suspension" in ev["proposition"].lower()) or (
                "exact per-tab" in claim["statement"] and "estimated" in ev["proposition"].lower()
            ) or ("safer" in claim["statement"] and "filtering" in ev["proposition"].lower()):
                kernel.link(project_id, "evidence", ev["id"], "supports", "claim", claim["id"], actor="calibration")
    for d in decisions:
        for f in factors:
            if any(token in (d["question"] + d["selected_option"]).lower() for token in f["statement"].lower().split()[:2]):
                kernel.link(project_id, "decision", d["id"], "addresses", "factor", f["id"], actor="calibration")
    for r in risks:
        kernel.link(project_id, "decision", decisions[0]["id"], "addresses", "risk", r["id"], actor="calibration")

    work_specs = [
        ("Reconstruct problem, constraints, and evaluation context", "Can the full hackathon objective be framed without conflating demo and product claims?", "frame", "Historical context, constraints, rubric, and stop conditions recorded."),
        ("Map browser/API/stack alternatives", "Which architecture survives low-resource and offline constraints?", "decision_space", "Alternatives, rejected paths, and feasibility limits recorded."),
        ("Implement and test Phase 1 extension slice", "Can a minimal extension demonstrate safe tab actions and local state?", "implementation", "Extension loads, safe action works, and local observations are recorded."),
        ("Revise after browser/API and AI failures", "What changed when exact process attribution and unconstrained AI failed?", "verify_attack", "Architecture pivot, safety filter, lifecycle fixes, and claim boundaries recorded."),
    ]
    works = []
    for objective_text, question, phase, acceptance in work_specs:
        work = create_work_package(
            kernel,
            project_id,
            objective=objective_text,
            question=question,
            inputs=["historical conversation record"],
            exclusions=["Independent energy validation", "Production deployment"],
            evidence_contract="Record source, method, conditions, result, limitations, and affected decision.",
            acceptance=acceptance,
            owner="historical-project-team",
            reviewer="retrospective-calibration",
            actor="calibration",
        )
        work = assign_work_package(kernel, work["id"], owner="historical-project-team", actor="calibration")
        work = start_work_package(kernel, work["id"], actor="calibration")
        work = submit_work_package(kernel, work["id"], output_ids=[f"historical_{phase}"], actor="calibration")
        work = review_work_package(
            kernel,
            work["id"],
            accepted=True,
            findings=["Retrospective record mapped; substantive real-world validity remains outside this calibration."],
            reviewer="retrospective-calibration",
            actor="calibration",
        )
        works.append(work)

    handoff = create_handoff(
        kernel,
        project_id,
        sender="systems-integrator",
        receiver="implementation-worker",
        work_package_id=works[2]["id"],
        context="Retrospective Phase 1 build record",
        objective="Implement only the bounded extension slice under resource and claim constraints.",
        inputs=["architecture decision records", "safe candidate rules"],
        exclusions=["Exact per-tab energy claim", "Unreviewed destructive actions"],
        evidence_contract="Return local test observations and failure limitations.",
        expected_output="Tested local implementation slice",
        acceptance="No unsupported claim upgrades; safe action path is traceable.",
        authority="worker_only",
        actor="calibration",
    )
    acknowledge_handoff(kernel, handoff["id"], accepted=True, acknowledgement="Retrospective package accepted.", actor="calibration")

    gate1 = prepare_gate(
        kernel,
        project_id,
        phase="frame",
        criteria=["Mission and constraints recorded", "Demo and product objectives separated"],
        evidence_packet=[objective["id"]],
        actor="calibration",
    )
    kernel.advance_gate(gate1["id"], "conditional_proceed", authority="historical-project-owner", next_phase="decision_space", unresolved_conditions=["Independent validation remains open"], rationale="Sufficient context for bounded architecture exploration.", actor="calibration")
    gate2 = prepare_gate(
        kernel,
        project_id,
        phase="decision_space",
        criteria=["Alternatives mapped", "API limitation recorded", "Claim boundaries stated"],
        evidence_packet=[e["id"] for e in evidence],
        unresolved_conditions=["Energy attribution calibration not performed"],
        actor="calibration",
    )
    kernel.advance_gate(gate2["id"], "conditional_proceed", authority="retrospective-calibration", next_phase="requirements_direction", unresolved_conditions=["Energy attribution calibration not performed", "Independent expert review absent"], rationale="The historical project proceeded with a heuristic design while recording the limitation.", actor="calibration")
    gate3 = prepare_gate(
        kernel,
        project_id,
        phase="verify_attack",
        criteria=["Unsafe AI candidates excluded", "Failed exact attribution path not reintroduced", "Known claim limits preserved"],
        evidence_packet=[claims[0]["id"], claims[1]["id"], claims[2]["id"]],
        actor="calibration",
    )
    kernel.advance_gate(gate3["id"], "conditional_proceed", authority="retrospective-calibration", next_phase="operate_learn", unresolved_conditions=["No controlled field validation"], rationale="The revision record demonstrates important failure-triggered replanning, but not external validation.", actor="calibration")
    kernel.update("project", project_id, {"status": "completed"}, actor="calibration")
    return kernel, project_id


def report(kernel: OperatingKernel, project_id: str) -> dict:
    packet, data = kernel.continuation_packet(project_id)
    entity_counts = {
        kind: len(kernel.list_entities(kind, project_id=project_id))
        for kind in ["objective", "factor", "evidence", "decision", "risk", "work_package", "claim", "gate", "handoff"]
    }
    status_counts = {}
    for kind in ["factor", "evidence", "decision", "risk", "work_package", "claim", "gate", "handoff"]:
        status_counts[kind] = {}
        for item in kernel.list_entities(kind, project_id=project_id):
            status = item.get("status", item.get("evidence_state", "unknown"))
            status_counts[kind][status] = status_counts[kind].get(status, 0) + 1
    report = {
        "calibration": "TabVolt retrospective",
        "project_id": project_id,
        "evidence_boundary": "Historical conversation record and its reported local observations; not independent validation.",
        "entity_counts": entity_counts,
        "status_counts": status_counts,
        "link_count": len(data["links"]),
        "event_count": len(kernel.events(project_id)),
        "event_chain_valid": kernel.verify_event_chain(),
        "coverage_checks": {
            "objective_to_factor": any(link["relation"] == "addresses" and link["src_type"] == "objective" for link in data["links"]),
            "evidence_to_claim": any(link["relation"] == "supports" for link in data["links"]),
            "decision_to_risk": any(link["relation"] == "addresses" and link["dst_type"] == "risk" for link in data["links"]),
            "work_package_and_handoff": any(item.get("status") == "acknowledged" for item in data["handoff"]),
            "conditional_gates": sum(1 for item in data["gate"] if item.get("decision") == "conditional_proceed"),
            "claim_limitations_preserved": all(bool(item.get("limitations")) for item in data["claim"]),
        },
        "observed_framework_friction": [
            "Retrospective mapping requires a clear distinction between historical conversation evidence and independent verification.",
            "A factor can be both treated and still open; status and evidence state must remain separate.",
            "A project graph needs typed links because the same object can support, challenge, derive, or address another object.",
            "The framework records why the architecture changed after failure, which was not reliably visible in a raw conversation alone.",
            "Gate conditions preserve unresolved energy-attribution and independent-review gaps instead of hiding them behind completion.",
        ],
        "residual_gaps": [
            "No controlled energy or battery measurement was performed in this retrospective.",
            "No current browser API re-validation was performed.",
            "No independent reviewer or external domain expert participated.",
            "No actual TabVolt source code was imported into the kernel.",
        ],
    }
    OUT.joinpath("tabvolt-calibration-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    OUT.joinpath("tabvolt-calibration-report.md").write_text(
        "# TabVolt Retrospective Calibration\n\n"
        "This is a retrospective calibration of the Universal Enterprise kernel against the historical TabVolt project record. It is not a new TabVolt validation and does not upgrade historical conversation evidence into independent proof.\n\n"
        f"**Project ID:** `{project_id}`  \n"
        f"**Entity count:** `{sum(entity_counts.values())}`  \n"
        f"**Typed links:** `{report['link_count']}`  \n"
        f"**Events:** `{report['event_count']}`  \n"
        f"**Event chain valid:** `{report['event_chain_valid']}`\n\n"
        "## Coverage checks\n\n"
        + "\n".join(f"- `{key}`: `{value}`" for key, value in report["coverage_checks"].items())
        + "\n\n## Observed framework friction\n\n"
        + "\n".join(f"- {item}" for item in report["observed_framework_friction"])
        + "\n\n## Residual gaps\n\n"
        + "\n".join(f"- {item}" for item in report["residual_gaps"])
        + "\n\n## Generated continuation packet\n\n"
        + packet
        + "\n",
        encoding="utf-8",
    )
    return report


if __name__ == "__main__":
    kernel, project_id = create_record()
    try:
        result = report(kernel, project_id)
        print(json.dumps(result, indent=2))
    finally:
        kernel.close()
