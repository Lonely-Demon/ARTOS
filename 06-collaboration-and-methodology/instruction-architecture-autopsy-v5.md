# Engineering Autopsy: The Instruction Architecture — v5

## Changelog

### v5 (this version)
- **Section 10 marked satisfied, not left reading as an open requirement.** The category-space artifact this section required now exists as its own document — enumerated, provenance-audited via content-independence, sensitivity-mapped for all six Conditional-tier items — and has already been through two rounds of review and correction. The artifact itself states that it satisfies this section; this section previously didn't state the reverse. It does now.

### v4
Provenance audit collapsed from two tests into one: content-independence, checked by inspection, replacing a version that partly leaned on an unverifiable temporal-priority claim. The pilot's gating criteria gained an opportunistic check against the sensitivity map's predictions, using data the pilot was already producing. Section 9 updated to reflect this partial, non-comprehensive mitigation.

### v3
Consolidation gained an explicit sub-task translating harmonized process-position findings into updated or confirmed-unchanged trigger language for phase-sensitive policies. The provenance test was split into two explicit criteria, naming the cognitive-science vocabulary that passes the second. The sensitivity-map requirement was added to section 10, to be committed before the pilot runs rather than judged at consolidation after results are visible.

### v2
Corrected an untagged introspective prediction about phase-awareness (given a structural field instead); a category-space example that leaked a discovered finding's structure (corrected via a provenance rule and a phrasing rule); and a consolidation stage blind to the difference between genuine disagreement and a structural artifact of the blind pass's own design (fixed with mode decomposition and a three-way non-convergence taxonomy). Relabeled the keystone claim: blind extraction is inter-rater reliability plus coverage extension on the file-behavior mode, not a second independent evidentiary mode.

### v1
Original architecture: the epistemological frame, audience analysis, the contamination boundary, the authority structure and freedom map, information architecture, snapshot engineering, failure-mode countermeasures, stage structure with pilot, exclusions, and residual risks.

---

## What this document is, and the rule it's written under

This is the complete design rationale for the instruction that will eventually run the extraction — every structural decision, every ordering choice, every countermeasure, and the reasoning behind each. It is deliberately not the instruction itself. It is the layer beneath it: the engineering that determines what the instruction must be before a word of it gets drafted.

It's written under one governing constraint. The request is to design an instruction *for myself* — and this project's founding evidentiary rule is that a system's introspective account of its own processes is the least reliable evidence about how it actually behaves. That rule was established for humans, and there is no principled reason to exempt me from it. I have a self-model; it generates real hypotheses about what would work on me; but those hypotheses earn load-bearing status only where they converge with externally documented behavior. Where only my introspection supports a design choice, that choice is tagged as a hypothesis and, wherever possible, routed to empirical testing rather than trusted.

Each successive review has caught a different failure of this rule. v2 caught unhedged self-prediction and a leaked finding. v3 caught a capture mechanism with nowhere to discharge to, and a judgment relocated to precisely the moment it was least trustworthy. v4 caught a criterion resting on an unverifiable historical claim, and free empirical value the architecture wasn't asking for. This version closes the loop the others opened: the requirement they were all converging on now has a satisfied artifact behind it, and this document should say so.

---

## 1. Audience analysis: who actually reads this instruction

**The reader is not me-in-this-conversation.** It is a fresh instance with zero context. Words like *counterweight*, *flow*, *steer-don't-seize* are, to a fresh reader, either undefined jargon or terms it will interpret through general training rather than through what they came to mean here. Every such term must either be defined operationally inline or replaced with plain behavioral language.

**The reader is a capable planner, and that capability cuts both ways.** Performs best given goals, constraints, and rationale; performs worse when handed dense procedural checklists it will follow faithfully even where they're wrong. The instruction's register is specification-with-rationale, not procedure. But the same capability that makes it plan well makes it prone to helpful renovation — resolved structurally in section 3.

**The reader has documented behavioral leans that are engineering inputs, not trivia.** Reluctance to output "I don't know," with a tendency to fill genuine gaps with fabricated detail; verbosity past what a task needs; an internal safety mechanism that can silently degrade output when instructions ask it to "show" or "explain" its own reasoning; over-correction in response to emphatic instruction styles. Each gets a specific countermeasure in section 6.

**The reader is plural.** Five or more independent fresh instances across the sequential batches, plus a consolidating instance, plus possibly a verifying instance — the protocol of a small distributed system whose nodes never communicate directly and share no memory. Consistency comes from exactly two things: the protocol document being byte-identical at every node, and the state object passed between nodes being complete enough that no node ever needs what a previous node knew but didn't write down.

