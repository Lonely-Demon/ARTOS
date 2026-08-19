<!--
CHANGELOG — v2
- Fixed a content-independence leak in category #13 (Verification Timing) that I introduced and missed in v1: the original wording named "time pressure" as the example condition, which leaks D15's actual discovered context rather than naming a genuinely neutral placeholder. Whoever built the deployed Extraction Protocol from this artifact already caught and fixed this independently, generalizing to "varies across different conditions or circumstances." This version brings the source artifact into alignment with that correction, so the fix lives here too, not only downstream.
- Added Problem Framing as a fourth flagged candidate in Section 5, audited to the same standard as the original three. It's already being referenced consistently in the Consolidation Protocol and the operator's guide as one of four candidates; this closes the gap where the source document backing that reference only actually contained three.
-->

# Category-Space Artifact: Enumeration, Content-Independence Audit, Sensitivity Map

## What this document is, and a warning about how it must be used

This satisfies the pre-drafting requirement stated in the Instruction Architecture Autopsy, Section 10: enumeration, provenance audit via content-independence, and sensitivity mapping, in that order, before any batch-instance instruction gets drafted.

**This document must never be shown to a blind batch instance.** It exists specifically to show its own work — every category here is traced back to the capture-spec item that motivated it, so the audit is actually inspectable rather than asserted. That traceability is exactly what a blind instance must not see; knowing that a category exists *because* D14 was already found would contaminate the read the category is meant to test. This is internal working material for the operator and the consolidator. What actually travels to a batch instance is **Section 4 only** — the stripped list, with every D-item reference removed.

---

## 1. Enumeration and content-independence audit

Method: for each capture-spec item currently used to justify a policy or goal, write the neutral dimension a blind reader could be pointed at without knowing what was already found, then check the phrasing against the standing rule — *does it avoid encoding any specific, discovered fact about this person, even implicitly* — and note any correction made getting there.

