# Enterprise software lifecycle research findings

## NASA Software Engineering Requirements

Source: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4

Key findings from NPR 7150.2D (effective 2022-03-08, shown as expiring 2027-03-08):

- Requirements are foundational to the entire lifecycle, planning, estimating, monitoring, and the software product. Requirements development includes elicitation, analysis, documentation, verification, validation, and ongoing customer validation.
- Requirements should be captured, approved, maintained, and applied to COTS, GOTS, MOTS, OSS, and reused components as applicable.
- Requirements should be clear, complete, consistent, individually verifiable, and traceable to higher-level requirements.
- Software requirements analysis should derive from top-level systems requirements, safety/reliability analysis, hardware specifications, and hardware design.
- Software safety constraints, controls, mitigations, and assumptions between hardware, operator, and software belong in software requirements documentation.
- Requirements changes must be tracked and managed; inconsistencies among requirements, plans, and products require corrective action through closure.
- Requirements validation must consider the customer environment.
- Architecture is treated as a major quality/longevity determinant and as the basis for software design and code. It formalizes decomposition, dependencies, change impact, consistency rules, views/patterns, interfaces, qualities, and valid/invalid operating modes.
- Architecture must be documented, and high-risk categories require architecture review.
- Software design refines architecture into lower-level units, interfaces, data, dependencies, constraints, resources, and behaviour so implementation and testing are possible.
- Implementation includes coding methods, standards, criteria, and unit testing.

## OWASP SAMM

Source: https://owaspsamm.org/model/

Key finding: OWASP SAMM is a widely distributed model for improving secure software practices across organizations. Version 2 incorporates practitioner and community input and provides a maturity model for secure software practices. It is intended as a model that organizations can use to assess and improve security practices rather than a single mandatory lifecycle.

## Current synthesis implication

The software subsystem must make requirements, architecture, interfaces, quality attributes, safety constraints, change management, design detail, coding standards, testability, and secure-development maturity explicit. Security and assurance are not only final release checks; they shape the lifecycle and can be assessed for maturity over time.

## Microsoft Security Development Lifecycle

Source: https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle

Key findings:

- Microsoft SDL uses five core phases—requirements, design, implementation, verification, and release—with two supporting activities for response and related security operations. Each core phase contains mandatory checks and approvals.
- Security and privacy requirements begin in requirements, based on data handled, threats, regulations, industry requirements, and prior incidents.
- Threat modelling begins in design, uses component and interaction analysis plus data-flow diagrams, and remains maintained through changes.
- Verification separates manual review by someone other than the developer from automated checks. Checks include static analysis, binary analysis, credential/secret scanning, encryption scanning, fuzz testing, configuration validation, and open-source component governance including version, vulnerability, and legal obligations.
- Release uses staged/safe deployment rings rather than releasing immediately to all users. Post-release monitoring and incident response are part of the lifecycle.
- Transferable insight: secure development is a continuous control system embedded in requirements, design, implementation, verification, release, and response. Independence of review and staged rollout are structural safeguards.

## DORA software delivery performance

Source: https://dora.dev/guides/dora-metrics/

Key findings:

- DORA measures software delivery performance through throughput and instability.
- Throughput metrics include change lead time, deployment frequency, and failed-deployment recovery time.
- Instability metrics include change fail rate and deployment rework rate.
- Metrics should be used to inform continuous improvement, not as a simplistic quality score.
- DORA recommends small change batches because they are easier to reason about, move through delivery, and recover from when failures occur.
- Transferable insight: the enterprise software subsystem needs operational feedback metrics and should design work/release increments for reversibility and recovery.

## ISO/IEC/IEEE lifecycle standards

Sources:
- https://www.iso.org/standard/63712.html
- https://standards.ieee.org/ieee/15288/10424/

Key findings:

