# ARTOS — Universal Virtual Enterprise Workspace

ARTOS is the canonical repository for the Universal Virtual Enterprise project. It contains the original project evidence, the synthesized collaboration model, canonical architecture and lifecycle outputs, assurance records, the operating-kernel implementation, evaluations, calibrations, and durable continuity state.

The repository is organized by **evidence role and lifecycle position**, not by the order in which files happened to be created. Numbered directories are intentional: they provide a stable navigation path for future sessions and agents.

## Start here

A new session should read the following in order:

| Order | Path | Purpose |
|---:|---|---|
| 1 | [`00-control/README.md`](00-control/README.md) | Repository governance and navigation rules. |
| 2 | [`00-control/continuity/working-continuity-state.md`](00-control/continuity/working-continuity-state.md) | Durable project state, decisions, residual gaps, and next action. |
| 3 | [`01-source-archive/consolidation/operational-extract.md`](01-source-archive/consolidation/operational-extract.md) | Compact collaboration and reasoning model. |
| 4 | [`01-source-archive/consolidation/comprehensive-report.md`](01-source-archive/consolidation/comprehensive-report.md) | Detailed evidence-reconciled collaboration model. |
| 5 | [`02-canonical-architecture/drafts/universal-enterprise-blueprint-v2.0.md`](02-canonical-architecture/drafts/universal-enterprise-blueprint-v2.0.md) | Current canonical universal-enterprise architecture baseline. |
| 6 | [`03-enterprise-software-lifecycle/enterprise-software-lifecycle-v2.0.md`](03-enterprise-software-lifecycle/enterprise-software-lifecycle-v2.0.md) | Current canonical software lifecycle subsystem. |
| 7 | [`05-operating-kernel/README.md`](05-operating-kernel/README.md) | Executable reference implementation and its boundaries. |

## Repository map

| Directory | Contents | Status |
|---|---|---|
| `00-control/` | Repository manifest, placement policy, continuity state, and governance. | Authoritative control layer. |
| `01-source-archive/` | Original conversations, sequential snapshots, and original consolidation outputs. | Immutable provenance archive; do not rewrite source files. |
| `02-canonical-architecture/` | Universal Enterprise architecture versions and capability/assembly drafts. | Architecture baselines and linked drafts. |
| `03-enterprise-software-lifecycle/` | Enterprise software lifecycle versions, assurance operations, research corpus, and findings. | Lifecycle subsystem and supporting research. |
| `04-review-and-assurance/` | Improvement cycles, ten adversarial cycles, change logs, and residual critiques. | Review and challenge record. |
| `05-operating-kernel/` | Kernel implementation, contracts, worker evaluations, calibration, tests, and validation reports. | Executable reference system. |
| `06-collaboration-and-methodology/` | Extraction protocols, reasoning-model artifacts, collaboration analysis, and methodology documents. | Supporting method and behavioural context. |
| `07-project-reference-extracts/` | Compact NHAI extracts, workflow maps, archive skim indexes, and cross-project navigation aids. | Derived navigation and project precedent. |
| `08-experiments-and-projects/` | Bounded project calibrations, isolated worker experiments, and their evidence packages. | Active validation and integration work. |
| `09-release-artifacts/` | Versioned packaged releases and export bundles. | Generated deliverables; source remains elsewhere. |

## Evidence discipline

The repository distinguishes **Verified**, **Measured locally**, **Estimated**, **Design inference**, **Hypothesis**, **Open**, and **Excluded** evidence states. Original conversations and generated reports are evidence of what was discussed or observed in their context; they are not automatically authoritative external facts. Synthetic tests and retrospective calibrations do not establish independent real-world validation.

The operating kernel is a local reference implementation, not yet a production multi-agent harness, secure remote service, multi-tenant system, or proof of universal domain competence.

## Canonical working rule

The repository is the project’s source of truth. Sandbox copies may be used for execution, but material implementation, research, generated reports, and continuity changes must be reconciled into ARTOS before they are treated as canonical. Runtime databases, Python bytecode, temporary logs, and other reproducible execution artefacts must remain untracked.
