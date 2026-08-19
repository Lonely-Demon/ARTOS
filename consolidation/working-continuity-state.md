# Working Continuity State

**Project:** Brain / Agent-Manus collaboration and future multi-agent harness
**Last updated:** 15 August 2026
**Purpose:** Durable state for resuming work after conversation compaction or in a new AI conversation.

> This file is a structured state record, not a raw conversation transcript. It preserves what matters for continuing the work: goals, decisions, rationale, constraints, source hierarchy, open questions, and the current next step.

## 1. Overall objective

The larger objective is to create a sophisticated, locally usable and deployable multi-agent harness assembled from strong open-source components. The harness should support the user's preferred way of working on difficult projects: deep upstream research, problem decomposition, landscape mapping, explicit factors and constraints, solution comparison, traceable decisions, adversarial review, controlled implementation, and high-quality final outputs.

The harness is not the immediate task. Before building it, the user wants to understand and define the collaboration behaviour, decision process, capabilities, and agent roles through accumulated project experience. Candidate open-source foundations discussed include DeerFlow 2.0, OpenManus, OpenHands, OpenClaw, and Hermes Agent. A tentative architecture considered Hermes as a personal coordinator, DeerFlow as a research/execution worker, and OpenHands as a coding worker, but this is not approved or final.

## 2. User's desired quality benchmark

The user wants final technical work to be comparable in intellectual rigour and completeness to work produced by an elite multidisciplinary engineering team with substantial time, expertise, and resources. This does not mean pretending to possess NASA/ISRO facilities, proprietary data, formal institutional authority, specialist laboratories, or physical validation that has not occurred.

The intended benchmark is disciplined, evidence-aware, systems-level work in which important variables, constraints, alternatives, dependencies, trade-offs, failure modes, and validation requirements are brought into view. The objective is not impossible perfection. It is informed robustness:

> The major ways the solution could fail should be considered before presentation; remaining uncertainties should be visible, bounded, mitigated, deferred, excluded, or explicitly accepted.

The user's desired final state is calculated trade-offs rather than late surprises.

## 3. Collaboration contract

The user prefers plain-text discussion first. Do not create a formal document unless explicitly requested or unless the user reviews and approves the content for preservation. Avoid overproducing documents and avoid adding abstract methodology when a direct explanation is enough.

The assistant should reconstruct prior context before proposing changes; avoid jumping to conclusions; begin with upstream research and problem decomposition on non-trivial projects; map multiple relevant domains; surface alternatives and hidden factors; preserve rationale and rejected paths; and provide specific, evidence-based counterweight rather than generic agreement.

The assistant is a counterweight, not a replacement for the user's judgment. The user retains goals, values, contextual knowledge, final trade-offs, and the decision that the work is sufficient. The assistant should not silently redirect the project toward a generic standard or treat AI-declared completion as authoritative.

During exploration, the assistant should avoid interrupting every idea with a full critique. It should surface only concerns that could materially change the direction. At commitment points—architecture selection, implementation, claims, safety, delivery, or a claimed-complete state—the assistant should become more rigorous and perform a specific coverage and failure check.

The assistant should distinguish evidence states: Verified, Measured locally, Estimated, Design inference, Hypothesis, Open, and Excluded. It must not present assumptions, synthetic outputs, simulations, demos, or prototypes as real-world validation.

The assistant should maintain this continuity file and update it after material changes, decisions, reversals, major discoveries, or phase transitions. It should not append every conversational turn.

## 4. Source-of-truth hierarchy

Use these sources in this order when reconstructing the collaboration model:

1. `operational-extract.md` — compact active collaboration rules and policy hooks.
2. `comprehensive-report.md` — canonical reconciled model, evidence tiers, caveats, and contradictions.
3. `purpose-and-reasoning-full-account.md` — why the counterweight model exists and its authority boundary.
4. `capture-spec-v6-process-position-and-context-caveat.md` — capture scope, policy tiers, contradictions, and process position.
5. `extraction-protocol-v2.md`, `category-space-artifact-v2.md`, `consolidation-protocol-v2.md`, and `how-to-use-this-foundation-v2.md` — methodology governance.
6. `snapshot-after-file-9.md` and earlier snapshots — blind extraction traceability and evidence evolution.
7. Historical conversation exports — project-specific reasoning, decisions, revisions, and original context. They are not automatically authoritative sources for external factual claims.
8. `cognitive-modeling-frameworks-integrated-report.md` and `instruction-architecture-autopsy-v5.md` — explanatory lenses and residual design risks, not runtime facts about the user.
9. `Comprehensive Summary of Referenced Task.md` — rapid orientation to the earlier context-review task.