- ISO/IEC/IEEE 12207 provides processes for defining, controlling, and improving software life-cycle processes within an organisation or project. It can be applied to software within a larger system, alongside systems engineering processes.
- ISO/IEC/IEEE 15288:2023 establishes a common framework of process descriptions for human-made systems, system elements, and systems of systems, across life-cycle stages and with stakeholder involvement.
- The standards support the user's universal-enterprise idea: software rarely exists in isolation; software processes and system processes must be coordinated when hardware, people, procedures, facilities, and software interact.
- IEEE material associated with 15288 notes that assurance can sit as a process view over systems/software life-cycle processes, focused on claims such as dependability, safety, and security.
- Measurement is treated as a lifecycle process that supports planning, managing, assessing, and decision-making. It does not prescribe one universal metric set or documentation medium; the user selects measures and methods appropriate to the project.
- ISO/IEC/IEEE 15289 addresses life-cycle documentation information items. The standards do not force every project to create every document or a single packaging format; processes and information should be tailored.
- Requirements engineering is iterative and recursive across the lifecycle, and a related standard addresses requirements engineering for systems and software.
- Transferable insight: the enterprise should use process families and outcomes rather than a rigid document checklist. Systems, software, assurance, measurement, requirements, and documentation are connected but tailored by project context and risk.

## Requirements engineering and software quality

Source: https://www.iso.org/standard/72089.html

Key findings:

- ISO/IEC/IEEE 29148:2018 specifies processes and information products for requirements engineering across the system and software life cycle.
- It provides guidance for applying requirements processes from ISO/IEC/IEEE 15288 and 12207 and specifies information-item content and format guidance.
- It applies across man-made systems, software-intensive systems, software/hardware products, and services, regardless of project scope, methodology, size, or complexity.
- Transferable insight: PRD, BRD, SRS, system requirements, and traceability artefacts should be treated as tailored information products within a requirements process, not as isolated document names.

## NIST AI Risk Management Framework

Source: https://www.nist.gov/itl/ai-risk-management-framework

Key finding: NIST AI RMF is intended to improve AI trustworthiness while enabling innovation and mitigating risk. It should complement, not replace, software engineering, security, privacy, domain, and operational controls.

Transferable insight: AI capability cells require additional governance for trustworthiness, risk, measurement, evaluation, human authority, data/model provenance, misuse, and lifecycle change. AI is not just another implementation component within the software pipeline.

## Google engineering practices

Source: https://google.github.io/eng-practices/

Key findings:

- Google publishes generalized engineering practices across languages and projects, including separate guides for code reviewers and change authors.
- Code review is treated as a code-health practice, not only a defect hunt. The change is expected to be self-contained and reviewable, and reviewer/author responsibilities are explicit.
- Transferable insight: the enterprise pipeline needs clear change units, author checklists, reviewer standards, review independence, and a distinction between substantive issues and non-blocking style comments.

## GitLab product development flow

Source: https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/

Key findings:

- GitLab uses a repeatable cross-functional flow for turning an idea into customer value, while allowing open-source contributions to enter at different points.
- The flow defines required outcomes/actions but treats other practices as recommendations; teams can tailor or skip phases when confidence is high and the risk is low.
- GitLab explicitly states its phases are not waterfall: phases may overlap or occur in parallel, and the purpose is to achieve outcomes and de-risk later work.
- The workflow uses current status and a maintained issue description as a single source of truth so contributors do not need to reconstruct state from every comment.
- Product validation is a track that can run ahead of the build track. It investigates the problem, business goals, metrics, hypotheses, user research/experiments, MVC, and risks to value, usability, feasibility, and viability.
- Transferable insight: the universal enterprise should separate discovery/validation from build execution when useful, maintain a current source of truth, represent work states explicitly, allow phase overlap, and tailor/skip phases based on confidence and risk rather than ceremony.

## ISO/IEC 25010 product quality

Source: https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:en

Key findings:

- The software/product quality model can support eliciting and defining product and information-system requirements, checking requirement completeness, identifying design objectives, defining testing objectives, identifying quality-control criteria, defining acceptance criteria, and establishing measures of quality characteristics.
- Transferable insight: quality attributes must become explicit requirements and measures rather than being treated as vague aspirations. The quality model should feed product requirements, architecture, test planning, acceptance, and assurance.

## OWASP ASVS

Source: https://owasp.org/www-project-application-security-verification-standard/

Key findings:

- OWASP ASVS provides a basis for testing web-application technical security controls and a list of requirements for secure development.
- It can serve as a metric, guidance for building controls, and a procurement/contract specification for security verification.
- Requirements have stable versioned identifiers and are available in machine-readable formats such as CSV and JSON.
- Transferable insight: security requirements should be versioned, traceable, testable, and usable as acceptance/contract criteria rather than kept as unstructured security prose.

## Assurance cases

Source: https://www.iso.org/standard/52926.html

Key findings:

