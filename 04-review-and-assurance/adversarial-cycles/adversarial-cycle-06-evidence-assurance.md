# Adversarial Cycle 06 — Evidence, Epistemology, and Assurance

## Review question

Does the enterprise’s evidence and assurance model distinguish reliable support from merely plausible, authoritative-looking, repeated, or internally consistent reasoning?

## Reviewer lenses

### Scientific methodologist

The current evidence states are useful but too coarse. “Verified primary evidence” does not automatically mean true or relevant. A primary source may be biased, outdated, underpowered, misinterpreted, or outside the project context. A secondary source may be more rigorous or may merely repeat an error. Evidence status needs quality, relevance, context, and limitations.

**Revision:** Add claim type, evidence role, method quality, relevance, context match, freshness, independence, replication status, uncertainty, and known limitations to evidence objects.

### Measurement scientist

A result is not complete without a defined measurand/target, reference, method, calibration, uncertainty, conditions, and decision threshold where quantitative claims matter. NIST describes measurement uncertainty as representing incomplete knowledge about values reasonably attributable to a measurand [1].

**Revision:** Add an evidence profile for measurements and quantitative tests: target/measurand, instrument/model, calibration/reference, sample, conditions, uncertainty, coverage, analysis method, decision threshold, and validity boundary.

### Reproducibility reviewer

Reproducibility, replicability, repeatability, and independent confirmation are not interchangeable. Reproducing a computation with the same data and code differs from replicating a result under new data or conditions. The National Academies highlights methods, design, incentives, roles, responsibilities, and independent confirmation as factors in scientific reliability [2].

**Revision:** Track reproduction level separately: not attempted, same-input reproduction, independent code reproduction, new-sample replication, cross-condition replication, field validation, and external confirmation.

### Assurance-case reviewer

An assurance case can become advocacy disguised as structure. A neat claim-argument-evidence tree may omit inconvenient evidence, use circular reasoning, treat assumptions as facts, or allow the author to choose an overly narrow claim.

**Revision:** Every assurance case must include scope, decision consequence, defeaters/rebuttals, missing evidence, alternative explanation, independent reviewer, claim expiry/review trigger, and authority status. The output can be “insufficient assurance” or “claim not admissible.”

### Bayesian/uncertainty reviewer

The enterprise uses confidence language without calibration. A model’s confidence, a reviewer’s confidence, and an evidence strength are different quantities. Combining them informally can create false certainty.

**Revision:** Separate epistemic status from subjective confidence. Use quantitative probabilities only when their meaning, data, assumptions, and calibration are defensible. Otherwise use explicit uncertainty classes and decision thresholds.

### Research integrity reviewer

Parallel research does not automatically eliminate confirmation bias. Teams can share the same initial framing, search results, model priors, incentives, and missing sources. More reports can create an illusion of convergence.

**Revision:** Design disagreement: independent framing, controlled disclosure for selected analyses, source-diversity checks, red-team countersearch, negative-result capture, and comparison of assumptions before synthesis.

## Falsifications

### Falsification 1 — Source hierarchy equals evidence strength

Primary/secondary classification is useful for provenance but insufficient for validity. Relevance, method, bias, context, uncertainty, and replication matter.

### Falsification 2 — More citations improve truth

Citation count can increase authority appearance without improving support. Every citation needs a proposition-to-source mapping and a check that the source actually supports the claim.

### Falsification 3 — Repeated AI agreement is independent evidence

Multiple model outputs can be correlated through shared training, sources, prompts, or orchestration. Agreement should be treated as convergence under a shared information environment until independence is established.

### Falsification 4 — Assurance structure proves assurance

A structured assurance case can be wrong, incomplete, or strategically narrow. It is a reasoning object for review, not a certificate.

### Falsification 5 — Unknown is one state

A missing measurement, a failed measurement, an untested condition, an unapplicable factor, a contradicted claim, and an impossible-to-observe property have different implications.

### Falsification 6 — A successful test generalizes automatically

A test supports only its tested configuration, population, method, environment, and time unless external validity is justified.

## Accepted evidence revisions

1. Separate provenance, validity, relevance, uncertainty, and authority instead of one evidence state.
2. Add claim taxonomy: descriptive, causal, predictive, normative, legal/regulatory, safety, capability, performance, and outcome claims.
3. Add evidence roles: support, challenge, boundary, calibration, feasibility, verification, validation, replication, and external authority.
4. Add evidence profile fields for method, context, sample, configuration, uncertainty, calibration, analysis, limits, and decision threshold.
5. Track repeatability, reproducibility, replicability, cross-condition validation, and external confirmation separately.
6. Add negative evidence, failed tests, null results, contradictory sources, and non-observations as first-class objects.
7. Add source/claim support extraction and citation audit; a source cannot be promoted merely because it is prestigious.
8. Add assurance-case defeaters, alternative explanations, claim expiry, independent review, and inadmissible/insufficient states.
9. Add evidence conflict resolution with preserved dissent rather than forced consensus.
10. Propagate uncertainty into downstream requirements, decisions, claims, and risk.

## Cycle 6 judgement

The original evidence and assurance architecture was strong in traceability but too optimistic about labels and structure. The corrected model treats evidence as a **contextual, typed, uncertainty-bearing, contestable object** and assurance as a reviewable argument with possible failure. This makes the enterprise less rhetorically impressive but substantially more defensible.

## References

[1] [NIST Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty)  
[2] [National Academies — Reproducibility and Replicability in Science](https://www.nationalacademies.org/projects/DBASSE-BBCSS-17-03)  
[3] [ISO/IEC 15026-2 Assurance Case](https://www.iso.org/standard/52926.html)
