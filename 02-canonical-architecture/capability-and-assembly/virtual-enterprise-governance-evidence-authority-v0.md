# Virtual Enterprise Governance, Evidence, and Authority v0

**Status:** Provisional governance design for the universal virtual enterprise.

## 1. Why governance is the spine

A universal capability system can produce enormous breadth but still fail if its teams do not share evidence, authority, standards, and accountability. Governance is therefore not a separate administrative layer. It is the mechanism that keeps specialist branches from producing mutually incompatible, overconfident, unsafe, or unauditable work.

The governance spine must answer five questions for every material project decision:

1. What is being decided?
2. Who is allowed to recommend, approve, reject, or revisit it?
3. What evidence supports the decision?
4. What consequences and residual risks remain?
5. What would cause the decision to change?

## 2. Authority model

### User / mission owner

The user owns the mission, personal objectives, values, major trade-offs, acceptable ambition, and final sufficiency judgment unless authority is explicitly delegated. The system may recommend, challenge, compare, and warn; it must not silently substitute its own objective.

### Enterprise orchestrator

The orchestrator assembles capabilities, manages the project graph, schedules work, detects missing branches, maintains phase state, and prepares decisions. It does not automatically become the authority for high-impact domain decisions.

### Systems integrator

The systems integrator owns cross-branch coherence. It can identify contradictions, require interface clarification, reopen affected work, and recommend a system-level decision. It should not erase specialist dissent to create artificial consensus.

### Capability lead

A capability lead owns the quality and integration of a branch's work. It may make local decisions within scope and escalate decisions that affect other branches, safety, claims, budget, or project objectives.

### Executor

An implementation or research team may perform authorised work and report observed results. It may not claim broader validation than its evidence supports or modify an external system beyond its granted permissions.

### Assurance / review authority

Independent assurance may challenge work, request evidence, impose conditions, require remediation, block progression within the governance process, and escalate unresolved risk. A creator should not approve its own high-consequence work without independent review.

### External authority

Human domain experts, legal counsel, regulators, clinical authorities, certification bodies, laboratory results, customer approvals, and other external authorities may be required. The virtual enterprise must identify when it lacks the authority to decide.

## 3. Decision classes

| Class | Examples | Default authority |
|---|---|---|
| Local reversible | Formatting, task ordering, non-material implementation detail | Capability lead or executor within contract |
| Technical significant | Architecture, interface, data model, major dependency, tool selection | Capability lead with systems integration review; record decision |
| Cross-branch | Requirement, interface, scope, cost, or risk affecting multiple branches | Systems integrator and relevant leads; escalate if unresolved |
| High-impact | Safety, clinical, financial, legal, privacy, security, public claim, irreversible external effect | Independent assurance plus authorised human/external authority |
| Mission-level | Objective, ambition, values, major trade-off, continue/stop, public commitment | User/mission owner |

## 4. Evidence state model

Every material claim or recommendation receives an evidence state:

| State | Meaning | Permitted use |
|---|---|---|
| Verified primary evidence | Directly supported by a reliable primary source, measurement, test, or authoritative record | Can support a bounded claim with citation/provenance |
| Verified secondary evidence | Supported by a credible secondary source with traceable origin | Can inform decisions; may require primary confirmation for high-impact use |
| Reproduced analysis | Calculation, code, model, simulation, or analysis that has been checked/reproduced | Supports analytical claims within model assumptions |
| Observed prototype result | Measured in a prototype or controlled test | Supports only the tested conditions and configuration |
| Design inference | Reasoned conclusion derived from evidence and assumptions | Must be labelled as inference and kept falsifiable |
| Assumption | Temporarily accepted premise not yet confirmed | Must have owner, impact, and validation path |
| Lead / unverified | Plausible information requiring confirmation | Cannot support a final high-consequence claim |
| Contradicted | Evidence conflicts with the claim or assumption | Must trigger review or explicit resolution |
| Unknown | Relevant issue for which evidence is absent | Must be addressed, bounded, deferred, or excluded explicitly |

The system must preserve the source, date, method, context, confidence, affected decisions, and what would change the evidence state.

## 5. Claim discipline

A team may not silently upgrade the status of its output. Research does not become validation merely because it is detailed. A demonstration does not become production reliability. A simulation does not become field performance. A prototype does not become certification. A public or competition narrative may compress evidence but may not strengthen it.

Every important final claim should be traceable to:

> **Objective/factor → requirement → design decision → implementation or experiment → result → permitted claim**

## 6. Readiness gates

Every major phase can result in proceed, proceed with conditions, loop back, descope, pause, or stop.

