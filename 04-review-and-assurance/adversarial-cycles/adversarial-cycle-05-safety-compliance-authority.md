# Adversarial Cycle 05 — Safety, Compliance, Law, and External Authority

## Review question

Can the universal enterprise responsibly handle safety, privacy, law, regulation, certification, and external authority across arbitrary domains, or does it risk producing generic compliance language and unsafe confidence?

## Reviewer lenses

### Regulatory counsel

The current compliance model is too generic for a global system. Legal obligations vary by jurisdiction, actor role, product classification, data, sector, deployment, contract, date, and activity. The same system may be a different legal object in different contexts. A framework can prepare analysis and evidence but cannot make a legal conclusion without qualified authority.

**Revision:** Make compliance classification an explicit intake and reclassification process. Track jurisdiction, actor/provider/deployer role, use context, sector, data, risk category, effective dates, guidance version, obligation, owner, evidence, exceptions, and legal reviewer.

### Safety engineer

A risk register and assurance case do not by themselves make a system safe. Safety requires hazard identification, causal scenarios, safeguards, independence, verification, monitoring, emergency behaviour, human responsibilities, and an authority willing to accept residual risk. A purely digital risk model may fail to represent physical or socio-technical harm.

**Revision:** Add a safety-case profile with hazard log, causal chain, severity, exposure, controllability, safeguards, independence, verification, operational constraints, emergency response, residual risk, and external sign-off requirements.

### Privacy engineer

Privacy is not merely confidentiality. A system can be secure and still cause unacceptable privacy risk through purpose, collection, inference, retention, linkage, visibility, or harmful use. NIST frames privacy as enterprise risk management for innovative products and services while protecting individuals [1].

**Revision:** Add privacy threat and impact assessment, purpose/use limitation, data-flow and retention mapping, individual impact, rights/consent basis where applicable, minimisation, deletion, access, redress, and privacy review triggers.

### AI regulator

The EU AI Act illustrates why generic AI compliance is invalid: obligations are risk-based and depend on the use context and role. High-risk contexts can require risk management, data quality, logging, documentation, human oversight, robustness, cybersecurity, accuracy, post-market monitoring, and incident reporting [2].

**Revision:** Add an AI regulatory classification object with jurisdiction, actor role, use case, risk tier, prohibited-use check, obligation matrix, effective date, guidance, evidence, and legal review status.

### Mission authority

The enterprise may identify a legally or ethically prohibited path that appears technically valuable. User preference or project ambition cannot override law, safety, rights, or external authority.

**Revision:** Add hard-stop conditions. The system can explain, propose lawful alternatives, or request authorised review, but it must not continue execution under a prohibited or unauthorised condition.

### Field/operator reviewer

Safety and compliance are often lost during deployment because the operating environment, training, maintenance, human workload, or incident process differs from the design assumptions.

**Revision:** Treat operating constraints, training, support, maintenance, monitoring, reporting, and field changes as part of the safety/compliance baseline. Reassess when deployment context changes.

## Falsifications

### Falsification 1 — A compliance matrix means compliant

A matrix shows claimed mapping, not legal validity. It can be stale, incomplete, jurisdictionally wrong, or based on a misclassification.

### Falsification 2 — A safety score means safe

A numerical score can hide unknown hazards, dependencies, human factors, or unacceptable catastrophic scenarios. Safety needs a structured argument and appropriate external authority.

### Falsification 3 — The universal enterprise can cover all law

The system can discover likely obligations and organise review. It cannot replace counsel, regulators, certification bodies, clinical authorities, or responsible officials.

### Falsification 4 — Security is privacy

Security controls protect assets and systems; privacy also concerns purpose, use, inference, visibility, retention, and individual impact.

### Falsification 5 — One regulatory status is permanent

Classification, guidance, jurisdiction, model, data, deployment, and role changes can change obligations. Compliance status must have freshness and re-evaluation triggers.

### Falsification 6 — External approval is only a final signature

External authority may shape problem definition, requirements, test design, evidence, and operating controls throughout the lifecycle. A final signature cannot rescue a design that was never reviewable under the authority’s process.

## Accepted safety/compliance revisions

1. Add jurisdiction/actor/use-context classification before detailed design.
2. Add hard-stop and escalation rules for prohibited, unsafe, or unauthorised paths.
3. Add safety-case and privacy-impact profiles distinct from generic risk registers.
4. Add obligation freshness, guidance version, owner, reviewer, evidence, and exception status.
5. Add deployment, training, maintenance, human-factors, field-change, post-market, and incident obligations.
6. Add domain-specific authority adapters for clinical, aerospace, robotics, financial, infrastructure, and other high-consequence contexts.
7. Allow lawful/safer alternative generation when the requested path is prohibited or cannot be responsibly justified.
8. Separate “prepared for review,” “reviewed,” “approved,” “certified,” and “in operation under monitored conditions.”

## Cycle 5 judgement

The baseline was too optimistic about generic compliance and treated safety as a cross-cutting property without enough authority and jurisdiction structure. The corrected model makes safety, privacy, and law **classification- and authority-dependent control systems**. It can organise deep preparation, but it cannot self-certify or override external authority.

## References

[1] [NIST Privacy Framework](https://www.nist.gov/privacy-framework)  
[2] [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)  
[3] [ISO 31000 Risk Management](https://www.iso.org/standard/65694.html)