---

## 2. The keystone decision: methodology travels, findings don't

The naive architecture hands the extraction model everything — the full spec including all current findings — and asks it to verify and extend those findings against the source files. This is efficient, continuous, and wrong: models told what to expect in a person's material reliably find it, converting extraction into an echo.

**What convergence actually proves.** The blind pass and the conversation-derived model's file leg both assess the *same* mode — file behavior — so their agreement is not a second evidentiary mode. It is inter-rater reliability on the file-behavior mode, plus coverage extension where the blind pass reads files or regions the original sampling never touched. Convergence remains the strongest check this benchmark-less project can manufacture; the contamination boundary remains fully load-bearing.

**The boundary, drawn with a single test, checked by inspection.** What travels with every batch: the methodology — goals in generic form, the behavioral policies, the tagging taxonomy, the update and contradiction policies, the output schema, and the category space. What is withheld until consolidation: every current finding about this specific person.

The category space that travels must pass one test: **content-independence**, checked the same way the phrasing rule is already checked — by inspection, not by appeal to history. Does the category, as phrased, avoid encoding any specific, discovered fact or pattern about this particular person? A category fails if reading it reveals, even implicitly, something already found about this person specifically. It passes if it names a dimension any person's material could in principle be checked against, regardless of what that check turns out to show.

This is the load-bearing test, and it replaces a two-part version that leaned partly on temporal priority — whether something was authored before any file was opened. Temporal priority is not, by itself, independently verifiable by inspecting the artifact: it requires trusting a historical record external to the category text itself. Content-independence requires no such trust; it's confirmable directly, the same way the phrasing rule already gets confirmed.

Applied this way, both the original interview-derived dimensions (problem framing, decomposition, evidence threshold, decision style, stopping behavior, verification habits, communication patterns, phase-noting) and vocabulary drawn from the cognitive-science research passes (decision caution and evidence-extraction efficiency; metacognitive calibration; search-persistence and patch-leaving thresholds; planning-versus-habit tendency) pass cleanly. None of them, as phrased, encodes anything specific to this person; each names a dimension, not a discovered polarity.

Where temporal priority also happens to hold — and in this project, the research passes did run before any of the nine files were opened — that's worth noting as corroborating evidence. It is not required, and this audit does not claim to have verified it beyond what the project's own conversational record shows; an audit conducted without access to that record should rely on content-independence alone and treat any temporal claim here as uncorroborated by inspection.

**Phrasing rule, unchanged.** Categories name dimensions, never discovered polarities or structures.

**The tradeoff, named and allocated.** Categories generic enough to guarantee leak-free independence are also generic enough to plausibly miss clean recurrences of subtle, unconfirmed items. Independence wins. The consequence is handled precisely via the sensitivity map (sections 7, 10), not just asserted.

**The interview stays out of the blind passes**, kept as a separate evidentiary mode the blind pass never touches — the actual load-bearing independence claim in this architecture.

---

## 3. Authority structure: fixed spec, engaged intelligence, and the freedom map

**Full freedom:** execution strategy within a batch — reading order, internal planning, attention allocation.

**Zero freedom:** the taxonomy, the tags, the schema, the policies, the thresholds, the promotion and contradiction rules. Consistency across instances is itself a correctness requirement; a distributed system's protocol is not improvable by one node unilaterally.

**The pressure valve:** an operator-notes channel where any instance records disagreement with the spec or observations the taxonomy has no place for. Flag, never fix.

**Precedence, stated rather than implied:** care-override above everything, unconditionally. Epistemic rules above output-shape rules. Output-shape rules above stylistic preference. Conflicts resolve by this ladder, never by which instruction appeared last.

---

## 4. Information architecture: ordering, structure, and where redundancy lives

**Order:** role and purpose framing first, brief. Then the methodology. Then the incoming state snapshot. Then the source file content, placed before the task query per the first-party finding on longform material. Instructions and the restated output schema at the very end.

**Phase, structural rather than hoped-for.** Traces directly to the person's answer that intervention belongs at a specific phase, before building begins. Carried structurally: a process-position field in the schema (section 5) and phase-noting as a generic, content-independent category (section 2).

**Structural redundancy, not emphatic redundancy:** the most at-risk disciplines appear both in the opening framing and the closing schema section, plainly worded, never in emphatic style.

**Worked examples, chosen adversarially:** one complete finding entry with every schema field populated; one exemplary insufficient-evidence entry, shown as a full, respectable output; one example of contradiction handling done correctly — branching on a moderating condition rather than averaging.

