# Adversarial Cycle 09 — Product Value, Human Factors, and Operational Reality

## Review question

Can the virtual enterprise produce systems that people can actually use, adopt, operate, support, and benefit from, or does technical depth obscure poor product value and socio-technical failure?

## Reviewer lenses

### Human-centred designer

A technically correct system can still be unusable, unhelpful, inaccessible, or harmful. NIST’s human-centred design summary, based on ISO principles, emphasizes explicit understanding of users, tasks, and environments; user involvement; iterative evaluation; whole-user experience; and multidisciplinary perspectives [1].

**Revision:** Add a human-systems/product-value control loop: context of use, user/workflow requirements, design hypothesis, evaluation, observed friction, adoption risk, accessibility, training, and operational impact.

### Operations and adoption lead

The project may assume that a user will change behaviour merely because a technically superior option exists. Real adoption is shaped by incentives, workload, trust, authority, training, support, interoperability, procurement, maintenance, and failure consequences.

**Revision:** Add adoption and change-readiness objects: affected roles, workflow delta, incentives, training, support, resistance, fallback, migration, and success evidence.

### Safety/human-factors reviewer

Automation can create over-reliance, deskilling, alert fatigue, mode confusion, responsibility gaps, and unsafe workarounds. A human approval button does not guarantee meaningful oversight.

**Revision:** Evaluate human authority, observability, comprehension, intervention time, workload, automation bias, error recovery, escalation, and whether the human can actually reject or correct the system.

### Product economist

The virtual enterprise may optimize technical output instead of user outcomes. An elegant system with no adoption, no willingness to pay, no operational owner, or no measurable improvement is not a successful product.

**Revision:** Require outcome hypotheses, baseline, leading indicators, user evidence, value realization, cost-to-serve, and stop criteria. Keep product/mission value distinct from feature completion.

### Accessibility reviewer

Accessibility is often inserted as a quality attribute but not tested in context. It can be a legal obligation, a safety issue, or a product-value requirement depending on the domain.

**Revision:** Add user-group and access-context coverage, accessibility requirements, evaluation evidence, assistive-technology or alternative-path tests where applicable, and owner/review triggers.

### UX-scope reviewer

The master architecture should not become an enormous UI/UX design document. Detailed interaction design belongs in a specialist product/UX subsystem, while the master system retains the decisions that affect mission value, safety, accessibility, workflow, and architecture.

**Revision:** Represent UX as a linked specialist view with traceable outcomes, requirements, evaluations, and decisions. Do not duplicate screen-level detail in the master document.

### Field reality reviewer

The system can be designed around ideal procedures while operators work around it. Workarounds are signals, not user failures. Field conditions, maintenance, support, and data entry burden can invalidate the intended ConOps.

**Revision:** Add operational observation, feedback, support tickets, incident learning, field-change review, and periodic revalidation of the ConOps.

## Falsifications

### Falsification 1 — User satisfaction proves value

Users may like a system that produces no meaningful outcome, or dislike a necessary safety control. Satisfaction is one signal, not the complete value case.

### Falsification 2 — A successful demo proves adoption

A demo can remove real-world constraints such as training, interruptions, data quality, integration, support, incentives, and accountability.

### Falsification 3 — Human-in-the-loop proves human control

A nominal human step may be too late, too opaque, too rushed, or too difficult to reject. Human authority must be tested in realistic context.

### Falsification 4 — UI quality is the whole human factor

Human systems integration includes roles, procedures, training, workload, maintainability, supportability, safety, and operations, not only screens.

### Falsification 5 — The master document needs every UX detail

Excessive UI detail can make the master architecture stale and obscure system-level decisions. Specialist views should remain linked, versioned, and traceable.

### Falsification 6 — Operators will use the intended workflow

If the system creates friction, users may bypass it, enter low-quality data, create unsafe workarounds, or use external tools. Intended and observed workflows must be compared.

## Accepted product/human-system revisions

1. Add human-centred context, workflow, evaluation, and outcome loops.
2. Add adoption, change-readiness, training, support, accessibility, and migration assessment.
3. Add meaningful-human-oversight tests for high-impact automation and AI.
4. Add baseline/outcome/value measures and cost-to-serve rather than feature-count measures.
5. Add operational observation and workaround feedback into product and systems decisions.
6. Keep detailed UI/UX in a specialist linked view while retaining system-level human and workflow requirements in the master model.
7. Add user and operator representation to relevant reviews, without treating a user panel as a substitute for safety or legal authority.

## Cycle 9 judgement

The virtual enterprise is strong at technical and epistemic depth but could still optimize the system from the inside out. The corrected design treats the product as a **socio-technical intervention**: value, usability, safety, adoption, operation, maintenance, and human authority must be evidenced alongside technical performance.

## References

[1] [NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design)  
[2] [ISO 9241-210 Human-centred design](https://www.iso.org/standard/77520.html)