| Source | Finding language (does not travel) | Category language (travels) | Audit |
|---|---|---|---|
| D1 | Revises beliefs at a rate that may depend on how volatile a domain is assumed to be | **Belief-revision rate.** When new information appears, how much a stated plan, estimate, or conclusion shifts in response, and whether this varies across different kinds of domains or situations. | PASS. No rate, direction, or domain comparison asserted. |
| D3 | Confidence doesn't always track accuracy, and the gap may vary by domain | **Confidence calibration.** How stated or implied confidence in a claim relates to how well-supported that claim turns out to be, and whether the relationship differs across domains or conditions. | PASS. No gap, direction, or specific domain (deadline pressure) named. |
| D4 | A small number of decisions get made fast and locked early; everything else stays negotiable | **Decision-commitment patterns.** When, how, and on what evidence a choice gets committed to. | PASS, with history. This is the exact category that leaked in an earlier version of the autopsy via a "versus leaves everything else open" clause, which encoded the discovered bimodal structure. That clause is dropped here; this wording is the one already ruled clean. |
| D5 | Sometimes runs a practiced approach, sometimes builds a fresh plan; the choice isn't always matched to the situation | **Planning-versus-habit tendency.** When a familiar type of problem recurs, whether a previously-used approach gets reapplied or a fresh plan gets built for the specific situation. | PASS. Dropped the evaluative "isn't always matched" clause — that's a judgment on the finding, not a neutral dimension. |
| D6 | Losses, gains, and low-probability risks may not be weighted at face value | **Risk and tradeoff framing.** How potential losses, gains, and low-probability outcomes are weighted relative to each other when options are compared. | PASS. No skew or direction asserted. |
| D7 | Recognizes "good enough, and more," and stops rather than over-refining | **Sufficiency recognition.** What, if anything, signals that a deliverable or decision has reached an adequate point, and what happens once that point is reached. | PASS. Doesn't assume such a signal exists or that stopping actually occurs. |
| D8 | Has an internal stopping signal for research/exploration, not externally specified | **Search-persistence and stopping threshold.** How much exploration or information-gathering precedes moving to a next step, and what, if anything, signals that it has run its course. | PASS. Doesn't assert the signal is internal. |
| D9 | Attention during free exploration may gravitate to a specific kind of information gap | **Curiosity direction.** During open-ended or undirected exploration, what kind of gap or unresolved question draws attention. | PASS. No specific gap-type asserted. |
| D11 | Breaks a large problem into parts in a fairly consistent shape | **Problem decomposition.** How a large or ambiguous problem gets broken into smaller parts, and whether any structure recurs across different problems. | PASS. Doesn't assert consistency or name a shape. |
| D12 | Before proposing an approach, works through why the obvious versions don't hold up | **Feasibility-testing sequence.** Whether, and at what point relative to proposing or endorsing an approach, that approach gets tested against likely failure modes. | PASS. Doesn't assert the testing happens *before* proposal — that ordering is the discovered finding; the category asks the relative-timing question generically. |
| D13 | Builds a reference/documentation base before designing anything | **Upstream mapping.** Whether and how a reference base, prior-art survey, or constraint map gets assembled relative to when solution design begins. | PASS. Doesn't assert this happens by default. |
| D14 | Regularly, unprompted, asks whether something important has been overlooked | **Gap-checking behavior.** Whether, how, and under what circumstances a check for overlooked considerations occurs without being prompted for it. | PASS. Doesn't assert regularity or frequency — those are the discovered strength of this specific finding. |
| D15 | States or treats something as working before it's confirmed, specifically under time pressure | **Verification timing.** The relationship between treating or presenting something as complete or functioning and actually confirming that it is, including whether this relationship varies across different conditions or circumstances. | PASS, corrected. The original version of this artifact named "time pressure" as the example condition, which leaks D15's actual discovered context — the same class of error the D4 audit already caught once, recurring here in a different entry. The deployed extraction protocol already generalized this independently; this version matches that fix. |
| D16 | Logistics and communication needs get attention later than technical ones | **Attention allocation across task types.** The relative timing and priority given to technical work compared to logistics, scheduling, or communication-related work. | PASS. Doesn't assert technical work comes first. |
| D17 | Full-ambition design first, pragmatic scoping-down later | **Scope evolution.** How the scope or ambition of a design changes between its initial framing and its actual implementation, in either direction. | PASS, corrected. First draft implicitly presupposed the ambition-then-cut-down direction; "in either direction" was added specifically to strip that. |
| D18 | A current project explicitly carries forward and refines a prior one | **Cross-project continuity.** Whether and how a new piece of work references, reuses, or builds on structure, ideas, or decisions from previously discussed work. | PASS. Doesn't assert this happens. |
| D20 | Output quality held up under real adversity (sleep deprivation, wrong information, travel fatigue) | **Output-quality stability under strain.** Whether the quality of reasoning or deliverables changes under adverse conditions such as time pressure, incomplete or incorrect information, fatigue, or disrupted plans. | PASS, corrected. First draft's "stability" framing risked implying quality holds up; the finding itself is that direction, so the category must stay genuinely open on it. |

**Phase-noting — cross-cutting, not a peer to the eighteen above.** This isn't a search target; it's an instruction attached to *every* entry recorded under any category. **Process position:** for any behavior recorded, note where within the person's reasoning arc for that instance it occurred, in observable terms ("before any commitment had been made," "after the space was mapped, before building began") — never fitted into a predetermined stage template. "Not phase-linked" and "insufficient evidence to place" are valid values. Audit: elicited, not imposed, per the same rule the snapshot design already applies to phase language generally — passes because it structurally cannot presuppose a specific arc.

---

## 2. What deliberately gets no category entry, and why

