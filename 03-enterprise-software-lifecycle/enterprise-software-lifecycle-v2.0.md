# Enterprise Software Lifecycle Subsystem v2.0

**Parent:** Universal Virtual Enterprise Blueprint v2.0  
**Input:** An upstream project/system concept with problem model, operating context, requirements, factors, evidence, alternatives, selected direction, risks, claims, and validation needs.  
**Output:** A software product or subsystem whose maturity-appropriate product, engineering, security, safety, privacy, compliance, assurance, deployment, operations, and evolution evidence is traceable.

## 1. What this subsystem is

This subsystem translates a system or product concept into software that can be understood, built, tested, secured, deployed, operated, maintained, and retired. It is not a document factory and not a single waterfall sequence. It is a linked information and execution lifecycle with continuous loops for discovery, delivery, assurance, operations, and learning.

The lifecycle is **risk-adaptive**. Low-risk, reversible work can move through lightweight continuous discovery and delivery. Novel, irreversible, regulated, safety-sensitive, privacy-sensitive, or high-impact work requires stronger baselines, independent review, external authority, explicit assurance, and controlled release. The artefacts are views over linked project objects; they are created to enable decisions, handoffs, tests, governance, operations, or continuation.

## 2. Inputs and authority boundary

The upstream framework supplies the problem and system context, stakeholders, ConOps, factors, alternatives, requirements at the system level, selected concept, interfaces, risks, evidence states, assumptions, claims, and validation gaps. The software subsystem translates those into software responsibility, product outcomes, software requirements, architecture, implementation, and operation.

The software subsystem may recommend, design, implement, test, and prepare evidence. It cannot self-authorise legal compliance, clinical acceptability, safety certification, regulatory approval, or high-impact deployment. It must identify when an external human authority or specialist review is required.

## 3. Lifecycle control loops

| Loop | Core question | Main control |
|---|---|---|
| Portfolio/value | Is this software effort worth the investment and consequence? | Value, opportunity cost, resource, and stop decision. |
| Product/discovery | Is this the right user problem, workflow, and outcome? | User/system evidence, ConOps, product hypothesis, adoption. |
| Requirements | What must the software do and how well? | Traceable, validated, verifiable requirements and quality profile. |
| Architecture | How should it be structured, secured, operated, and evolved? | Viewpoints, ADRs, threat model, interfaces, assurance case, baselines. |
| Implementation | Can it be built and integrated with controlled change? | Small changes, review, provenance, component governance, handoffs. |
| Verification | Does it satisfy requirements and controls? | Risk-based tests, security, safety, accessibility, performance, data/model evaluation. |
| Validation | Does it solve the real problem in context? | User, operator, domain, outcome, and field evidence. |
| Release/operations | Can it be introduced, monitored, supported, and recovered? | Progressive deployment, ownership, SLOs, incidents, rollback/compensation. |
| Evolution/retirement | Should it change, remain, migrate, or end? | Change impact, freshness, debt, deprecation, retention, and closure. |

These loops overlap. An operational incident may reopen requirements and architecture. A feasibility discovery may change the product scope. A security finding may stop implementation. A user observation may invalidate an outcome hypothesis.

## 4. Stage 0 — Intake, framing, and portfolio decision

Record the raw request, upstream concept baseline, sponsor, intended users, domain, maturity target, consequences, expected value, resource envelope, deadline, dependencies, and authority requirements. Classify whether the software is a prototype, experiment, internal tool, product, subsystem, or high-impact service.

The portfolio decision considers opportunity cost, scarce capabilities, reuse, expected value of additional research, cost/latency, risk, reversibility, and stop conditions. It records what would justify pause, pivot, descope, or stop.

**Views:** initiative brief, business/mission case, portfolio assessment, initial capability activation plan, resource/risk envelope.  
**Gate:** Is the effort worth discovery at this consequence and investment level?

## 5. Stage 1 — Product, system, and operating definition

Translate the upstream mission into a software mission. Define product boundary, users, operators, stakeholders, outcomes, non-goals, software responsibility, authority, human decisions, external systems, data, and lifecycle. Create a Concept of Operations and system context describing actual use with people, procedures, hardware, data, and external services.

