# Enterprise Software Assurance, Safety, Security, Compliance, and Operations v1

## 1. Purpose

Enterprise software quality is not one property and cannot be established by one final test. The software subsystem must create a defence-in-depth assurance system in which product value, technical correctness, security, privacy, safety, compliance, reliability, operability, and maintainability are addressed throughout the lifecycle.

The assurance subsystem should be activated according to consequence, novelty, uncertainty, reversibility, exposure, and maturity. It should not impose high-assurance ceremony on a harmless prototype, but it must not permit a high-impact system to inherit prototype-level controls.

## 2. Assurance dimensions

| Dimension | Core question | Typical evidence |
|---|---|---|
| Product/value | Does the software solve the intended problem and create the intended outcome? | User research, acceptance, outcome measures, operational observation |
| Functional correctness | Does the implementation satisfy functional requirements? | Unit, integration, system, acceptance tests, traceability |
| Quality attributes | Is it sufficiently performant, reliable, maintainable, portable, accessible, and usable? | Quality requirements, benchmarks, load/resilience tests, reviews |
| Security | Does it resist misuse, attack, unauthorised access, and supply-chain compromise? | Threat model, ASVS controls, scans, tests, penetration assessment |
| Privacy | Is data collected, used, shared, retained, and deleted lawfully and appropriately? | Data inventory, privacy assessment, access controls, retention/deletion evidence |
| Safety | Can failures cause physical, clinical, financial, environmental, or critical operational harm? | Hazard analysis, safeguards, fail-safe behaviour, safety review, validation |
| Compliance | Are applicable laws, regulations, standards, contracts, and policies addressed? | Applicability assessment, compliance matrix, control evidence, specialist review |
| Reliability/operations | Can the service be operated, monitored, recovered, and supported? | SLOs/SLIs, monitoring, runbooks, incident/recovery tests |
| Maintainability | Can it be changed, upgraded, migrated, and retired without unacceptable risk? | Architecture, dependency inventory, technical debt, migration and deprecation plans |
| Claim integrity | Are internal and public claims proportional to evidence? | Claim register, provenance, limitations, independent review |

## 3. Security and privacy lifecycle

### Preparation

Identify the product's data and assets, stakeholders, threat environment, exposure, business impact, applicable obligations, security ownership, and required verification level.

### Requirements

Define security and privacy requirements from data classification, threats, regulations, industry practice, prior incidents, and operational context. Requirements should be versioned, testable, traceable, and assigned to an owner.

### Design

Create system context and data-flow diagrams, define trust boundaries, enumerate actors and abuse cases, model threats, choose security architecture, establish identity/access, secrets, encryption, isolation, logging, retention, and recovery.

Threat models must be living artefacts. Changes to architecture, data, integrations, deployment, or attack surface should trigger review.

### Implementation

Use approved languages/frameworks, secure coding standards, dependency and component governance, secret management, static analysis, code review, secure defaults, configuration control, and reproducible builds.

### Verification

Use risk-appropriate static analysis, dependency and license scanning, secret scanning, binary/container analysis, fuzzing, configuration validation, authentication/authorisation tests, security tests, privacy tests, and penetration testing where appropriate. OWASP ASVS can provide versioned, testable application-security requirements [1].

### Release and response

Require vulnerability status, risk acceptance, remediation plans, monitoring, incident response, rollback, and ownership before release. Post-release vulnerabilities and incidents should produce corrective actions and feed back to threat models, requirements, architecture, and secure-development practice.

## 4. Safety and high-impact system controls

The system should classify harm before choosing assurance depth. Relevant harm classes include physical injury, clinical harm, financial loss, legal exposure, privacy harm, environmental damage, discrimination, critical-service interruption, reputational damage, and unsafe automation.

For high-impact systems, the enterprise should create:

- hazard and failure-mode analysis;
- safety constraints and derived controls;
- safe-state and fallback behaviour;
- human authority and override policy;
- automation-bias and over-reliance analysis;
- fault detection and degraded modes;
- incident escalation and response;
- monitoring and auditability;
- verification and validation evidence;
- independent specialist review;
- and external authority requirements.

For AI/agentic systems, this expands to model/data provenance, evaluation sets, failure taxonomy, uncertainty handling, tool permission boundaries, prompt/instruction conflict, misuse, privacy, drift, monitoring, and human approval. NIST AI RMF provides a risk-management complement to ordinary software and security controls [2].

The system must not use model confidence, test pass rate, or fluent output as a substitute for safety evidence.

## 5. Compliance and legal control

Compliance begins with applicability, not with copying a generic checklist. The enterprise must identify the jurisdiction, sector, data types, product claims, contractual commitments, deployment geography, affected persons, and regulatory classification.

The compliance workstream produces:

1. An applicability assessment.
2. A register of obligations and authoritative interpretations.
3. Mapping from obligation to requirement, control, owner, evidence, and status.
4. Gaps, exceptions, compensating controls, and due dates.
5. Review and sign-off requirements.
6. Change monitoring for regulatory or contractual updates.
7. A statement of what has been assessed and what remains outside enterprise authority.

A compliance matrix is not legal advice or certification. Formal sign-off must come from the required legal, regulatory, clinical, security, or certification authority.

## 6. Verification architecture

Verification must be layered:

### Creator checks

