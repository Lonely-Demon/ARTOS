# Minimum Operational Contract v0.2

**Status:** Autonomous implementation baseline
**Parent:** Universal Virtual Enterprise Blueprint v2.0
**Purpose:** Define the smallest useful, local-first operating contract that can preserve project continuity, trace decisions, govern work, and support later agent workers.

## 1. Scope

This reference slice is a project knowledge and coordination kernel. It is not yet a general autonomous enterprise, model router, secure multi-tenant platform, legal/compliance authority, or production deployment system.

The kernel must support one project with one or more human or AI contributors. It must preserve structured current state, append-only event history, evidence and provenance, decisions and rejected alternatives, work packages, gates, claims, and a continuation packet. It must be usable without an active network connection and must make no external side effects by default.

## 2. Non-goals for this slice

The slice does not attempt to provide remote worker execution, production authentication, multi-tenant isolation, arbitrary tool execution, autonomous approvals, real-time collaboration, semantic conflict resolution, vector retrieval, model selection, or domain-specific expert competence. These are later capability increments and must not be implied by the reference implementation.

## 3. Canonical objects

The minimum object set is:

| Object | Required purpose | Minimum fields |
|---|---|---|
| Project | Canonical mission container | id, title, objective, scope, constraints, status, current_phase, owner, created_at, updated_at |
| Objective | Desired outcome and success condition | id, project_id, statement, success_condition, priority, status |
| Factor | Problem/constraint/unknown that may affect a decision | id, project_id, statement, category, consequence, evidence_state, treatment, status |
| Evidence | Traceable support/challenge for a claim or decision | id, project_id, proposition, source, method, conditions, evidence_state, limitations, captured_at |
| Decision | Choice with alternatives and consequences | id, project_id, question, options, selected_option, rationale, rejected_alternatives, authority, status, revisit_trigger |
| Risk | Uncertainty with possible consequence and treatment | id, project_id, statement, cause, consequence, likelihood, severity, mitigation, residual_state, status |
| Work package | Bounded unit of work and handoff contract | id, project_id, objective, question, inputs, exclusions, evidence_contract, acceptance, owner, reviewer, status |
| Claim | Permitted statement whose strength is controlled by evidence | id, project_id, statement, scope, evidence_state, permitted_wording, limitations, status |
| Gate | Readiness decision controlling phase transition | id, project_id, phase, criteria, evidence_packet, unresolved_conditions, decision, authority, status |
| Event | Append-only record of material state change | id, project_id, event_type, entity_type, entity_id, payload, actor, occurred_at |

Each object also has a stable identifier, schema version, and provenance metadata. Unknown fields must not silently change the meaning of an object.

## 4. Evidence states

The allowed evidence states are: `verified`, `measured_locally`, `estimated`, `design_inference`, `hypothesis`, `open`, and `excluded`. The kernel must not automatically upgrade a claim or evidence state. Any upgrade is an explicit event with a reason and supporting evidence.

## 5. State and history

The database stores the current projection for readable queries and an append-only event log for reconstruction and audit. Every write is transactional. Every material write emits an event. Event payloads are JSON and include the prior state hash where practical. Deletion is represented as a tombstone rather than destructive erasure in this slice.

## 6. State transitions

Project status: `draft → active → paused → completed | stopped`.

Work package status: `proposed → scoped → assigned → in_progress → submitted → reviewed → accepted | returned | escalated → closed`.

Decision status: `open → options_mapped → recommendation → under_review → accepted | accepted_with_conditions | rejected | deferred | reopened`.

Gate status: `not_ready → packet_prepared → review_in_progress → proceed | conditional_proceed | loop_back | descope | pause | stop`.

Invalid transitions must be rejected with an explanatory error and must not emit a state-change event.

## 7. Minimum workflow

The implementation exposes the following phase names: `frame`, `problem_context`, `decision_space`, `requirements_direction`, `canonical_output`, `implementation`, `verify_attack`, and `operate_learn`.

A gate may advance a project only when the gate decision is explicit. `proceed` advances to the configured next phase; `conditional_proceed` advances while recording unresolved conditions; `loop_back` returns to a named prior phase; `descope` records a reduced scope; `pause` preserves state without advancement; and `stop` closes the project as stopped.

The kernel does not judge whether evidence is substantively sufficient. It records gate criteria, packets, reviewer findings, authority, and decision. Substantive judgement remains with the configured reviewer or human authority.

## 8. Traceability

The minimum traceability links are:

`objective → factor → decision → work_package → evidence → claim`

and

`requirement/decision → gate → project_phase`.

Links are typed, directional, and stored separately from object payloads so they can be queried and validated.

## 9. Continuity packet

A generated continuation packet must contain project identity and status, current phase, objective, active work packages, decisions and rejected alternatives, factors and risks, evidence states, claims and permitted wording, gate history, recent event summary, open questions, assumptions, next actions, and known limitations. It must be human-readable Markdown and machine-readable JSON.

## 10. Safety boundary

No kernel command may invoke an external tool, contact an external service, modify a user repository, send a message, deploy code, or change a real-world system unless a later worker layer explicitly adds a policy-controlled execution capability. This slice is stateful but side-effect free outside its own workspace.

## 11. Acceptance tests

The slice is acceptable when it can: create and resume a project; create all minimum objects; link them; reject invalid state transitions; preserve event history; produce a continuation packet; reconstruct a project from events in a test database; prevent unsupported claim upgrades; record a conditional gate; and survive a simulated interrupted write without corrupting the current projection.

## 12. Explicit residual gaps

This contract does not prove domain expertise, reviewer independence, security against a hostile multi-tenant environment, correctness of evidence, real-world project value, or the quality of future agent workers. Those gaps require later tests, external sources, human/domain review, and operational use.
