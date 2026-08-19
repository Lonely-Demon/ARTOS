# Universal Virtual Enterprise: Project and Software Subsystem Integration v0

## 1. Integration premise

The universal enterprise must not treat every project as a software project and must not force every domain into one lifecycle. It should provide a stable upstream framework for understanding and selecting a solution, then activate one or more downstream execution pipelines appropriate to the selected system.

The upstream project framework answers **why, what, for whom, under which conditions, and with what trade-offs**. Downstream pipelines answer **how to design, build, verify, deploy, operate, and evolve each part of the selected system**.

Software is one downstream subsystem. Other future subsystems may cover hardware, robotics, scientific research, manufacturing, clinical validation, regulatory approval, field deployment, supply chain, and other domains.

## 2. Upstream framework output contract

Before a downstream pipeline is activated, the upstream system should provide an appropriate version of the following:

1. Project frame and mission objective.
2. Stakeholders, users, operators, affected parties, and authority boundaries.
3. Problem model and causal failure structure.
4. Concept of Operations or equivalent operating narrative.
5. System boundary and software/hardware/people/process decomposition.
6. Requirements, constraints, factors, assumptions, and exclusions.
7. Solution landscape and alternatives considered.
8. Selected system concept and architecture drivers.
9. Decision records and rejected alternatives.
10. Evidence and provenance status.
11. Risk, hazard, security, compliance, and operational concerns.
12. Desired maturity target and resource envelope.
13. Prototype/implementation objective and success conditions.
14. Open questions and validation gates.
15. Permitted and prohibited claims.

The downstream pipeline must be able to identify which upstream items are settled, provisional, or still open. It must not treat an upstream concept as an implementation-ready specification if its maturity does not justify that interpretation.

## 3. Software subsystem input interpretation

The software pipeline receives the upstream package and performs a software-scope extraction:

- What functions are software responsibilities?
- Which system requirements flow into software requirements?
- Which physical, operational, human, or regulatory constraints affect software?
- What interfaces exist with hardware, people, organisations, or external systems?
- Which data is needed and who owns it?
- What software failures can cause system-level harm?
- What must be measured or verified before software can support the wider system?
- What is the software maturity target: feasibility prototype, demo, pilot, internal service, production product, or high-assurance system?

The output is a software mission frame, not yet a PRD or architecture.

## 4. Software lifecycle subsystem

The software pipeline then moves through its own tailored stages:

### Software intake and product framing

Translate system objectives into a software objective, identify users and stakeholders, define the software product boundary, establish business/value context, and determine whether the initiative should proceed.

### Product and operational definition

Create the software product definition, user outcomes, workflows, scope, non-goals, success measures, acceptance intent, and Concept of Operations details that software must support.

### Feasibility and technical discovery

Research data, integrations, technologies, open-source components, models, performance, cost, security, and deployment constraints. Use prototypes to retire high-risk assumptions.

### Requirements engineering

Derive functional, quality, data, interface, security, privacy, safety, compliance, operational, accessibility, and maintenance requirements. Link them to upstream factors and objectives.

### Architecture and design

Define software architecture, data and API boundaries, identity and permissions, deployment topology, dependencies, observability, failure handling, and evolution strategy. Record significant choices through ADRs or equivalent decision records.

### Planning and implementation

Create the implementation breakdown, repository and environment strategy, coding and review controls, dependency and secret management, migrations, build automation, and controlled handoffs.

### Verification and validation

Test the software against requirements and validate it against the actual system and user objectives. Include appropriate unit, integration, system, acceptance, performance, resilience, security, data, model, and operational tests.

### Release and operational readiness

Verify deployment, rollback, configuration, monitoring, support, incident response, backup, recovery, vulnerability status, documentation, ownership, and training as appropriate.

### Operation and evolution

Collect telemetry, incidents, feedback, cost, reliability, security, and usage evidence. Feed discoveries into the software backlog, requirements, architecture decisions, risks, and upstream system framework.

## 5. Boundary between upstream and software work

The upstream framework owns system-level coherence. The software pipeline owns software-specific realisation. Neither should silently absorb the other's responsibilities.