The author or builder checks the work against its work package, requirements, coding/design standards, and acceptance criteria.

### Peer review

A technically competent peer checks correctness, clarity, maintainability, risks, and omissions. Google engineering practice treats code review as a code-health control and separates change author and reviewer responsibilities [3].

### Automated checks

CI and build pipelines run tests, static analysis, dependency/security scans, schema checks, contract checks, formatting/linting, reproducibility checks, and policy checks.

### Specialist review

Security, privacy, safety, data, performance, accessibility, domain, legal/compliance, or operations specialists review relevant risk areas.

### Independent review

A separate team or reviewer challenges high-consequence architecture, claims, failure modes, and evidence. The reviewer should not have a direct incentive to approve its own work.

### Red-team challenge

The red-team actively seeks failures, misuse, bypasses, hidden dependencies, alternative solutions, misleading claims, and conditions outside the happy path.

### Acceptance/authority review

The appropriate customer, operator, product authority, mission owner, regulator, clinical authority, or other decision-maker decides whether residual risk is acceptable.

## 7. Quality engineering

Quality attributes should be derived from the system context and made measurable. ISO/IEC 25010 describes how a quality model can support requirements, design objectives, testing objectives, quality-control criteria, acceptance criteria, and product-quality measures [4].

The enterprise should define a quality profile for each product. A quality profile may cover functional suitability, performance, compatibility, usability/accessibility, reliability, security, maintainability, flexibility/portability, observability, cost, and operational fitness as relevant.

Each quality attribute should have:

- a requirement or target;
- rationale and affected stakeholders;
- architecture implications;
- measurement method;
- test or review method;
- acceptance threshold;
- owner;
- known trade-offs;
- and residual limitation.

Quality is not identical to code coverage. Tests must be connected to risk, requirements, usage, failure consequences, and real operating conditions.

## 8. Release and operational assurance

Before release, the operational readiness review should confirm:

- version, build provenance, and reproducibility;
- requirement and test evidence;
- defect, vulnerability, privacy, safety, and compliance status;
- configuration and secrets;
- data migration and rollback;
- deployment and release strategy;
- monitoring, logging, tracing, and alerting;
- SLO/SLI or equivalent reliability measures;
- support ownership and escalation;
- runbooks and recovery procedures;
- backups, restoration, disaster recovery, and continuity;
- cost/capacity expectations;
- user/operator communication and training;
- and known limitations and claim boundaries.

The release decision should identify who approved it, what evidence was reviewed, which residual risks were accepted, and what conditions apply.

## 9. Operational learning loop

After release, operations are part of engineering. The enterprise observes:

- availability and latency;
- errors and change failures;
- recovery time;
- usage and adoption;
- user outcomes;
- security events and vulnerabilities;
- data quality and drift;
- cost and capacity;
- support load;
- accessibility issues;
- and unexpected behaviour.

Incidents produce postmortems that identify root cause, detection gap, contributing conditions, customer impact, corrective action, owner, due date, and affected architecture/requirements. Recurring instability can require a reliability-focused phase before more feature work, following the principle of SRE error budgets [5]. DORA metrics can provide delivery feedback on throughput and instability [6].

## 10. Handoff and separation-of-duty rules

A handoff is complete only when the receiver can act without silently guessing. It includes context, objective, scope, constraints, inputs, requirements, interfaces, evidence, acceptance, risks, authority, and update obligations.

A creator should not be the sole approver of high-impact work. Where the project is small and roles must be combined, the conflict is recorded and an independent review is added before the consequence-bearing gate.

Security, safety, compliance, and operations teams should be involved early enough to influence requirements and architecture. They must not be reduced to final document generators.

## 11. Assurance proportionality

| Project profile | Assurance minimum |
|---|---|
| Low-risk reversible tool | Automated tests, peer review, basic security, owner acceptance, backup/recovery appropriate to data |
| Public prototype/demo | Reproducible build, central proof test, basic dependency/security review, limitations and data handling |
| Internal operational product | Requirements, architecture, access control, monitoring, backup, support, rollback, acceptance, incident process |
| Enterprise product | Full traceability, independent security/quality review, operational readiness, recovery, change control, compliance mapping |
| Safety/high-impact product | Hazard/safety analysis, independent assurance, specialist/external review, controlled deployment, audited evidence |
| AI/agentic high-impact product | Model/data evaluation, red-team, tool permission, human authority, provenance, drift, abuse response, continuous monitoring |

## 12. What the virtual enterprise should automate

It should automate evidence collection, traceability links, document/view generation, status and dependency tracking, test execution, policy checks, change-impact analysis, release checklists, monitoring summaries, risk reminders, and continuity updates.

It should assist with threat modelling, requirements quality checks, architecture challenge, test generation, code review, incident analysis, compliance evidence mapping, and red-team scenario generation.

It should not silently automate high-impact approvals, legal conclusions, clinical authority, safety certification, production actions with uncontrolled blast radius, or public claims beyond verified evidence.

## References

[1] [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)  
[2] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)  
[3] [Google Engineering Practices](https://google.github.io/eng-practices/)  
[4] [ISO/IEC 25010:2023 Product quality model](https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:en)  
[5] [Google SRE Error Budget Policy](https://sre.google/workbook/error-budget-policy/)  
[6] [DORA Software Delivery Performance Metrics](https://dora.dev/guides/dora-metrics/)
