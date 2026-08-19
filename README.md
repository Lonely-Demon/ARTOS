# ARTOS — Universal Virtual Enterprise Workspace

ARTOS is the canonical repository workspace for the Universal Virtual Enterprise project. It contains the original project conversations, snapshots, consolidated collaboration model, and the first local-first operating-kernel reference implementation.

## Repository contents

| Path | Role |
|---|---|
| Root Markdown files | Original project conversation exports covering NHAI, VitalNet, TabVolt, LegacyBridge, EcoFarm, and related work. |
| `snapshots/` | Sequential reasoning snapshots preserved during the original synthesis process. |
| `consolidation/comprehensive-report.md` | Detailed evidence-reconciled model of the user’s working style and collaboration requirements. |
| `consolidation/operational-extract.md` | Compact reloadable operational extract for future sessions and agents. |
| `operating-kernel-reference/` | Executable local-first reference slice of the Universal Enterprise operating kernel, workflow facade, API adapter, worker contract, tests, calibration, and audits. |

## Canonical working rule

Future work on the Universal Virtual Enterprise should begin by inspecting this repository, especially the operational extract, comprehensive report, relevant snapshots, and the latest operating-kernel implementation state. The original project exports are evidence and precedent; they are not automatically authoritative external facts.

The repository is the project’s canonical source workspace. Local sandbox copies may be used for execution, but material implementation and continuity changes should be reconciled back into ARTOS rather than maintained only outside the repository.

## Current implementation state

The operating-kernel reference is deliberately bounded. It supports project state, typed entities and links, append-only events, evidence states, claims, decisions, risks, work packages, handoffs, gates, continuation packets, a local API, and a review-only worker boundary. It is not yet a production multi-agent harness, secure remote service, multi-tenant system, or proof of universal domain competence.

The current implementation has passed its local automated suite and a synthetic worker-boundary smoke test. The TabVolt calibration is retrospective and must not be interpreted as independent validation of either TabVolt or the larger framework.

## Evidence discipline

The project preserves the following distinctions:

- **Verified:** supported by an appropriate external or independently checked source.
- **Measured locally:** observed in the local implementation or historical project environment.
- **Estimated:** calculated or modelled from stated assumptions.
- **Design inference:** reasoned architecture or workflow proposal.
- **Hypothesis:** plausible but not sufficiently tested.
- **Open:** unresolved and requiring future evidence.
- **Excluded:** a claim or path that must not be presented as established.

Synthetic tests, prototypes, generated documents, and historical conversation reports must never be presented as independent real-world validation.
