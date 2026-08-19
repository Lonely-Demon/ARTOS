# Virtual Enterprise Project Assembly and Collaboration v0

**Status:** Provisional design for the universal capability system.

## 1. Purpose

The virtual enterprise should transform an arbitrary mission into a temporary, coherent project organisation. It must decide which capabilities are needed, how deeply each should be decomposed, which teams must work in parallel, where independent review is required, and how all outputs converge into a single defensible project state.

The enterprise should not activate every possible capability. It should assemble a project-specific graph from a universal capability tree, governed by the shared operating kernel.

## 2. Mission-to-project assembly flow

### Step 1: Mission intake

The user or authorised sponsor provides an opportunity, problem, request, competition prompt, product idea, research question, or system challenge. The intake may be incomplete, ambiguous, or biased toward a proposed solution.

The enterprise records the raw request without prematurely treating it as the problem definition.

### Step 2: Mission framing

The mission layer clarifies the objective, desired outcome, urgency, resources, constraints, stakeholders, risk level, maturity target, and authority boundaries. It identifies whether the task is research, concept design, product development, implementation, validation, delivery, or a combination.

The output is a project frame and initial uncertainty map.

### Step 3: Capability detection

The orchestrator analyses the frame and proposes the capability branches required. It identifies obvious domains, adjacent domains, assurance needs, lifecycle needs, and likely missing expertise.

It should explicitly ask: Which capability could invalidate the current interpretation if omitted? This is how compliance, physics, supply chain, safety, human factors, or operations are activated even when the initial request does not mention them.

### Step 4: Capability-depth selection

For every activated branch, the orchestrator decides the required depth:

- **Reference:** a quick contextual check is sufficient.
- **Advisory:** a specialist produces an analysis or recommendation.
- **Workstream:** multiple specialists investigate and integrate a domain.
- **Subsystem:** a complete design, build, validation, or lifecycle path is required.
- **Independent assurance:** the branch must review another branch's work without owning the original decision.

Depth is determined by consequence, uncertainty, irreversibility, novelty, resource availability, and the branch's ability to change the architecture.

### Step 5: Project graph formation

The active capabilities are connected into a project graph. Nodes represent capability cells or teams. Edges represent dependencies, data flows, decision dependencies, review relationships, or feedback paths.

The graph should distinguish:

- work that can proceed independently;
- work that depends on a resolved question;
- work that must be performed by an independent reviewer;
- work that must be jointly resolved by multiple disciplines;
- and work that must wait for user or external authority.

### Step 6: Work-package creation

Each team receives a bounded work package. A work package includes the question or objective, context, scope, constraints, evidence standard, inputs, required output, affected decisions, deadline or priority, dependencies, prohibited assumptions, and escalation rules.

A team should never be asked merely to “research semiconductors” or “design the backend.” The task must state what decision the work supports and what evidence would change that decision.

### Step 7: Parallel investigation and controlled interaction

Teams work in parallel when their questions are sufficiently independent. They should not all receive every intermediate output, because uncontrolled context sharing increases noise and anchoring. The orchestrator should provide the minimum context required, then update teams when a finding materially changes their work.

Teams may interact through structured requests:

- clarification request;
- dependency request;
- challenge request;
- evidence request;
- interface negotiation;
- change-impact notification;
- escalation;
- or convergence review.

### Step 8: Local synthesis

Each parent branch integrates its child outputs before sending a conclusion upward. A semiconductor branch, for example, should reconcile device physics, process, packaging, thermal, manufacturing, reliability, and cost findings rather than forwarding disconnected reports to the central orchestrator.

Parent synthesis must preserve disagreement and uncertainty. It should not erase a minority view simply because one recommendation was selected.

### Step 9: Cross-branch integration

The systems/product layer examines whether the active branches form a coherent system. It checks requirements, interfaces, constraints, operating concept, lifecycle, dependencies, and trade-offs.

Cross-branch conflicts are made explicit. For example, a materials choice may improve thermal performance but harm manufacturability; a security control may reduce usability; a research recommendation may require unavailable data; a software architecture may conflict with hardware power limits.

The enterprise should create a decision packet that presents the conflict, options, criteria, consequences, and recommendation for human or authorised decision.

### Step 10: Independent assurance

Assurance branches review the integrated work rather than only individual outputs. They attack the problem, evidence, architecture, safety, security, compliance, claims, and operational viability.

Where possible, the reviewer should not be the same agent or team that created the design. Independence is a structural relationship, not merely a prompt saying “be critical.”

### Step 11: Gate decision

The relevant authority decides whether to proceed, proceed with conditions, loop back, descope, pause, or stop. The decision records the evidence, unresolved conditions, owner, due date, and effect on the project graph.

### Step 12: Reconfiguration