Include accessibility, support, training, maintenance, procurement, adoption, failure consequences, and operating environment at the appropriate depth. Detailed UI/UX belongs in a linked specialist view; the master system retains the decisions that affect workflow, safety, accessibility, authority, and outcomes.

**Views:** BRD/business view, PRD/product view, ConOps, system context, responsibility map, outcome metrics, claims boundary, initial privacy/security/compliance screen.  
**Gate:** Is the software problem, value, authority, scope, and operating context clear enough to validate?

## 6. Stage 2 — Problem, solution, and human validation

Validate the problem, workflow, solution hypothesis, user/operator context, usefulness, usability, accessibility, adoption, viability, and operational fit. Use observation, interviews, domain review, experiments, prototypes, data, and customer/operator participation as appropriate. Preserve contradictory findings and record what would disconfirm the proposition.

Human-centred design is iterative: understand context, specify requirements, produce design solutions, and evaluate them. A successful demo is not adoption evidence; satisfaction is not the whole value case; a nominal human approval is not meaningful oversight.

**Views:** validated problem/solution hypotheses, workflow model, user/operator evidence, minimum valuable capability, adoption/change-readiness, accessibility and human-authority analysis, residual uncertainty.  
**Gate:** Is the software worth building, and is the value proposition sufficiently supported for the intended maturity?

## 7. Stage 3 — Technical feasibility and research

Investigate data, integrations, APIs, open-source components, models, tools, performance, cost, licensing, deployment, privacy, security, reliability, scaling, accessibility, recovery, and operational dependencies. Use small experiments to retire architecture-changing uncertainty.

Every experiment records its question, conditions, method, configuration, result, limits, affected decision, evidence state, and next action. Register datasets, models, sources, tools, workers, dependencies, licences, versions, hashes where possible, build path, freshness, evaluation, known threats, and rollback.

**Views:** feasibility report, benchmark, architecture spike, build/buy/reuse analysis, component/model/source registry, SBOM and provenance plan, cost/resource estimate, risk-retirement plan.  
**Gate:** Are the architecture-changing uncertainties retired, controlled, bounded, or explicitly deferred?

## 8. Stage 4 — Requirements and quality profile

Derive stakeholder, system, software, data, interface, operational, security, privacy, safety, compliance, accessibility, and quality requirements from the upstream concept, ConOps, hazards, threats, architecture drivers, human context, and lifecycle needs.

Requirements must be clear, feasible, prioritised, traceable, validated, and individually verifiable where appropriate. Requirement validity is distinct from requirement quality: a well-written requirement can still express the wrong need. Record source, rationale, owner, priority, status, acceptance, verification method, evidence state, dependencies, affected capabilities, and change history.

The quality profile selects relevant attributes such as functional suitability, performance, compatibility, usability/accessibility, reliability, security, maintainability, portability, observability, cost, energy, resilience, and AI trustworthiness. Quantitative targets define the target/measurand, conditions, uncertainty, reference, and decision threshold.

**Views:** stakeholder/system/software requirements, SRS, quality profile, safety/security/privacy requirements, data/interface contracts, acceptance criteria, traceability graph, baseline/change log.  
**Gate:** Are requirements and quality targets valid, testable, traceable, and accepted at the intended authority level?

## 9. Stage 5 — Architecture, design, and assurance

Create architecture views for context, functional structure, interfaces, data, storage, identity, trust, deployment, quality, cost, failure, recovery, observability, evolution, external dependencies, and operations. Use architecture viewpoints appropriate to stakeholder concerns; there is no single sufficient architecture diagram.

Threat-model workers, agents, tools, memory, sources, models, dependencies, data, integrations, deployment, and human interactions. Use ADRs for significant decisions, including options, criteria, rationale, consequences, rejected alternatives, dependencies, and revisit triggers.

For material claims, build an assurance case with claim, subclaims, argument, evidence, assumptions, defeaters/rebuttals, justifications, reviewer, residual gap, and expiry/review trigger. The case may conclude insufficient assurance or inadmissible claim.