The extracted archive was found in `/home/ubuntu/agent_manus_review/`. The uploaded `Agent_Manus.zip` contained 30 Markdown files, not 29.

## 5. Relevant project evidence

### NHAI / LUMIS

NHAI is the closest process sibling for broad, systems-level project work. Its foundational documents include operational problem landscape, problem landscape, solution landscape, operational factors, and a cross-reference index. The work moves from prompt interpretation to problem reconstruction, operational and solution landscapes, factor cataloguing, triage, decision mapping, architecture, validation, and later compression into a submission narrative.

The important pattern is not the number of factors or documents. It is that each factor is connected to causal consequences and decisions, and the cross-reference index reveals what is not explicitly covered. Problems are triaged into what must be addressed, acknowledged, deferred, or excluded. The output is an evidence-backed system concept, not merely a pitch.

### VitalNet

VitalNet is a socio-technical innovation system rather than a conventional software-only project. It combines healthcare workflow, structured information capture, triage/explanation, clinician briefing, persistence, dashboards, access boundaries, offline operation, governance, and deployment concerns.

The strongest direction became a narrower closed loop: frontline intake → independent prototype triage/explanation → doctor briefing → persistence → dashboard/feedback. The system must not be presented as clinically validated, medically superior, or a substitute for clinical authority. Synthetic data and prototype behaviour do not prove clinical safety.

VitalNet demonstrates the value of narrowing a broad vision into a defensible first slice while preserving the larger roadmap. It also shows the importance of distinguishing stable identity/facility boundaries from dynamic case-access/referral boundaries.

### TabVolt

TabVolt is the clearest software-heavy build project. It was created under extreme hackathon constraints, on low-spec hardware, with a browser extension as the product. The project used constraint-led stack selection, decision matrices, a master implementation context, locked file boundaries, forward-compatible schemas, phased build prompts, and explicit forbidden changes.

The project also demonstrates evidence-driven revision. The initial direct per-tab process-measurement assumption failed on standard browser platforms; the architecture pivoted to heuristic estimation. Later AI suggestions were made safer by structurally filtering active, pinned, and audible tabs before prompt construction and providing deterministic fallback behaviour.

TabVolt shows that a software project needs both technical coherence and a memorable proof of value. Its competition result is historical user-reported context, not independent evidence of universal efficacy. The project should not claim direct per-tab power measurement or guaranteed energy/carbon savings without calibration and validation.

## 6. Common workflow Version 0.1

The current project-agnostic workflow is:

1. Frame the project: collect prompt, rules, goals, evaluation criteria, resources, constraints, and deliverables; separate the full technical objective from the compressed submission objective.
2. Reconstruct the real problem: understand users, stakeholders, current workflow, causal failure, operating environment, and consequences rather than merely repeating the prompt.
3. Map the problem, solution, and operational landscapes across relevant domains.
4. Build a factor catalogue and evidence/uncertainty map; connect factors to consequences and decisions.
5. Triage findings into must address, must acknowledge, can defer, or excluded.
6. Define requirements, success conditions, exclusions, and verification methods.
7. Map and compare solution families and architecture alternatives using explicit criteria.
8. Record decisions, rejected alternatives, dependencies, consequences, and revisit conditions.
9. Produce the full canonical technical output: the detailed, prototype-ready or implementation-ready body of work.
10. Define the smallest meaningful end-to-end prototype or implementation slice.
11. Prepare controlled handoffs to people, research agents, coding agents, or specialists.
12. Build and learn in phases while maintaining whole-system context and revising the design when reality contradicts assumptions.
13. Stress-test the result across problem validity, technical feasibility, operational fit, safety, alternatives, evidence, integration, scope, and communication.
14. Finalise the strongest defensible solution and distinguish demonstrated, measured, estimated, hypothesised, and unvalidated elements.
15. Compress the canonical output into the required competition deck, proposal, pitch, README, or executive summary.
16. Preserve a continuation package containing decisions, rejected alternatives, evidence, risks, validation results, implementation state, public claim boundaries, and the next action.