**XML throughout,** confirmed as the first-party-recommended structuring convention for this model generation.

---

## 5. State-handoff engineering: the snapshot as the system's only memory

**The schema, field-complete.** An identifier; the behavior in plain language; evidence entries, each a verbatim quote with source-file locator and chronological position; the process position — where within the person's reasoning arc the behavior occurs, in observable anchors, with "not phase-linked" and "insufficient evidence to place" as first-class values; the evidence tag; the temporal tag; current confidence; the falsifiability note; a candidate operational implication or explicit "none yet"; and the contradiction log. At snapshot level: open questions, the operator-notes channel, and the tombstone list.

**Two position fields, two different axes.** Chronological position is calendar-time, serving the contradiction policy's evolution-versus-context distinction. Process position is arc-time, serving the model's eventual use for timing an intervention correctly.

**Phase language is elicited, not imposed** — free text anchored to observable markers, per the elicit-before-labeling policy. Harmonizing five vocabularies into one, and translating the result into policy language, are the consolidator's job (section 7).

**Quotes are the evidence payload itself.** Quote fidelity at capture time is load-bearing; verification must be front-loaded, while the file is still in context; consolidation can audit only internal consistency, never source fidelity.

**Growth is bounded by policy.** A small cap of the strongest verbatim instances, plus a running count of additional sightings with locators only.

**Hygiene:** update rather than duplicate; delete-if-wrong, with a tombstone note.

**Chronology survives batching** via the locator on every evidence entry, regardless of ingestion order.

---

## 6. Countermeasures: each documented lean, met with a specific mechanism

**Gap-filling and the reluctance to say "insufficient evidence."** Countered four ways: the valued-output framing at both load-bearing positions; the worked insufficient-evidence example; a standing prohibition on claims true of most people; the falsifiability requirement.

**The reasoning-transparency safety mechanism.** All deliverables framed everywhere as work products, never as the executor's reasoning made visible. The final instruction gets a dedicated trigger-phrase audit; the pilot watches for the degradation signature.

**Verbosity, scoped rather than suppressed.** Brevity and expansiveness instructions attach to specific named outputs, never to the task globally.

**Emphasis over-correction.** Calm wording, positional redundancy, no shouting.

**Self-report inside the files.** In-file self-description is tagged as a distinct, lesser evidentiary class than contemporaneous behavior; divergence between the two is itself recorded as a finding.

**The crisis content.** Every batch instance is pre-positioned via the traveling methodology; the care-override sits at the top of the precedence ladder, unconditionally, in every instance.

---

## 7. Stage structure: pilot, batches, consolidation, verification

**The pilot** runs one small batch first, gated on: verbatim quote spot-checks; demonstrated capacity for insufficient-evidence marking; complete schema adherence including process position; the snapshot arriving as final answer text; no degradation or fallback signature; and, wherever the pilot batch's content bears on a claim in the sensitivity map (section 10), an explicit check of whether that prediction held — did the category catch the item where the map predicted it would, or correctly register absence where it predicted it wouldn't. This last check is opportunistic rather than comprehensive: it tests only whatever the pilot batch happens to touch, and says nothing about map claims the pilot batch doesn't bear on. But it uses data the pilot is already producing, at no additional cost, and any mismatch is grounds to revise the sensitivity map before the full batch sequence relies on it. Fail any gating criterion, revise and re-pilot.

**The batch sequence** runs the identical protocol document at every node with only the snapshot varying. The operator's role between batches is thin: carry the snapshot forward, spot-check when inclined, hold the stopping judgment.

**Consolidation is where the two worlds meet.** Its inputs: the final blind-derived snapshot, and the conversation-derived model with its interview-based self-report evidence.

- **Mode decomposition and the non-convergence taxonomy:** the blind output reconciles only against file-behavior components; self-report components are outside its jurisdiction. Non-convergence splits three ways — opposition (invokes the contradiction policy in full), absence, and mode-explained confidence differentials (neither triggers anything). Absence is graded against the sensitivity map: meaningful negative evidence only where a category was mapped, in advance, as equipped to catch that item; uninformative otherwise, as a lookup, not a judgment made in the moment.
- **Phase translation:** harmonizing the five instances' process-position vocabulary into one coherent account is only half the job. For every policy whose trigger language references phase — currently P3 alone, "before the build phase" — the harmonized findings must be explicitly checked against that language, and either confirm it unchanged or produce updated trigger language, as a stated output of consolidation. A trigger point the existing policy doesn't encode is itself a finding, logged and carried forward.

Convergences are recorded as inter-rater agreement plus coverage extension, per section 2. This stage remains the architecture's least-tested component.

