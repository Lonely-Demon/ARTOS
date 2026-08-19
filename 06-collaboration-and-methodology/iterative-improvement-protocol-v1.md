# Iterative Improvement Protocol v1

## 1. Purpose

The universal-enterprise blueprint is treated as a living engineering design. It will improve through repeated cycles of research, comparison, contradiction review, revision, and stress testing. The goal is not to accumulate documents or delay implementation indefinitely. The goal is to reduce important blind spots and improve architecture quality until additional research produces less value than the time and complexity it costs.

## 2. Improvement cycle

Each cycle follows this sequence:

1. **Baseline:** record the current blueprint version, assumptions, open uncertainties, and known weaknesses.
2. **Gap hypothesis:** identify a specific area where new research could change the architecture, governance, subsystem boundary, implementation roadmap, or quality threshold.
3. **Targeted research:** search authoritative standards, high-quality engineering practice, relevant open-source systems, case studies, and domain evidence. Sources are recorded as they are found.
4. **Comparison:** compare new evidence against the current design, not merely add it to the corpus.
5. **Contradiction review:** identify conflicts among sources, conflicts with the user's project examples, and conflicts within the blueprint.
6. **Decision:** retain, revise, add, remove, defer, or explicitly reject the proposed change.
7. **Stress test:** examine whether the revised design survives failure, misuse, scale, domain changes, resource limits, and project examples.
8. **Record:** update the canonical blueprint, assumptions ledger, change log, research findings, and residual uncertainties.
9. **Value assessment:** estimate whether another cycle is likely to materially improve a consequential part of the design.

## 3. What counts as a material improvement

A research cycle is valuable if it does at least one of the following:

- reveals a missing capability, lifecycle stage, risk, authority boundary, or failure mode;
- changes how capabilities should be decomposed or assembled;
- changes a major subsystem boundary or interface;
- improves evidence, traceability, safety, security, compliance, or operational control;
- identifies a contradiction or invalid assumption;
- provides a reusable mechanism that reduces future project risk or coordination cost;
- simplifies the system without sacrificing important coverage;
- or improves the staged construction path and makes the first kernel more testable.

A cycle is not considered materially valuable merely because it finds another framework with different terminology, adds another document type, expands a list of specialist domains, or increases document length without changing decisions.

## 4. Improvement ledger

Every cycle should record:

| Field | Meaning |
|---|---|
| Cycle ID | Stable identifier for the research/revision loop |
| Focus | Specific area under investigation |
| Baseline | Blueprint version before research |
| Hypothesis | What might be missing or wrong |
| Sources | Sources actually read and assessed |
| New findings | Evidence that could affect design |
| Contradictions | Conflicts found |
| Decision | Keep, revise, add, remove, defer, or reject |
| Affected artefacts | Files, entities, processes, or assumptions changed |
| Stress test | Failure cases or project examples used |
| Residual uncertainty | What remains unresolved |
| Value score | Expected improvement relative to effort |
| Next action | Continue, narrow, pause, or stop |

## 5. Stopping rule

Research should stop when all of the following are substantially true:

1. The major architectural alternatives and capability branches are visible.
2. Further likely findings would refine implementation details rather than change the enterprise structure or important controls.
3. The operating kernel has a coherent minimum data model and a practical first slice.
4. The software lifecycle covers the full lifecycle and its requirements, architecture, quality, security, safety, operations, and retirement concerns.
5. The project graph, capability-cell contract, handoffs, gates, evidence model, and authority boundaries are internally consistent.
6. Known gaps are visible, categorised, and assigned a treatment: research, test, specialist review, mitigation, deferral, or exclusion.
7. A new research cycle has a low probability of changing a high-consequence decision relative to its expected effort.
8. The remaining unknowns are implementation or domain-specific questions that should be resolved by a real project calibration rather than further abstract research.

The stopping rule is not a numerical claim of completeness. It is a decision-readiness threshold. If a new cycle reveals an architecture-changing gap, the stopping decision is invalidated and the loop resumes.

## 6. Anti-patterns

The loop must avoid research as avoidance, framework accumulation, name-driven architecture, source-count vanity, false consensus, unverified claims, unbounded scope, and continuous document expansion. Each cycle must have a decision hypothesis and a defined reason for stopping.

## 7. Autonomous operating rule

When user feedback is unavailable, make provisional decisions using the existing vision and evidence, mark assumptions explicitly, preserve alternatives, and avoid irreversible implementation or external side effects. Continue research and design autonomously, but do not claim validation that requires experiments, specialist authority, legal review, or real deployment.
