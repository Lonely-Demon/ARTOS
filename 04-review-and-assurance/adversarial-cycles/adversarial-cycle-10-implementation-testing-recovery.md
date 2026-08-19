# Adversarial Cycle 10 — Implementation, Testing, Observability, and Recovery

## Review question

Can the enterprise turn its architecture into reproducible, testable, observable, recoverable work, or does the conceptual design fail when it meets code, tools, state, deployment, and real incidents?

## Reviewer lenses

### Build/reproducibility engineer

The implementation baseline mentions reproducible builds and provenance but does not establish a minimum reproducibility contract. Without pinned dependencies, source/configuration baselines, build environment, toolchain, data/model versions, and artifact integrity, a result may not be rebuildable or auditable.

**Revision:** Define reproducibility levels: rerunnable analysis, reproducible build, repeatable test, independently rebuilt artifact, and deployable rollback image. Each level records what is fixed, what is variable, and what evidence is required.

### Test architect

The test list risks becoming a checklist detached from failure consequences. Testing must be derived from requirements, hazards, threats, architecture, quality profile, and operational scenarios. It must include test oracles and define what a failure means.

**Revision:** Add risk-based test design with coverage of requirements, architecture paths, states, transitions, interfaces, failure modes, abuse modes, configurations, environments, and user outcomes. Track untestable claims explicitly.

### AI evaluation lead

For AI and agents, conventional pass/fail tests are insufficient. Outputs may be variable, contextual, and difficult to oracle. Evaluation sets can leak into tuning, become stale, or fail to cover rare but dangerous behaviour.

**Revision:** Add evaluation governance: dataset separation, scenario taxonomy, adversarial tests, human evaluation protocol, calibration, uncertainty, drift, regression, cost/latency, tool/permission, memory, and red-team results. Define release thresholds and rollback triggers.

### Observability architect

Telemetry is not the same as understanding. OpenTelemetry provides vendor-neutral instrumentation for traces, metrics, and logs, but does not provide the backend or decide what is meaningful [1]. A virtual enterprise needs semantic events that join mission, project, work package, agent, tool, data, decision, artefact, approval, and deployment context.

**Revision:** Add an enterprise semantic event model and trace context. Define redaction, retention, access, integrity, sampling, time synchronization, cost, and observability coverage. Observability must not leak secrets or sensitive research.

### Incident responder

The current recovery idea is not operationally executable without recovery objectives, authority, procedures, preserved evidence, and tested restoration. NIST SP 800-61 Rev. 3 places incident response within broader cybersecurity risk management, linking preparation, detection, response, recovery, and improvement [2].

**Revision:** Add incident classes, severity, detection sources, containment authority, playbooks, communication, evidence preservation, affected-scope discovery, state/credential repair, rollback, recovery objectives, verification, and post-incident changes.

### State-integrity reviewer

The operating kernel is a high-value stateful system. A corrupted current projection, stale cache, partial branch merge, or false event can alter mission state and downstream decisions. Backups alone do not establish logical correctness.

**Revision:** Add immutable event/history where appropriate, state hashes or integrity checks, snapshot/restore, replay, branch reconciliation, conflict handling, idempotent transitions, invariant checks, and human review for high-impact repair.

### Release engineer

Progressive delivery can limit blast radius but may be impossible for some physical, regulated, or tightly coupled systems. Rollback may also be unsafe if data migrations, external side effects, or learned model states are not reversible.

**Revision:** Classify reversibility and define rollback, roll-forward, compensating action, quarantine, and manual recovery paths. Test restoration and compensation, not merely deploy rollback.

## Falsifications

### Falsification 1 — Passing tests means ready

Tests may miss unmodelled hazards, wrong requirements, integration effects, operational conditions, or human misuse. Readiness requires evidence across the relevant assurance profile.

### Falsification 2 — Code coverage measures assurance

Coverage can show executed code paths without showing requirement, state, threat, user, data, or failure-mode coverage.

### Falsification 3 — Telemetry equals observability

Logs and traces without semantic context, accessible storage, correct sampling, integrity, and response procedures may not support diagnosis or accountability.

### Falsification 4 — Backup equals recovery

A backup can be stale, incomplete, corrupted, inaccessible, or logically inconsistent. Recovery must be exercised and verified against defined objectives.

### Falsification 5 — Rollback is universally safe

External side effects, migrations, data changes, notifications, model updates, and physical actions may not be reversible. Recovery may require compensation or human intervention.

### Falsification 6 — Independent review catches everything

Reviewers are constrained by time, evidence visibility, expertise, incentives, and framing. Testing and assurance require layered methods, adversarial scenarios, and operational feedback.

## Accepted implementation revisions

1. Add reproducibility tiers and build/test provenance requirements.
2. Derive testing from risk, requirements, hazards, threats, states, interfaces, and outcomes.
3. Add AI/agent evaluation governance and release/rollback thresholds.
4. Add semantic execution context across the kernel and workers.
5. Add privacy/security controls for telemetry and audit data.
6. Add incident playbooks and recovery objectives for workers, tools, data, credentials, artefacts, and project state.
7. Add state invariants, snapshots, replay, reconciliation, idempotence, and repair authority.
8. Classify reversibility and provide rollback, roll-forward, compensation, quarantine, and manual recovery paths.
9. Test recovery and incident response as operational capabilities.
10. Feed incident, test, and observability evidence into requirements, architecture, assurance, capability cards, and project continuity.

## Cycle 10 judgement

The conceptual architecture can become implementable only when it defines reproducibility, semantic execution events, test oracles, recovery objectives, state integrity, and non-reversible side effects. The corrected implementation model is **evidence-producing, observable, replayable where possible, and recoverable according to defined consequences—not merely coded and tested**.

## References

[1] [OpenTelemetry — What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)  
[2] [NIST SP 800-61 Rev. 3 Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
