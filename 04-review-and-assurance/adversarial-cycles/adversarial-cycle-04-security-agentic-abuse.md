# Adversarial Cycle 04 — Security, Identity, and Agentic Abuse

## Review question

Are the current governance and kernel security controls sufficient when every worker, tool, source, model, memory store, and external system may be compromised, deceptive, stale, or operating under an unintended interpretation?

## Reviewer lenses

### Zero-trust security architect

“Least privilege” is necessary but underspecified. It does not answer which identity, resource, purpose, context, time, data class, and action are being authorised. Local execution, previous approval, project membership, or trusted network location cannot imply trust. NIST Zero Trust Architecture explicitly moves protection toward users, assets, and resources rather than static network perimeters [1].

**Revision:** Model every action authorization as a contextual policy decision over subject, capability, project, resource, purpose, operation, data class, environment, time, risk, and required approval. Make permissions short-lived, scoped, revocable, and observable.

### Agent security red-team

Prompt injection is only one symptom. A worker may receive malicious source material, poisoned retrieval content, a tool result containing instructions, a compromised skill, an adversarial model response, or a forged approval. The worker may then attempt a legitimate-looking action under an illegitimate instruction.

**Revision:** Treat all external content, tool output, retrieved text, model output, and inter-agent messages as untrusted data until classified. Preserve instruction provenance and separate control instructions from content. Use context isolation, output validation, tool schemas, policy checks, and action confirmation.

### Confused-deputy reviewer

An agent with broad privileges can be tricked into using its authority on behalf of another source or worker. Capability cards do not prevent a trusted worker from being misdirected.

**Revision:** Require the kernel—not the worker—to evaluate authority at the point of action. The worker proposes an action; a policy enforcement point evaluates identity, scope, resource, risk, approval, and side-effect budget. A worker cannot grant itself authority.

### Memory and continuity reviewer

The continuity file and project memory are valuable attack and failure surfaces. A poisoned memory item could persist across sessions, contaminate future research, alter routing, or create false project history. Cross-project reuse may leak sensitive context or cause inappropriate transfer.

**Revision:** Separate project-local memory from reusable knowledge. Require provenance, trust status, scope, expiry/freshness, and review before memory becomes an instruction or decision premise. Never let generated summaries silently become canonical history.

### Supply-chain reviewer

The threat is not limited to libraries. Models, prompts, skills, agents, tool servers, browser extensions, datasets, retrieved corpora, container images, and external APIs are all supply-chain components. Reputation or popularity is not provenance.

**Revision:** Expand SBOM-like component records to AI/agent assets, including source, version, hash where possible, owner, licence, permissions, build path, evaluation, known threats, change history, and rollback. Use isolated test/quarantine before activation.

### Incident responder

The baseline lists quarantine and recovery but does not define an incident boundary. An agent may have made many actions across branches before detection; the damage may include false evidence, altered decisions, external side effects, or contaminated memory.

**Revision:** Define incident levels, kill/quarantine actions, credential revocation, affected-scope discovery, replay, state restoration, evidence preservation, notification, claims review, and post-incident control changes. The system should assume partial compromise and continue in degraded mode where safe.

## Falsifications

### Falsification 1 — Tool allowlists are sufficient

A permitted tool can still be used with dangerous parameters, poisoned inputs, wrong project context, excessive volume, or unauthorized data. Tool identity is not action authorization.

### Falsification 2 — Human approval eliminates risk

A human may approve a misleading summary, suffer automation bias, lack context, or approve a compound action without seeing its consequences. Approval must be informed, scoped, reversible where possible, and supported by meaningful previews.

### Falsification 3 — Sandboxing equals safety

A sandbox may prevent host escape while still allowing data exfiltration, destructive changes inside the project, cost exhaustion, poisoned artefacts, or incorrect external communication. Sandbox boundaries must match assets and side effects.

### Falsification 4 — Audit logs are enough

An audit trail after the fact does not prevent a destructive action. Prevention, detection, containment, recovery, and learning are distinct controls.

### Falsification 5 — Independent agents are independent reviewers

Two agents may share models, prompts, retrieval sources, blind spots, or orchestration incentives. Apparent plurality does not establish independence.

### Falsification 6 — Zero trust means no collaboration

Zero trust does not prohibit useful collaboration; it replaces implicit trust with explicit, contextual, continuously evaluated authorization. The enterprise can collaborate if it makes boundaries and policy decisions visible.

## Accepted security revisions

1. Separate capability identity, authority, data access, and action permission.
2. Put a policy enforcement point between every worker and material side effect.
3. Use plan/preview/approve/execute for consequential actions, with dry-run and rollback where possible.
4. Add purpose, context, time, risk, data class, and approval to authorization decisions.
5. Treat external content, tool outputs, memory, prompts, skills, models, and inter-agent messages as untrusted until classified.
6. Add project-local memory isolation, provenance, freshness, expiry, and promotion review.
7. Extend supply-chain governance to models, prompts, skills, datasets, workers, containers, tools, and retrieval sources.
8. Add incident severity, containment, scope discovery, replay, state repair, claim review, and degraded operation.
9. Add secure defaults, egress controls, rate/cost/side-effect budgets, and permission expiry.
10. Test the security architecture against attack paths from MITRE ATLAS, OWASP agentic guidance, NIST CSF, and project-specific threats [2] [3] [4].

## Cycle 4 judgement

The baseline security model was directionally sound but too control-list oriented. The main upgrade is to treat security as a **runtime authority and containment architecture**, not a set of static policies. The kernel must make every material action attributable, contextual, reviewable, reversible where possible, and recoverable after partial compromise.

## References

[1] [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)  
[2] [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)  
[3] [MITRE ATLAS](https://atlas.mitre.org/)  
[4] [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
