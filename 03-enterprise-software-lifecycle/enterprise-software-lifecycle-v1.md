# Enterprise Software Lifecycle Subsystem v1

**Parent system:** Universal Virtual Enterprise  
**Input:** Upstream project/system concept package  
**Output:** Software product or software subsystem with maturity-appropriate evidence, documentation, deployment, operation, and evolution capability.

## 1. Purpose and design principles

This subsystem converts a system-level mission or solution concept into software that can be deliberately designed, implemented, verified, released, operated, maintained, and retired. It is not a single methodology. It is a set of coordinated process families that can be tailored for a hackathon prototype, an internal tool, a public product, a regulated system, a safety-critical system, or an AI/agentic product.

The pipeline is iterative. It may run product validation and technical feasibility in parallel, return to requirements after testing, reopen architecture after operations, and skip low-value phases when confidence is already high and risk is low. A phase exists to produce an outcome or reduce uncertainty, not merely to generate paperwork.

The pipeline uses the following principles:

- **Problem before feature:** software exists to support a real user, business, operational, or system outcome.
- **System context before isolated application:** software responsibilities, interfaces, people, hardware, data, facilities, and procedures are explicit.
- **Requirements are engineered:** needs become clear, complete, consistent, verifiable, traceable requirements [1] [2].
- **Architecture is a decision layer:** structure, qualities, interfaces, dependencies, and evolution rules are decided before implementation becomes expensive [3].
- **Security, privacy, safety, and compliance are designed in:** they are present from requirements through operations [4] [5].
- **Creator and verifier are separated when consequences justify it:** independent review is a control, not a courtesy [6].
- **Release is staged and observable:** deployment, rollback, monitoring, and response are part of the lifecycle [7] [8].
- **Documentation serves decisions and continuity:** names such as BRD, PRD, SRS, and ADR are useful views, not mandatory artefacts for every project.
- **Evidence is bounded:** a prototype, simulation, test, or model supports only the claims justified by its conditions.

## 2. Inputs from the upstream project framework

The upstream framework should provide the software pipeline with a versioned system package containing:

1. Mission and project objective.
2. Stakeholders, users, operators, customers, and affected parties.
3. Problem model and causal failure structure.
4. Concept of Operations and system context.
5. System boundary and allocation of responsibility among software, hardware, people, procedures, and external organisations.
6. System requirements, constraints, factors, assumptions, and exclusions.
7. Solution alternatives and selected system concept.
8. Architecture drivers and cross-system interfaces.
9. Risk, hazard, security, privacy, compliance, and operational concerns.
10. Evidence, provenance, confidence, contradictions, and unresolved questions.
11. Desired maturity target, resource envelope, and delivery constraints.
12. Prototype or implementation objective and success conditions.
13. Permitted and prohibited claims.

The software pipeline first creates a **software allocation and readiness assessment**. It records which upstream requirements flow to software, which are not software responsibilities, which remain system-level validation obligations, and which upstream assumptions must be tested before software architecture is locked.

## 3. Lifecycle stages and gates

| Stage | Main purpose | Primary gate |
|---|---|---|
| 0. Intake | Register and classify the initiative | Is this worth framing? |
| 1. Product/mission framing | Establish software purpose, value, scope, and authority | Is the software objective clear? |
| 2. Problem and user validation | Confirm the problem, workflow, users, and desired outcome | Is the problem worth solving and understood? |
| 3. Feasibility and R&D | Retire architecture-changing technical uncertainty | Is a credible path feasible? |
| 4. Requirements engineering | Define what software must do and how well | Are requirements clear, testable, and traceable? |
| 5. Architecture and design | Define how the system will satisfy requirements | Is the architecture coherent, secure, evolvable, and feasible? |
| 6. Planning and implementation readiness | Prepare controlled construction | Can implementation begin with bounded risk? |
| 7. Incremental implementation | Build and integrate small, reviewable changes | Does each increment satisfy its contract? |
| 8. Verification and validation | Establish correctness, quality, security, and usefulness | Is the product ready for its target maturity? |
| 9. Release readiness and deployment | Introduce the product safely | Can this version be released and recovered? |
| 10. Operations and support | Observe, operate, recover, and learn | Is the live product controlled and improving? |
| 11. Evolution and retirement | Change, migrate, deprecate, and close responsibly | Is the product still justified and supportable? |