**Views:** architecture baseline, design, ADRs, API/data contracts, threat model, hazard/safety analysis, privacy impact, compliance mapping, assurance case, quality trade-off record, deployment/operations architecture, architecture verification plan.  
**Gate:** Is the architecture coherent across requirements, human context, security, safety, data, supply chain, operations, cost, and assurance?

## 10. Stage 6 — Planning and implementation readiness

Create work packages that include objective, context, source baseline, requirements, interfaces, constraints, evidence contract, acceptance, dependencies, authority, prohibited changes, cost/latency budget, escalation, and return path. Decompose by meaningful risk and value, not arbitrary task count.

Define repository, branching, code review, CI/CD, environments, secrets, dependency, migration, compatibility, test, observability, rollout, rollback/compensation, and support practices. Assign work only to capability cells with adequate competence, freshness, access, authority, independence, and capacity.

Handoff modes are explicit: consultation, contribution, delegation, review, approval, ownership transfer, collaboration, service, or facilitation. A handoff transfers only what the contract states.

**Views:** delivery plan, backlog/work-package graph, implementation standards, capability assignments, component registry, test strategy, secure-development plan, migration/compatibility plan, release strategy, handoff packages.  
**Gate:** Are the increments, interfaces, environments, controls, ownership, acceptance, and recovery paths ready?

## 11. Stage 7 — Implementation and integration

Build code, data, infrastructure, configuration, tests, migrations, documentation, and integrations through small, reviewable changes. Use reproducible builds to the required level and capture source, toolchain, dependency, configuration, model/data, and environment provenance.

Maintain SBOM/component inventory, licences, vulnerabilities, exceptions, exploitability status, and rollback. Apply automated checks for tests, static analysis, secrets, dependencies, licences, configuration, policy, schemas, contracts, reproducibility, and observability. Apply independent peer review for material changes. Record deviations, decisions, technical debt, and impact.

For agentic systems, separate plan from execute, validate tool parameters and outputs, enforce permissions at runtime, isolate context and memory, preserve execution traces, and use dry-run/approval for consequential actions.

**Views:** source/build baselines, tests, review results, provenance, SBOM, dependency/licence status, traceability updates, defects, risks, technical debt, execution traces.  
**Gate:** Has the implementation produced controlled evidence and remained within baseline, authority, and scope?

## 12. Stage 8 — Verification, validation, and independent assurance

Verification tests satisfaction of requirements and controls. Validation tests whether the system solves the intended problem in its intended context. Both are required.

Test strategy is risk-based and covers requirements, architecture paths, states, transitions, interfaces, configurations, threats, hazards, misuse, data quality, user outcomes, recovery, performance, accessibility, migration, and supply chain. Code coverage is not sufficient assurance.

AI/agent evaluation covers model/data/prompt lineage, evaluation-set separation, scenario taxonomy, adversarial behaviour, tool permissions, prompt/instruction conflict, memory, inter-agent trust, robustness, calibration, drift, human oversight, cost, latency, regression, and rollback thresholds.

Independent assurance reviews claims, argument, evidence, assumptions, defeaters, source freshness, capability competence, security, privacy, safety, compliance, operations, and external-validation requirements.

**Views:** test evidence, defect/remediation record, replication status, assurance status, red-team findings, acceptance report, residual-risk/claim register, release recommendation.  
**Gate:** Do the available evidence and authority support the claims and maturity transition?

## 13. Stage 9 — Release and progressive deployment

Release readiness includes reproducible version, requirements/test evidence, defects/vulnerabilities, data/configuration, secrets, migrations, rollback or compensation, monitoring, ownership, runbooks, backup/recovery, support, user communication, training, compliance, safety, security, accessibility, and known limitations.

Use feature flags, canary/ring deployment, staged environments, progressive exposure, quarantine, or equivalent controls according to risk. The release authority records proceed, proceed with conditions, delay, rollback, roll-forward, compensation, descope, or stop.

**Views:** release candidate, release notes, readiness packet, go/no-go decision, deployment/rollback/compensation plan, operational baseline, support package, claim boundary.  
**Gate:** Can this maturity level be introduced, monitored, supported, and recovered within the defined authority and consequence envelope?