The canonical technical output comes first. The round-one competition submission is derived by synthesis and compression; it is not a separate competing objective and should not discover the architecture while being written.

## 7. Engineering-practice refinements currently proposed for Version 0.2

External research from NASA, Google SRE, NIST, and Architecture Decision Record practice mostly confirms Version 0.1 but suggests six additions:

1. **Readiness gates:** lightweight go, go-with-conditions, return-for-work, or descope decisions between major stages.
2. **Concept of Operations (ConOps):** an explicit description of who uses the system, how the workflow operates, what information moves, what decisions/actions result, and how failure is handled.
3. **End-to-end traceability:** factor/problem → requirement → design decision → implementation element → verification method → permitted claim.
4. **ADR-style decision records:** concise records for architecturally significant choices, preserving context, alternatives, rationale, and consequences.
5. **Failure-triggered replanning:** short postmortems whenever an important assumption fails, an integration diverges, or evidence weakens a core claim.
6. **Integrated security, reliability, and operations:** especially for software, AI, data, infrastructure, and systems with real-world consequences.

These additions should be tailored to risk, complexity, reversibility, deadline, project type, and maturity. Do not import NASA-level ceremony into every small project.

## 8. Current recommended next step

The next step is to collaboratively refine Version 0.1 into a practical Version 0.2, beginning with the purpose and readiness conditions of each phase. The workflow should be discussed in plain text first, not turned into a formal specification immediately.

After Version 0.2 is coherent, test it on one bounded but meaningful software or AI-system example. Do not use the entire multi-agent harness as its first test unless necessary; the harness is broad enough to bias the workflow toward its own assumptions.

Only after the workflow survives a concrete example should it be translated into the behavioural and architectural specification for the multi-agent harness.

## 9. Open questions and nuances to refine later

The user has expressed that some workflow preferences are currently intuitive feelings that are difficult to articulate. Do not force premature verbal precision. Let concrete examples and phase-by-phase use reveal them.

Still-open design questions include:

- How formal should each readiness gate be for a small project, competition sprint, serious innovation project, or safety-sensitive system?
- What minimum contents must every project-state record contain?
- When should the assistant interrupt exploration, and when should it wait until a commitment gate?
- How should research depth and stopping conditions be judged without imposing premature closure?
- How should the workflow change between hardware, software, AI, hybrid, research, and time-boxed hackathon projects?
- Which decisions require ADR-style records and which should remain informal?
- How should a future harness route research, coding, review, memory, and execution agents while preserving one coherent project state?
- What is the smallest useful software/AI example for calibrating the workflow?

## 10. Recovery instructions for a new conversation

If this file is reopened after compaction, first read it in full. Then inspect `operational-extract.md` if the task concerns collaboration behaviour, and inspect the relevant historical project export only when project-specific detail is needed.

Resume from the current phase: **collaboratively refine the workflow into Version 0.2, beginning with phase purpose and readiness gates.** Do not restart the entire archive review unless a specific contradiction or missing source requires it.

Use plain text unless the user explicitly requests a document. Do not claim that this file contains every word of prior conversations; it contains the current durable state and should be updated whenever the project changes materially.

## 11. External reference sources used for workflow calibration

