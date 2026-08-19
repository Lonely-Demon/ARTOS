# Universal Enterprise Operating Kernel v1

## 1. Purpose

The operating kernel is the minimum shared infrastructure that allows recursive specialist teams to cooperate without losing context, evidence, authority, or change history. It is the trunk of the universal enterprise.

The kernel should initially be a **project knowledge and coordination system**, not a fully autonomous organisation. It should support local-first use, structured artefacts, resumable work, explicit approvals, and later remote workers.

## 2. Core design principles

The kernel maintains one canonical current state while preserving historical versions and dissent. It separates facts, inferences, assumptions, decisions, and claims. It treats every delegated task as a contract. It records not only outputs but the conditions under which they were produced. It can reopen earlier work when later evidence changes the system.

It should be possible to use the kernel with a single human and one AI, with a team of human/AI collaborators, or with a dynamic multi-agent project graph. The same information model should support all three modes.

## 3. Core entities

### Project

Contains mission, objective, owner, stakeholders, domain, maturity, scope, constraints, current phase, active graph, baseline, status, and next gate.

### Objective and outcome

Contains desired outcome, value hypothesis, success condition, priority, evidence method, owner, and relationship to upstream mission.

### Capability and team

Contains branch, subdomain, mandate, activation criteria, depth, parent capability, members/agents, authority, methods, evidence contract, and availability.

### Work package

Contains objective, question/decision supported, context, inputs, scope, exclusions, constraints, assumptions, evidence standard, expected artefact, acceptance criteria, dependencies, owner, reviewer, priority, status, and escalation triggers.

### Artefact

Contains type, title, version, owner, source baseline, status, audience, relationships, evidence references, approvals, change history, and permitted use. Examples include a problem model, PRD, BRD, requirements set, architecture, ADR, code baseline, test report, compliance matrix, or runbook.

### Evidence item

Contains claim or proposition, source/observation, provenance, method, date, conditions, confidence, evidence state, affected decisions, limitations, reviewer, and what would change its status.

### Factor and constraint

Contains factor, category, causal explanation, affected stakeholder/system, consequence, decision impact, evidence state, treatment, owner, and coverage status.

### Requirement

Contains identifier, source, level, statement, rationale, priority, owner, status, verification method, validation method, dependencies, risks, implementation links, and change history.

### Decision

Contains question, context, options, criteria, selected option, rationale, rejected alternatives, consequences, dependencies, confidence, authority, review, status, and revisit trigger.

### Risk or hazard

Contains cause, event, consequence, affected assets/stakeholders, likelihood/plausibility, severity, detectability, owner, mitigation, contingency, trigger, residual state, and acceptance authority.

### Handoff

Contains sender, receiver, package, context, objective, inputs, scope, exclusions, evidence contract, expected output, acceptance, authority, dependencies, risks, due priority, status, and acknowledgement.

### Gate

Contains phase, objective, evidence packet, readiness criteria, unresolved conditions, review results, recommendation, decision, authority, owners, due dates, and next state.

### Review

Contains reviewer type, independence, scope, inputs, findings, severity, required actions, disposition, approval, and relationship to gate.

### Claim

Contains statement, audience, evidence state, supporting evidence, scope, limitations, permitted wording, owner, reviewer, and use contexts.

### Change event

Contains change, trigger, initiator, affected baseline, impact analysis, affected entities, approvals, implementation, verification, and closure.

### External validation

Contains authority, claim or requirement, method, evidence, conditions, date, limitations, result, and formal status.

## 4. Relationships

The kernel should represent a graph such as:

> Objective → factor/constraint → requirement → decision → architecture/design → implementation → test/observation → claim → operational feedback

Additional relationships include:

- Project activates Capability.
- Capability creates Work Package.
- Work Package produces Artefact.
- Artefact contains or supports Evidence.
- Requirement is derived from Objective or Factor.
- Decision satisfies or allocates Requirement.
- Decision affects Risk and Architecture.
- Implementation changes Requirement/Decision/Artefact.
- Test verifies Requirement and Evidence.
- Claim is supported by Evidence.
- Change Event impacts every linked entity.
- Gate evaluates a baseline and controls progression.

## 5. State machines

### Work package state

Proposed → Scoped → Assigned → Accepted → In progress → Submitted → Reviewed → Accepted / Returned / Escalated → Closed.

### Artefact state

