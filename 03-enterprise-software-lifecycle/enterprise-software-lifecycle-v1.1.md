# Enterprise Software Lifecycle Subsystem v1.1

**Parent:** Universal Virtual Enterprise v1.1  
**Status:** Revised after Improvement Cycle 001  
**Input:** Upstream project/system concept package  
**Output:** A software product or subsystem with maturity-appropriate product, engineering, assurance, security, operations, and lifecycle evidence.

## 1. Revision summary

Version 1.0 defined the full software lifecycle. Version 1.1 adds controls required for a universal enterprise that coordinates specialist and agentic teams:

- capability cards and competence/freshness evidence;
- assurance-case argumentation in addition to flat claim/evidence links;
- kernel and worker threat models;
- agentic incident response and state repair;
- data, model, source, tool, dependency, licence, and SBOM governance;
- quality profiles and measurable quality attributes;
- portfolio, cost, latency, and value-of-information controls;
- build provenance and component/VEX handling;
- AI management-system concerns and continual improvement;
- coverage and omission review;
- and operational feedback tied to requirements, architecture, claims, and upstream systems.

## 2. Lifecycle control model

The software subsystem remains a set of overlapping loops:

| Loop | Core question | Control additions in v1.1 |
|---|---|---|
| Product/value | Is this the right problem and outcome? | Portfolio value, user evidence, outcome metrics |
| Requirements | What must software do and how well? | Quality profile, safety/security/privacy, traceability |
| Architecture | How should it be structured and evolve? | Threat/assurance case, supply-chain and agent boundaries |
| Implementation | Can it be built and integrated safely? | Capability cards, handoff contracts, provenance, small changes |
| Verification | Is it correct and secure under relevant conditions? | Independent review, ASVS, fuzzing, abuse/misuse, assurance evidence |
| Release | Can this version be introduced and recovered? | Progressive rollout, approvals, SBOM, rollback, monitoring |
| Operations | Is it useful, reliable, secure, and supportable? | SLOs, incident response, postmortems, cost, outcome, drift |
| Evolution | What should change, remain, or retire? | Change impact, freshness, model/data governance, deprecation |

## 3. Capability readiness before delegation

Before assigning a material software task to a team, agent, tool, or external provider, the enterprise evaluates its capability card:

- relevant domain and method;
- demonstrated competence or benchmark evidence;
- knowledge/source freshness;
- known blind spots and failure modes;
- independence and conflicts;
- authority and side-effect permissions;
- data and tool access required;
- cost/latency profile;
- and required reviewer or external authority.

A coding agent may be competent at implementing a bounded change but not at architecture approval. A security scanner may detect classes of issues but not establish overall security. A language model may synthesise research but not serve as legal or clinical authority. Capability cards make these boundaries explicit.

## 4. Stage 0 — Intake and portfolio decision

Record the raw request, upstream concept version, sponsor, intended users, domain, maturity, consequences, expected value, resource envelope, deadline, dependencies, and initial risk. Assess whether the software effort is a product, subsystem, internal tool, prototype, experiment, or high-impact service.

Add portfolio questions:

- What is the opportunity cost?
- Which capabilities are scarce?
- What can be reused?
- What is the minimum valuable investment?
- What is the expected value of additional research?
- What would cause pause, pivot, descope, or stop?

**Outputs:** initiative brief, business/mission case, portfolio decision, initial capability activation plan, budget and risk envelope.

## 5. Stage 1 — Product, system, and operating definition

Translate the upstream system objective into a software mission. Define product boundary, users, operators, stakeholders, outcomes, value, non-goals, lifecycle, authority, human decisions, software responsibilities, and system interfaces.

Maintain a Concept of Operations and system context that shows how software is used with people, hardware, data, procedures, and external systems. Record affected parties, failure consequences, support expectations, accessibility, adoption, and operational environment.

**Outputs:** BRD/business view, PRD/product view, ConOps/software operating narrative, responsibility map, success metrics, claims boundary, initial security/privacy/compliance screen, and capability activation request.

## 6. Stage 2 — Problem and solution validation

Validate the user problem, workflow, value hypothesis, proposed solution, usability/accessibility, feasibility, viability, adoption, and operational fit. Product validation may run ahead of build and may overlap with technical feasibility. When confidence is already high and risk is low, the team can shorten the path; when confidence is low, it must continue validation before expensive implementation.

Use research, observation, interviews, experiments, prototype interaction, data, domain review, and customer/operator involvement. Preserve contradictory findings and record what would disconfirm the proposition.

**Outputs:** validated problem and solution hypotheses, user/outcome evidence, workflow model, MVC or minimum valuable capability, updated ConOps, metrics, and residual uncertainty.