## 14. Stage 10 — Operations, incidents, and feedback

Operations monitor health, usage, performance, cost, security, privacy, data quality, model drift, user outcomes, accessibility, and product value. Maintain ownership, SLO/SLI or equivalent targets, dashboards, semantic traces, alerts, runbooks, support, backup/recovery, incident response, vulnerability response, and postmortems.

Incidents include worker misuse, tool compromise, credential exposure, prompt injection, poisoned memory, false evidence, state corruption, data breach, deployment failure, model drift, unsafe outcome, and ordinary software failure. Response includes detection, containment, permission revocation, evidence preservation, scope discovery, replay, state repair or rollback, claim impact review, notification, recovery verification, and control updates.

Observability is not merely logs. The system needs semantic context joining mission, project, work package, worker, tool, data, decision, artefact, approval, deployment, and incident. Telemetry must have privacy, integrity, retention, access, sampling, and cost controls.

**Views:** service ownership, SLO/SLI, dashboards, incident playbooks, runbooks, backups, recovery objectives, postmortems, outcome/value reports, capability-card updates, assurance updates.  
**Gate:** Is the product controlled, useful, reliable, secure, supportable, and improving in its actual environment?

## 15. Stage 11 — Evolution, retirement, and learning

Manage change impact, technical debt, upgrades, dependencies, data/model/prompt changes, compatibility, regulatory changes, support ownership, deprecation, data retention/deletion, migration, and retirement. Every material change identifies affected requirements, decisions, architecture, tests, assurance claims, permissions, operations, public claims, and external authority.

Retired components and knowledge remain traceable for audit, incident analysis, legal obligations, and future reuse. A system is not complete merely because it has launched; it is complete when its continued operation, evolution, or retirement is responsibly controlled.

**Gate:** Is continued operation justified, or can the system be migrated or retired safely and accountably?

## 16. Lifecycle tailoring

The subsystem selects a quality and control profile by consequence, reversibility, novelty, uncertainty, external side effects, data sensitivity, user vulnerability, legal context, and operational blast radius. The profile determines required evidence depth, independence, approval, testing, configuration control, human authority, deployment pattern, and operations.

A reversible prototype may need a concise frame, requirements, threat screen, peer review, test evidence, and clear limitations. A healthcare, aerospace, financial, infrastructure, or agentic system with consequential effects may need formal safety/privacy cases, strong baselines, independent assurance, external authority, field validation, monitored rollout, and post-market controls.

## 17. Core anti-failure rules

The subsystem must never treat document count as maturity, a passing test as general validity, a successful demo as adoption, a human checkbox as meaningful oversight, a primary source as automatically true, a model confidence score as calibrated certainty, a security scan as overall security, a backup as recovery, or an approved plan as a safe execution.

It must preserve dissent, negative evidence, failed tests, contradictory findings, unverified claims, and conditions outside the evidence boundary. It must be able to conclude that a feature, release, claim, project, or entire path should stop.

## 18. References

[1] [ISO/IEC/IEEE 29148 Requirements Engineering](https://www.iso.org/standard/72089.html)  
[2] [ISO/IEC/IEEE 25010 Product Quality](https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:ed-2:v1:en)  
[3] [ISO/IEC 15026-2 Assurance Case](https://www.iso.org/standard/52926.html)  
[4] [ISO/IEC/IEEE 42010 Architecture Description](https://www.iso.org/standard/50508.html)  
[5] [NASA NPR 7150.2D Software Engineering Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)  
[6] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)  
[7] [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)  
[8] [NIST Privacy Framework](https://www.nist.gov/privacy-framework)  
[9] [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)  
[10] [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)  
[11] [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)  
[12] [MITRE ATLAS](https://atlas.mitre.org/)  
[13] [CISA Software Bill of Materials](https://www.cisa.gov/topics/information-communications-technology-software-supply-chain-security/sbom)  
[14] [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/)  
[15] [Team Topologies](https://teamtopologies.com/key-concepts)  
[16] [DORA Software Delivery Metrics](https://dora.dev/guides/dora-metrics/)  
[17] [NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design)