A gate can return **proceed**, **proceed with conditions**, **loop back**, **descope**, **pause**, or **stop**. Gate evidence and conditions are recorded in the shared kernel.

## 4. Stage 0 — Intake and portfolio framing

### Purpose

Determine what has been proposed, why it matters, who owns the decision, how urgent it is, what type of software effort it may become, and whether it deserves discovery effort.

### Activities

The portfolio/mission team records the raw request, upstream concept version, sponsor, stakeholders, domain, expected benefit, urgency, resource envelope, maturity target, known constraints, likely risks, external dependencies, and whether the software is a product, subsystem, internal capability, experiment, or support tool.

The team classifies consequence and reversibility. A small internal tool and an AI system that influences clinical, financial, safety, or infrastructure decisions must not enter the pipeline with the same control depth.

### Outputs

- Initiative brief.
- Initial business/mission case.
- Sponsor and decision authority.
- Preliminary scope and non-goals.
- Maturity target.
- Initial risk and assumption register.
- Initial stakeholder map.
- Initial capability activation request.
- Recommended discovery depth.

### Gate

Proceed when there is a sufficiently clear reason to investigate, an accountable owner, a rough scope, and a defensible use of resources. Reject, defer, or descope when the initiative has no meaningful objective, owner, evidence path, or available capacity.

## 5. Stage 1 — Product and mission framing

### Purpose

Translate the upstream system objective into a software-specific mission without losing the larger system context.

### Activities

Define the software product boundary, users, operators, customers, affected parties, value hypothesis, business or operational outcomes, success metrics, non-goals, constraints, dependencies, expected lifecycle, and public/operational claims. Identify what software must not decide and where humans retain authority.

### Outputs

- Product/mission brief.
- BRD or equivalent business/operational requirements view.
- Stakeholder and responsibility map.
- Product boundary and allocation map.
- Initial PRD or product-definition view.
- Initial ConOps/software operating narrative.
- Success metrics and failure consequences.
- Initial compliance and security applicability screen.

BRD and PRD are not universal standards with one mandatory format. They are useful views of business/operational need and product intent. In a small project they may be combined; in a complex programme they should be separated by audience and authority.

### Gate

The software objective, scope, users, outcomes, non-goals, and authority boundaries are understood well enough to investigate the problem. If the value hypothesis is weak or the software boundary is unclear, return to upstream systems/product work.

## 6. Stage 2 — Problem, user, and operational validation

### Purpose

Confirm that the software is addressing a real and sufficiently important problem, in a real workflow, for identifiable users or operators.

### Activities

Study current workflows, pain points, workarounds, stakeholders, incentives, environment, adoption barriers, accessibility, trust, user decisions, consequences of errors, and the relationship between software output and human action. Run interviews, observation, data analysis, experiments, prototypes, literature, or market research as appropriate.

Define hypotheses and determine what evidence would confirm or disconfirm them. Where the problem is poorly understood, validation should precede substantial build work. Cross-functional product workflows such as GitLab's treat validation as a track that may run ahead of build and may be shortened when confidence is already high [9].

### Outputs

- Validated problem statement.
- Workflow and stakeholder model.
- User/outcome hypotheses.
- Value, usability, feasibility, viability, and operational-risk findings.
- Updated ConOps.
- Product success measures.
- Minimum viable capability or minimum valuable change.
- Problem validation evidence and unresolved questions.

### Gate

Proceed when the problem and desired outcome are sufficiently understood and the project can name what successful use would look like. If the problem is not important, the workflow is inaccessible, or the claimed value cannot be measured, stop, reframe, or return upstream.

## 7. Stage 3 — Feasibility, R&D, and technical discovery

### Purpose

Retire the uncertainties most capable of overturning the product, requirements, architecture, or business case.

### Activities

Investigate data availability and quality, external APIs, hardware dependencies, open-source projects, model capability, performance, security, cost, licensing, scalability, integration, deployment, reliability, and legal/operational constraints. Compare build, buy, reuse, open-source, partner, and defer options.

Run narrow experiments and prototypes that answer high-value questions. A prototype must state its question, conditions, method, result, limitations, and effect on the decision. It must not be mistaken for final product evidence.