A gate packet should contain the phase objective, completed outputs, evidence status, unresolved issues, alternatives considered, risk changes, conditions, and the recommended next action.

The minimum gates are:

- **Frame gate:** objective, scope, stakeholders, resources, maturity, and success condition are clear enough to begin.
- **Understanding gate:** the real problem, operating context, and causal boundaries are understood enough to direct research.
- **Decision-space gate:** major factors, alternatives, dependencies, and architecture-changing unknowns are visible.
- **Architecture gate:** the chosen direction is coherent, requirements and interfaces are explicit, and alternatives/trade-offs are recorded.
- **Build/validation gate:** the first meaningful test or implementation is defined with acceptance criteria and claim boundaries.
- **Assurance gate:** technical, operational, safety, security, compliance, and claim risks have been challenged at appropriate depth.
- **Release/delivery gate:** output is complete enough for its maturity target, operational responsibilities are assigned, and limitations are communicated.

The gate formality is tailored to risk. A high-consequence project may require an independent review board and signed evidence; a reversible prototype may need a concise checklist and peer review.

## 7. Assurance architecture

Assurance is layered rather than concentrated in one final reviewer:

1. **Self-check:** the creator verifies its own output against the work package.
2. **Peer review:** a related specialist checks technical coherence and omissions.
3. **Systems integration review:** cross-branch requirements and interfaces are checked.
4. **Independent specialist review:** a separate capability attacks the relevant discipline.
5. **Red-team review:** the preferred concept is actively broken through failure, misuse, alternative, and evidence attacks.
6. **Decision authority review:** the authorised person or body decides whether residual risk is acceptable.
7. **Operational evidence:** actual use, tests, incidents, or field data feed back after delivery.

The same agent should not be the sole creator, verifier, and approver of high-impact work.

## 8. Safety and harm boundaries

The enterprise must classify the consequences of failure before choosing its review depth. It should identify who could be harmed, how harm occurs, whether the system can fail safely, whether humans retain meaningful authority, and what evidence is required before progression.

Safety-critical or high-impact projects need explicit hazard analysis, failure modes, safeguards, fallback behaviour, monitoring, incident response, and external review where appropriate. AI systems require additional controls for uncertainty, hallucination, instruction conflict, tool misuse, data leakage, automation bias, and human over-reliance.

The virtual enterprise must not treat safety as a confidence score or claim that a model is safe merely because it passed a limited test.

## 9. Security, privacy, and compliance boundaries

Security and privacy are architecture constraints from the beginning. The system should identify assets, data classes, trust boundaries, actors, permissions, attack surfaces, supply-chain risks, secrets, logging, retention, and recovery.

Compliance work should identify applicable laws, regulations, standards, contracts, and internal controls for the actual domain and jurisdiction. A compliance matrix should connect each obligation to a control, owner, evidence, review status, and residual gap.

The virtual enterprise may research compliance and prepare evidence, but it must not claim legal compliance, certification, regulatory approval, clinical acceptability, or formal safety sign-off without the appropriate authority.

## 10. Change and configuration control

Any material change to a requirement, factor, assumption, dependency, interface, architecture, claim, or public commitment should create a change event. The event identifies affected artefacts, downstream teams, tests, risks, approvals, and release implications.

The system should maintain baselines for the project frame, requirements, architecture, implementation, test evidence, and public claims. A new version should not silently overwrite the rationale for the old version.

## 11. Risk and uncertainty management

The risk register should include technical, operational, safety, security, privacy, legal, regulatory, financial, supply-chain, adoption, schedule, capability, and evidence risks. Each risk should have cause, consequence, likelihood/plausibility, severity, owner, mitigation, contingency, trigger, residual state, and validation requirement.

A risk may be accepted only by an authority appropriate to its consequence. “We do not know” is not a risk treatment; it is a state that must be converted into research, test, mitigation, boundary, deferral, or explicit exclusion.

## 12. Auditability and continuity

The enterprise must be able to reconstruct why a significant decision was made, what evidence was available, who reviewed it, what dissent existed, what assumptions were active, what changed later, and which claims were permitted at the time.

The continuity system should preserve project state without replacing the full source archive. It should include a current summary, decision index, evidence index, requirements/traceability, open issues, known limitations, and next actions.

## 13. Governance failure modes

Governance itself can fail through excessive ceremony, false precision, gate theatre, duplicated reviews, unaccountable central orchestration, bureaucratic artefact production, forced consensus, stale requirements, and unreviewed AI authority. The system must record why a control exists and allow proportional tailoring.
