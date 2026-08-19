# Component Evaluation Matrix v0.1

**Purpose:** Evaluate open-source agent projects against the Universal Enterprise boundary contract before adoption.

## Evidence rule

Scores in this first matrix are **provisional design judgements from public README/repository metadata**, not execution results. A candidate may only be promoted from candidate to integrated worker after a bounded local experiment produces measured evidence.

## Required capability contract

A worker adapter must be able to receive a scoped task package and return a typed result. The package must include project ID, work-package ID, objective, context, inputs, exclusions, evidence contract, allowed tools, allowed paths, side-effect budget, deadline, acceptance criteria, and return format. The result must include status, artefact references, evidence references, execution trace, deviations, unresolved risks, and reproducibility metadata.

The worker must not receive unrestricted project state by default. It must not write canonical state directly, change approvals, upgrade claims, or perform external side effects outside the policy-controlled adapter.

## Criteria and weights

| Criterion | Weight | Pass condition |
|---|---:|---|
| Bounded task execution | 15 | Can execute a scoped assignment and return a typed result. |
| Workspace/tool isolation | 15 | Can limit filesystem, network, credentials, and tools. |
| Reproducibility/provenance | 10 | Can record versions, configuration, inputs, outputs, and execution conditions. |
| Human/policy control | 15 | Can separate planning, execution, approval, and consequential actions. |
| Memory/context isolation | 10 | Can scope context and memory to the assigned project/work package. |
| Observability/recovery | 10 | Can expose progress, failures, interruption, retry, and recovery state. |
| Integration surface | 10 | Has a stable API/CLI/protocol suitable for an adapter. |
| Local/deployed portability | 5 | Can run in the intended local and remote environments. |
| Maintenance/licensing/supply chain | 5 | License, dependency, release, and security posture are inspectable. |
| Domain capability quality | 5 | Demonstrates useful performance for the specific worker role. |

## Provisional comparison

Scores below are initial review scores on a 0–5 scale and should not be treated as measured capability.

| Candidate | Task | Isolation | Provenance | Control | Memory | Observability | Integration | Portability | Supply chain | Domain fit | Weighted interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DeerFlow | 4 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 4 | Strong worker substrate; requires a hard wrapper around authority and deployment. |
| OpenHands | 4 | 3 | 3 | 3 | 2 | 3 | 4 | 4 | 3 | 5 for coding | Strong coding worker candidate; workspace and credential boundaries are mandatory. |
| Hermes Agent | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 5 | 3 | 3 | Strong personal coordinator candidate; memory and gateway trust surface need testing. |
| OpenClaw | 3 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 2 | 2 | Personal gateway candidate; not an enterprise control plane. |
| OpenManus | 3 | 2 | 2 | 2 | 1 | 2 | 3 | 4 | 3 | 3 | Simple experimental worker; useful for comparison, not governance. |

## Promotion stages

A candidate moves through `discovered → contract-mapped → locally-installed → isolated-smoke-tested → task-benchmarked → adversarially-tested → accepted-for-role → integrated → retired/rejected`.

No candidate may be marked `accepted-for-role` from documentation alone. A benchmark must include at least one success case, one malformed task package, one prompt/instruction conflict, one tool/path boundary attempt, one interruption, one unavailable dependency, one unsupported claim attempt, and one recovery or rollback case.
