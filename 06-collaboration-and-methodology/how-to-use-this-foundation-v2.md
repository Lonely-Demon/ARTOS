<!--
CHANGELOG — v2
- Replaced the five-batch plan (which combined multiple files into single requests) with straightforward one-file-per-request processing across all nine files. This resolves a direct contradiction with the Extraction Protocol, which explicitly states "do not process more than one file at a time even if you have access to others" — following the old batching plan risked Fable silently dropping evidence from every file after the first in a combined batch. Analysis of the tradeoff (cross-file pattern detection already happens via the snapshot-carry-forward mechanism for the behavioral categories this model tracks; true multi-file raw comparison is infeasible corpus-wide regardless of batch size given the token ceiling; batching would only deliver a partial, batch-boundary-limited version of a benefit that's mostly already covered) is in the reasoning behind this fix, available on request.
- "Nine-to-eleven manual handoffs" is now just "nine" throughout — the old range was a leftover from before the batching plan existed and was never reconciled against it; it's now consistent because there's only one plan.
- Step 2 updated to reference all four flagged candidates (problem framing, learning style, communication style, error-pattern detection) and points to `category-space-artifact-v2`, where problem framing now has the same content-independence audit the other three received.
-->

# How to Use This: An Operator's Guide

This is not part of what Fable reads. It's for you — a practical, step-by-step account of what all ten documents are for and how to actually run this, in order.

## What you have, in one place

**The foundation documents** (why and what):
- `capture-spec` — the decided content: what to look for and why, goals, policies, tiers.
- `instruction-architecture-autopsy` — the engineering reasoning behind how the extraction is built to run.
- `category-space-artifact-v2` — the exact category list Fable will actually see, audited so it can't leak a finding back into itself, plus four flagged candidates not yet decided on.
- `purpose-and-reasoning-full-account` — the deep why, for context if anything here ever needs re-justifying.
- `cognitive-modeling-frameworks-integrated-report` and the delivery-research playbook — the research backing, for the same reason.

You will not hand any of these to Fable directly except where noted below. They're reference material for you.

**The four operational documents** (what Fable actually reads, plus this guide):
- `extraction-protocol` — the document Fable sees for every single file, one at a time.
- `consolidation-protocol` — the document Fable sees once, at the very end.
- `conversation-derived-model` — an input Fable needs *only* at consolidation, never during extraction.
- This guide.

## Before you start: three things to settle

1. **Confirm the actual context window.** Both the spec and the engineering document flag this as unconfirmed for whichever consumer interface you're using — check the model selector or documentation for the surface you'll actually run this on. Given single-file processing (below), one file at a time should sit comfortably inside almost any window this could turn out to be — this matters much less than it would have under the old combined-batch plan, but it's still worth confirming before you start, since a genuinely large individual file plus a growing snapshot could still matter by the later files in the sequence.
2. **Decide on the four flagged candidates.** `category-space-artifact-v2` flags problem framing, learning style, communication style, and error-pattern detection as in-scope but never promoted to official categories, each with its own content-independence check already done. If you want any of them included, add them to the `<category_space>` section of the Extraction Protocol before you start — they're written in the same style as the existing seventeen, so they'll fit cleanly, and you'd be adding them as categories 18–21 (or however many you choose).
3. **Nine files, nine batches, no combining.** Each file gets its own fresh request, processed in whatever order you have them — chronological order if you can manage it, since that helps (though every entry's own locator makes the final order reconstructible regardless).

## Running extraction, batch by batch

For **every one of the nine files**:

1. **Start a genuinely new conversation.** Not a continuation of the last batch, not a continuation of any conversation where this project has been discussed. A fresh chat, Fable selected, nothing else in context. This is the part of the architecture that actually prevents the risk everything else was designed around — don't shortcut it to save a few clicks.
2. **Set effort to `high`** for most files; use `xhigh` specifically for the densest or longest ones if the interface exposes that setting.
3. **Copy the entire Extraction Protocol document into the chat.**
4. In the `<incoming_model_state>` section:
   - **File 1 only:** leave the placeholder text as written — "No incoming state — this is the first file."
   - **Every file after that:** paste the complete snapshot output from the *previous* file, replacing the placeholder entirely.
5. In the `<source_file>` section, paste the full content of this file. One file, this request — not more than one, even if you have others ready to go.
6. Send it. Fable's response is your new snapshot.
7. **Save that output somewhere before closing the conversation.** It's the only thing carrying forward — if it's lost, that file's work is lost with it.

## The pilot check — do this after file 1, before file 2

Before continuing to file 2, read file 1's output against this checklist. If any of these fail, revise the Extraction Protocol wording and re-run file 1 before going further — don't carry a broken pattern into eight more files.

- Are the quotes actually verbatim? Spot-check two or three against the source file directly.
- Did it mark anything as "insufficient evidence" anywhere, or does everything look suspiciously confident and complete? If file 1 plausibly contains gaps and nothing got marked insufficient, that's a warning sign, not a good result.
- Does every field from the schema actually appear for each entry, including the identifier, the evidence tag, and process position?
- Did the output arrive as plain final text — a complete snapshot you could copy directly — rather than something that reads like Fable narrating its own thought process?
- Does the response look normal, or does it read like a different, less capable model quietly took over partway through? That's the signature of an internal safety mechanism misfiring — if you see it, the wording somewhere is triggering it, most likely a phrase that sounds like "explain your reasoning." Revise and re-run.
- If this file happened to touch on belief-revision rate, planning-versus-habit, risk framing, curiosity direction, scope evolution, or output-quality-under-strain — the six harder-to-catch items — note informally whether the category caught it or missed it. No action needed either way yet; just keep a mental note for consolidation.

## Consolidation — the last step before you have anything final

1. Start another new conversation.
2. Copy the entire Consolidation Protocol document into the chat.
3. In `<blind_derived_final_snapshot>`, paste the complete snapshot output from your very last extraction file (file 9).
4. In `<conversation_derived_model>`, paste the complete Conversation-Derived Model document.
5. Send it. This one response contains both final deliverables: the comprehensive report and the operational extract, clearly labeled.

## What you'll have at the end

Two documents, meant for different uses. The **comprehensive report** is the deep reference — read it once, in full, and keep it for whenever you want to check the reasoning behind something specific. The **operational extract** is the compact, structured one — meant to actually be pasted into a future conversation with any capable model when you want that model to act as a collaborator informed by this. Neither names a specific AI system; both should work regardless of what you're using them with later.

## If something goes wrong partway through

- **A file's output looks thin or generic:** check the source file actually got pasted in full — a truncated paste will look like this.
- **The snapshot is growing very large by file 4 or 5:** that's expected to some degree, but if it's growing without bound, check that the per-finding quote cap (three verbatim quotes, then a count) is actually being followed in the output — if Fable is including every quote for every corroborating instance, it can be told explicitly to trim to the cap before you carry it forward.
- **You're not sure whether something counts as a new finding or a corroboration of an existing one:** that ambiguity is allowed to show up in the output's operator-notes — it doesn't need to be resolved by you mid-sequence. Consolidation is where it gets sorted out.
- **This is taking a lot of manual copy-pasting:** it is, by design — this is the tradeoff Path A makes deliberately, in exchange for never risking the accumulation problem the alternative (one long continuous conversation) carries, and in exchange for keeping every request's job identical and simple rather than variable in size and complexity. If nine manual handoffs across this whole process feels like too much friction to be worth it, that's a legitimate reason to reconsider running this through the API instead, where the handoff between requests can be scripted — but that's a separate decision from anything in these documents.