Draft → Internal review → Baseline candidate → Approved baseline → Superseded / Withdrawn.

### Decision state

Open → Options mapped → Recommendation → Under review → Accepted / Accepted with conditions / Rejected / Deferred / Reopened.

### Gate state

Not ready → Packet prepared → Review in progress → Proceed / Conditional proceed / Loop back / Descope / Pause / Stop.

### Change state

Proposed → Impact analysis → Approval → Implementing → Verified → Baseline updated → Closed.

## 6. Kernel services

### Project-state service

Provides current state, phase, active work, blockers, decisions, risks, and next actions. It must be readable without replaying the raw conversation.

### Evidence/provenance service

Stores source and evidence states, tracks contradictions, prevents unsupported claim upgrades, and links evidence to affected decisions.

### Work orchestration service

Creates work packages, activates capability cells, tracks dependencies, routes handoffs, detects blocked work, and manages retries/reconfiguration.

### Traceability service

Maintains relationships among objectives, factors, requirements, decisions, implementations, tests, claims, and operational observations.

### Gate/review service

Prepares evidence packets, schedules reviewers, records findings, tracks conditions, and produces gate decisions.

### Artefact/version service

Stores or references files, code, diagrams, datasets, reports, test results, and snapshots with version and baseline metadata.

### Change-impact service

Identifies downstream artefacts, teams, tests, claims, permissions, and releases affected by a change.

### Authority/permission service

Controls who or what may read, write, approve, deploy, invoke tools, access sensitive data, or cause external side effects.

### Continuity service

Maintains durable project summaries, decisions, assumptions, next actions, and cross-project precedent without treating raw conversation as the source of truth.

### Measurement service

Collects project, quality, reliability, delivery, cost, and outcome measures selected for the project. It supports decisions rather than forcing one universal metric set.

## 7. First implementation roadmap

### Kernel slice 1 — Structured continuity

Implement project state, objectives, current phase, decisions, assumptions, open questions, risks, and next actions using human-readable Markdown or structured records. The first test is resumption after context loss.

### Kernel slice 2 — Evidence and artefact graph

Add artefact registry, evidence items, sources, confidence states, claims, cross-reference, and versioning. The first test is whether a claim can be traced back to evidence and a project decision.

### Kernel slice 3 — Work packages and handoffs

Add capability registry, work-package contracts, assignments, acknowledgements, outputs, reviews, blockers, and dependency graph. The first test is whether multiple collaborators can work without losing shared context.

### Kernel slice 4 — Gates and assurance

Add phase gates, gate packets, reviewer roles, independent review, conditions, red-team findings, approvals, and loopback. The first test is whether the system can prevent a premature architecture or unsupported claim from being baselined.

### Kernel slice 5 — Software lifecycle integration

Add requirements, architecture, ADR, repository/build references, test results, security controls, release records, operational readiness, incidents, and postmortems. The first test is whether an upstream concept can generate a traceable software delivery plan.

### Kernel slice 6 — Dynamic team assembly

Add capability ontology, routing, recursive team cells, parallel work, parent synthesis, conflict packets, and reconfiguration. The first test is whether specialist outputs converge without central context overload or hidden disagreement.

### Kernel slice 7 — Tool and worker execution

Add sandboxed local and remote workers, task queues, resumable execution, artifact exchange, tool permissions, logs, health checks, budgets, and failure recovery. The first test is a bounded research or coding worker with controlled side effects.

### Kernel slice 8 — Domain pipelines

Add robotics/hardware, scientific, manufacturing, clinical/high-impact, regulatory, commercial, and other domain modules as demand requires. Each must conform to the same interface and governance spine.

## 8. Local and remote deployment model

The local control plane should contain personal identity, sensitive project state, approvals, authority, and the canonical source of truth. Workers may run locally or remotely depending on compute, uptime, isolation, and cost.

Remote workers should receive scoped task packages rather than unrestricted access to the full project. Returned artefacts and evidence are reviewed before entering the canonical state. Synchronisation should be explicit, versioned, auditable, and conflict-aware.

## 9. Kernel non-goals

The first kernel should not attempt to contain every specialist skill, replace all project-management tools, autonomously approve high-impact actions, make legal/clinical/regulatory determinations, or build a general-purpose autonomous company in one release.

It should first prove one thing: **multiple capable contributors can work on one serious project, preserve why they did what they did, challenge one another, and converge into a traceable project state.**
