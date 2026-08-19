# Adversarial Cycle 02 — Systems Architecture and Decomposition

## Review question

Does the capability-tree/project-graph/governance-spine architecture provide enough structure to build and evolve a universal enterprise, or does it hide missing architecture viewpoints, brittle interfaces, configuration drift, and recursive decomposition failure?

## Reviewer lenses

### Systems architect

The tree, graph, and spine are useful structural metaphors, but they are not yet an architecture description. A serious architecture must show stakeholder concerns, viewpoints, views, relationships, interfaces, constraints, lifecycle states, and correspondence between views. ISO/IEC/IEEE 42010 treats architecture description as a way to create, analyse, and sustain architectures using viewpoints, frameworks, and description languages [1].

**Revision:** Define a view catalogue rather than a single diagram. At minimum, include mission/outcome, capability, stakeholder/ConOps, functional/workflow, information/evidence, technical/deployment, security/trust, governance/authority, assurance, operations, and configuration views.

### Configuration manager

The baseline assumes that versioning and event history are enough. They are not enough unless the enterprise identifies configuration items, establishes approved baselines, controls changes, accounts for status, and verifies that the current product matches the approved information. NASA treats configuration management as a lifecycle backbone connecting requirements, interfaces, risk, technical data, assessments, and decisions [2].

**Revision:** Add configuration management as a kernel service with configuration-item identification, baseline types, change authority, status accounting, verification, and audit.

### Interface architect

The project graph expresses dependencies but not stable interface contracts. A branch may produce an output that is semantically valid for itself but unusable by another branch. Interoperability requires schemas, identifiers, versioning, preconditions, postconditions, error states, latency/cost expectations, and change compatibility.

**Revision:** Every capability-cell and cross-branch boundary receives an interface contract. The contract covers input/output schema, evidence/provenance, confidence, failure states, timing, authority, side effects, version compatibility, and escalation.

### Complexity theorist

Recursive decomposition can create a fractal bureaucracy. If every branch can spawn more branches, the architecture may have no stable stopping rule and can generate circular ownership. The decomposition must terminate at a task that can be assigned, executed, reviewed, and accepted under a defined contract.

**Revision:** Add recursion stop conditions: bounded uncertainty, clear owner, verifiable output, manageable risk, and no unresolved cross-boundary dependency that requires deeper decomposition.

### Integration lead

The design is too centred on internal capabilities. Real systems depend on external institutions, suppliers, laboratories, regulators, APIs, users, and physical environments. These actors are not just sources or stakeholders; they are external system elements with interfaces, availability, authority, failure modes, and contractual boundaries.

**Revision:** Add external-system/interface objects and an integration context view. The project graph must represent relationships outside the virtual enterprise, including authority boundaries and unverifiable dependencies.

### Configuration/security reviewer

A centralized governance spine can create a single canonical state that every branch reads and writes. This increases integrity risk, availability risk, and blast radius. A safer architecture separates current projections, append-only history, branch-local states, policy decisions, evidence repositories, and execution environments.

**Revision:** Treat the spine as a governed federation of control services, not a single database or unrestricted central process. The architecture should support degraded operation, reconciliation, recovery, and partial isolation.

## Falsifications

### Falsification 1 — A tree is enough

A tree represents decomposition but not cross-cutting concerns, feedback, interfaces, competing authorities, or external dependencies. The enterprise must use tree plus graph plus views plus baselines.

### Falsification 2 — A project graph is enough

A graph of tasks and dependencies does not establish whether the nodes share compatible definitions, configurations, authority, evidence, or versioned interfaces. The graph needs typed edges, contracts, baselines, and change impact.

### Falsification 3 — One canonical state is enough

A single current state can conceal history, branch dissent, concurrent changes, invalid transitions, and corrupted updates. The kernel requires state projections plus event/history, with controlled transitions and recovery.

### Falsification 4 — Version numbers are configuration management

Versioning an artefact does not by itself define the approved baseline, authority, dependency set, system configuration, or verification that the artefact matches the product. Configuration management must be an explicit lifecycle service.

### Falsification 5 — Viewpoint completeness can be assumed

The system cannot have a universal fixed diagram that serves every domain. Different projects and stakeholders require different views. The enterprise should use a viewpoint catalogue and select views by project concerns.

## Accepted architecture revisions

1. Add an architecture-description package with concern-driven views.
2. Add configuration-management service and configuration-item registry.
3. Define functional, allocated, product/build, and as-operated baselines, adapting the exact set to project maturity.
4. Add typed, versioned interface contracts to capability cells and project-graph edges.
5. Add external-system and authority objects to the project graph.
6. Add recursive decomposition stop conditions and ownership constraints.
7. Separate canonical projections, append-only history, branch state, control policy, evidence, and execution.
8. Add a configuration verification loop that checks product/implementation against approved baselines.

## Cycle 2 judgement

The tree/graph/spine concept remains useful but was under-specified. The strongest revision is to treat it as an architecture description with multiple views and to add configuration and interface management as first-class kernel services. The enterprise is not a universal tree; it is a **configuration-controlled, concern-oriented, recursively decomposable system of systems**.

## References

[1] [ISO/IEC/IEEE 42010:2011 Architecture Description, replaced by 2022 edition](https://www.iso.org/standard/50508.html)  
[2] [NASA Systems Engineering Handbook — Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/)
