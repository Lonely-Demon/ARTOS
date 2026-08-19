# Adversarial Cycle 03 — Enterprise Software Lifecycle and Artefacts

## Review question

Does the enterprise software lifecycle create a reliable path from concept to operated product, or does it create a document-heavy waterfall, duplicate artefacts, and fragile handoffs that slow delivery without improving quality?

## Reviewer lenses

### Product leader

The lifecycle has the right concerns but risks treating BRD, PRD, ConOps, requirements, SRS, architecture, and assurance as sequential documents. In practice, these are often living views of one evolving product/system model. If teams must finish each document before learning from users or implementation, the process will lock in bad assumptions.

**Revision:** Treat artefacts as versioned views and baselines of a linked information graph. Allow discovery, feasibility, architecture, and implementation to overlap while controlling which claims and decisions are mature enough to baseline.

### Agile/continuous-delivery reviewer

The lifecycle’s stages can be interpreted as gated handoffs rather than feedback loops. That would conflict with small changes, continuous integration, progressive delivery, and operational learning. A gate should control risk and authority, not prohibit all useful learning before a document is complete.

**Revision:** Add two levels of flow: a continuous delivery loop for low-risk/reversible work and an evidence-gated loop for consequential changes. The same lifecycle applies, but the depth, independence, and approval threshold vary by consequence, reversibility, novelty, and blast radius.

### Enterprise architect

The document list does not specify which artefact is authoritative when views disagree. A PRD, SRS, ADR, test, runbook, and deployed configuration may all claim different behaviour.

**Revision:** Every controlled artefact needs authority, baseline, version, status, owner, source requirements, affected claims, supersession, and verification. The kernel should detect contradictions rather than merely link documents.

### Requirements engineer

The requirements stage risks accepting “testable” requirements that are not actually validated against user outcomes, operational context, or architecture. A requirement can be syntactically clear and still be wrong, unnecessary, or impossible to operate.

**Revision:** Separate requirement quality from requirement validity. Require source, rationale, stakeholder validation, technical feasibility, acceptance method, verification method, and change impact. Preserve rejected requirements and why they were rejected.

### Security and privacy lead

The lifecycle includes security/privacy, but a single stage can tempt teams to complete threat modelling once and treat the system as safe. Threats change with architecture, dependencies, deployment, data, and attacker knowledge.

**Revision:** Make threat and privacy review recurring events triggered by boundary, dependency, data, privilege, model, deployment, and major change updates.

### AI/ML lead

AI systems do not fit ordinary build-test-release semantics. Model/data/prompt changes may change behaviour without changing application code. Evaluation can be dataset-specific and may decay in production.

**Revision:** Add an AI/model lifecycle gate for dataset and model lineage, evaluation coverage, drift, human oversight, rollback, approval, and allowed operating context. Model/data/prompt changes are configuration changes with impact analysis.

### Operations lead

The lifecycle ends too cleanly at operations. An enterprise product needs explicit service ownership, support model, on-call or escalation, incident taxonomy, cost ownership, capacity, resilience, data retention, and end-user communication. A runbook alone does not create operational readiness.

**Revision:** Add a service acceptance package: owner, support tier, SLO/SLI or equivalent, dependencies, runbooks, dashboards, alerts, backup/recovery, incident procedures, cost budget, known limitations, and retirement triggers.

### Handoff and team-design reviewer

The lifecycle says work packages should contain context and acceptance, but it does not define whether a handoff is a transfer of ownership, a request for contribution, or a review. These are different interactions and should not be conflated.

**Revision:** Define handoff modes: consultation, contribution, delegation, review, approval, and ownership transfer. Each has different authority, feedback, acceptance, and completion semantics.

## Falsifications

### Falsification 1 — More artefacts guarantee enterprise quality

A large document set can increase inconsistency, stale information, and process theatre. Quality comes from decisions, evidence, traceability, review, implementation, operation, and learning—not document count.

### Falsification 2 — Gates must be sequential and universal

Low-risk software can move continuously; high-impact software requires stronger gates. A universal process that uses the high-assurance path for every change will be unusable.

### Falsification 3 — Requirements are fixed before implementation

Requirements are hypotheses about need and behaviour. Implementation, user observation, operations, and security review can invalidate them. Change should be controlled, not prohibited.

### Falsification 4 — Software release is the end of the pipeline

Operational and product evidence may reveal that the software is not useful, safe, secure, affordable, or maintainable. Release is a transition into another evidence-producing phase.

### Falsification 5 — One test strategy covers all software

Web systems, data pipelines, AI agents, safety-sensitive software, infrastructure, and internal tools require different verification profiles. A universal lifecycle needs a quality/test profile selector, not one universal checklist.

## Accepted lifecycle revisions

1. Artefacts become linked, versioned views with explicit authority and baseline status.
2. Gates become risk-adaptive decision points rather than mandatory sequential document approvals.
3. Add continuous discovery/delivery and a separate evidence-gated path for high-consequence changes.
4. Add contradiction detection between requirements, architecture, tests, runbooks, configuration, and deployment.
5. Add recurring security/privacy/threat review triggers.
6. Add an AI/model/data/prompt lifecycle gate and configuration-impact rules.
7. Add a service-acceptance package with explicit ownership and operational obligations.
8. Distinguish consultation, contribution, delegation, review, approval, and ownership-transfer handoffs.
9. Add quality-profile and test-strategy tailoring by consequence, reversibility, novelty, and blast radius.
10. Treat operations and retirement as evidence-producing lifecycle phases, not postscript documentation.

## Cycle 3 judgement

The lifecycle baseline is directionally correct but would become harmful if interpreted as a mandatory waterfall or document factory. The revised form is a **risk-adaptive, linked-information lifecycle** with continuous learning for ordinary work and evidence-gated control for consequential work. This is a major correction because the virtual enterprise must be capable of both elite depth and practical speed.