- ISO/IEC 15026-2 defines an assurance case as a top-level claim, systematic argumentation, evidence, and explicit assumptions. The argument connects subordinate claims to evidence and assumptions.
- Assurance cases can support safety, reliability, maintainability, human factors, operability, and security claims.
- The standard focuses on structure and content consistency/comparability and does not require one terminology, graphical form, or physical implementation.
- Transferable insight: the kernel should upgrade the claim/evidence link into an assurance graph capable of representing arguments, assumptions, rebuttals, gaps, and reviewer confidence—not just a flat evidence list.

## OWASP Top 10 for Agentic Applications 2026

Source: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

Key finding: OWASP describes a globally peer-reviewed framework developed with more than 100 industry experts, researchers, and practitioners to identify critical risks in autonomous/agentic AI systems that plan, act, and make decisions across complex workflows.

Transferable insight: the virtual enterprise must treat agentic execution as a distinct security and governance problem, with explicit controls for planning, acting, decision authority, tool use, inter-agent trust, memory/project-state access, monitoring, and safe deployment. Ordinary web-application controls and ordinary LLM prompt controls are not sufficient on their own.

## CISA SBOM and software supply-chain transparency

Source: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom

Key findings:

- CISA describes SBOM as a nested inventory of software components and a key building block for software security and supply-chain risk management.
- SBOM supports transparency, vulnerability management, component sharing, and understanding of assembled products.
- VEX provides an attestation about whether a product is affected by a known vulnerability.
- CISA also provides AI SBOM guidance, indicating that AI systems and supply chains need component transparency.
- Transferable insight: the software pipeline and capability registry need component/model/tool inventories, provenance, license, version, vulnerability status, and applicability/exception records.

## NIST incident response

Source: https://csrc.nist.gov/pubs/sp/800/61/r3/final

Key findings:

- NIST SP 800-61 Rev. 3 (April 2025) integrates incident-response recommendations throughout cybersecurity risk management and aims to reduce incidents and improve detection, response, recovery, and efficiency.
- Transferable insight: incident response should be part of the full governance and lifecycle system, not an isolated operations document. Agentic incidents, supply-chain events, data breaches, and product failures should drive containment, recovery, lessons, control changes, and evidence updates.

## ISO/IEC 42001 AI management systems

Source: https://www.iso.org/standard/42001

Key findings:

- ISO/IEC 42001 specifies requirements for establishing, implementing, maintaining, and continually improving an AI Management System within organisations developing or using AI products/services.
- It addresses governance of AI risks and opportunities, transparency, traceability, reliability, ethical considerations, and continual improvement.
- It applies to organisations of any size and across industries.
- Transferable insight: AI governance needs an organisational management layer—policy, accountability, risk/opportunity process, continual improvement, and traceability—not only model evaluation or prompt controls.

## NIST Cybersecurity Framework 2.0

Source: https://www.nist.gov/cyberframework

Key findings:

- NIST CSF 2.0 helps organisations understand and improve cybersecurity risk management across industry, government, and organisations.
- The framework provides profiles, mappings, and quick-start guides to tailor cybersecurity outcomes to organisational goals and risk.
- Transferable insight: the virtual enterprise should maintain cybersecurity context, profiles, mappings, roles, and risk outcomes rather than treating security as isolated technical checks. Governance and organisational context are first-class controls.

## NIST AI RMF Playbook

Source: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook

Key findings:

- The Playbook gives suggested actions, references, and guidance for the four AI RMF functions: Govern, Map, Measure, and Manage.
- It is intended to incorporate trustworthiness considerations in the design, development, deployment, and use of AI systems.
- It is voluntary and designed to be tailored to industry, use case, and organisational needs; it is intended to evolve through review and feedback.
- Transferable insight: AI governance in the enterprise should be an operational loop rather than a static policy. Every AI-enabled capability should have governance, mapping, measurement, management, evidence, and improvement actions appropriate to risk.

## MITRE ATLAS

Source: https://atlas.mitre.org/

Key findings:

- MITRE ATLAS is a living knowledge base of adversary tactics and techniques against AI-enabled systems based on real-world attack observations and realistic demonstrations.
- The published interface represents tactics, techniques, mitigations, case studies, and filters for predictive, generative, agentic, and enterprise AI.
- Transferable insight: agent and AI red-team work should be threat-informed and scenario-based, using a living taxonomy rather than only generic prompt tests. The enterprise should map threats to assets, controls, tests, incidents, and residual risk.

