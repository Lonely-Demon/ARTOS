# ARTOS File-Placement Policy

ARTOS should remain navigable as the project grows. New material must be placed according to what it is and how it should be used, not according to the session in which it was created.

## Placement rules

| Material | Location | Rule |
|---|---|---|
| Original conversation export | `01-source-archive/conversations/` | Preserve exact source content; do not edit for later interpretation. |
| Sequential reasoning snapshot | `01-source-archive/snapshots/` | Preserve snapshot order and original filename when possible. |
| Original consolidation output | `01-source-archive/consolidation/` | Preserve provenance; later corrections belong in a new version elsewhere. |
| Current continuity state | `00-control/continuity/` | One active durable state file; update after material decisions or phase changes. |
| Architecture baseline or version | `02-canonical-architecture/` | Keep versioned baselines; mark superseded drafts rather than deleting them. |
| Software lifecycle baseline or supporting corpus | `03-enterprise-software-lifecycle/` | Separate lifecycle specifications from research and assurance material. |
| Adversarial review or improvement cycle | `04-review-and-assurance/` | Preserve reviewer lens, findings, accepted revisions, and residual uncertainty. |
| Kernel source and tests | `05-operating-kernel/implementation/` | Source code and automated tests only; no runtime databases. |
| Kernel contracts and data models | `05-operating-kernel/contracts/` | Interfaces, schemas, state models, and implementation contracts. |
| Worker/component evaluation | `05-operating-kernel/evaluations/` | Matrix, audit, and captured public source materials. |
| Calibration case | `05-operating-kernel/calibrations/<case>/` | Inputs, mapping scripts, outputs, and case-specific notes. |
| Validation report | `05-operating-kernel/reports/validation/` | Test results, adversarial reports, smoke reports, and limitations. |
| Collaboration/methodology support | `06-collaboration-and-methodology/` | Behavioural model, extraction method, protocol, and reasoning-model support. |
| Compact project navigation extract | `07-project-reference-extracts/` | Derived maps, indexes, and cross-project extracts; cite source files. |
| Release bundle/export | `09-release-artifacts/` | Packaged snapshots of existing repository content; never the only copy. |

## Naming rules

Use lowercase kebab-case for new machine-oriented filenames, retain original names for provenance archives, and include a version suffix when a document is versioned. Use `README.md` for directory-level orientation and avoid generic names such as `final.md`, `notes.md`, or `new.docx`.

## Duplication rules

Do not maintain two competing canonical copies. A derived summary may link to a source, but it must state that it is derived. If content changes materially, create a new version and record the supersession or relationship in the continuity state or an index.

## Generated artefacts

Runtime databases, caches, Python bytecode, temporary logs, test workspaces, and other reproducible execution files remain untracked. Human-readable reports and reproducible JSON outputs may be committed when they document a meaningful run, but their evidence state and generation context must be explicit.

## Provenance requirement

Every imported research or project artefact should have a discoverable source path, repository commit context, or source note. Never silently merge an external document into a canonical baseline.
