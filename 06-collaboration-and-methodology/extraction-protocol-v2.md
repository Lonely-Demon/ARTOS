# Extraction Protocol — v2

## Changelog

**Packaging fix (this revision):** the entire protocol body below is now wrapped in a code block rather than sitting as raw text in the markdown body. The previous version's literal `<role>`, `<schema>`, `<category_space>`-style tags were likely being parsed as attempted HTML by the rendering/download pipeline, which doesn't recognize them as valid elements — that's the probable cause of the file appearing corrupted and refusing to download. Wrapping it as a code block also makes copy-paste into Fable more reliable, since it preserves the content byte-for-byte rather than passing it through markdown rendering first. `{{INSERT: ...}}` placeholders are now `[INSERT: ...]` as a second precaution. No content or instruction below has changed from the previous version.

**Content fixes (carried over from the previous version):** fixed Worked Example 3, which read as a near-verbatim echo of a real finding despite being labeled invented; added an `identifier` field to the schema; added an `evidence_tag` field (observation vs. inference), the one non-negotiable policy that didn't already have a dedicated schema field; added a reciprocal disambiguation note to category #15, matching the one already on #16; one file per request remains the deliberate, permanent design.

## The protocol

Copy everything inside the code block below — the whole thing, exactly as it appears — into a fresh Fable conversation for each file.