[NASA Program/Project Life Cycle](https://www.nasa.gov/reference/3-0-nasa-program-project-life-cycle/)  
[NASA System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/)  
[Google SRE Error Budget Policy](https://sre.google/workbook/error-budget-policy/)  
[Architectural Decision Records](https://adr.github.io/)  
[NIST Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf)


## 12. Universal enterprise vision (new clarification)

The larger goal is a general-purpose virtual enterprise that can assemble world-class capabilities for any domain, not merely a multi-agent software development tool. The user described a recursively expanding organisation in which the best relevant disciplines, methods, tools, and public capability references can be activated around any mission—such as a semiconductor mission involving semiconductor physics, device architecture, process technology, lithography, packaging, thermal engineering, circuit design, computer architecture, verification, fabrication economics, supply chain, software/toolchains, manufacturing, reliability, safety, IP/legal, and commercial strategy.

The appropriate mental model is a **capability tree + project graph + governance spine**. The capability tree decomposes broad branches into specialist sub-branches; the project graph dynamically activates and connects the branches needed for a mission; the governance spine carries shared project state, evidence, requirements, decisions, risks, approvals, handoffs, and assurance across all branches.

Each team/capability cell should have a mandate, scope, activation criteria, recursive decomposition, inputs, methods/tools, outputs, evidence contract, quality criteria, interfaces, authority, escalation rules, and continuity requirements. External organisations such as Nvidia, Intel, AMD, Qualcomm, MediaTek, TSMC, ASML, research institutions, or regulators may be represented as public capability references, benchmarks, precedents, or ecosystem nodes, but not impersonated or treated as accessible proprietary teams.

The virtual enterprise should be built incrementally. The first operating kernel should manage project state, objectives, stakeholders, capabilities, work packages, artifacts, evidence, factors, requirements, decisions, risks, handoffs, gates, reviews, claims, external validation, and change events. Later stages add the upstream project framework, research/team assembly, software lifecycle, assurance, domain pipelines, and persistent local/remote execution.

The immediate autonomous design artefacts are:
- `virtual-enterprise-capability-ontology-v0.md`
- `virtual-enterprise-project-assembly-v0.md`
- `virtual-enterprise-governance-evidence-authority-v0.md`
- `virtual-enterprise-subsystem-integration-v0.md`
- `virtual-enterprise-staged-construction-v0.md`

These are provisional architecture artefacts, not final specifications. The universal enterprise model must preserve human authority, independent validation, and explicit limits where physical tests, legal/regulatory review, specialist expertise, or institutional sign-off are required.


## 13. Autonomous continuation while user unavailable

The user instructed the assistant to proceed without feedback, treating the user's vision as the governing objective, while recording assumptions and rationale. The current autonomous objective is to design a universal recursively decomposable virtual enterprise and its first major subsystems.

### Architectural baseline produced

The following provisional artefacts were created:

- `universal-enterprise-blueprint-v0.md` — consolidated blueprint for the capability tree, project graph, governance spine, operating kernel, upstream project framework, downstream software subsystem, gates, assumptions, and staged construction.
- `virtual-enterprise-capability-ontology-v0.md` — recursive capability ontology and reusable team-cell contract.
- `virtual-enterprise-project-assembly-v0.md` — mission-to-project assembly, dynamic capability activation, work packages, collaboration patterns, roles, handoffs, integration rules, and scaling.
- `virtual-enterprise-governance-evidence-authority-v0.md` — authority model, evidence states, gates, assurance, safety, security, compliance, risk, audit, change control, and continuity.
- `virtual-enterprise-subsystem-integration-v0.md` — upstream project framework to downstream software/hardware/scientific/manufacturing/clinical/regulatory/commercial pipeline interface.
- `virtual-enterprise-staged-construction-v0.md` — incremental construction from operating specification and kernel to domain pipelines and local/remote operation.
- `operating-kernel-v1-data-model-and-roadmap.md` — kernel entities, relationships, state machines, services, roadmap, and local/remote deployment.

### Enterprise software research and design produced

Authoritative and public engineering sources reviewed include ISO/IEC/IEEE 12207, 15288, and 29148; NASA systems/software lifecycle and NPR 7150.2D; NIST SSDF and AI RMF; OWASP SAMM and ASVS; Microsoft SDL; Google SRE; DORA; Google Engineering Practices; GitLab Product Development Flow; and ISO/IEC 25010.

The research synthesis is in:

- `enterprise-software-research-findings.md`
- `enterprise-software-practice-corpus.md`
- `enterprise-software-lifecycle-v1.md`
- `enterprise-software-assurance-operations-v1.md`

### Current technical interpretation

Enterprise software is not a fixed checklist of BRD, PRD, SRS, ADR, and other document names. It is a set of connected lifecycle process families and information products. The virtual enterprise should maintain an underlying information graph and generate tailored views for product, system, engineering, security, compliance, operations, reviewers, and executives.

The enterprise software subsystem consumes the upstream system concept and derives software responsibility, product definition, ConOps, requirements, architecture, implementation, verification, release, operations, maintenance, and retirement. It must feed feasibility findings, incidents, performance, security, data, cost, and operational discoveries back to the upstream systems layer.

### Important new research principles

- Requirements must be clear, complete, consistent, verifiable, validated in the customer environment, baselined, change-controlled, and traceable.
- Architecture is a durable decision layer that formalizes decomposition, interfaces, qualities, dependencies, valid/invalid states, and change impact.
- Security and privacy begin in requirements and design; threat modelling, data flow, independent review, automated checks, component governance, staged deployment, and incident response are lifecycle controls.
- Systems and software lifecycle processes should be tailored to project scope, maturity, risk, methodology, and consequence; standards do not mandate one document package.
- Product validation may operate ahead of build execution, and lifecycle phases may overlap or be skipped when confidence and risk justify it.
- Quality attributes should become measurable requirements, test objectives, acceptance criteria, and architecture drivers.
- AI/agentic products require model/data provenance, evaluation, uncertainty, misuse/red-team, tool permissions, human authority, drift, monitoring, and incident controls.
- Operational evidence and delivery metrics should drive continuous improvement, not become simplistic optimisation targets.

### Autonomous assumptions

- The user wants a universal capability ecosystem, not merely a multi-agent software tool.
- The phrase “best organisations/subsystems” is interpreted as capability and precedent mapping, not literal impersonation or access to proprietary institutional knowledge.
- The universal system should use a capability tree for recursive decomposition, a project graph for dynamic activation and dependency, and a governance spine for shared state and authority.
- The first implementation should begin with a local-first operating kernel, not a huge number of autonomous agents.
- The kernel should first prove continuity, evidence, handoffs, decision traceability, gate control, and safe reconfiguration on a real project.
- The upstream NHAI/VitalNet/TabVolt-derived project framework is the first general discovery/systems subsystem; enterprise software is the first detailed downstream execution subsystem.
- “World-class” and “almost perfect” are treated as aspirations implemented through breadth, layered specialist review, independent assurance, evidence discipline, and operational feedback—not a literal guarantee of zero defects or a replacement for physical/legal/regulatory/expert authority.
- UI/UX remains a project-specific subsystem and should not dominate master architecture documents.

## 14. Current next stage

The architecture and research baseline are now sufficient to move from conceptual design toward a detailed implementation specification for the operating kernel and its first project-calibration workflow. The immediate recommended construction path is: structured continuity → evidence/artefact graph → work packages/handoffs → gates/assurance → software lifecycle integration → dynamic team assembly → controlled workers → domain pipelines.


## 15. Iterative improvement cycles completed

The user requested repeated research, comparison, revision, and improvement until marginal benefit no longer justified further research time. Three targeted improvement cycles were completed.

### Cycle 001: Broad gap and contradiction review

Reviewed the universal enterprise, software lifecycle, assurance, and kernel baselines. Main gaps identified were capability competence/freshness, assurance arguments, kernel security, data/model/source governance, portfolio economics, orchestration quality, completeness measurement, taxonomy governance, external capability integration, concurrent branch/merge semantics, human authority escalation, agent-specific incident response, knowledge freshness, and enterprise-output evaluation.

Artefact: `improvement-cycle-001-gap-review.md`.

### Cycle 001 research and revision

Research covered ISO assurance cases, OWASP agentic security, ISO/IEC 42001, NIST CSF, CISA SBOM/VEX, NIST incident response, requirements/quality practices, and public engineering practices. The revised files add capability cards, assurance graphs, kernel/worker security, data/model/source registries, supply-chain provenance, portfolio/economic controls, AI management, and operational incident feedback.

Artefacts: `universal-enterprise-blueprint-v1.1.md`, `enterprise-software-lifecycle-v1.1.md`, `improvement-cycle-001-change-log.md`.

### Cycle 002: AI and agent risk operationalisation

NIST AI RMF Playbook and MITRE ATLAS were used to refine Govern/Map/Measure/Manage loops and threat-informed red teaming. Capability activation now distinguishes discoverable, available, eligible, activated, trusted for recommendation, trusted for execution, and trusted for approval.

Artefact: `improvement-cycle-002-revision.md`.

### Cycle 003: Kernel security, execution trace, and reliability

NIST Zero Trust Architecture and OpenTelemetry were used to refine the control plane. The kernel should not trust local workers or previously approved identities implicitly; access is contextual and revocable. Material work should carry trace context across assignments, retrieval, model/tool calls, artefacts, reviews, approvals, tests, deployment, incidents, and state changes. Current state should be separated from append-only/tamper-evident event history, with branch/merge control for concurrent work.

Artefact: `improvement-cycle-003-revision-and-stop-assessment.md`.

### Research stopping assessment

The architecture-level research loop has now covered recursive capability decomposition, dynamic project assembly, evidence/provenance, assurance arguments, requirements/architecture/software lifecycle, safety/security/compliance/quality/operations/retirement, AI governance, agentic threats, supply-chain transparency, incident response, capability competence, portfolio/economic control, zero-trust access, and execution observability. Further broad research is now lower value than implementation/calibration on a real bounded project. New research should be triggered by an implementation failure, domain-specific gap, or architecture-changing evidence.

## 16. Current improved baseline

The current working baseline is Universal Enterprise v1.1 plus the three improvement-cycle addenda. It is a recursively decomposable virtual enterprise with a capability tree, project graph, governance spine, and four conceptual control planes: governance/control, knowledge/evidence, execution, and external world.

The main residual uncertainties are implementation-level: kernel storage/versioning, concrete identity and sandboxing, event/audit integrity and recovery, semantic branch/merge, capability evaluation calibration, assurance-case usability, agentic red-team implementation, local/remote threat modelling, and external authority integration.

The next practical improvement is a controlled implementation/calibration cycle for the operating kernel on a bounded real project. Abstract research should not resume unless that cycle reveals an architecture-changing gap.


## 17. Ten-cycle adversarial destruction and revision

The user requested ten explicit cycles in which the system reasons against its own reasoning, assumes every conclusion may be flawed, uses different specialist lenses, and iterates until marginal research value is no longer worth the time.

The ten cycles were completed and recorded in `adversarial-cycle-01-baseline-falsification.md`, `adversarial-cycle-02-systems-architecture.md`, `adversarial-cycle-03-software-lifecycle.md`, `adversarial-cycle-04-security-agentic-abuse.md`, `adversarial-cycle-05-safety-compliance-authority.md`, `adversarial-cycle-06-evidence-assurance.md`, `adversarial-cycle-07-teams-handoffs-coordination.md`, `adversarial-cycle-08-economics-scale-incentives.md`, `adversarial-cycle-09-product-human-operations.md`, and `adversarial-cycle-10-implementation-testing-recovery.md`.

The consolidated outputs are `universal-enterprise-blueprint-v2.0.md`, `enterprise-software-lifecycle-v2.0.md`, and `adversarial-ten-cycle-change-log-v1.md`.

The major revisions are: concern-oriented architecture views; configuration-controlled baselines; typed interfaces and external-system objects; risk-adaptive linked lifecycle views rather than document waterfall; contextual runtime authorization and untrusted-content boundaries; project-local memory isolation; jurisdiction/role/use-specific safety/privacy/compliance classification; richer evidence objects with uncertainty, replication, calibration, and defeaters; cognitive-load and interaction-mode controls; explicit ownership and handoff semantics; resource/cost/value-of-information governance; human-centred product and operational loops; reproducibility tiers; semantic execution traces; incident playbooks; state integrity, replay, reconciliation, compensation, and recovery objectives.

The final stopping judgment is that broad abstract research should pause. Ten cycles produced architecture-changing findings across every major control plane; the remaining uncertainties are primarily empirical and implementation-specific. The next high-value work is to implement and attack a bounded operating-kernel slice on a real project. New research should be triggered by observed implementation failure, a domain-specific gap, or architecture-changing evidence.


## 18. Autonomous gap-closure increment

The user authorised autonomous continuation without routine feedback and instructed the assistant to close as much of the remaining gap as possible without human intervention. The autonomous construction path therefore began with a local-first reference implementation rather than another abstract architecture document.

### Implemented reference workspace

A new workspace was created at `/home/ubuntu/agent_manus_review/operating-kernel-reference/`.

The minimum operational contract is in `minimum-operational-contract-v0.2.md`. It defines the bounded first slice, canonical objects, evidence states, transitions, gates, traceability links, continuity packet, safety boundary, acceptance tests, and explicit non-goals.

The implementation includes:

- `kernel.py`: SQLite-backed current projection, append-only event chain, transactions, typed entities, typed links, lifecycle transitions, gate advancement, evidence-state controls, tombstones, event verification, reconstruction, and continuity export.
- `workflow.py`: work-package creation, assignment, execution, submission, review, handoffs, acknowledgements, gates, and continuation helpers.
- `worker_contract.py`: transport-neutral task-package and worker-result schema; workers are review-only and cannot directly write canonical state, approve, upgrade claims, or perform external side effects.
- `api.py`: unauthenticated localhost-only FastAPI adapter for local development; it must not be exposed remotely in this form.
- `cli.py`: local command-line entry points for demo seeding, project creation, packets, events, and integrity checks.
- `test_kernel.py` and `test_api.py`: acceptance, workflow, worker contract, API, and adversarial regression tests.

### Calibration and evidence

`calibrate_tabvolt.py` maps the historical TabVolt project record into the kernel. It creates 1 objective, 8 factors, 5 evidence objects, 4 decisions, 4 risks, 4 work packages, 3 claims, 3 gates, and 1 handoff with 22 typed links and 95 events. The calibration passes coverage checks and preserves the distinction between historical participant-observed local measurements, design inferences, open claims, and explicitly excluded exact-energy claims. Generated outputs are in `calibration-output/`.

This is a retrospective calibration, not independent validation of TabVolt or proof that the framework improves project quality.

### Open-source component audit

The current public GitHub repositories and README material for DeerFlow, OpenHands, OpenManus, Hermes Agent, and OpenClaw were inspected. The audit is in `open-source-component-audit-v0.md`; the evaluation contract and provisional matrix are in `component-evaluation-matrix-v0.1.md`.

Current role hypothesis:

- DeerFlow: long-horizon research/execution worker candidate.
- OpenHands: coding/implementation worker candidate.
- Hermes: personal interaction/coordinator interface candidate.
- OpenClaw: personal gateway/channel candidate.
- OpenManus: experimental general/browser/data-analysis worker candidate.

None is allowed to replace the kernel’s canonical state, authority, evidence admission, or approval layer. OpenHands source was cloned shallowly for static boundary inspection only; no candidate runtime was executed.

### Adversarial repair and validation

The adversarial report is `adversarial-test-report-v0.1.md`. Initial tests exposed and repaired cross-project link contamination, tombstone audit visibility, draft-project gate activation, and SQLite thread incompatibility in the local API. A final run passes 20 tests. The only remaining test-run warning is a dependency deprecation warning from the installed Starlette/httpx test client; it does not affect the test result but should be cleaned in a future dependency refresh.

`worker_smoke.py` runs a synthetic, deterministic adapter-boundary test. It confirms that a compliant worker result remains review-only and rejects claim upgrades, external side effects, project identity mismatch, and missing reproducibility metadata. It explicitly does not execute DeerFlow, OpenHands, Hermes, OpenClaw, or OpenManus and does not measure their quality.

### Current residual gaps

The reference system is not production-ready, remotely secure, multi-tenant, independently validated, domain-capable, or a complete multi-agent harness. It still lacks a formal policy engine, authentication and identity, secrets management, encryption and backup/recovery procedures, robust event-sourced rebuild semantics, semantic concurrent branch merge, real worker execution adapters, capability competence benchmarks, domain catalogues, human/external authority integration, and measured comparison against ordinary project workflows. These remain the next implementation priorities.

Current stopping judgement for this increment: enough implementation exists to move from design-only work to an evidence-generating reference system. Further work should continue through controlled worker integration and project calibration rather than expanding the universal ontology.


## 19. ARTOS is now the canonical repository workspace

The user instructed that all future work for this project should use `https://github.com/Lonely-Demon/ARTOS`, which contains the original conversation files, snapshots, and consolidation materials. ARTOS is now the canonical project workspace rather than the sandbox-only review directory.

The repository was cloned and audited. Its original archive contains nine project conversation exports, nine sequential snapshots, `consolidation/comprehensive-report.md`, and `consolidation/operational-extract.md`. The repository is currently a document/conversation archive with the new reference implementation added under `operating-kernel-reference/`.

The autonomous operating-kernel reference, calibration outputs, component audit, tests, worker smoke harness, README, and this continuity state were imported into ARTOS. The repository copy passed the same 20-test local suite. A repository README was added to explain the canonical archive and evidence boundaries.

A cleaned branch was created and pushed:

- Branch: `manus/operating-kernel-reference-v0.1`
- Commit: `1fa8859 Add operating kernel reference baseline`
- Pull request URL: `https://github.com/Lonely-Demon/ARTOS/pull/new/manus/operating-kernel-reference-v0.1`

Runtime databases and Python bytecode were removed from version control and `.gitignore` was added. The next work should continue from the ARTOS branch/repository, and any future material created in the sandbox must be reconciled back into ARTOS before being treated as canonical.
