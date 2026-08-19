# 05 — Operating Kernel

This is the executable reference spine of the Universal Virtual Enterprise. It converts a bounded part of the architecture into testable local behaviour while preserving strict authority and evidence boundaries. It is deliberately a **reference slice**, not the full multi-agent harness.

## Areas

| Path | Contents |
|---|---|
| `implementation/` | Kernel, workflow facade, local API, worker contract, worker smoke harness, CLI, and automated tests. |
| `contracts/` | Minimum operational contract and operating-kernel data model/roadmap. |
| `evaluations/` | Open-source component audit, evaluation matrix, and captured public README materials. |
| `calibrations/tabvolt/` | Retrospective TabVolt mapping script and generated calibration outputs. |
| `reports/validation/` | Adversarial test report, autonomous gap-closure report, final test log, and worker smoke report. |

## What the reference slice currently proves

The implementation stores one project’s structured current state in SQLite, preserves append-only event history, supports typed traceability links, enforces selected lifecycle transitions, records evidence states, controls claim upgrades, executes bounded work-package and handoff flows, records gates and conditional progression, validates review-only worker returns, and generates Markdown/JSON continuation packets.

The TabVolt retrospective calibration demonstrates how an existing project record can be mapped into the model while preserving historical evidence boundaries and unresolved validation gaps.

## Local validation

From this directory, run:

```bash
cd implementation
python3 -m unittest -v
python3 worker_smoke.py
```

The calibration script is under `calibrations/tabvolt/`. Its outputs are intentionally separated from source code. Runtime databases, Python bytecode, and temporary test artefacts must remain untracked.

## Safety boundary

The current slice has no remote worker execution, arbitrary tool invocation, external messaging, deployment, authentication, multi-tenant isolation, or autonomous approval. It is side-effect free outside its own SQLite database and generated files. Future workers must enter through the typed adapter contract and return results for review; they must not write canonical state directly.

The local API is unauthenticated and intended for localhost development only. It must not be exposed remotely in its current form.

## Evidence boundary

Passing automated tests establish **Measured locally** behaviour of this implementation under the tested cases. The architecture and contracts are **Design inference**. The TabVolt retrospective contains a mixture of historical participant-observed local measurements, design inferences, hypotheses, and explicitly excluded claims. No result here proves domain expertise, independent review, real-world energy savings, production security, or universal enterprise quality.

## Next implementation increment

The next increment should add a narrow adapter API around the kernel, policy evaluation for task packages, concurrency/recovery tests, and one isolated worker experiment. DeerFlow and OpenHands are the first candidates for that experiment, but neither is the authority layer or canonical source of truth.