- **D2** — vocabulary-only, already folded into D1's category rather than standing alone.
- **D10** — already folded into D8's category (the stopping-support policy absorbed it directly in the spec).
- **D19** — retired from the Model layer entirely; its content now lives in G1/G2. Goals aren't search targets, they're what policies serve.
- **D21** — the crisis instance. Deliberately **not** a search category. The care-override (G4/P9) already travels as a universal policy and applies regardless of whether anything is actively being searched *for*. Turning a person's crisis moment into a named search target would be the wrong kind of category to hand a blind reader — it reframes something that needs care into something to be found, which is exactly backwards.
- **IH1, IH2, IH3** — the interaction hypotheses. These encode relationships *between* already-known findings, which makes them more contamination-risky than any individual D-item, not less. They are not searched for directly; they get tested at consolidation by cross-referencing what the blind pass independently found under the relevant home categories (IH1 against Sufficiency Recognition / Search-Persistence and Upstream Mapping; IH2 against Feasibility-Testing Sequence and Upstream Mapping).

---

## 3. Sensitivity map — the six Conditional-tier items

For each, its home category, a sensitivity rating, and the reasoning behind it — committed now, before the pilot runs, per the standing rule that this judgment must not be made after results are visible.

**D1 — belief-revision rate.** Home: Belief-revision rate. **Sensitivity: Low–Moderate.** Detecting this needs multiple instances of new information landing in a *similar* domain, with visible before/after belief states, to assess rate and domain-dependence at all — a single revision doesn't establish a rate. This is structurally demanding to catch regardless of how well the category is phrased.

**D5 — planning-versus-habit.** Home: Planning-versus-habit tendency. **Sensitivity: Moderate–High.** Needs a recognizably similar problem *type* to recur across the corpus. Given the source material spans multiple distinct projects, some recurring problem-type (an architecture decision, a stopping call) is plausible, which makes this comparatively catchable.

**D6 — risk/tradeoff framing.** Home: Risk and tradeoff framing. **Sensitivity: Moderate.** Needs an explicit, sufficiently detailed risk-laden decision somewhere in the files — present or absent depending on what the corpus actually contains, not on category quality.

**D9 — curiosity direction.** Home: Curiosity direction. **Sensitivity: Low.** Needs genuinely undirected exploration, distinct from goal-directed project work, which appears to be the dominant mode of the source material based on everything reviewed in this project so far. If the files are mostly task-driven, this may simply not surface, regardless of how the category is phrased. Flagged as one of the two hardest items to catch by construction.

**D17 — scope evolution.** Home: Scope evolution. **Sensitivity: Moderate–High.** Needs one project's arc visible from initial framing through later implementation — plausible if any file sequence tracks a single project that far. **Cross-note:** keep this separated from D18 (Cross-Project Continuity) in the traveling list — one tracks change *within* a project over time, the other tracks connections *between* separate projects. A blind instance could plausibly conflate "this project's scope changed" with "this project connects to an earlier one" without a clarifying line; one is added in Section 4.

**D20 — output-quality stability under strain.** Home: Output-quality stability under strain. **Sensitivity: Low.** Needs a second episode of genuine adversity, comparable to the one existing instance, to appear elsewhere in the corpus. Adversity moments are presumably uncommon in ordinary project correspondence; this may simply not recur. Tied with D9 as the hardest to catch, and for the same structural reason — the category is right, the corpus may just not contain enough raw material regardless.

No claim is made here about the other eleven categories' sensitivity — the rule only requires mapping the Conditional tier, since these are specifically the items where a second independent instance would change something (promotion). The Established and Gated items would still benefit from blind recurrence as bonus inter-rater confirmation, but nothing in the architecture depends on it.

---

## 4. The final traveling category list — what actually goes in the batch-instance protocol

Stripped of every D-item reference. This is the version to paste directly into the category-space section of the instruction.

