# Universal Virtual Enterprise Blueprint v1.1

**Status:** Revised after Improvement Cycle 001  
**Purpose:** Define a universal, recursively decomposable, evidence-governed virtual enterprise that can assemble and coordinate high-quality capabilities for arbitrary domains.

## Executive summary

The universal enterprise is a **capability ecosystem with a control system**, not a flat set of agents. It contains a capability tree, a project-specific graph, and a governance spine. Version 1.1 adds five control planes that were missing from the first baseline:

1. **Competence and capability governance:** capability cells now carry evidence of competence, method, freshness, limits, and evaluation.
2. **Assurance and argumentation:** important claims are supported by structured claims, arguments, evidence, assumptions, rebuttals, and reviewer status.
3. **Kernel security and agent incident response:** the operating kernel is treated as a high-value system with identity, isolation, permissions, audit, recovery, and worker incident controls.
4. **Data, model, source, and supply-chain governance:** data, models, tools, sources, dependencies, licenses, vulnerabilities, and provenance are explicit lifecycle objects.
5. **Portfolio, economics, and orchestration measurement:** the system manages scarce capability, cost, latency, duplicate work, coverage, and value of information.

These additions do not change the basic architecture. They make it capable of governing the quality and limits of the specialist branches rather than merely activating them.

## 1. The three structural views

### Capability tree

The capability tree defines reusable capability families and recursively decomposes them into disciplines, methods, teams, tools, and workers. It is versioned and governed. It is not assumed to be complete merely because it contains many branches.

### Project graph

The project graph activates and connects a mission-specific subset of the capability tree. It represents requirements, dependencies, evidence, work packages, interfaces, decisions, reviews, and feedback. It supports independent branches, competing analyses, parent synthesis, and controlled reconfiguration.

### Governance spine

The governance spine carries project state, evidence, assurance arguments, requirements, decisions, risks, authority, handoffs, gates, claims, changes, incidents, and measurement. It is also responsible for security and isolation of the kernel itself.

## 2. Capability governance

A capability is not trusted merely because it has an impressive name or a capable model behind it. Each capability cell has a **capability card** containing:

- mandate, scope, and non-goals;
- domain, methods, tools, and operating assumptions;
- competence evidence, benchmark results, prior outcomes, and reviewer status;
- source and knowledge provenance;
- freshness and review date;
- known strengths, blind spots, and failure modes;
- applicable project types and maturity levels;
- authority and side-effect permissions;
- cost, latency, compute, and availability profile;
- required inputs and output contract;
- independence/conflict-of-interest status;
- escalation and external-validation requirements;
- and conditions for deactivation or substitution.

Capability cards are not permanent reputational scores. They are context-dependent evidence about what a capability can do under specified conditions. The system should prefer diverse and independent evidence over one global ranking.

The capability ontology itself is versioned. Additions, merges, aliases, retirements, and taxonomy changes are recorded because a capability reclassification can change routing and past project comparisons.

## 3. Completeness and omission control

The enterprise cannot prove that it has considered every factor in the world. It can, however, make omission risk visible and systematically reduce it.

Every project should maintain a coverage map across:

- problem and stakeholder domains;
- operational and lifecycle phases;
- technical disciplines;
- legal/regulatory obligations;
- safety/security/privacy concerns;
- solution families and alternatives;
- supply chain and external dependencies;
- claims and evidence;
- and implementation/validation stages.

The system should run omission probes such as:

- What discipline could invalidate this architecture?
- What stakeholder is affected but not represented?
- What failure occurs outside the happy path?
- What external authority could reject the claim?
- What dependency, regulation, or environmental condition is stale or absent?
- What alternative is not being considered because of anchoring?
- What is the cheapest test that could disprove the central assumption?

A coverage gap is not automatically a defect. It becomes a governed state: research, review, test, mitigation, deferral, or explicit exclusion.

## 4. Assurance argument system

The evidence graph is extended into an assurance graph. An assurance case represents:

- top-level claim;
- subordinate claims;
- argument linking claims;
- evidence supporting each claim;
- explicit assumptions and justifications;
- rebuttals and counter-evidence;
- reviewer confidence and independence;
- residual gaps and conditions;
- and permitted use contexts.

This structure follows the assurance-case principle that claims, arguments, evidence, and assumptions should connect systematically for properties such as safety, reliability, maintainability, operability, and security [1].

An assurance case is not a statement that a system is perfect. It is a transparent explanation of why a claim should be trusted within its scope, what assumptions it depends on, what evidence is weak, and what would invalidate it.

## 5. Kernel security and agent incident control

The operating kernel contains sensitive project state, authority, evidence, source access, worker permissions, and possibly secrets. It therefore has its own threat model and security lifecycle.

Minimum controls include:

- project and tenant isolation;
- least-privilege identity and access;
- separate secret management;
- sandboxed tool execution;
- explicit side-effect permissions;
- artefact and source trust classification;
- immutable or tamper-evident audit events;
- approval and delegation expiry;
- remote-worker isolation;
- model/tool allowlists and budget limits;
- backup, recovery, and state repair;
- monitoring and alerting;
- and incident response.

