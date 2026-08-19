# Universal Virtual Enterprise: Staged Construction and First Operating Kernel v0

## 1. Construction principle

The virtual enterprise should be built as a series of usable capability increments. The first increment must create shared project coherence; later increments add specialist depth, automation, and external integrations.

The objective is not to create thousands of agents before the system has demonstrated that teams can share state, preserve evidence, converge on decisions, and revise work when reality changes.

## 2. Stage 0 — Operating specification

Define the capability-cell contract, project-state schema, evidence states, authority boundaries, gate outcomes, handoff format, change-impact format, and continuity rules.

**Exit condition:** the system has a stable vocabulary for projects, capabilities, work packages, artefacts, requirements, decisions, evidence, risks, gates, reviews, and approvals.

## 3. Stage 1 — Kernel-assisted single-coordinator operation

Implement a local-first project kernel with one coordinator and structured files or database records. The coordinator can create a project frame, maintain a research/decision ledger, register evidence, route bounded tasks, record handoffs, and prepare gate packets.

At this stage, specialist work may be performed manually or through external tools, but every output is normalized into the common kernel.

**Purpose:** validate the operating model before complex delegation.

**Exit condition:** a real project can be continued across sessions without losing the current state, decisions, evidence, risks, or next actions.

## 4. Stage 2 — First reusable upstream framework module

Implement the project-discovery and systems-thinking module based on the NHAI/VitalNet/TabVolt-derived workflow. It should support project framing, problem reconstruction, landscape mapping, factor cataloguing, solution comparison, decision records, architecture, adversarial review, canonical output, and submission compression.

**Purpose:** make the user's strongest existing reasoning workflow executable as a reusable capability.

**Exit condition:** the module can produce a structured, traceable output for a new project without relying on raw conversation reconstruction.

## 5. Stage 3 — Research and specialist team assembly

Add a capability registry and dynamic project graph. The system can activate research, domain, systems, product, software, engineering, assurance, and communication teams according to the mission.

Teams receive work-package contracts and return normalized outputs. Parent branches synthesize child outputs. Cross-branch conflicts become decision packets rather than hidden inconsistencies.

**Purpose:** move from one coordinator to a team-of-teams model.

**Exit condition:** multiple specialist branches can work in parallel and converge into one current project state with traceable dependencies.

## 6. Stage 4 — Software engineering subsystem

Add the enterprise-grade software lifecycle as a downstream module. It should consume the upstream system concept and produce product definition, requirements, architecture, ADRs, implementation plans, code handoffs, test evidence, security/compliance artefacts, release readiness, operational plans, and lifecycle records.

**Purpose:** turn the universal project framework into an implementation-ready software product pipeline.

**Exit condition:** a software project can proceed from upstream concept to controlled implementation and operational readiness with traceability and review.

## 7. Stage 5 — Independent assurance and controlled side effects

Add independent reviewers, red-team workflows, threat/safety analysis, evidence checks, claim audits, approval gates, sandboxed tools, permissions, audit logs, rollback, and human confirmation for consequential actions.

**Purpose:** prevent the system from becoming a self-approving autonomous organisation.

**Exit condition:** the enterprise can produce a gate decision that clearly separates creator output, independent review, residual risk, and authorised approval.

## 8. Stage 6 — Domain execution pipelines

Add specialist pipelines one at a time according to actual demand: robotics/hardware, scientific research, manufacturing, clinical/high-impact, infrastructure, regulatory, commercial, and other domains.

Each pipeline uses the same interface envelope and governance spine but has domain-specific requirements, artefacts, evidence, testing, and external validation.

**Purpose:** expand capability without fragmenting the operating model.

**Exit condition:** multiple domain pipelines can collaborate on a hybrid project with cross-subsystem traceability.

## 9. Stage 7 — Persistent local-and-remote enterprise

Separate local personal control and sensitive project state from remote workers and long-running execution. Workers may run locally, on a persistent home/office machine, or in isolated remote environments depending on compute, uptime, privacy, and cost.

The system should support task queues, resumable work, event logs, status, health checks, artifact storage, access control, sandboxing, and recovery. The remote layer must not automatically receive the entire personal or project corpus.

**Purpose:** support long-running multi-agent work without sacrificing local authority and privacy.

**Exit condition:** projects can continue across sessions and environments with explicit synchronization and no ambiguous source of truth.

## 10. First operating kernel data model

The minimum kernel should represent:

| Entity | Purpose |
|---|---|
| Project | Mission, frame, maturity, status, owner, and current baseline |
| Objective | Desired outcome and success condition |
| Stakeholder | User, operator, customer, affected party, or authority |
| Capability | Available branch/team/skill and activation status |
| Work package | Bounded task with objective, inputs, output, evidence, and acceptance |
| Artifact | Versioned output with type, owner, status, and relationships |
| Evidence item | Source, observation, calculation, test, inference, confidence, and provenance |
| Factor/constraint | Condition that affects problem, requirement, design, or validation |
| Requirement | Testable system, product, software, safety, security, or operational need |
| Decision | Choice, options, criteria, rationale, consequences, and revisit trigger |
| Risk/hazard | Cause, consequence, likelihood, severity, owner, mitigation, and residual state |
| Handoff | Contract between teams with dependencies and acceptance conditions |
| Gate | Readiness decision, evidence, conditions, and authority |
| Review | Peer, specialist, independent, red-team, or authority review |
| Change event | Material change and impact on downstream state |
| Claim | Public or internal assertion linked to evidence and permitted scope |
| External validation | Human, laboratory, legal, regulatory, clinical, customer, or field evidence |

## 11. First practical project for calibration

The first kernel should be calibrated on one bounded but serious project. The multi-agent harness itself should not be the only test because it can bias the system toward its own assumptions. Suitable calibration projects include a bounded software/AI system, a robotics concept slice, or a deliberately scoped NHAI-style problem.

The calibration should test:

- continuity across sessions;
- framing and decomposition;
- capability activation;
- structured research handoffs;
- evidence and contradiction handling;
- decision recording;
- adversarial review;
- gate packets;
- canonical output generation;
- and the ability to reopen earlier work after a new finding.

## 12. Construction risks

The main risks are attempting to build the entire capability tree before the kernel works; creating a central orchestrator that becomes a bottleneck; allowing agents to create incompatible local memories; confusing breadth with expertise; automating high-impact decisions; adding formal documents without decision value; integrating open-source projects with overlapping planners and permissions; and treating simulated capability as equivalent to real-world validation.

The staged design addresses these by starting with the kernel, adding one reusable upstream module, adding one software pipeline, and then expanding only when a real project demonstrates the need.
