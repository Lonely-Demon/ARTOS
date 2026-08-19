# Improvement Cycle 001 Change Log

## Baseline

The cycle began from Universal Enterprise Blueprint v0, Enterprise Software Lifecycle v1, Assurance/Operations v1, Operating Kernel v1, and the previously established NHAI/VitalNet/TabVolt-derived workflow.

## Research focus

The cycle investigated assurance cases, agentic security, AI management systems, cybersecurity governance, incident response, software supply-chain transparency, SBOM/VEX, requirements engineering, product quality, capability routing, and operational improvement.

## Sources read

- ISO/IEC/IEEE 15026-2 Assurance Case: https://www.iso.org/standard/52926.html
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- ISO/IEC 42001 AI Management Systems: https://www.iso.org/standard/42001
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- CISA Software Bill of Materials: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
- NIST SP 800-61 Rev. 3 Incident Response: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- ISO/IEC/IEEE 29148 Requirements Engineering: https://www.iso.org/standard/72089.html
- ISO/IEC 25010 Product Quality Model: https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:en
- Microsoft Security Development Lifecycle: https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle
- Google Engineering Practices: https://google.github.io/eng-practices/
- GitLab Product Development Flow: https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

## Major discoveries

The first baseline had a capability tree and project graph but lacked evidence that activated capabilities were competent, current, independent, properly scoped, and economically justified. It had a claim/evidence relationship but not a full assurance argument connecting claims, subordinate claims, arguments, evidence, assumptions, rebuttals, and reviewer confidence. It had software security controls but did not treat the kernel and agent workers as a distinct high-value attack surface. It also lacked explicit data/model/source/supply-chain governance, agent incident response, portfolio/economic control, and measurable coverage/omission control.

## Changes accepted

### 1. Capability governance plane

Add capability cards with mandate, scope, methods, competence evidence, benchmarks, freshness, limitations, independence/conflicts, cost/latency, authority, and activation limits. Version the capability ontology and govern taxonomy changes.

### 2. Assurance argument plane

Extend the evidence graph into an assurance graph supporting claims, arguments, evidence, assumptions, justifications, rebuttals, residual gaps, reviewer confidence, and permitted use contexts.

### 3. Kernel and worker security plane

Threat-model the operating kernel, project state, remote workers, tools, memory, inter-agent communication, credentials, and side effects. Add isolation, permissions, approval, audit, kill/quarantine, replay, state repair, and incident response.

### 4. Data/model/source/supply-chain plane

Register datasets, models, prompts/skills, sources, APIs, tools, dependencies, infrastructure, and artefacts with version, provenance, licence/rights, freshness, security status, evaluation, retention, and allowed use. Add SBOM/build provenance/VEX-style controls for software.

### 5. Portfolio and orchestration measurement plane

Add budget, capacity, cost, latency, duplicate work, value-of-information, coverage, contradiction, review, rework, outcome, and reliability measurements. Treat metrics as diagnostic rather than a single performance score.

### 6. Enterprise software revision

Add capability readiness, assurance cases, quality profiles, data/model/source registries, SBOM/provenance, agentic threat/incident controls, AI management concerns, staged release/recovery, and upstream feedback.

## Rejected or deferred ideas

- Building a static list of every profession or institution was rejected in favour of dynamic capability discovery and activation.
- Treating every document name as mandatory was rejected in favour of an information graph with tailored views.
- Treating research source count as completeness was rejected in favour of coverage/omission review and decision impact.
- Requiring all specialist branches to activate on every project was rejected in favour of risk/novelty/depth tailoring.
- Treating assurance as one final reviewer was rejected in favour of layered creator, peer, specialist, independent, red-team, authority, and operational assurance.

## Residual uncertainties

- Capability competence scoring and calibration need real project data; a global score would be misleading.
- Coverage metrics cannot prove that every possible factor has been found; they can only expose structured gaps and omission risk.
- Assurance cases need a practical representation in the first kernel without creating excessive authoring burden.
- Agentic security threats will evolve; current OWASP guidance should be treated as a baseline subject to updating.
- Legal, regulatory, clinical, safety, and certification authority cannot be simulated fully by the enterprise.
- Portfolio economics and value-of-information need calibration against actual compute, research, worker, and project costs.
- Local/remote security and multi-tenant isolation require implementation-level threat modelling.

## Cycle assessment

The cycle produced architecture-level improvements rather than mere terminology changes. It should be followed by a stress-test cycle against NHAI, robotics, VitalNet, TabVolt, and the future harness itself. Further research should focus only on residual uncertainties or findings that could change the revised architecture.