### Outputs

- R&D/feasibility report.
- Technology and dependency assessment.
- Build-versus-buy/open-source evaluation.
- Data and integration assessment.
- Benchmark or experiment results.
- Technical risk retirement plan.
- Revised cost/resource estimate.
- Revised assumptions and architecture drivers.
- Recommendation to proceed, change path, or descope.

### Gate

Proceed when the core path is feasible enough to define requirements and architecture, or when remaining uncertainty has a credible test and is not architecture-blocking. Return upstream when an assumption fails or a dependency makes the concept infeasible.

## 8. Stage 4 — Requirements engineering

### Purpose

Transform stakeholder and system needs into clear, measurable, consistent, feasible, traceable, and verifiable software requirements.

### Requirement classes

- Functional behaviour.
- User and workflow behaviour.
- Interfaces and integration contracts.
- Data quality, lineage, retention, and ownership.
- Performance, capacity, latency, and throughput.
- Availability, reliability, resilience, and recovery.
- Security, privacy, identity, access, and auditability.
- Safety, human authority, fail-safe behaviour, and misuse prevention.
- Accessibility and inclusive use where relevant.
- Maintainability, portability, compatibility, and supportability.
- Cost, energy, and resource constraints.
- Compliance and contractual obligations.
- Deployment, observability, migration, and operational requirements.
- AI/model requirements for evaluation, uncertainty, provenance, drift, and human oversight.

### Activities

Elicit, analyse, decompose, derive, allocate, negotiate, prioritise, document, verify, validate, baseline, and change-control requirements. Every requirement should have an owner, source, rationale, priority, status, acceptance/verification method, dependencies, and evidence state.

Requirements are iterated with users, systems engineering, safety, security, architecture, and implementation. NASA and ISO/IEC/IEEE guidance both treat requirements as lifecycle foundations rather than one-time documents [2] [3] [6].

### Outputs

- Stakeholder requirements view.
- System requirements allocated to software.
- Software requirements specification or equivalent.
- Quality-attribute requirements.
- Interface and data requirements.
- Acceptance criteria.
- Requirements traceability matrix/graph.
- Requirements verification and validation record.
- Requirements change log.

### Gate

Requirements are sufficiently clear, complete, consistent, feasible, prioritised, individually verifiable, and traceable. Open requirements must have owner and resolution path. A requirement may remain provisional only when its effect is controlled and the next phase can test it safely.

## 9. Stage 5 — Architecture and technical design

### Purpose

Define a durable software structure that satisfies requirements, exposes trade-offs, controls risk, and supports implementation, verification, operation, and future change.

### Architecture views

The architecture should include the views needed by the project:

- Context and system boundary.
- Stakeholders, users, actors, and trust boundaries.
- Logical decomposition and responsibilities.
- Runtime and data flows.
- APIs and external interfaces.
- Data model, storage, lineage, and lifecycle.
- Identity, access, secrets, and security controls.
- Deployment, infrastructure, environments, and topology.
- Performance, capacity, cost, and resource budgets.
- Failure, recovery, state, and degraded modes.
- Observability and operations.
- Evolution, compatibility, migration, and retirement.
- AI/model/tool boundaries and evaluation where relevant.

### Activities

Compare architecture alternatives against requirements and quality attributes. Record ADRs for significant decisions. Threat-model the design, identify hazards and abuse cases, analyse dependencies and supply chain, define interfaces and contracts, and identify what must be proven analytically or experimentally.

### Outputs

- Architecture baseline.
- System/software context.
- Architecture decision records.
- Design and interface specifications.
- Data and API contracts.
- Threat model and initial safety analysis.
- Quality-attribute trade-off record.
- Deployment and operations architecture.
- Architecture verification plan.
- Technical debt and evolution strategy.

### Gate

The architecture is coherent with requirements and ConOps, boundaries and interfaces are explicit, quality attributes have a credible treatment, security/safety risks are addressed, and implementation/test teams can work without guessing central design intent.

## 10. Stage 6 — Planning and implementation readiness

### Purpose

Convert the approved architecture into a controlled, executable construction plan.

### Activities

Define work breakdown, increments, dependencies, ownership, milestones, repositories, environments, coding standards, branching/merge policy, CI checks, secrets, dependency policy, data migrations, API compatibility, test strategy, observability, release strategy, and descope options.

