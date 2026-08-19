# Universal Enterprise Operating Kernel — Local Reference Slice

This directory contains the first local-first implementation increment of the Universal Virtual Enterprise. It is deliberately a **reference slice**, not the full multi-agent harness.

## What it currently proves

The implementation stores one project’s structured current state in SQLite, preserves append-only event history, supports typed traceability links, enforces selected lifecycle transitions, records evidence states, controls claim upgrades, executes bounded work-package and handoff flows, records gates and conditional progression, validates review-only worker returns, and generates Markdown/JSON continuation packets.

The TabVolt retrospective calibration demonstrates how an existing project record can be mapped into the model while preserving historical evidence boundaries and unresolved validation gaps.

## Files

| File | Purpose |
|---|---|
| `kernel.py` | SQLite-backed operating-kernel reference implementation. |
| `workflow.py` | Work packages, assignments, handoffs, review, gates, and continuation helpers. |
| `worker_contract.py` | Transport-neutral task-package and worker-result boundary. |
| `test_kernel.py` | Acceptance, workflow, worker-contract, and adversarial regression tests. |
| `calibrate_tabvolt.py` | Retrospective calibration against the historical TabVolt record. |
| `minimum-operational-contract-v0.2.md` | Implemented minimum contract and explicit non-goals. |
| `component-evaluation-matrix-v0.1.md` | Candidate worker evaluation criteria and provisional mapping. |
| `open-source-component-audit-v0.md` | Static public-repository audit of DeerFlow, OpenHands, OpenManus, Hermes, and OpenClaw. |
| `adversarial-test-report-v0.1.md` | Test coverage, defects, repairs, and residual risks. |

## Run locally

From this directory:

```bash
python3 -m unittest -v
python3 cli.py seed-demo --db demo.sqlite3
python3 calibrate_tabvolt.py
```

The calibration command creates `calibration-output/` containing a SQLite project database, a machine-readable report, a human-readable report, and generated continuation material.

## Safety boundary

The current slice has no remote worker execution, arbitrary tool invocation, external messaging, deployment, authentication, multi-tenant isolation, or autonomous approval. It is side-effect free outside its own SQLite database and generated files. Future workers must enter through the typed adapter contract and return results for review; they must not write canonical state directly.

## Current evidence state

The automated tests are **Measured locally**. The architecture and contracts are **Design inference**. The TabVolt retrospective contains a mixture of historical participant-observed local measurements, design inferences, hypotheses, and explicitly excluded claims. No result here proves domain expertise, independent review, real-world energy savings, production security, or universal enterprise quality.

## Next implementation increment

The next increment should add a narrow adapter API around the kernel, policy evaluation for task packages, concurrency/recovery tests, and one isolated worker experiment. DeerFlow and OpenHands are the first candidates for that experiment, but neither is the authority layer or canonical source of truth.