The project graph changes as evidence arrives. A failed experiment may activate a new materials branch, remove a solution path, reopen requirements, or change the prototype sequence. A new regulatory finding may add compliance and legal work. A production incident may return the project to architecture or requirements.

The system must treat reconfiguration as normal lifecycle behaviour, not as an organisational failure.

## 3. Collaboration patterns

### Independent parallel research

Used when multiple domains can investigate separate questions without premature convergence. Outputs include evidence and implications, not just summaries.

### Complementary decomposition

Used when different branches own different parts of one system. A systems integrator maintains the interfaces and resolves conflicts.

### Competing analysis

Used when a decision is high-consequence or the first recommendation may be anchored. Multiple teams receive the same question with intentionally independent approaches before synthesis.

### Creator–reviewer separation

Used for safety, security, compliance, critical architecture, public claims, or irreversible decisions. A separate team reviews the creator's work.

### Red-team challenge

Used to attack assumptions, failure modes, misuse, alternatives, and communication claims. The red-team produces concrete failure conditions and recommended responses.

### Convergence workshop

Used when multiple teams disagree or when the system must choose one architecture. The output is a decision packet, not a forced consensus. Dissent and rejected alternatives remain recorded.

### Escalation to user or external authority

Used when the choice depends on user values, budget, acceptable risk, legal interpretation, domain sign-off, physical test, or authority unavailable to the enterprise.

## 4. Team leadership roles

### Mission orchestrator

Maintains the project objective, decomposes work, activates branches, tracks progress, identifies missing capabilities, and manages the project graph.

### Systems integrator

Maintains whole-system coherence. Ensures that requirements, ConOps, architecture, interfaces, constraints, and lifecycle assumptions remain consistent across branches.

### Capability lead

Owns a branch's scope, decomposes it recursively, integrates child outputs, and represents the branch in cross-branch decisions.

### Work-package owner

Owns the completion and quality of a bounded task. This can be a human, agent, or mixed team.

### Evidence/provenance steward

Ensures that claims, calculations, data, sources, tests, and inferences are labelled and traceable.

### Assurance lead

Coordinates independent quality, safety, security, compliance, reliability, and red-team review.

### Project-state steward

Maintains decisions, requirements, assumptions, risks, open questions, artefacts, changes, and handoff state in the operating kernel.

### Decision authority

Makes or approves decisions that cannot be delegated safely. The user remains the ultimate authority for personal objectives, values, major trade-offs, and sufficiency unless explicitly assigning authority elsewhere.

## 5. Handoff contract

Every handoff should contain:

1. Work-package identity and parent project.
2. Objective and decision supported.
3. Relevant context and current state.
4. Inputs and source locations.
5. Scope and explicit exclusions.
6. Known constraints and assumptions.
7. Required evidence standard.
8. Expected artefact and acceptance criteria.
9. Dependencies and interfaces.
10. Authority and approval requirements.
11. Risks, failure modes, and escalation triggers.
12. Provenance and confidence expectations.
13. Due priority and stopping condition.
14. Required update to shared project state.

A receiving team should be able to understand the task without reading the raw conversation, while still having access to the evidence needed to challenge the handoff.

## 6. Integration rules

The project graph should maintain one canonical current state, but not one forced opinion. It must preserve competing interpretations until a decision is made.

A branch may not silently change another branch's requirements, interfaces, claims, or assumptions. It must issue a change-impact notification. The affected branch can accept, reject, or escalate the change.

A downstream discovery that invalidates an upstream assumption must be able to reopen upstream work. The system should record the reason and affected artefacts rather than hiding the loop.

A team may recommend an action but may not claim validation it did not perform. A coding team may report that a test passed; it may not claim production reliability. A research team may report literature evidence; it may not claim field feasibility. A communication team may compress claims; it may not upgrade their evidence status.

## 7. Dynamic scaling and proportionality

The enterprise should scale by risk and novelty, not by ambition alone. A reversible low-impact task may use one coordinator and one implementer. A novel semiconductor, aerospace, clinical, or safety-critical system may require multiple independent analysis teams, formal requirements, specialist review, simulation, prototype tests, compliance analysis, and external validation.

The project graph should record why a branch was not activated. This prevents missing capability from being mistaken for an intentional exclusion.

## 8. Core collaboration failure modes to prevent

The architecture must actively prevent:

- disconnected specialist reports with no systems integration;
- duplicate research by multiple teams that cannot see each other's decisions;
- anchoring on the first proposed solution;
- creators approving their own work;
- a central orchestrator becoming a single point of cognitive failure;
- untracked changes that invalidate downstream work;
- reports without evidence or decision implications;
- excessive activation of irrelevant specialists;
- false consensus that erases dissent;
- and context loss across long-running tasks or different tools.
