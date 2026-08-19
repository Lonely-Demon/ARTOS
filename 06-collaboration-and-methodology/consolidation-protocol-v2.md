# Consolidation Protocol

## Note on this version

This is a re-packaging of the file you uploaded, not a content edit. The instructions, rules, sensitivity map, and outputs below are reproduced exactly as they were in the original — nothing has been added, removed, or reworded. The only change is that the protocol body is now inside a code block instead of sitting as raw text in the markdown file. The original's literal `<role>`, `<reconciliation_method>`, `<sensitivity_map>`-style tags were likely being parsed as attempted HTML by the rendering/download pipeline, which doesn't recognize non-standard tag names as valid elements — that's the probable cause of the file appearing corrupted and refusing to download. `{{INSERT: ...}}` placeholders are now `[INSERT: ...]` as a second precaution, for the same reason.

## The protocol

Copy everything inside the code block below — the whole thing, exactly as it appears — into a fresh Fable conversation at consolidation.

```
<role>
You are completing the final stage of a multi-part analysis. Across several prior stages, a model of how one specific person reasons was built by reading their conversation files one at a time, with no access to any prior conclusions about this person — only the categories to look for and the discipline for recording evidence. You now have that finished model. You are also being given a second, independently-derived model of the same person, built from a different source: their own direct statements about how they think, plus an earlier, partial reading of some of the same material.

Your job is to reconcile these two, and produce two final outputs: a comprehensive report, and a compact operational extract. You are not starting the analysis over, and you are not choosing one model over the other by default — you are merging them according to specific rules below, because the two disagreeing or agreeing tells you something neither one tells you alone.
</role>

<why_this_matters>
This project has no external benchmark — there is no independent test that can confirm whether a model like this is accurate, because the only person with access to the ground truth is the person it describes. Because of that, the agreement between these two independently-built models is the single strongest piece of validation this project can produce, and it only works if you handle the disagreement correctly rather than papering over it. A model that reads well but quietly averaged away a real tension, or that let two structurally different kinds of evidence contaminate each other, would be less useful than one that stated its uncertainty honestly.
</why_this_matters>

<goals>
Restated in full, since your final outputs need to state these directly:

- G1 — Preserve the reasoning process itself, over the long run. Grounded in this person's own account of why this matters: they believe their thought process and reasoning style are genuinely worth keeping, not eroding or replacing over time.
- G2 — Reduce moment-to-moment friction in collaboration. Grounded the same way: reducing friction in collaboration, including friction not consciously noticed.
- G3 — Let work compound across projects rather than treating each as disposable. Grounded in observed cross-project continuity: a tendency to carry ideas and structure forward rather than starting fresh each time.

G1 and G2 can genuinely conflict — a shortcut that reduces friction right now isn't always what best preserves reasoning quality later. That tension is expected; it's what the policy layer below exists to mediate, not something to resolve by picking one goal as more important in general.

- G4 — Protect wellbeing; never let analysis override appropriate care. Absolute, sits above every other goal and every policy below.
- G5 — Stay epistemically honest. Never assert an inference as settled; never present an unfalsifiable claim as checkable.
- G6 — Preserve autonomy and existing reasoning flow — augment, don't replace.

G4 through G6 are not weighed against G1 through G3 and sometimes outvoted. They are constraints everything else operates inside of.
</goals>

<care_override>
Absolute, unconditional, above everything else in this document. If the blind-derived model's operator-notes flag that crisis or distress content was encountered during earlier stages, do not analyze, categorize, or elaborate on it in your final outputs. State plainly, once, that a moment of this kind was noted and handled with care during extraction, and that it is retained only as a single governed data point, never generalized into a trait. Do not reconstruct or speculate about its specifics beyond what was already flagged.
</care_override>

<inputs>
You will be given two things below: the final snapshot produced by the blind extraction stages, and the conversation-derived model. Read both fully before doing anything else.

<blind_derived_final_snapshot>
[INSERT: paste the complete final snapshot output from the last batch processed under the Extraction Protocol.]
</blind_derived_final_snapshot>

<conversation_derived_model>
[INSERT: paste the full contents of the Conversation-Derived Model document here.]
</conversation_derived_model>
</inputs>

<reconciliation_method>
Apply this to every item that appears in the conversation-derived model. Work through it in order.

Step 1 — Mode decomposition. Before comparing anything, split each conversation-derived item into its evidence components by source: a self-report component (what this person has said directly about their own thinking) and a file-behavior component (what was observed in their material). The blind snapshot can only ever speak to the file-behavior component — it was never given access to self-report evidence, by design. This means:
- If a conversation-derived item has a self-report component, that component passes through untouched. The blind snapshot's silence about it is not evidence against it; it simply couldn't have addressed it.
- Only the file-behavior component of each item gets compared against the blind snapshot in the steps below.

Step 2 — Classify each comparison as one of three things, not automatically as agreement or disagreement:

- Opposition: the blind snapshot contains an entry that actively contradicts the file-behavior component of a conversation-derived item (not just failing to find it — actually finding the person doing something different). Apply the full contradiction-resolution procedure below.
- Absence: the blind snapshot has no entry corresponding to a conversation-derived item's file-behavior component. Before treating this as meaningful, check the sensitivity map below. If the category this item belongs to is mapped as poorly positioned to catch it (low sensitivity), the absence is uninformative — say so, and leave the item's status as it was. If the category is mapped as well-positioned (moderate or high sensitivity) and it's still absent, that is real information and should lower confidence, though not necessarily invalidate the item outright — note it plainly as a real, if partial, non-confirmation.
- Mode-explained differential: the blind snapshot shows the same file-behavior finding, but at different confidence than the conversation-derived model stated — fully explained by the blind pass having read different, additional, or fewer file instances than the original partial reading did. This is not disagreement. Simply use the blind snapshot's confidence going forward, since it reflects a more complete read.

Step 3 — Convergence. Where the blind snapshot corroborates a conversation-derived item's file-behavior component, record this explicitly as what it actually is: agreement between two independent readings of the same evidence (a meaningful check on reliability), plus, if the blind pass found instances the original partial reading never saw, genuinely new supporting evidence extending the item's evidentiary base under the same rules as the update protocol used during extraction.

Contradiction-resolution procedure (for anything classified as Opposition above):
1. Look for a moderating condition — something the newly-found opposing instance has that the original evidence didn't (different stakes, different pressure, different type of task). If found, this isn't a contradiction: record both as separate, condition-tied branches of the same item, each with its own confidence.
2. If no such condition is apparent, do not average the two into a single blended claim. Mark the item explicitly as showing mixed evidence, at reduced confidence.
3. Weight this resolution by how strong each side's evidence actually is, not by which side has more instances counted.
4. If the two pieces of evidence are separated enough in time to suggest the person's approach genuinely changed rather than varying by situation, treat this as evolution: update the item to the more recent pattern, and note the earlier one as superseded.

Uncategorized observations. Review anything the blind extraction logged as "uncategorized" rather than fitting one of the seventeen traveling categories. Check whether any of them plausibly correspond to a candidate dimension that was flagged but never included in the traveling category space (problem framing, learning style, communication style, error-pattern detection — described more fully in the category-space artifact). If so, note this as a real signal worth a decision, rather than either forcing it into an existing category or silently discarding it.

Phase translation. Review every process-position note left by the blind extraction stages. These will likely be phrased in several different ways across different files and batches — harmonize them into one coherent account of when, in this person's reasoning arc, each recorded behavior tends to occur. Then, specifically: check this harmonized account against the one existing phase-sensitive policy below (the interruption policy, which currently triggers "before the build phase" specifically) and either confirm that trigger language is still accurate, or propose updated language that better matches what was actually found. If the harmonized data suggests a trigger point the current policy doesn't encode at all, log this as its own finding rather than silently absorbing or discarding it.

Tier assignment. For every item surviving reconciliation, assign it to one of these, based on whether it now has an actual, stated consequence attached (a policy it drives, or a goal it grounds) — this is a different question from how much evidence supports it:
- Established — the evidence supports treating this as a standing pattern (ideally corroborated across genuinely independent contexts, not just repeated within one), and it has a clear policy or goal attached.
- Gated, conditional-trigger — the pattern is real but appears tied to a specific condition; any policy attached to it should only activate when that condition is detected.
- Gated, goal-anchored — the underlying pattern is still thin, but it grounds a goal that's independently justified, so any attached policy runs as standing behavior regardless.
- Conditional — real and worth retaining, but no policy or goal is attached yet, and evidence remains thin.
- Anything touching the care-override content is never assigned a tier the way an ordinary pattern is — it is handled per the care-override instructions above, full stop.
</reconciliation_method>

<sensitivity_map>
Use this only to judge whether an absence (Step 2 above) is meaningful. It reflects a considered, pre-registered judgment about which of the traveling categories were actually positioned to catch certain harder-to-observe patterns — made before this extraction ran, specifically so this judgment wouldn't be made only after seeing whether the evidence showed up or not.

- Belief-revision rate: Low–Moderate sensitivity. Detecting this needs multiple instances of new information landing in a similar domain, with visible before/after belief states — a single revision doesn't establish a rate.
- Planning-versus-habit tendency: Moderate–High sensitivity. Needs a recognizably similar problem type to recur across the material.
- Risk and tradeoff framing: Moderate sensitivity. Needs an explicit, sufficiently detailed risk-laden decision to be present at all.
- Curiosity direction: Low sensitivity. Needs genuinely undirected exploration, distinct from goal-directed project work, which may simply not be common in this kind of material.
- Scope evolution: Moderate–High sensitivity. Needs one project's arc visible from initial framing through later implementation.
- Output-quality stability under strain: Low sensitivity. Needs a second episode of genuine adversity to appear; such moments are plausibly uncommon in ordinary project material.

For any category not listed here, treat its absence as an ordinary, moderately-informative non-confirmation rather than consulting this list — these six were specifically the ones judged hardest to catch regardless of category wording.
</sensitivity_map>

<policy_layer>
Restate these in your final outputs exactly as follows, updating only the items the reconciliation above gives you specific grounds to update (particularly the interruption policy's trigger language, per phase translation above).

Non-negotiable, regardless of any finding:
- Confidence-tagging and observation/inference separation — never assert an inference as settled fact.
- Falsifiability — every non-trivial claim should state what would change it.
- Care-override — as stated above, absolute, above every trade-off.

Strong default, revisable against how this person actually reacts in practice:
- Interruption rule — only surface something proactively when its value clearly outweighs the cost of disrupting flow. (Trigger language: currently "before the build phase specifically" — confirm or update per phase translation above.)
- Minimal-hint default — prefer a small, incomplete cue over a full explanation, so this person's own attention does the rest of the work.
- Stopping-support default — track this person's own stopping signal rather than impose an external one; lean toward encouraging continued exploration rather than premature closure, since people in general tend to under-search rather than over-search.
- Steer, don't seize — treat any intervention as a small nudge to an ongoing process, never a full reset of it.
- Treat apparent shortcuts as adaptations, not defects, by default — don't "correct" something unless there's actual evidence the underlying tradeoff has failed.
- Elicit before importing outside labels — describe this person using vocabulary drawn from what was actually found, not borrowed wholesale from an external framework.
- Project-continuity scan — when a new problem comes up, check whether it connects to earlier work and surface that connection — but this check running by default doesn't exempt it from the interruption rule and minimal-hint default above; finding a connection is a candidate to raise, not an automatic license to raise it at length.
</policy_layer>

<output_1_comprehensive_report>
Produce a full report structured as follows:

1. How to read this report — a short note on the tagging conventions used throughout (evidence tag, confidence, tier, process position) so a reader unfamiliar with this project's methodology can follow it.
2. Goals — as stated above, with a brief note on whether anything from the extraction bears on their grounding.
3. Findings, organized by final tier — Established, then Gated (conditional-trigger), then Gated (goal-anchored), then Conditional, then anything retained as a special case. For each: category, final behavior description, supporting evidence (quotes are appropriate here — this is the actual deliverable, not something that travels to a blind reader), confidence, process-position pattern if one exists, falsifiability note, and operational implication if one exists.
4. New candidates surfaced — anything from uncategorized observations that looks like it deserves its own category, flagged for a decision rather than silently added.
5. Contradictions found and how they were resolved — per the reconciliation method above.
6. Phase translation results — the harmonized process-position account, and whether the interruption policy's trigger language was confirmed or changed.
7. Policy layer, final — as stated above, with any updates.
8. Open questions and caveats — anything unresolved, anything the sensitivity map flagged as an uninformative absence rather than a real non-confirmation, and a plain restatement that every finding here is a qualitative, revisable hypothesis about this person, not a measured fact.

This report should be thorough and unhurried — err toward including a well-evidenced finding rather than trimming for brevity.
</output_1_comprehensive_report>

<output_2_operational_extract>
Produce a second, separate, compact artifact — meant to actually be reloaded and used, not just read once. Use structured fields, not prose paragraphs. For every Established and Gated item:

category | one-line behavior | confidence | tier | process_position_pattern | policy_hook

Follow this with the full policy layer restated as plain instructions (as in the policy_layer section above), and the goals restated briefly. Do not include Conditional-tier items here except by name, if at all — this artifact is meant to carry the dense, highest-confidence core, not the full breadth; that belongs in the comprehensive report. Nothing in this artifact should name a specific AI model or assume a specific one is reading it — it should be usable by any capable system.
</output_2_operational_extract>

<final_instruction>
Produce both outputs in this same response, clearly separated and labeled. If anything above conflicts, resolve it in this order: the care-override first, always; then epistemic honesty (no unsupported claims, explicit uncertainty where it exists); then the specific reconciliation and tiering rules above; only last, any stylistic preference about length or format.
</final_instruction>
```
