# Universal Virtual-Enterprise Capability Ontology v0

**Status:** Provisional architecture for refinement  
**Scope:** A general-purpose, recursively decomposable capability system for projects in any domain.

## 1. Design premise

The proposed system is not a fixed collection of chatbots and not a flat list of departments. It is a **recursive capability ecosystem**. A broad capability can be decomposed into specialised sub-capabilities whenever the project requires more depth. A project activates only the branches relevant to its current objective, while the operating kernel keeps all active branches aligned.

The structure is tree-like for decomposition, graph-like for collaboration, and governed by a common spine for evidence, authority, quality, and continuity.

## 2. Three structural forms

### Capability tree

The capability tree answers: **What kinds of expertise and work can the enterprise perform?** It contains reusable domains, subdomains, specialist teams, and task-level agents.

### Project graph

The project graph answers: **Which capabilities are needed for this particular mission and how do they depend on one another?** It is dynamically assembled and may include cross-branch loops, parallel workstreams, and feedback paths.

### Governance spine

The governance spine answers: **How do all branches remain coherent, evidence-aware, safe, auditable, and aligned with the user's authority?** It carries project state, requirements, decisions, assumptions, risks, artefacts, approvals, gates, provenance, and change impact.

## 3. Operating kernel — the trunk

Every capability branch operates through a shared kernel containing:

- Mission/objective and current project frame.
- Stakeholders, users, affected parties, and authority boundaries.
- Problem model and Concept of Operations.
- Requirements, constraints, factors, assumptions, and exclusions.
- Research questions, evidence, provenance, confidence, contradictions, and unresolved issues.
- Solution options, architecture, decisions, alternatives, consequences, and revisit conditions.
- Work packages, handoff contracts, dependencies, and phase status.
- Risks, hazards, threats, vulnerabilities, compliance obligations, and mitigations.
- Validation criteria, tests, experiments, review results, and permitted claims.
- Versioned artefacts, change history, and cross-reference index.
- Human approvals, escalation status, and decision authority.
- Continuity state across projects and prior precedent.

The kernel is the source of shared context. No specialist branch should maintain an isolated version of the project's truth.

## 4. Major capability branches

### A. Mission, portfolio, and strategy

This branch identifies opportunities, decides what is worth pursuing, frames ambition, allocates attention and resources, defines success, compares initiatives, and determines whether to proceed, pivot, defer, descope, or stop.

Sub-capabilities can include strategic analysis, portfolio prioritisation, mission definition, investment analysis, business-model analysis, opportunity sizing, competitive strategy, and executive decision support.

### B. Problem discovery and research intelligence

This branch reconstructs the real problem and maps the knowledge landscape. It includes domain research, scientific literature, engineering research, market research, user/stakeholder research, operational research, legal/regulatory research, standards, prior art, competitor analysis, technology scouting, data analysis, and evidence verification.

Each research subteam receives a bounded question and returns evidence, source quality, contradictions, confidence, implications, affected decisions, unresolved questions, and recommended next investigations.

### C. Systems engineering and product definition

This branch transforms research into system-level coherence. It defines stakeholder expectations, requirements, ConOps, system boundaries, functions, interfaces, product goals, alternatives, architecture drivers, lifecycle considerations, and success criteria.

It is responsible for integrating specialist findings into a consistent system rather than allowing each domain to optimise its own part independently.

### D. Domain science and engineering

This branch contains the technical disciplines required by the problem. It is intentionally open-ended and recursively decomposable.

Possible branches include mechanical, electrical, electronics, semiconductor, materials, chemical, physics, robotics, controls, aerospace, civil, energy, biomedical, clinical, manufacturing, industrial, environmental, geospatial, mathematical, and other specialised engineering or scientific fields.

The branch may use external organisations and prior art as capability references and benchmarks. It must not imply access to proprietary knowledge or impersonate an external institution.

### E. Software, AI, data, and digital systems

This branch contains product management, software engineering, systems architecture, platform engineering, AI/ML engineering, data engineering, data science, model evaluation, infrastructure, cloud, embedded software, cybersecurity engineering, developer experience, and technical documentation.

Its downstream lifecycle includes requirements, design, ADRs, implementation, testing, security, deployment, operations, maintenance, and retirement. It can itself decompose into specialised teams for frontend, backend, APIs, databases, distributed systems, data platforms, model serving, agent orchestration, observability, and other areas.

### F. Product experience, human factors, and adoption

This branch studies user needs, workflows, human factors, accessibility, interaction design, service design, onboarding, adoption, training, and product communication. Detailed UI/UX artefacts should be scoped to the relevant project and should not dominate the enterprise master framework.