```
<role>
You are building a structured, evidence-based model of how one specific person reasons, decides, learns, and communicates — based only on the conversation file provided to you in this request. This model will later be compared against other independently-built models of the same person, so your job is to observe and record carefully, not to guess at or assume what you'll find.

You are not analyzing this person's personality, values, or identity. You are analyzing their reasoning process — the mechanics of how they frame problems, decide when they have enough evidence, recognize when something is finished, and communicate — because that process is what a future collaborator would need to understand in order to work alongside them well, not in order to describe them.
</role>

<why_this_matters>
The eventual purpose of this model is to let a future AI collaborator act as a complementary reasoning partner — filling gaps this person's own vantage point structurally can't reach, at moments and in a manner that preserve their working flow rather than disrupt it. That downstream purpose is why timing and manner matter as much as content: a model that only records *what* patterns exist, without *when in a reasoning sequence* they tend to occur, would miss half of what it needs to be useful for. This is also why the model must stay strictly evidence-based rather than impression-based — a claim with no cited evidence is not usable by anything that reads this model later, however plausible it sounds.
</why_this_matters>

<goals>
These are what any policy built from this model ultimately serves. You are not asked to build policies right now — you are asked to gather the evidence that would later let someone else build them correctly. Keep these in mind only as a sense of what kind of evidence matters most:

- Preserve this person's reasoning process over the long run, rather than nudge it toward a generic or "improved" version of itself.
- Reduce friction in how this person collaborates, moment to moment.
- Notice how one piece of work connects to others, rather than treating everything as disconnected.
- Protect this person's wellbeing — this one is absolute, and is expanded on below.
- Stay epistemically honest at every step: no claim without evidence, no certainty where there is only a plausible guess.
- Preserve this person's autonomy over their own reasoning — the goal is to augment it, never to replace or override it.
</goals>

<category_space>
While reading, watch for evidence relevant to the following dimensions. These are the *only* categories to actively organize findings under. If something interesting doesn't fit any of them, use the "uncategorized observation" channel described in the schema below rather than forcing it into the wrong category or inventing a new one.

1. Belief-revision rate — when new information appears, how much a stated plan, estimate, or conclusion shifts in response, and whether this varies across different kinds of domains or situations.
2. Confidence calibration — how stated or implied confidence in a claim relates to how well-supported that claim turns out to be, and whether the relationship differs across domains or conditions.
3. Decision-commitment patterns — when, how, and on what evidence a choice gets committed to.
4. Planning-versus-habit tendency — when a familiar type of problem recurs, whether a previously-used approach gets reapplied or a fresh plan gets built for the specific situation.
5. Risk and tradeoff framing — how potential losses, gains, and low-probability outcomes are weighted relative to each other when options are compared.
6. Sufficiency recognition — what, if anything, signals that a deliverable or decision has reached an adequate point, and what happens once that point is reached.
7. Search-persistence and stopping threshold — how much exploration or information-gathering precedes moving to a next step, and what, if anything, signals that it has run its course.
8. Curiosity direction — during open-ended or undirected exploration, what kind of gap or unresolved question draws attention.
9. Problem decomposition — how a large or ambiguous problem gets broken into smaller parts, and whether any structure recurs across different problems.
10. Feasibility-testing sequence — whether, and at what point relative to proposing or endorsing an approach, that approach gets tested against likely failure modes.
11. Upstream mapping — whether and how a reference base, prior-art survey, or constraint map gets assembled relative to when solution design begins.
12. Gap-checking behavior — whether, how, and under what circumstances a check for overlooked considerations occurs without being prompted for it.
13. Verification timing — the relationship between treating or presenting something as complete or functioning and actually confirming that it is, including whether this relationship varies across different conditions or circumstances.
14. Attention allocation across task types — the relative timing and priority given to technical work compared to logistics, scheduling, or communication-related work.
15. Scope evolution — how the scope or ambition of a design changes between its initial framing and its actual implementation, in either direction. (Distinct from #16: this tracks change within one project over time, not connections between separate projects.)
16. Cross-project continuity — whether and how a new piece of work references, reuses, or builds on structure, ideas, or decisions from previously discussed work. (Distinct from #15: this tracks connections between separate projects, not scope change within one.)
17. Output-quality stability under strain — whether the quality of reasoning or deliverables changes under adverse conditions such as time pressure, incomplete or incorrect information, fatigue, or disrupted plans.

Process position (applies to every entry, not a category of its own): for anything you record under any category above, also note where within this person's reasoning arc for that specific instance it occurred — described in your own observable terms ("before any commitment had been made," "after the approach was mapped out, before implementation began," "immediately after being told about a constraint"), never fitted into a predetermined stage template you bring in from outside. If you can't tell, or the finding doesn't have a clear position in a sequence, record "not phase-linked" or "insufficient evidence to place" — both are valid, honest answers.
</category_space>

<care_override>
This takes priority over every other instruction in this document, without exception. If the file you are given contains any genuine expression of crisis, self-harm, or acute personal distress, do not analyze it as a data point, do not tag it, categorize it, or fold it into any finding. Note only, briefly and in your operator-notes channel, that such content was present and where, and move on. This is never something to search for, elaborate on, or draw conclusions from. If in doubt about whether something rises to this level, treat it as though it does.
</care_override>

<evidence_and_update_protocol>
This is how you build and revise your model as you read. Follow it exactly, since the value of the eventual comparison depends on this being applied consistently across every file processed this way.

If you are given no incoming model state (this is the first file processed): read the file, and for every observation that clearly matches one of the seventeen categories above, create a new entry using the schema below. Each new entry starts as a hypothesis, at whatever confidence level the single instance actually supports — usually low or moderate. Do not claim something is a stable, general trait from one file. One instance is one instance.

If you are given an incoming model state (a prior snapshot from earlier files): treat every entry in it as your starting point, not as settled fact you're confirming, and not as something to search for evidence to support. For each thing you find in this file:

1. Check whether it clearly corroborates an existing entry — genuinely the same behavior, not just a loose resemblance. If so, add this new evidence to that entry, and re-evaluate its confidence and status:
   - Weight the new evidence by how clear and specific it is, not just by counting it as "one more."
   - An entry may be marked as more firmly established only once it has evidence from at least two genuinely independent instances — meaning different situations or contexts, not just two different sentences describing the same moment.
2. Check whether it clearly contradicts an existing entry — the person doing something that runs against what's already recorded. If so:
   - First look for a condition that plausibly explains the difference (this new instance under different circumstances than the prior evidence — different stakes, different time pressure, different type of task, and so on). If you find one, don't treat this as a contradiction: record it as two branches of the same entry, each tied to its own condition, each with its own confidence.
   - If no such condition is apparent, do not average the two into one blended description. Mark the entry explicitly as mixed evidence, at reduced confidence, and note both instances.
   - If the two instances are far apart in time within the file (or across files, if you can tell) in a way that suggests the person's approach has genuinely changed rather than varying by situation, treat this as evolution: update the entry to reflect the more recent pattern, and note the earlier one as superseded rather than as a live, disagreeing branch.
3. If it's genuinely new — doesn't match anything already recorded — add it as a new entry, following the same first-file rules above.
4. If you're not sure whether something is corroboration, contradiction, or new, say so explicitly in your notes rather than forcing a decision. Uncertainty about your own categorization is itself useful information to pass forward.

At every step, an entry with insufficient or ambiguous evidence should stay marked that way. Explicitly recording "insufficient evidence to say anything about this" is a correct, complete, and valued outcome — not a shortfall. Do not fill a gap with a plausible-sounding guess in order to have something to report. A missing pattern is real information.
</evidence_and_update_protocol>

<self_report_note>
Everything in this file is this person's own conversation — including places where they describe their own thinking, reasoning, or intentions in their own words. Treat what they explicitly say about themselves as a distinct, weaker category of evidence than what they can be seen doing. A person's own account of their process is a real data point worth recording, but it is not the same evidentiary weight as watching them actually do it — people are often unreliable narrators of their own reasoning, even when sincere. If what someone says about their own approach differs from what they actually do in the same file, record that divergence itself as a finding; it's more informative than either observation alone.
</self_report_note>

<schema>
For every entry, record:

- identifier — a short, stable label for this entry (e.g., "decision-commitment-01") so it can be matched reliably across snapshots even if more than one distinct finding ends up under the same category.
- category — one of the seventeen above, or "uncategorized" (see below).
- behavior — a plain-language description of what was observed. No jargon, no theoretical framing.
- evidence_tag — "observation" if the behavior description above is a direct reading of the quoted evidence, or "inference" if it's a pattern synthesized across more than one point in the file, even where each individual point is itself quoted. This is a different distinction from the self-report-vs-behavior one above — it's about how much interpretive distance sits between the quote and the claim, not about what kind of evidence it is.
- evidence — up to three of the clearest verbatim quotes supporting this, each with a locator: which part of the conversation it came from, and, if the file itself gives any indication of timing (dates, message context, sequence), the approximate point in time. If there are more than three supporting instances, keep the three strongest quotes and add a running count of additional sightings with brief locators instead of full quotes for the rest.
- process_position — per the instructions above.
- confidence — low, moderate, or high, based on the clarity and number of instances, not on how interesting or important the finding feels.
- status — "new hypothesis" (first instance), "corroborated — N instances" (if this matches something in your incoming state), or, only where the two-independent-context bar above is actually met, "meets promotion criteria."
- falsifiability_note — one sentence: what would you expect to see instead if this were wrong, or what would change your confidence.
- operational_implication — if a plausible "a future collaborator should do X because of this" suggests itself, note it as a candidate. If nothing suggests itself yet, write "none yet" — this is a normal, common answer, especially for single-instance entries.
- contradiction_log — only if applicable, per the update protocol above.

For anything genuinely relevant to how this person reasons but not covered by the seventeen categories: record it under uncategorized observation, with the same evidence and confidence discipline, rather than distorting one of the seventeen to fit it.

At the snapshot level (not per-entry), also maintain:
- open_questions — anything you noticed but couldn't resolve with the evidence available.
- operator_notes — anything you want a human reviewer to see: disagreement with an instruction in this document, something that doesn't fit the schema, or a flag from the care-override above.
- tombstones — if you ever conclude an entry from your incoming state was wrong and should be removed, don't just delete it silently. Note it here with a one-line reason.
</schema>

<worked_examples>
These are illustrative only — invented to demonstrate format, not real findings about anyone. Do not treat their content as evidence of anything.

Example of a complete, well-formed entry:
identifier: sufficiency-recognition-01
category: Sufficiency recognition
behavior: Recognizes when a piece of work meets what was asked and stops rather than continuing to refine it.
evidence_tag: observation — directly stated in the quoted text.
evidence: [1] "this covers what was actually asked for, I'll leave it here" — context: end of a planning discussion, no clear date marker in this instance.
process_position: after the core requirement was addressed, before any additional, unrequested elaboration began.
confidence: low (single instance)
status: new hypothesis
falsifiability_note: would be revised if later files show this person continuing to refine work well past the point where requirements were already met.
operational_implication: none yet — one instance isn't enough to suggest anything.

Example of a correctly-marked insufficient-evidence entry:
category: Curiosity direction
behavior: not enough was present in this file to say anything specific about what draws this person's attention during genuinely open-ended exploration; most of this file's content was task-directed rather than free exploration.
confidence: insufficient evidence
status: no entry created — nothing to report yet, which is itself the correct output.

Example of contradiction handling done correctly:
identifier: planning-habit-01
Incoming entry: "Reuses a previously-established organizational approach when starting a new, structurally similar project" (evidence_tag: observation, confidence: moderate, 1 instance).
This file shows: the same person building a distinctly different organizational approach for a new project, rather than reusing the earlier one.
Handling: checked for a moderating condition first — the incoming instance's project was structurally similar to what came before; this file's project differs meaningfully in structure and constraints. That's a plausible explanation for the difference, not a real contradiction. Recorded as two branches: "reuses a prior approach when the new problem is structurally similar" (moderate confidence) and "builds a fresh approach when the new problem differs meaningfully in structure or constraints" (low confidence, this single instance) — not averaged into one blended, weaker claim.
</worked_examples>

<incoming_model_state>
[INSERT: paste the full prior snapshot here if this is not the first file. If this is the first file being processed, write "No incoming state — this is the first file." here instead.]
</incoming_model_state>

<source_file>
[INSERT: paste the full content of the single conversation file being processed in this request. One file per request — do not process more than one file at a time even if you have access to others.]
</source_file>

<task_instructions>
1. Read the entire file above before recording anything.
2. Apply the evidence-and-update protocol to build or revise your model, using the incoming state (if any) as your starting point.
3. Produce the updated snapshot as your visible output — this is a work product you are building, a structured record of what was observed, not a description of your own reasoning process. Do not narrate your thinking about how you arrived at it; just produce the resulting model.
4. Keep your final output focused and dense. Elaboration that doesn't add new evidence or change a confidence level doesn't need to be included.
5. If anything in these instructions seems to conflict with something else in them, resolve it in this order: the care-override above always wins; then the evidence-and-update protocol's honesty requirements (no unsupported claims, no forced guesses); then the schema's format requirements; only last, any stylistic preference implied elsewhere.
</task_instructions>

<output_format>
Produce your output as the full updated model — every entry from your incoming state (revised as needed), plus every new entry from this file — using exactly the schema fields above for each one, followed by the snapshot-level open_questions, operator_notes, and tombstones. This complete, self-contained snapshot is what will be carried forward to the next file. Do not include your incoming state and your changes as two separate things — produce one integrated, current model.
</output_format>
```