Plan increments around small, meaningful, reversible slices. DORA's guidance supports small changes because they are easier to reason about, deploy, and recover [11].

### Outputs

- Delivery/implementation plan.
- Backlog or work-package map.
- Repository and environment plan.
- Coding and review standards.
- Dependency and component inventory.
- Test and quality strategy.
- Security implementation plan.
- Migration and compatibility plan.
- Release and rollback strategy.
- Handoff packages for implementation teams.

### Gate

Implementation can begin with bounded scope, known dependencies, acceptance conditions, testability, secure defaults, and a defined path to integration. If the plan depends on unverified architecture or missing access, return to R&D or architecture.

## 11. Stage 7 — Incremental implementation and integration

### Purpose

Build the product in reviewable increments while maintaining architectural, security, quality, and operational integrity.

### Activities

Implement code, data, configuration, infrastructure, tests, documentation, and migrations according to approved work packages. Use small self-contained changes, peer review, automated checks, reproducible builds, dependency controls, secret management, static analysis, and contract validation.

Google's public engineering-practice guidance treats code review as a code-health practice and separates author and reviewer responsibilities [13]. Microsoft SDL adds static analysis, binary analysis, secret scanning, encryption scanning, fuzzing, configuration validation, and component governance [9].

### Outputs

- Source code and configuration.
- Build artefacts and manifests.
- Unit/component tests.
- Updated documentation.
- Migration and interface changes.
- Code-review records.
- Automated-check results.
- Updated traceability and change impact.
- Known defect and technical-debt records.

### Gate

Each increment satisfies its work-package acceptance criteria, passes required automated/manual reviews, preserves interfaces and security controls, and is integrated into a testable baseline.

## 12. Stage 8 — Verification and validation

### Purpose

Establish both implementation correctness and real-world/product suitability.

### Verification levels

- Static/code/configuration analysis.
- Unit and component testing.
- API and contract testing.
- Integration testing.
- System/end-to-end testing.
- Regression testing.
- Performance, load, capacity, and latency testing.
- Resilience, failure-injection, recovery, and disaster testing.
- Security testing, scanning, fuzzing, penetration testing, and configuration review.
- Privacy and data-governance testing.
- Accessibility testing.
- Migration and compatibility testing.
- AI/model evaluation, red-team, drift, robustness, and misuse testing.
- Human acceptance and operational scenario testing.

### Validation questions

- Does the software solve the intended user or operational problem?
- Does it work in the customer/operator environment?
- Does it produce the intended action or outcome?
- Can users understand and safely rely on it?
- Does it respect the larger system's safety, privacy, and operational boundaries?
- Are the claims supported by the actual test conditions?

### Outputs

- Test strategy and plans.
- Test cases and data.
- Traceability from requirements to tests/results.
- Defect and remediation records.
- Performance/resilience/security results.
- Validation and acceptance report.
- Independent review findings.
- Residual-risk and claim register.

### Gate

The product meets its maturity-appropriate evidence threshold. Critical failures are resolved, mitigated, bounded, or accepted by appropriate authority. The team can state clearly what has been demonstrated and what remains unvalidated.

## 13. Stage 9 — Release readiness and deployment

### Purpose

Introduce the product into its environment with controlled risk, recovery, and ownership.

### Readiness checks

- Correct version and reproducible build.
- Requirements and test evidence complete for target maturity.
- Critical vulnerabilities and defects addressed or formally accepted.
- Configuration, secrets, identity, access, and data controls ready.
- Migrations tested and reversible where possible.
- Rollback or forward-fix plan ready.
- Monitoring, alerts, dashboards, logs, and tracing ready.
- Support, ownership, escalation, and runbooks assigned.
- Backup, restoration, disaster recovery, and business continuity addressed.
- User/operator communication, training, and documentation ready.
- Compliance, privacy, safety, and security approvals obtained where required.

### Deployment strategy

Use progressive rollout, canary/ring deployment, feature flags, staged environments, or equivalent controls when the product's risk warrants them. Microsoft SDL describes safe deployment rings and monitoring as part of release practice [9].

### Outputs

