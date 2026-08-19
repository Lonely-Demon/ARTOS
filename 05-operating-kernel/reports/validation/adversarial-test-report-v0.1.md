# Operating Kernel Adversarial Test Report v0.1

**Scope:** Local-first reference kernel, workflow facade, worker contract, and TabVolt retrospective calibration.

## Evidence boundary

All results in this report are measured locally from automated tests and static source inspection. They demonstrate behaviour of this reference implementation under the tested cases; they do not demonstrate production security, multi-user isolation, domain correctness, or real-world project value.

## Test coverage

The suite contains 17 passing tests covering:

| Attack or acceptance case | Result |
|---|---|
| Create and reload a project | Pass |
| Create minimum objects and typed traceability links | Pass |
| Reject invalid project and work-package transitions | Pass |
| Require explicit reason for claim evidence-state upgrade | Pass |
| Record gate packet, review, conditional proceed, and project advancement | Pass |
| Preserve append-only event chain and reconstruct projection | Pass |
| Roll back an interrupted transaction | Pass |
| Generate Markdown and JSON continuation packets | Pass |
| Preserve tombstone history while hiding deleted entities from normal reads | Pass |
| Execute work-package assignment, handoff, acknowledgement, submission, and review | Pass |
| Return rejected work for rework | Pass |
| Require explicit task-package tool/path/side-effect boundaries | Pass |
| Keep worker results review-only and prevent direct claim upgrades | Pass |
| Reject cross-project traceability links | Pass |
| Activate a draft project only when a gate proceeds | Pass |
| Seed a self-consistent demo project | Pass |

## Defects found and repaired

### Cross-project contamination

The first implementation validated that link endpoints existed but did not verify that both endpoints belonged to the supplied project. This could have allowed a malformed or compromised caller to connect evidence, claims, or decisions across project boundaries. The kernel now rejects cross-project links, and a regression test covers the condition.

### Historical tombstone visibility

The first ordinary query path hid tombstoned records correctly but also made it impossible to inspect them through the historical query mode. This conflicted with the audit requirement. Normal reads still hide tombstones, while `include_deleted=True` exposes the retained historical record.

### Gate activation from draft

A project that proceeded through its first gate could remain in `draft` status while advancing its phase. The gate transition now activates a draft project when the decision is proceed or conditional proceed.

### Test expectation mismatch

One test initially treated `active → completed` as invalid even though the lifecycle correctly permits completion. The test was corrected rather than weakening the transition table.

## Remaining adversarial risks

The reference implementation still has important gaps. SQLite access is local and not designed for concurrent multi-process writers. Event-chain integrity detects tampering but does not prevent a privileged process from rewriting the database. The projection rebuild currently covers entity creation and updates but is not a complete event-sourced database recovery engine. The worker contract validates shapes, not worker truthfulness. There is no authentication, multi-tenant isolation, encryption-at-rest policy, network policy enforcement, sandbox implementation, secrets manager, or formal authorization engine. These are intentionally outside the first slice but must be addressed before remote or consequential execution.

The calibration project also reveals a workflow risk: a historical project can be mapped richly while still lacking independent validation. The kernel preserves that gap through evidence states, claim limitations, and conditional gates, but it cannot create missing evidence by itself.

## Current conclusion

The kernel reference slice is internally coherent and testable enough to serve as a construction baseline. It is not yet safe to expose as a multi-user or remotely reachable service, and it is not yet a substitute for external domain review or controlled experimentation. The next engineering increment should focus on a real API/CLI adapter, explicit policy evaluation, concurrency/recovery testing, and a first scoped worker integration in an isolated environment.