| Question | Primary owner |
|---|---|
| Is this the right problem to solve? | Upstream mission/problem framework |
| What should the complete system accomplish? | Upstream systems/product framework |
| What part belongs to software? | Joint decision; systems integrator resolves boundary |
| What software requirements follow? | Software requirements team, traced to system requirements |
| How should software be built? | Software architecture and engineering pipeline |
| Does software satisfy its requirements? | Software verification |
| Does the complete system solve the real problem? | Upstream validation with software and other subsystems |
| Does the software operate safely and reliably? | Software assurance and operations, with system-level review |
| Did deployment reveal a wrong system assumption? | Software operations reports upstream; systems integrator reopens affected work |

## 6. Cross-subsystem interface envelope

Every downstream subsystem should receive and return a standard interface package:

### Input envelope

- Mission and project identity.
- Current system baseline and version.
- Relevant objectives and requirements.
- Scope and exclusions.
- Interfaces and dependencies.
- Evidence and assumption states.
- Risks and authority boundaries.
- Maturity and resource target.
- Required outputs and acceptance conditions.
- Claims the subsystem may and may not make.

### Output envelope

- Completed artefacts and versions.
- Findings and decisions.
- Evidence and provenance.
- Requirements satisfied, changed, or rejected.
- Interfaces implemented or still open.
- Tests and validation results.
- Risks, incidents, limitations, and residual uncertainty.
- New assumptions or constraints discovered.
- Change-impact notifications to other subsystems.
- Recommended next action and gate status.

## 7. Upstream feedback from software

Software implementation is a source of system knowledge, not merely an execution step. It may reveal:

- a system requirement is technically infeasible;
- a data source is unavailable or unreliable;
- a user workflow is impractical;
- an integration dependency changes the operating model;
- security or privacy constraints alter the product;
- performance or cost changes the business case;
- a prototype demonstrates a narrower or broader value proposition;
- or a software failure creates a new system-level hazard.

These findings must flow back to the systems integrator and upstream framework. The project should reopen the relevant stage rather than bury the discovery in an implementation issue tracker.

## 8. Maturity tailoring

The same software subsystem can operate at multiple depths:

| Maturity | Minimum appropriate output |
|---|---|
| Idea/feasibility | Product frame, feasibility questions, architecture hypotheses, risk and test plan |
| Competition concept | Coherent product/system definition, technical architecture, implementation path, evidence limits |
| Demonstration prototype | Reproducible build, scoped requirements, prototype tests, known limitations, demo claims |
| Pilot | Operational users, monitoring, security/privacy baseline, support and rollback, acceptance evidence |
| Enterprise production | Full lifecycle governance, traceability, security/compliance evidence, operations, recovery, change control, maintenance |
| High-assurance/high-impact | Independent verification, formal safety/security/compliance evidence, specialist/external authority, controlled deployment and audit |

The pipeline must never make a prototype appear production-ready solely because it passed a demonstration.

## 9. Other downstream pipelines

The same interface should support future pipelines:

- **Hardware/robotics:** requirements, physics, materials, mechanical/electrical design, manufacturing, integration, environmental testing, field validation, maintenance.
- **Scientific research:** hypothesis, literature, methods, data, experiment, reproducibility, analysis, peer review, limitations, publication or decision output.
- **Manufacturing:** design-for-manufacture, supplier, process, quality, yield, tooling, logistics, inspection, sustainment.
- **Clinical/high-impact:** clinical workflow, risk, ethics, safety, evidence, human authority, validation, regulatory and institutional review.
- **Regulatory/compliance:** applicable obligation, interpretation, control, evidence, audit, gap, remediation, sign-off.
- **Commercial/market:** customer, value, adoption, competition, pricing, channel, messaging, launch, feedback.

A complex project can activate several pipelines simultaneously. The systems integrator owns the interfaces and the enterprise kernel owns the shared state.

## 10. Integration failure modes

The architecture must prevent the upstream framework from becoming an impractical research report with no implementation path, and prevent the software pipeline from reducing a complex system into a feature backlog.

It must also prevent duplicate or contradictory requirements, lost upstream constraints, software teams making system-level claims without validation, downstream discoveries failing to reopen upstream work, compliance being treated as a final document, and independent assurance being activated only after public claims are written.
