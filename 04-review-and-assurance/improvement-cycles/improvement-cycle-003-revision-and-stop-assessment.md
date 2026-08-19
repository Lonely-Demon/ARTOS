# Improvement Cycle 003 Revision and Stop Assessment

## Focus

This cycle targeted the operating kernel itself: remote/local trust assumptions, worker/tool authorization, execution visibility, state recovery, and the ability to reconstruct what actually happened across recursive work.

## New evidence

NIST Zero Trust Architecture states that trust should not be inferred from network location or ownership and that authentication and authorization are discrete functions before resource access [1]. OpenTelemetry provides a vendor-neutral approach to generating, exporting, and collecting traces, metrics, and logs across applications and infrastructure [2].

## Accepted revisions

### 1. Zero-trust kernel boundary

The kernel must not trust a worker because it is local, because it is part of the project, or because it was previously approved. Each request to access a resource or cause a side effect requires identity, context, scope, permission, and risk-appropriate authorization. Permissions should expire, be revocable, and be visible in the audit trail.

### 2. Execution trace

The kernel should create a trace context for every material work package and propagate it through capability activation, retrieval, model calls, tool calls, file changes, reviews, approvals, tests, deployments, incidents, and state updates. The trace is not a raw conversation transcript; it is an operational record of what was attempted, by whom/what, with which inputs, under which policy, producing which artefacts and effects.

### 3. Event and state separation

The kernel should distinguish an append-only or tamper-evident event/audit history from current-state projections. Current state is convenient to read and edit through authorised transitions; history is needed to reconstruct, compare, repair, and investigate. A state update should not erase the event that caused it.

### 4. Branch/merge control

Parallel work should occur in branch-local working states. A merge packet must identify the baseline, changed entities, conflicting requirements/decisions, evidence differences, affected claims, and proposed resolution. The canonical baseline updates only after an authorised synthesis/review transition.

### 5. Observability as a first-class kernel service

The kernel should measure not only application health but enterprise execution: queue and worker health, latency/cost, retries, blocked work, duplicate work, evidence retrieval, tool failures, authority denials, reviewer findings, rework, state changes, and incident response. Metrics must support diagnosis and improvement rather than reward output volume.

## Stop assessment

The first three improvement cycles have now covered the major conceptual control categories:

- universal recursive capability decomposition;
- dynamic project assembly and cross-branch collaboration;
- evidence, provenance, claims, and assurance arguments;
- requirements, architecture, software lifecycle, security, safety, compliance, quality, operations, and retirement;
- AI governance and agentic threat modelling;
- supply-chain transparency and build provenance;
- incident response and postmortem learning;
- capability competence and activation trust;
- portfolio/economic control and marginal-value stopping;
- zero-trust access, state recovery, and execution observability.

Further broad research into additional lifecycle frameworks is now unlikely to change the top-level architecture enough to justify its cost. The remaining uncertainty is primarily implementation and calibration uncertainty: how the kernel schemas, permissions, versioning, merge logic, worker sandbox, evaluation, and user workflow perform in an actual project.

The correct next improvement is therefore not another abstract research sweep. It is a controlled implementation/calibration cycle in which the kernel is tested with a real but bounded project and the resulting failures feed a new targeted cycle.

## Residual uncertainties requiring implementation or external validation

1. The data model needs a real storage and versioning implementation.
2. Zero-trust policy must be translated into concrete identity, secret, sandbox, network, and tool controls.
3. Event/audit history must be tested for integrity, privacy, retention, replay, and repair.
4. Branch/merge semantics must be tested with concurrent work and contradictory outputs.
5. Capability competence and diversity measures require real task outcomes and calibration.
6. Assurance-case authoring must be tested for usefulness versus burden.
7. Agentic red-team scenarios require actual worker/tool implementations.
8. The local/remote control-plane boundary requires deployment-specific threat modelling.
9. Human and external authority requirements remain domain-specific and cannot be replaced by this framework.

## References

[1] [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)  
[2] [OpenTelemetry: What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