## 7. Stage 3 — Technical feasibility and R&D

Investigate data, integrations, APIs, open-source components, models, tools, performance, cost, licensing, deployment, security, privacy, reliability, scaling, accessibility, and operational dependencies.

For every major experiment, record the question, conditions, method, result, limitations, affected decision, evidence state, and next action. Register datasets, models, sources, tools, dependencies, and builds with version, provenance, licence/rights, evaluation, freshness, and known limitations.

**Outputs:** feasibility report, benchmark, architecture spikes, build/buy/reuse assessment, component/model/source registry, SBOM/build-provenance plan, cost/resource estimate, risk retirement plan, and recommendation.

## 8. Stage 4 — Requirements engineering and quality profile

Derive requirements from stakeholders, system objectives, ConOps, hazards, security/privacy/compliance, architecture drivers, quality model, and operational needs. Requirements must be clear, complete, consistent, feasible, prioritised, traceable, and individually verifiable [1] [2].

The quality profile converts vague quality goals into requirements, measures, design objectives, test objectives, acceptance criteria, and owners. It may include functional suitability, performance, compatibility, usability/accessibility, reliability, security, maintainability, portability, observability, cost, energy, resilience, and AI trustworthiness as relevant [3].

For each requirement record source, rationale, priority, owner, status, acceptance method, verification method, evidence state, dependencies, affected capability, and change history.

**Outputs:** stakeholder/system/software requirements, quality profile, safety/security/privacy requirements, interface/data requirements, acceptance criteria, traceability graph, requirements V&V record, and baseline/change log.

## 9. Stage 5 — Architecture, design, and assurance case

Define context, decomposition, interfaces, data flows, storage, identity, trust boundaries, deployment, quality attributes, costs, failure modes, recovery, valid/invalid states, observability, evolution, and external dependencies.

Threat-model the system, including supply chain, data, integrations, workers, agents, tools, memory, and deployment. For high-impact claims, create an assurance case containing top-level claim, subordinate claims, argument, evidence, assumptions, rebuttals, justifications, reviewer status, and residual gap. Assurance cases can support safety, reliability, maintainability, operability, human factors, and security claims [4].

Use ADRs for significant decisions, including options, criteria, rationale, consequences, rejected alternatives, dependencies, and revisit triggers. Use architecture review independent of the creator when risk warrants it.

**Outputs:** architecture baseline, design, ADRs, API/data contracts, threat model, hazard/safety analysis, assurance case, quality trade-off record, deployment/operations architecture, and architecture verification plan.

## 10. Stage 6 — Planning and implementation readiness

Create implementation work packages with objective, context, source baseline, requirements, interfaces, constraints, evidence contract, acceptance, dependencies, authority, prohibited changes, and escalation. Decompose work into small, meaningful, reversible increments.

Define repository, branching, code-review, CI/CD, environments, secrets, dependency, migration, compatibility, testing, observability, rollout, rollback, and support practices. Assign work only to capability cells whose competence, access, and authority are adequate.

**Outputs:** delivery plan, backlog/work-package graph, implementation standards, component registry, test strategy, secure-development plan, migration/compatibility plan, release strategy, and handoff packages.

## 11. Stage 7 — Implementation and integration

Build code, data, infrastructure, configuration, tests, documentation, migrations, and integrations through small reviewable changes. Use reproducible builds and capture build provenance. Maintain SBOM/component inventory, licences, vulnerabilities, exceptions, and VEX-style exploitability information where applicable; CISA identifies SBOM as a key software security and supply-chain building block [5].

Apply automated checks for tests, static analysis, secret exposure, dependencies, licences, configuration, policy, schemas, contracts, and reproducibility. Apply manual peer review separated from the author for material changes. Record deviations and change impact.

**Outputs:** source and build baselines, test changes, review results, build provenance, SBOM, dependency/license status, updated traceability, defects, risks, and technical debt.

## 12. Stage 8 — Verification, validation, and independent assurance

Verification includes static, unit, component, integration, contract, system, regression, performance, resilience, recovery, security, privacy, accessibility, migration, data-quality, and configuration tests as applicable. OWASP ASVS can provide versioned security requirements and verification criteria for web applications [6].

AI/agentic software additionally requires evaluation sets, model/data provenance, failure taxonomy, robustness, misuse, prompt/instruction conflict, tool permission, memory access, inter-agent trust, drift, cost, and human-oversight tests. OWASP's 2026 agentic guidance identifies agentic AI as a distinct security-risk domain for systems that plan, act, and decide across workflows [7].

Validation asks whether the system works for the intended users and environment, creates the intended outcome, and can be safely relied upon within its scope.

