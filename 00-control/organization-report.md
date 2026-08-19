# ARTOS Organization Report

## Result

ARTOS has been reorganized into a numbered, role-based repository structure. The original conversation archive and snapshots were moved into a clearly labelled provenance area without changing their content. Architecture, lifecycle, assurance, methodology, implementation, evaluation, calibration, experiment, and release materials now have separate homes.

## Preserved source archive

| Source class | Location | Count |
|---|---|---:|
| Original project conversations | `01-source-archive/conversations/` | 9 |
| Sequential snapshots | `01-source-archive/snapshots/` | 9 |
| Original consolidation files | `01-source-archive/consolidation/` | 2 |

## Organized implementation and design material

The current universal-enterprise architecture is under `02-canonical-architecture/`, the software lifecycle subsystem is under `03-enterprise-software-lifecycle/`, and its adversarial and improvement history is under `04-review-and-assurance/`. The operating-kernel implementation is under `05-operating-kernel/`, with source, contracts, evaluations, calibrations, and validation reports separated into subdirectories.

The collaboration and methodology materials are under `06-collaboration-and-methodology/`. Compact project extracts are under `07-project-reference-extracts/`. Future real-project calibrations and isolated worker experiments have a reserved location under `08-experiments-and-projects/`, while packaged exports remain under `09-release-artifacts/`.

## Validation

The reorganized implementation suite completed **20 tests successfully** from `05-operating-kernel/implementation/`. The reorganized TabVolt calibration completed successfully with **22 typed links**, **95 events**, a valid event chain, and all coverage checks passing. The calibration script was updated to use repository-relative imports and its output directory.

Runtime databases and Python bytecode were removed from the working tree and are excluded by `.gitignore`. The latest validation logs are retained under `05-operating-kernel/reports/validation/` as generated run records; they do not replace the source tests.

## Governance

Future agents should begin with `00-control/README.md`, `00-control/repository-manifest.md`, and `00-control/continuity/working-continuity-state.md`. New files must follow `00-control/file-placement-policy.md`. Source archive files remain provenance records, derived documents must identify their source, and no competing canonical copies should be created.