1. **Belief-revision rate** — when new information appears, how much a stated plan, estimate, or conclusion shifts in response, and whether this varies across domains or situations.
2. **Confidence calibration** — how stated or implied confidence in a claim relates to how well-supported that claim turns out to be, and whether this differs across domains or conditions.
3. **Decision-commitment patterns** — when, how, and on what evidence a choice gets committed to.
4. **Planning-versus-habit tendency** — when a familiar type of problem recurs, whether a previously-used approach gets reapplied or a fresh plan gets built.
5. **Risk and tradeoff framing** — how potential losses, gains, and low-probability outcomes are weighted relative to each other when options are compared.
6. **Sufficiency recognition** — what, if anything, signals that a deliverable or decision has reached an adequate point, and what happens once it does.
7. **Search-persistence and stopping threshold** — how much exploration precedes a next step, and what, if anything, signals it has run its course.
8. **Curiosity direction** — during open-ended exploration, what kind of gap or unresolved question draws attention.
9. **Problem decomposition** — how a large or ambiguous problem gets broken into parts, and whether any structure recurs across problems.
10. **Feasibility-testing sequence** — whether, and when relative to proposing an approach, it gets tested against likely failure modes.
11. **Upstream mapping** — whether and how a reference base or constraint map gets assembled relative to when solution design begins.
12. **Gap-checking behavior** — whether, how, and under what circumstances a check for overlooked considerations occurs unprompted.
13. **Verification timing** — the relationship between presenting something as complete and confirming that it is, including whether this varies across different conditions or circumstances.
14. **Attention allocation across task types** — the relative timing and priority given to technical work versus logistics or communication work.
15. **Scope evolution** — how the scope or ambition of a design changes between initial framing and implementation, in either direction. *(Distinct from #16: this tracks change within one project over time, not connections between projects.)*
16. **Cross-project continuity** — whether and how a new piece of work references, reuses, or builds on structure or decisions from previously discussed work. *(Distinct from #15: this tracks connections across projects, not scope change within one.)*
17. **Output-quality stability under strain** — whether the quality of reasoning or deliverables changes under adverse conditions such as time pressure, incomplete information, fatigue, or disrupted plans.

Plus the cross-cutting instruction: **Process position** — for every entry recorded under any category above, note where in the reasoning arc it occurred, in observable terms, not a fixed stage template.

---

## 5. Flagged, not included — candidates for a decision, not additions

Four dimensions from the original interview-era list are in-scope (process, not identity) and were never promoted to a capture-spec item — plausibly because the earlier sampling-based reads never happened to surface a clean instance, which is exactly the situation a full blind read could resolve differently. Not included in Section 4 unless confirmed; flagging rather than deciding.

- **Problem framing** — how the actual problem, question, or goal gets defined and initially stated, before any decomposition or solution work begins. Distinct from Problem Decomposition (#9), which is about breaking an *already-framed* problem into parts, not about how the framing itself gets set. Audit: doesn't presuppose any particular framing style or approach — PASS.
- **Learning style** — how new information, tools, or unfamiliar problem types get approached and absorbed.
- **Communication style** — how explanations, requests, or updates get structured (dense vs. expansive, conclusion-first vs. building up to it). Distinct from Attention Allocation (#14 above), which is about *when* communication-type tasks get attention, not *how* communication is conducted.
- **Error-pattern detection** — when something doesn't work as expected, how it gets noticed, diagnosed, and corrected. Distinct from Verification Timing (#13), which is about premature claims of completion, not the response once an error is actually found.

---

## Status

This closes the pre-drafting requirement from autopsy Section 10: enumerated (seventeen dimensional categories plus the process-position instruction), audited (content-independence checked by inspection, three corrections made and shown, one of them — Verification Timing — caught only after the fact and fixed here), sensitivity-mapped (all six Conditional-tier items, committed before any pilot runs). Section 4 is ready to drop into the batch-instance protocol, and already has been. One thing needs a decision before the pilot: whether to include any of the four flagged candidates in Section 5.