## NIST Zero Trust Architecture

Source: https://csrc.nist.gov/pubs/sp/800/207/final

Key findings:

- NIST Zero Trust shifts protection from static network perimeters to users, assets, and resources.
- It assumes no implicit trust based solely on network location or ownership; authentication and authorization are discrete functions before resource access.
- Transferable insight: the virtual enterprise must authorize each worker, tool, project resource, artefact, and side effect explicitly. Local versus remote location cannot be treated as a trust boundary.

## OpenTelemetry

Source: https://opentelemetry.io/docs/what-is-opentelemetry/

Key findings:

- OpenTelemetry is a vendor/tool-agnostic observability framework and toolkit for generating, exporting, and collecting traces, metrics, and logs.
- It supports standard APIs, protocols, semantic conventions, SDKs, collectors, and instrumentation while leaving storage/visualization to other backends.
- Transferable insight: the operating kernel and workers need end-to-end trace context across work packages, agent calls, tool calls, artefacts, approvals, tests, deployments, and incidents. The kernel should not rely only on final text output to understand what occurred.

## NASA configuration management

Source: https://www.nasa.gov/reference/6-5-configuration-management/

Key findings:

- NASA describes configuration management as a lifecycle discipline that gives visibility into and controls changes to performance and functional/physical characteristics.
- It protects product integrity by controlling baselines and tracking changes; it connects technical planning, requirements, interfaces, risk, technical data, assessments, and decision analysis.
- NASA describes configuration planning/management, configuration identification, configuration change management, status accounting, and configuration verification as core elements.
- Transferable insight: the universal enterprise needs explicit baselines and configuration items for project state, requirements, architecture, capability ontology, evidence, code, models, worker policies, and deployed configurations. Current state alone is insufficient.

## ISO/IEC/IEEE 42010 architecture description

Source: https://www.iso.org/standard/50508.html

Key findings:

- The 2011 edition is withdrawn and replaced by ISO/IEC/IEEE 42010:2022; the archived page still identifies the architecture-description concepts.
- The standard addresses creation, analysis, and sustainment of architecture descriptions, including architecture viewpoints, frameworks, and description languages.
- Transferable insight: the virtual enterprise should not have one universal architecture diagram. It needs architecture views tailored to stakeholder concerns: capability, project workflow, information/evidence, security/trust, execution, deployment, governance, and assurance. The 2022 version should be used for current standard work.

## NIST Privacy Framework

Source: https://www.nist.gov/privacy-framework

Key findings:

- NIST Privacy Framework is a voluntary tool developed with stakeholders to help organisations identify and manage privacy risk through enterprise risk management while building innovative products/services.
- Transferable insight: privacy is not only a security property or legal checklist. The enterprise needs privacy risk ownership, data-flow context, purpose/necessity, individual impact, controls, evidence, and ongoing review.

## European Commission AI Act overview

Source: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

Key findings:

- The EU AI Act uses a risk-based approach and differentiates prohibited, high-risk, transparency, and minimal/no-risk contexts.
- High-risk obligations include risk assessment and mitigation, data quality, activity logging, documentation, deployer information, human oversight, robustness, cybersecurity, and accuracy; post-market monitoring and incident/malfunction reporting are also part of the lifecycle.
- The page is jurisdiction- and date-sensitive; requirements vary by role, use case, deployment, and current implementation guidance.
- Transferable insight: compliance architecture must classify jurisdiction, actor role, use context, risk category, lifecycle date, and obligation owner. The enterprise must not produce generic claims such as “AI compliant” without a current legal mapping and qualified review.

## National Academies reproducibility and replicability

Source: https://www.nationalacademies.org/projects/DBASSE-BBCSS-17-03

Key findings:

- The National Academies distinguishes the need to repeat research and independently confirm computations or results, and examines methodology, experimental design, incentives, roles, responsibilities, manipulation, and difficult-to-replicate phenomena.
- Transferable insight: evidence quality depends on method, design, incentives, independent confirmation, and context—not only a source label. The enterprise should preserve experiment conditions, data/code/configuration, independent reproduction, and limits.

## NIST measurement uncertainty

Source: https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty

Key findings:

- Measurement produces a value attributable to a defined measurand and normally relates to a standard/calibration process.
- Measurement uncertainty characterizes dispersion of values reasonably attributable to a measurand and expresses incomplete knowledge based on available information.
- Transferable insight: claims and tests need defined measurand/target, reference, method, calibration, uncertainty, coverage/conditions, and decision threshold where quantitative results matter. A measurement result without uncertainty and context is not a complete evidence object.

## Team Topologies

Source: https://teamtopologies.com/key-concepts

Key findings:

- Team Topologies warns that teams have cognitive limits and that adding tools, responsibilities, or domains can make competent teams ineffective.
- It distinguishes stream-aligned, enabling, complicated-subsystem, and platform team patterns and describes interaction modes such as collaboration, X-as-a-service, and facilitation.
- It cautions that the approach is not merely an organisation-chart exercise and should be applied to real work flow and value creation.
- Transferable insight: the virtual enterprise should optimise cognitive load and flow, not maximize specialist count. Specialist branches should have clear service boundaries, temporary enabling relationships, platform services, and an explicit interaction mode.

## GitLab Product Development Flow

Source: https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/

Key findings:

- GitLab publicly documents product-development roles, cross-functional flow, handoffs, and continuity practices for a distributed organisation.
- Transferable insight: the virtual enterprise needs explicit ownership and continuity semantics, not only task delegation. A handoff must identify who owns the next state, what is transferred, what remains with the originating team, and how work returns when blocked.

## FinOps Framework

Source: https://www.finops.org/framework/

Key findings:

- FinOps provides an operating model for managing cloud and technology cost with visibility, accountability, allocation, forecasting, and optimization.
- Transferable insight: the virtual enterprise needs cost ownership and resource visibility at mission, project, capability, worker, model, tool, and environment levels. Cost should be considered alongside value, risk, performance, and quality rather than treated as a finance-only afterthought.

## DORA software delivery performance

Source: https://dora.dev/guides/dora-metrics/

Key findings:

- DORA separates software delivery throughput from instability and measures change lead time, deployment frequency, failed-deployment recovery time, change-fail rate, and deployment rework rate.
- DORA warns against making metrics goals, using one metric, comparing unlike applications, siloed ownership, competition, and measurement that displaces improvement.
- Transferable insight: virtual-enterprise metrics should be contextual, balanced, team/system-oriented, and used for learning rather than ranking. Throughput must be paired with stability, recovery, outcome, cost, quality, and risk.

## NIST Human-Centered Design

Source: https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design

Key findings:

- NIST’s page describes human-centred design as based on explicit understanding of users, tasks, and environments; involving users throughout; iterative evaluation; whole user experience; and multidisciplinary perspectives.
- It identifies activities of understanding context of use, specifying user requirements, producing design solutions, and evaluating designs.
- The page warns that some content may be out of date, so current ISO 9241-210 should be consulted for formal standard work.
- Transferable insight: product value and human factors need a recurring evidence loop, but detailed UI/UX can remain a specialist subsystem/view rather than bloating the master technical document.

## NASA Human Systems Integration

Search lead: NASA Human Systems Integration Division and NASA Human Systems Integration Handbook. The previously attempted news URL returned 404 and is not treated as evidence.

Transferable insight from the search lead: complex-system human integration should include human performance, operations, safety, training, maintainability, and supportability—not only interface design. This should be handled through a domain-specific human-systems view and reviewed when operating context changes.

## OpenTelemetry

Source: https://opentelemetry.io/docs/what-is-opentelemetry/

Key findings:

- OpenTelemetry is an observability framework/toolkit for generating, exporting, and collecting telemetry such as traces, metrics, and logs; it is not itself a backend.
- It is vendor/tool agnostic and uses semantic conventions, APIs, SDKs, collectors, and context propagation to instrument systems.
- Transferable insight: the kernel needs standard execution context and semantic events across workers, tools, decisions, artefacts, approvals, and deployments. Observability storage/visualisation, retention, redaction, and access are separate design decisions.

## NIST SP 800-61 Rev. 3

Source: https://csrc.nist.gov/pubs/sp/800/61/r3/final

Key findings:

- NIST SP 800-61 Rev. 3 provides incident-response recommendations and considerations integrated with the CSF 2.0 cybersecurity risk-management context.
- Transferable insight: incident response should be integrated with preparation, detection, response, recovery, and broader risk management, not treated as a document opened only after a breach.
