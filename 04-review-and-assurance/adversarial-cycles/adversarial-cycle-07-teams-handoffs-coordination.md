# Adversarial Cycle 07 — Team Assembly, Handoffs, and Coordination

## Review question

Does the virtual-enterprise team model create the benefits of multidisciplinary collaboration, or does it create cognitive overload, coordination explosion, ambiguous ownership, and endless specialist handoffs?

## Reviewer lenses

### Organisation designer

A recursively decomposable tree can easily become an organisation chart in disguise. Team Topologies explicitly warns that teams have cognitive limits and that adding tools, responsibilities, or domains can make competent teams ineffective [1]. More branches are not automatically more expertise.

**Revision:** Add cognitive-load budgeting and limit each active team cell's mission, interfaces, tools, and simultaneous obligations. A capability may be available in the ontology without being activated in a project.

### Flow architect

The current architecture treats many interactions as generic collaboration. That creates ambiguity and unnecessary meetings. Team Topologies distinguishes collaboration, X-as-a-service, and facilitation, alongside stream-aligned, platform, enabling, and complicated-subsystem roles [1].

**Revision:** Every cross-team relationship chooses an interaction mode, expected duration, owner, service level, artefact contract, and exit condition. Collaboration is used for discovery/integration, service mode for stable reusable outputs, and facilitation for temporary capability transfer.

### Delivery owner

The governance model names many authorities but does not guarantee a single accountable owner for each outcome. If the mission owner, orchestrator, systems integrator, capability lead, assurance team, and executor can all influence a decision, ownership may become a negotiation rather than a responsibility.

**Revision:** Every mission outcome, requirement, decision, work package, interface, evidence item, and gate has a directly responsible owner and a decision authority. Consulted and reviewing parties cannot silently become co-owners.

### Handoff reviewer

A handoff can mean advice, contribution, delegation, review, approval, or ownership transfer. If these are not distinguished, a receiver may believe it owns the work while the sender believes it remains accountable. GitLab’s public product-flow material reinforces the importance of role clarity, handoffs, and continuity in distributed product development [2].

**Revision:** Encode handoff type, sender, receiver, transferred state, retained responsibility, acceptance criteria, return path, deadline, and escalation. Ownership transfer must be explicit; a consultation never transfers authority.

### Integration lead

Cross-branch synchronization can grow rapidly with the number of active teams. A universal enterprise may spend more time translating outputs than solving the problem. The systems integrator should not become a bottleneck through which every branch must pass.

**Revision:** Use hierarchical synthesis: team cell → branch lead → system integrator only for cross-boundary decisions. Stable platform capabilities should be consumed as services. Only high-risk or contradictory work receives full integration review.

### Human-factors reviewer

AI workers can simulate roles but do not possess identical accountability, tacit knowledge, motivation, or institutional authority. Treating a model as a “team” may hide missing human judgement and create false responsibility allocation.

**Revision:** Separate role simulation from authority. Every high-impact capability has a human or external authority requirement where appropriate. Capability cells must declare whether they provide analysis, recommendation, execution, review, or formal authority.

### Change manager

Dynamic assembly can cause team churn. Replacing a worker or adding a new specialist midstream may invalidate context, assumptions, or trust. Reconfiguration is not free.

**Revision:** Treat team topology changes as configuration changes with reason, impact assessment, state handoff, onboarding packet, capability version, and continuity check.

## Falsifications

### Falsification 1 — More teams produce better work

More teams expand coverage but increase coordination, translation, conflict, cost, latency, and cognitive load. Activation must be justified by expected decision value or risk reduction.

### Falsification 2 — Collaboration is always the best interaction

Long-term collaboration between every branch creates dependency and overload. Stable interfaces should become services; temporary skill gaps should use enabling relationships.

### Falsification 3 — The orchestrator can own everything

Central ownership makes the orchestrator a bottleneck and a single failure point. The orchestrator should coordinate, not absorb every technical decision or become the sole interpreter of all work.

### Falsification 4 — A handoff equals completion

Passing an artefact does not mean the receiver can use, verify, or own it. Handoffs require state, contract, acceptance, authority, and return paths.

### Falsification 5 — A role description defines capability

Naming a “security team,” “research team,” or “architect” does not establish competence, independence, current capacity, or authority. Capability cards and contextual evaluation remain necessary.

### Falsification 6 — Parallel work always accelerates progress

Parallel branches can duplicate research, diverge in assumptions, create merge conflicts, and delay synthesis. Parallelism should be selected when uncertainty or time benefit outweighs integration cost.

## Accepted team-system revisions

1. Add cognitive-load, handoff, and coordination budgets.
2. Classify active cells as stream-aligned, platform, enabling, complicated-subsystem, assurance, or authority patterns as appropriate.
3. Require interaction mode, owner, duration, contract, and exit condition for cross-team work.
4. Assign one directly responsible owner and one decision authority to each material object/outcome.
5. Distinguish consultation, contribution, delegation, review, approval, and ownership transfer.
6. Add hierarchical synthesis and avoid centralizing every branch through the systems integrator.
7. Add explicit human/external authority status to capability cards.
8. Treat topology changes as configuration changes with continuity and impact review.
9. Use parallel work selectively with a synthesis budget, divergence detection, and merge protocol.
10. Create a continuity packet for every ownership transfer.

## Cycle 7 judgement

The recursive team model is valuable but could become a coordination-heavy pseudo-organisation. The corrected model is a **dynamic team-of-teams system optimized for cognitive load and flow**, not an infinite roster of activated specialists. Its most important improvement is to make interaction mode and ownership as explicit as evidence and requirements.

## References

[1] [Team Topologies — Key Concepts](https://teamtopologies.com/key-concepts)  
[2] [GitLab Product Development Flow](https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/)
