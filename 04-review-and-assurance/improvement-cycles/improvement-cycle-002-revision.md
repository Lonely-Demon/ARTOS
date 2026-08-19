# Improvement Cycle 002 Revision Addendum

## Focus

This cycle targeted the remaining high-risk AI/agent issues: operational AI governance, measurable trustworthiness, threat-informed red teaming, and the distinction between a capability that can produce output and one that can be safely activated.

## New evidence

NIST's AI RMF Playbook organizes actionable guidance around Govern, Map, Measure, and Manage and is intended to incorporate trustworthiness throughout design, development, deployment, and use. It is explicitly voluntary and tailorable, which supports the virtual enterprise's risk-based depth model.

MITRE ATLAS provides a living threat-informed knowledge base for AI systems, including tactics, techniques, mitigations, and case studies across predictive, generative, agentic, and enterprise AI. This strengthens the need for a scenario-based AI/agent red-team subsystem rather than generic prompt testing alone.

## Accepted design revisions

### AI capability lifecycle

Every AI or agent capability should have four linked loops:

| Loop | Required work |
|---|---|
| Govern | Ownership, purpose, policy, authority, risk appetite, legal/ethical boundaries, lifecycle responsibility |
| Map | System context, users, data, model, tools, threats, harms, dependencies, assumptions, affected groups |
| Measure | Capability, robustness, safety, security, privacy, bias/fairness where applicable, cost, latency, drift, reliability, red-team results |
| Manage | Mitigation, deployment conditions, human oversight, monitoring, incident response, remediation, re-evaluation, retirement |

### Threat-informed agent assurance

Agent/AI red-team packages should map attack scenarios to assets, tactics, techniques, controls, test methods, evidence, residual risk, and corrective action. MITRE ATLAS and OWASP agentic guidance can serve as living references, but project-specific threat models remain necessary.

### Capability activation status

A capability card should distinguish:

- discoverable: the ontology knows the capability exists;
- available: the worker/source/tool can currently be invoked;
- eligible: it satisfies project permissions, freshness, competence, and risk conditions;
- activated: it is part of the project graph;
- trusted for recommendation: its output may inform decisions under stated conditions;
- trusted for execution: it may perform bounded actions;
- trusted for approval: exceptionally, it may approve a defined class of low-risk outputs.

This avoids treating a capability's existence or benchmark as permission to use it for consequential work.

### Control-plane separation

The operating kernel should conceptually separate:

1. **Governance/control plane:** identity, policy, authority, budgets, approvals, gates, audit, and incident control.
2. **Knowledge/evidence plane:** project state, sources, artefacts, requirements, decisions, claims, assurance arguments, and history.
3. **Execution plane:** agents, tools, code, experiments, remote workers, sandboxes, deployments, and external side effects.
4. **External world:** users, institutions, APIs, laboratories, regulators, production systems, and physical environments.

The execution plane must not be able to rewrite governance or evidence state without an authorised, auditable path. The control plane may constrain execution; execution returns observations and proposed updates for review.

## Rejected or deferred

A universal quantitative trust score for every capability was rejected because competence is context-dependent and a single number would create false precision. The design uses evidence-bearing capability cards and activation states instead.

A claim that the enterprise can guarantee AI trustworthiness was rejected. It can structure governance, tests, monitoring, and evidence, but high-impact assurance remains conditional and external where necessary.

A static, one-time adversarial checklist was rejected. Threat references and red-team scenarios must be living and updated.

## Remaining improvement value

The second cycle produced architecture-level changes: four control planes, AI lifecycle loops, activation trust states, and threat-informed red-team mapping. A third cycle would be worthwhile only if it targets a concrete unresolved architecture question, especially semantic merge/conflict, project-state repair, capability evaluation calibration, or local/remote kernel security. Broadly repeating lifecycle-framework research is unlikely to change the design enough to justify its cost.