Agent incidents include prompt injection, malicious artefacts, data exfiltration, unintended tool action, excessive agency, privilege escalation, inter-agent trust abuse, corrupted memory/project state, hidden instruction conflict, uncontrolled cost, and compromised worker or dependency.

The incident process should support containment, worker disable/quarantine, permission revocation, evidence preservation, replay, state comparison, recovery, impact analysis, corrective action, and review of affected claims and baselines.

## 6. Data, model, source, and supply-chain governance

The enterprise maintains registries for:

- datasets and data products;
- models and model versions;
- prompts/instruction packages and skills;
- external sources and research references;
- open-source libraries and services;
- APIs and tool providers;
- infrastructure and build environments;
- hardware/components where relevant;
- and produced artefacts.

Each registry item includes owner, provenance, version, licence/rights, date, fitness, limitations, dependencies, security status, evaluation, freshness, retention, and allowed use. Data and model changes create impact events because they may change outputs, claims, or safety status.

For software, component transparency includes SBOM-like inventory, build provenance, vulnerability status, licence obligations, and VEX/exception information where applicable. CISA treats SBOM as a key building block for software security and supply-chain risk management [2].

## 7. Portfolio, economics, and orchestration

The enterprise must decide not only what can be done, but what should be activated now. Portfolio governance manages:

- mission priority and strategic fit;
- budget and compute;
- capability capacity and scarcity;
- external expertise or laboratory access;
- deadlines and opportunity cost;
- dependency conflicts across projects;
- reuse and shared infrastructure;
- research depth and value of information;
- and stop/pivot/descope decisions.

Orchestration should record why a capability was activated, what context it received, what it cost, what uncertainty it reduced, and whether its output changed a decision. It should control context size, cost, latency, duplicate work, and unnecessary specialist activation.

Useful enterprise measurements include:

- decision-changing evidence per unit cost/time;
- unresolved high-impact uncertainty over time;
- duplicate research rate;
- contradiction detection and resolution;
- coverage-gap discovery;
- handoff return rate;
- review defect discovery;
- traceability completeness;
- rework caused by late discovery;
- outcome and user value;
- and system reliability/security.

These metrics are diagnostic, not a single leaderboard.

## 8. Capability assembly and assurance flow

The mission flow is now:

1. Intake and frame the mission.
2. Detect capability branches and potential omitted disciplines.
3. Evaluate capability cards, freshness, independence, limits, and cost.
4. Select depth and form a project graph.
5. Create work packages and evidence/assurance contracts.
6. Run independent or competing analyses where anchoring or consequence warrants it.
7. Synthesize at branch and systems levels while preserving dissent.
8. Build requirements, decisions, architecture, and assurance cases together.
9. Implement or experiment through controlled workers.
10. Verify, validate, red-team, and audit.
11. Make a gate decision through authorised authority.
12. Operate, monitor, learn, and reconfigure.

## 9. Integrated software subsystem

The enterprise software pipeline remains the detailed downstream subsystem. It now adds:

- capability cards for product, architecture, development, security, QA, SRE, compliance, and AI teams;
- assurance cases for high-impact software claims;
- data/model/source registries;
- SBOM/build provenance and component governance;
- agentic threat model and incident response where workers are used;
- explicit quality profiles and measurable quality requirements;
- portfolio and cost/latency controls;
- operational evidence and recovery-driven re-planning;
- and end-to-end traceability from upstream objective to deployed observation.

## 10. Revised staged construction

1. **Kernel security and state:** project state, evidence, identity, permissions, versioning, audit, and continuity.
2. **Coverage and assurance:** factor/coverage map, claim/evidence/argument graph, gates, reviewers, and change impact.
3. **Capability registry:** ontology versioning, capability cards, freshness, evaluation, activation depth, and substitution.
4. **Upstream project framework:** NHAI/VitalNet/TabVolt-derived discovery and systems design.
5. **Software lifecycle:** requirements, architecture, implementation, testing, secure development, release, operations, retirement.
6. **Controlled workers:** sandboxed research/coding/analysis workers with budgets, logs, resumability, and incidents.
7. **Dynamic team graph:** parallel work, competing analysis, parent synthesis, conflicts, and reconfiguration.
8. **Domain pipelines:** robotics, scientific, manufacturing, clinical, regulatory, semiconductor, and others.
9. **Portfolio and ecosystem:** cross-project capacity, reusable knowledge, external capability references, and strategic planning.

## 11. Residual boundaries

The enterprise still cannot honestly claim access to every world-class expert, proprietary data, laboratory, regulator, or physical validation environment. It must distinguish capability simulation from external expertise and generated reasoning from validated knowledge.

It must also resist becoming a bureaucratic document factory. The added control planes exist to improve decisions, evidence, safety, and coordination. If a control does not change a decision, protect a stakeholder, support a handoff, or preserve future trust, it should be simplified or removed.

## References

[1] [ISO/IEC 15026-2 Assurance case](https://www.iso.org/standard/52926.html)  
[2] [CISA Software Bill of Materials](https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom)  
[3] [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)  
[4] [ISO/IEC 42001 AI management systems](https://www.iso.org/standard/42001)  
[5] [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)  
[6] [NIST SP 800-61 Rev. 3 Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