**An optional final pass:** a separate fresh-context instance audits adversarially — Barnum test, falsifiability audit, internal-consistency sweep, register check per artifact.

**The deliverable pair:** the comprehensive report carries breadth; the operational extract carries the highest-confidence findings and the behavioral policies in structured fields, no model named anywhere in it.

---

## 8. What the instruction deliberately excludes, and why each exclusion is a choice

**The research corpus.** Its distilled products travel as rules and as content-independent category-space vocabulary; its full content would invite theory-first labeling and bury operative instructions in reference material.

**The spec's version history.** Legislative history, not current law.

**This conversation.** Its identity, its accumulated shorthand — none of it travels.

**The findings, until consolidation.** The keystone exclusion.

**The interview, from the blind passes.** Kept as an untouched second mode.

---

## 9. What the engineering cannot close: residual risk, stated plainly

**Quote fidelity is single-pointed.** Reduced by front-loaded verification and the pilot gate; not eliminated.

**The safety-mechanism risk is probabilistic.** Lexical auditing lowers the trigger likelihood; the pilot detects a trip; nothing prevents one with certainty.

**The independence claim is bounded by a deliberate allocation.** Category-space content-independence protects against finding-leakage at the cost of sensitivity to subtle, unconfirmed items — a real limit, made precise via the sensitivity map.

**The sensitivity map is a prediction, partially and opportunistically checked, not proven.** Committing it before the pilot runs removes the motivated-reasoning risk of judging category-fit after seeing results, and the pilot now checks it against whatever the pilot batch happens to touch (section 7) — a real, low-cost empirical signal that didn't exist before. But this coverage is incidental to what the pilot batch contains, not designed to test the map comprehensively. Most sensitivity-map claims will still go untested until the full batch sequence runs, and some may never be tested at all if the relevant items never surface in any batch.

**The trigger-language translation sub-task is new and untested.** Its value depends entirely on the consolidator producing a substantive update or a genuinely-checked confirmation, not a perfunctory pass.

**Phase harmonization across five vocabularies is untested**, as is everything downstream of it.

**The reconciliation stage has no precedent**, narrowed by mode decomposition and the non-convergence taxonomy, not eliminated as a novel piece of machinery.

**Snapshot growth is bounded by policy, not proof.** The pilot and first real batch produce the actual numbers.

**The empirical ceiling passes through untouched.** Every finding the system produces is a qualitative, revisable hypothesis, and the deliverables must say so about themselves.

**The consumer-interface context window is unconfirmed**, per the spec's own 2G caveat. This engineering document's batch-sizing assumptions inherit that uncertainty; if the actual window on whichever surface this runs on differs materially from 1M tokens, the batching plan needs re-deriving, not just re-checking.

---

## 10. Pre-drafting requirement — satisfied

The category-space artifact was required to produce three things, in this order, before the instruction is drafted:

1. **Enumeration** — every category that will travel with the batches, listed explicitly, with no vocabulary left implicit under a phrase like "and the rest."
2. **Provenance audit via content-independence, checked by inspection** — each enumerated category read and confirmed to avoid encoding any discovered, person-specific fact. Temporal priority, where it can actually be substantiated, is noted alongside as corroborating; it is never the basis on which a category passes or fails.
3. **Sensitivity mapping** — for the categories that survive the audit, an explicit table of which known Conditional-tier items each one is and isn't positioned to catch, committed before the pilot runs.

**This requirement is now satisfied.** The category-space artifact exists as its own document, has produced all three outputs in the required order, and has already been through two rounds of review and correction — a de-leaked category, a corrected interaction-hypothesis cross-reference, and a fourth flagged candidate added to its own open-decisions list. Its Section 4 is the traveling category list; nothing else in that artifact should reach a blind instance, per its own stated warning.

Four reviews have now each caught this document breaking its own stated rule, or leaving value unclaimed that the rule's own machinery already generates. v2 caught unhedged introspection and a leaked finding. v3 caught a capture mechanism with nowhere to discharge to, and a judgment made at the least trustworthy possible moment. v4 caught a criterion resting on a claim the artifact couldn't independently confirm, and a cheap empirical check the architecture was already positioned to run but wasn't asking for. This version closes something quieter than a catch: a requirement that had already been met, sitting in a document that hadn't yet said so. Not every revision here has been a correction of an error — some have been keeping the document's own account of itself current with what actually exists elsewhere. That upkeep is not a one-time step either. It has to be re-run every time a dependency changes, the same way the extraction it describes has to keep checking its own evidence rather than trusting its own conclusions.