- Release candidate and release notes.
- Go/no-go/conditional decision.
- Deployment and rollback plan.
- Configuration and migration record.
- Operational readiness review.
- Support/runbook package.
- User communication and training.
- Release evidence and baseline.

### Gate

The release has an authorised owner, an evidence-backed risk position, operational controls, recovery path, and a rollout appropriate to consequences. A prototype release must not be represented as production readiness.

## 14. Stage 10 — Operations, reliability, and support

### Purpose

Operate the product, detect failure, support users, protect data, recover from incidents, and generate evidence for improvement.

### Activities

Monitor service health, usage, performance, capacity, cost, security, accessibility, data quality, user feedback, and business/product outcomes. Maintain alerts, runbooks, on-call or support ownership, incident response, vulnerability response, backup/recovery, and postmortems.

Use reliability targets and delivery measures proportionately. Google SRE uses error budgets to balance reliability and feature work [10]. DORA measures throughput and instability through change lead time, deployment frequency, recovery time, change fail rate, and deployment rework [11].

### Outputs

- SLO/SLI or equivalent service targets.
- Monitoring and alerting.
- Operations dashboard.
- Runbooks and escalation.
- Incident and vulnerability records.
- Postmortems and corrective actions.
- Reliability/cost/performance trends.
- User and product feedback.
- Updated roadmap, risk, and technical-debt records.

### Gate/feedback

Operations should continuously feed evidence back to product, requirements, architecture, security, and the upstream system framework. A severe incident or repeated failure can force a reliability-focused phase, architecture revision, or product descope.

## 15. Stage 11 — Evolution, maintenance, and retirement

### Purpose

Keep the product useful, secure, supportable, compatible, and economically justified throughout its life.

### Activities

Manage requirements change, roadmap, technical debt, dependency upgrades, platform changes, security fixes, model/data changes, migrations, compatibility, deprecation, ownership transition, data retention, and end-of-life.

### Outputs

- Change impact analysis.
- Updated requirements and ADRs.
- Technical-debt and upgrade plan.
- Compatibility/migration plan.
- Deprecation notice and support transition.
- Data preservation/deletion plan.
- Retirement/closeout record.
- Lessons and reusable patterns.

## 16. Enterprise handoff contract

Every handoff must include the source baseline, objective, decision supported, context, inputs, scope, exclusions, constraints, assumptions, evidence standard, expected artefact, acceptance criteria, dependencies, authority, risks, escalation triggers, and required project-state update.

The sender is responsible for a complete handoff. The receiver is responsible for checking that the handoff is sufficient before accepting work. The receiver may reject or return an incomplete handoff instead of silently guessing.

## 17. Artefact generation rule

The enterprise should maintain an underlying information graph rather than treating documents as independent silos. Views such as BRD, PRD, ConOps, SRS, architecture, ADR, threat model, compliance matrix, test plan, release checklist, runbook, and postmortem should be generated or maintained from linked project state.

This makes it possible to detect contradictions, propagate changes, identify missing evidence, and produce tailored views for product, engineering, security, operations, reviewers, regulators, customers, and executives.

## 18. Tailoring

A small prototype may combine the initiative brief, PRD, requirements, architecture, and test plan into a few concise artefacts. A high-impact enterprise system may require formally separated baselines, independent reviews, detailed traceability, specialist sign-offs, audit evidence, and controlled release. The underlying lifecycle remains the same; depth, formality, and independence increase with risk and consequence.

## References

[1] [ISO/IEC/IEEE 29148:2018 — Requirements engineering](https://www.iso.org/standard/72089.html)  
[2] [NASA NPR 7150.2D — Software Engineering Life Cycle Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)  
[3] [IEEE/ISO/IEC 15288-2023 — System life cycle processes](https://standards.ieee.org/ieee/15288/10424/)  
[4] [NIST Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf)  
[5] [OWASP SAMM](https://owaspsamm.org/model/)  
[6] [Microsoft Security Development Lifecycle](https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle)  
[7] [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/)  
[8] [Google SRE Error Budget Policy](https://sre.google/workbook/error-budget-policy/)  
[9] [GitLab Product Development Flow](https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/)  
[10] [Google Engineering Practices Documentation](https://google.github.io/eng-practices/)  
[11] [ISO/IEC 25010:2023 Product quality model](https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:en)  
[12] [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)  
[13] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