The independent assurance team reviews the assurance case, claims, evidence, risks, source freshness, capability competence, security, safety, compliance, operations, and external-validation requirements.

**Outputs:** test evidence, defect/remediation record, assurance case status, red-team findings, acceptance report, residual-risk/claim register, and release recommendation.

## 13. Stage 9 — Release and progressive deployment

Release readiness checks include reproducible version, requirements/test evidence, defects/vulnerabilities, data and configuration, secrets, migrations, rollback, monitoring, ownership, runbooks, backup/recovery, support, user communication, training, compliance, safety, and security.

Use feature flags, canary or ring deployment, progressive rollout, staged environments, or equivalent controls according to risk. The release authority records whether to proceed, proceed with conditions, delay, rollback, descope, or stop.

**Outputs:** release candidate, release notes, readiness packet, go/no-go decision, deployment/rollback plan, operational baseline, support package, and claim boundary.

## 14. Stage 10 — Operations, incidents, and feedback

Monitor health, usage, performance, cost, security, data quality, model drift, user outcomes, accessibility, and product value. Maintain SLO/SLI or equivalent targets, dashboards, alerts, runbooks, support, backup/recovery, incident response, vulnerability response, and postmortems.

NIST SP 800-61 Rev. 3 places incident-response recommendations throughout cybersecurity risk management to improve preparation, detection, response, recovery, and effectiveness [8]. The same principle applies to agent incidents and project-state corruption.

Agent incidents require special handling: disable/quarantine workers, revoke permissions, preserve evidence, replay actions, compare project state, repair or roll back affected artefacts, assess claim impact, notify authorities, and update threat models and controls.

Operational evidence changes product requirements, architecture, roadmap, risks, capability cards, assurance cases, and upstream system assumptions. A serious incident can force a reliability or security freeze before feature work continues.

## 15. Stage 11 — Evolution, retirement, and learning

Manage change impact, technical debt, upgrades, dependency/model changes, data migration, compatibility, regulatory changes, support ownership, deprecation, data retention/deletion, and retirement.

Every significant change should identify affected requirements, decisions, architecture, tests, assurance claims, permissions, operations, and public claims. Retired components and knowledge should remain traceable for audit, incident analysis, or future reuse.

## 16. Artefacts as generated views

The enterprise should maintain a linked information graph and produce views such as:

- initiative brief and business case;
- BRD and PRD;
- ConOps and system context;
- requirements and SRS;
- quality profile;
- feasibility/R&D report;
- architecture and ADRs;
- data/API contracts;
- threat model and hazard/safety analysis;
- assurance case;
- privacy/compliance matrix;
- component/model/source registry and SBOM;
- delivery plan and work packages;
- test strategy and evidence;
- release readiness and rollback;
- runbooks, SLOs/SLIs, and monitoring;
- incident/postmortem;
- change, debt, migration, deprecation, and retirement records.

These names are views for different audiences. They should share identifiers, provenance, baseline, version, owner, status, and traceability.

## 17. Lifecycle gates

| Gate | Minimum question |
|---|---|
| Portfolio | Is this worth discovery at the proposed cost and consequence? |
| Product | Is the software problem, value, user, scope, and authority clear? |
| Feasibility | Are the architecture-changing uncertainties retired or controlled? |
| Requirements | Are requirements and quality targets testable, traceable, and validated? |
| Architecture | Is structure, security, safety, data, supply chain, and operations coherent? |
| Build | Are increments, contracts, environments, controls, and acceptance ready? |
| Assurance | Do independent reviews support the claims and expose residual risk? |
| Release | Can this maturity level be deployed, monitored, supported, and recovered? |
| Operations | Is the product controlled, useful, reliable, secure, and improving? |
| Retirement | Is continued operation justified, or can the system be migrated/retired responsibly? |

## 18. References

[1] [ISO/IEC/IEEE 29148 Requirements Engineering](https://www.iso.org/standard/72089.html)  
[2] [NASA NPR 7150.2D Software Engineering Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)  
[3] [ISO/IEC 25010 Product Quality Model](https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:en)  
[4] [ISO/IEC 15026-2 Assurance Case](https://www.iso.org/standard/52926.html)  
[5] [CISA Software Bill of Materials](https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom)  
[6] [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)  
[7] [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)  
[8] [NIST SP 800-61 Rev. 3 Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)  
[9] [ISO/IEC 42001 AI Management Systems](https://www.iso.org/standard/42001)  
[10] [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)  
[11] [Microsoft Security Development Lifecycle](https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle)  
[12] [Google Engineering Practices](https://google.github.io/eng-practices/)  
[13] [GitLab Product Development Flow](https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/)