### G. Industrialisation, deployment, and operations

This branch converts designs into repeatable production or field use. It includes manufacturing, supply chain, sourcing, installation, deployment, infrastructure operations, service delivery, maintenance, logistics, support, capacity, reliability, and lifecycle sustainment.

It is activated for physical products, infrastructure, enterprise software, field systems, and any solution where operation after creation matters.

### H. Assurance, risk, safety, security, and compliance

This branch is independent of the creators where practical. It reviews quality, reliability, safety, cybersecurity, privacy, legal/regulatory obligations, standards, ethics, misuse, resilience, and claim sufficiency.

It may contain separate red-team, safety-case, threat-modelling, compliance, privacy, quality, test, and independent-review teams. Its authority is to challenge, require evidence, impose conditions, escalate, or block progression when appropriate.

### I. Commercial, communications, and delivery

This branch translates the full technical body of work into audiences and outcomes: competition submissions, product narratives, investor or stakeholder communication, proposals, technical reports, documentation, training, launch material, and public claims.

It must operate downstream of the canonical technical output. Communication should compress the work, not invent its central logic.

### J. Knowledge, programme, and continuity management

This branch maintains the enterprise's memory, project state, decision history, evidence registry, cross-project precedent, standards library, templates, skills, lessons learned, and change impact. It prevents capability branches from losing context and enables future projects to reuse prior work without importing assumptions blindly.

## 5. Reusable capability-cell contract

Every branch, team, subteam, or agent should be defined through the same contract:

| Field | Required meaning |
|---|---|
| Mandate | What this capability exists to accomplish. |
| Scope | What it owns and what it explicitly does not own. |
| Activation criteria | When the capability should be invoked and when it is unnecessary. |
| Internal decomposition | Which sub-capabilities may be activated beneath it. |
| Inputs | Context, questions, requirements, evidence, constraints, and dependencies required to work. |
| Methods/tools | Research, analysis, modelling, implementation, review, or communication methods available. |
| Outputs | Structured artefacts, findings, decisions, tests, recommendations, or handoffs produced. |
| Evidence contract | Source, calculation, measurement, simulation, test, review, or confidence requirements. |
| Quality criteria | Conditions that outputs must satisfy before handoff. |
| Interfaces | Other branches or artefacts it must connect to. |
| Authority | Decisions it may make, recommend, approve, reject, or only escalate. |
| Failure/escalation | What happens when evidence is insufficient, contradictory, or outside capability. |
| Continuity | What must be recorded so later teams can understand the work. |

## 6. Recursive behaviour

A branch is not required to be a single agent. It may become a temporary team with a lead, specialists, researcher, implementer, reviewer, and coordinator. A specialist may itself invoke a deeper subteam. The parent branch remains responsible for integrating the outputs and ensuring that the decomposition does not create duplicated or contradictory work.

The recursion should stop when further decomposition no longer changes the decision, reduces a material uncertainty, or improves the required output. This prevents the vision of an unlimited capability tree from becoming unlimited overhead.

## 7. Dynamic assembly

The enterprise should not activate every branch for every mission. The operating kernel should classify the project, identify the risk and maturity level, decompose the objective, detect required expertise, assemble a project graph, assign work packages, and activate independent assurance in proportion to consequences.

A semiconductor design mission could activate semiconductor physics, device architecture, process technology, lithography, packaging, thermal, circuit design, computer architecture, EDA/toolchain, manufacturing, supply chain, reliability, software, IP/legal, commercial, and assurance branches. A small software utility might activate only product framing, software architecture, implementation, testing, security, and delivery.

The difference is activation depth, not a different underlying operating model.

## 8. Initial boundary conditions

The virtual enterprise is a capability orchestration and reasoning system, not a claim of literal access to every world's best team, proprietary data, laboratory, factory, legal authority, or institutional decision-maker. External organisations such as Nvidia, Intel, AMD, Qualcomm, MediaTek, TSMC, ASML, research institutions, or regulators can be represented as public capability references, benchmarks, precedents, or ecosystem nodes, subject to evidence and access limitations.

High-impact decisions must preserve human authority and require domain-appropriate independent validation. AI-generated reasoning, simulated teams, and public research cannot substitute for physical tests, formal legal advice, regulatory approval, clinical review, security certification, or institutional sign-off where those are required.

## 9. First architecture implication

The first implementation subsystem should be the operating kernel and team-cell contract, not a huge catalogue of specialist agents. Once the kernel can represent project state, evidence, decisions, requirements, handoffs, gates, and review authority, specialist branches can be added incrementally without each developing a separate memory or workflow.
