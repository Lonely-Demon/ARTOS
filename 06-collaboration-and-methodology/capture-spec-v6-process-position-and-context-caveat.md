# The Capture Spec — v6: Process Position, Context-Window Caveat

## Changelog

### v6 (this version)
- **Process position added as an explicit cross-cutting requirement.** Neither this document nor any earlier version ever named phase-within-a-reasoning-arc as its own dimension, even though D4's policy ("identify load-bearing decisions early") and P3's own design (interrupt before the build phase, per the original interview) were always implicitly phase-dependent. This was flagged during the engineering-design review and deferred to whenever the spec was next touched — this is that moment. Added as a cross-cutting instruction attached to every evidence entry, not a nineteenth Model target, matching how the category-space artifact and the engineering design both already treat it.
- **D14's "why a candidate" entry genericized.** Dropped "two tools" — a detail about the evidence-gathering process rather than about the person — for consistency with how source material is described everywhere else in this project's later documents.
- **2G's context-window figures caveated.** The 1M-token / 128k-output numbers were stated as fully verified; the delivery-research this project relies on explicitly notes these are confirmed for API access, not separately confirmed for Claude.ai's consumer chat interface — where this extraction is actually planned to run. Noted directly rather than left as an unstated assumption.

### v5
Added a standing constraint that nothing in the portable model may name a specific LLM, checked against the actual text and found already true in practice. Clarified that a "fresh request" under Path A means the master prompt itself, not just the accumulated findings, has to be present at every stage. Clarified that P10's check runs unconditionally but its surfacing still routes through P3 and P4.

### v4
Split "Gated" into two tiers that were bundled under one name in v3: *Conditional Trigger* (D3, D15, D16 — the policy waits for a specific detected context) and *Goal-Anchored* (D18 — the trait is unconfirmed, but the goal it grounds is independently justified and its policy runs regardless). Added P10 (project-continuity scan), closing a gap where G3 had been confirmed as a goal but had no policy behind it. Resolved ingestion (2G) into two explicit paths with a stated recommendation.

### v3
Made Model tiering explicit and consistent with Policy's, based on whether a live consequence is actually attached rather than on evidence strength alone. Swapped D17 and D18 once that criterion was stated directly. Defined what "independent context" means for promotion to Stable. Added an ingestion reality check flagging that Fable 5's real context window and output ceiling mean the nine source files can't be handled as a single request.

### v2
Added the Goals layer between Model and Policy. Added a temporal tag to every Model target, separate from its evidence tag. Added a bounded Interaction Hypotheses section. Added formal Update Policy and Contradiction Policy. Demoted framework names throughout. Retired D19, split into G1 and G2.

---

## A standing constraint: this describes the person, not a fit to any one model

Nothing in Parts 1 or 2 should ever name a specific model. Every policy is phrased as a plain instruction — "encourage explicit verification," "help identify load-bearing decisions early" — because the actual reader is whatever LLM this eventually runs through. This project was never about Fable or Claude understanding the person; Fable is simply the best tool currently available for extracting the model in the first place. The goal is a spec any capable LLM could pick up and act on as a complementary reasoning partner.

This already held in practice before it was stated: none of G1–G6, D1–D21, or P1–P10 names a model. The one deliberate exception is **2G**, and it stays an exception on purpose — 2G isn't part of the portable model at all. It's a note about the mechanics of running one specific extraction job through one specific tool. If this is ever re-extracted through a different model, 2G gets rewritten or discarded; nothing else does.

---

## Part 1 — What Should Be Captured, and Why

### 1A. Goals — Person-Specific

**G1. Preserve the reasoning process itself, over the long run.** Grounded by your own words in the original interview: preservation, "because I genuinely believe that my thought process and reasoning style is useful." Long-horizon — about not eroding or quietly replacing how you think over time.

**G2. Reduce moment-to-moment friction in collaboration.** Grounded by the same interview: personalization, "because it would reduce the friction... I usually have." Short-horizon — each individual interaction, not the reasoning process as a whole.

**G3. Let work compound across projects rather than treating each as disposable.** Grounded by D18 (NeuraX explicitly building on India Innovates). D18 isn't just a trait to note — it's evidence of something the system should actively pursue: looking for how current work connects to what came before and what's likely next. *(This goal has an actual policy behind it — see P10 in 2F.)*

Worth stating plainly: **G1 and G2 can conflict.** A shortcut that reduces friction right now isn't always what best preserves reasoning quality over the long run. That's expected, not a flaw — it's what the Policy layer exists to mediate.

### 1B. Goals — Universal / Override

Hold regardless of who's being modeled.

**G4. Protect wellbeing; never let analysis override appropriate care.** Directly grounds the care-override behavior first needed when reading the actual files.

**G5. Stay epistemically honest.** Never assert an inference as settled, never present an unfalsifiable claim as checkable.

**G6. Preserve autonomy and existing reasoning flow — augment, don't replace.** Close to a direct restatement of "counterweight, not correction" from the start of this project. Belongs here structurally, not in Policy.

G4–G6 sit **above** the trade space — constraints the optimization runs inside of, not terms weighed against G1–G3.

### 1C. Model — Descriptive Targets (candidates)

*Why each is a candidate at all. Bucket, temporal tag, and linkage are triage decisions — Part 2.*

| # | Behavior | Operational meaning | Possible supporting theories | Why a candidate |
|---|----------|---------------------|-------------------------------|------------------|
| D1 | Revises beliefs at a rate that may depend on how volatile a domain is assumed to be | Distinguishes domains where new information should immediately shift the plan from domains where it shouldn't | Hierarchical belief-updating models | Closest existing frame to "how fast do you revise" |
| D3 | Confidence in a claim doesn't always track how likely it is to be right, and the gap may vary by domain | Some domains may show a demonstrated over/under-confidence pattern | Confidence/accuracy separation models | Operationalizes the confidence-tagging requirement; partially evidenced (SSN verification-gap) |
| D4 | A small number of decisions get made fast and locked early; everything else stays negotiable | Distinguishes load-bearing/irreversible calls from reversible ones | Evidence-accumulation/decision-threshold models | File-evidenced, specific, tied to a real incident |
| D5 | Sometimes runs a practiced approach, sometimes builds a fresh plan for the situation | The choice isn't always matched to what the situation calls for | Planning-vs-habit models | Plausible, distinguishes autopilot from active replanning |
| D6 | Losses, gains, and low-probability risks may not be weighted at face value | Risk framing may skew from a neutral read of actual odds | Descriptive risk/decision models | Formalizes "tradeoff thinking" |
| D7 | Recognizes "good enough, and more" and stops rather than over-refining | A real, demonstrated stopping instinct | Satisficing / maximizing-tendency research | Matches your own words in the SSN retrospective almost exactly |
| D8 | Has an internal stopping signal for research/exploration, not externally specified | Same instinct as D7, applied to information-gathering | Patch-leaving / information-foraging models | Resolves Q7 from the original interview |
| D9 | Attention during free exploration may gravitate to a specific kind of information gap | Tells the counterweight where a hint is likely to land | Learning-progress / curiosity models | Real concept, no confirmed instance yet |
| D11 | Breaks a large problem into parts in a fairly consistent shape | Sets the default structure to preserve when extending the work | Decomposition-style research | Core ChatGPT category, reinforced by file evidence |
| D12 | Before proposing an approach, works through why the obvious versions don't hold up | Feasibility gets tested before commitment, not after | First-principles elimination reasoning | File-evidenced, specific, not covered elsewhere |
| D13 | Builds a reference/documentation base before designing anything | Upstream-mapping happens by default, unprompted | — (directly observed) | File-evidenced *and* independently self-articulated as a stated principle |
| D14 | Regularly asks, unprompted, whether something important has been missed | The clearest, most repeated signal in the whole project | — (directly observed across contexts) | Strongest evidence of any item — self-report plus repeated, independently-arising confirmation across separate contexts |
| D15 | States or treats something as working before it's confirmed | A real gap between "I think" and "I've checked" | — (directly observed) | File-evidenced, specific, actionable |
| D16 | Logistics/communication needs get attention later than technical ones | A real blind spot, not hypothetical | — (directly observed) | File-evidenced, specific, actionable |
| D17 | Architecture gets designed at full ambition; execution gets scoped down pragmatically later | Possibly a deliberate staging strategy, not necessarily a flaw | — (directly observed) | File-evidenced; kept neutral pending more instances |
| D18 | A current project explicitly carries forward and refines a prior one | Projects treated as continuing work, not disposable | — (directly observed) | File-evidenced; also grounds G3 |
| D20 | Output quality held up under real sleep deprivation, wrong information, travel fatigue | A positive data point on stress-resilience | — (directly observed) | File-evidenced, single instance |
| D21 | Acute distress surfaced once, under a specific compound condition (high effort, high stakes, irreversible loss, narrow margin) | A documented context, not a trait | — (directly observed) | Real, serious, must be handled with singular care |

*(D2 stays vocabulary-only. D10 stays folded into the stopping-support policy. D19 no longer appears — see Goals.)*

**Process position — cross-cutting, not a nineteenth target.** Several targets above are policy-mapped specifically because of *when* in a reasoning arc they occur, not just *that* they occur — D4's policy is explicitly about identifying load-bearing decisions *early*, and P3's own interruption design (2F) was built around interrupting *before* a specific phase begins, tracing directly to the original interview's answer about timing. Every finding, for every Model target, should also record where within the person's reasoning arc it occurred — in observable terms, never fitted to a predetermined stage template, with "not phase-linked" and "insufficient evidence to place" as valid values. This is a property attached to *evidence entries*, not a new target to search for on its own — the same way the category-space artifact and engineering design both already treat it.

### 1D. Interaction Hypotheses (candidates)

- **IH-candidate 1:** D7 (maximizer) × D13 (document-infrastructure) → large upfront research investment before committing to execution.
- **IH-candidate 2:** D12 and D13 may not be two independent traits at all — both could be downstream of one shared disposition ("map exhaustively before committing").
- **IH-candidate 3 (yours):** curiosity × verification lag → more exploration, less verification. Can't yet be evaluated — D9 isn't itself confirmed.

### 1E. Policy — Candidates

P1–P9 carry over from earlier, each needing an explicit answer to "which goal does this serve." **P10 is new as of v4**, added because that triage exposed a goal (G3) with nothing serving it.

### 1F. Process Policies (candidates)

- **An update policy** — how an observation becomes a hypothesis, and a hypothesis earns promotion to "stable."
- **A contradiction policy** — what happens when new evidence disagrees with what's already established.

---

## Part 2 — Triage & Decision Log

### 2A. Goals — finalized

G1–G6 confirmed. D19 is retired as a standalone Model item, not silently dropped — its two halves do different jobs and earned separate goal status.

### 2B. Model Targets — finalized, tiered

**The criterion:** an item earns active status only if it already has a stated, live consequence — a policy it runs, or a goal it grounds. A different axis from how much evidence exists.

That status splits into **three tiers**, because "the consequence runs conditionally" was quietly doing two different jobs under one name:

- **Established** — the linked policy runs proactively, by default, without needing anything detected first.
- **Gated — Conditional Trigger** — the behavior itself is context-dependent, so its policy fires only once that specific context is detected. Inactive by default.
- **Gated — Goal-Anchored** — the trait sits at insufficient data, but the goal it grounds is independently justified, and its policy runs as standing behavior regardless. Not waiting for a trigger — held back from Established only by honesty about the unconfirmed trait.
- **Conditional** — no live consequence attached at all.

D17 never had a policy attached — one was withheld on purpose, since the behavior could be a staging strategy or a flaw. D18 grounds G3, live from day one, on the same evidentiary footing as D17 — what separated them was never evidence strength, only whether a consequence was attached. D3, D15, and D16 are conditional in the trigger sense: each fires only in the specific context its evidence came from. D18 isn't conditional that way — G3's compound-work behavior is relevant to essentially any new project, so it shouldn't wait for a trigger the other three should.

**Established** — temporal tag supports confidence; consequence runs proactively

| # | Temporal tag | Linkage | Reasoning |
|---|--------------|---------|-----------|
| D4 | Leans stable | Policy-mapped | Help identify load-bearing decisions early — the fast-decide pattern works when that's right, misfires when it isn't |
| D7 | Leans stable | Policy-mapped | Occasionally offer a diminishing-returns estimate rather than only ever suggesting more |
| D8 | Leans stable | Policy-mapped | Track the person's own stopping signal; default toward encouraging continued search given humans' documented tendency to under-search |
| D11 | Leans stable | Policy-mapped | Preserve hierarchical structure already established rather than silently flattening it |
| D12 | Leans stable, one instance | Policy-mapped | Default to surfacing why an obvious approach might fail before endorsing it — see IH-candidate 2 |
| D13 | Leans stable — nearly as confirmed as D14 | Goal-grounding (G1) + policy-mapped | Support and extend the mapping rather than skip ahead — see IH-candidates 1 and 2 |
| D14 | **Stable** — the one item confident enough for this outright | Goal-grounding (G2) + policy-mapped (P3/P4) | The entire interruption/hint design exists to serve this exact demonstrated need |

**Gated — Conditional Trigger** — consequence is live, but fires only once its specific context is detected

| # | Temporal tag | Linkage | Reasoning |
|---|--------------|---------|-----------|
| D3 | Leans context-dependent (one instance, under deadline pressure) | Policy-mapped | Push back more assertively in domains showing demonstrated overconfidence — fires only once that pattern is detected |
| D15 | Context-dependent (one instance, under acute time pressure) | Policy-mapped | Encourage explicit verification before irreversible decisions — most load-bearing specifically under time pressure |
| D16 | Context-dependent leaning stable | Policy-mapped | Proactively surface logistics/communication items early |

**Gated — Goal-Anchored** — trait unconfirmed, but the goal it grounds runs as standing behavior regardless

| # | Temporal tag | Linkage | Reasoning |
|---|--------------|---------|-----------|
| D18 | Insufficient data on the trait itself | Goal-grounding (G3) + policy-mapped (P10) | The trait claim about the person stays unconfirmed until a second instance turns up, but the behavior it justifies doesn't wait for that |

**Conditional** — no live consequence yet

| # | Temporal tag | Reasoning |
|---|--------------|-----------|
| D1 | Insufficient data | Theoretical only |
| D5 | Insufficient data | Plausible, unconfirmed |
| D6 | Insufficient data | Plausible, unconfirmed |
| D9 | Insufficient data | Real concept, no instance yet |
| D17 | Insufficient data | No policy attached on purpose |
| D20 | Insufficient data | Real, but one hackathon isn't a pattern |

**Special case, not bucketed at all**

| # | Note |
|---|------|
| D21 | Doesn't fit this classification the way a reasoning pattern does. Governed directly by G4 + P9. Never generalized from n=1. |

**Process position, finalized.** Confirmed as a cross-cutting requirement rather than a new tiered target — every evidence entry for every Model target, regardless of tier, should also record where in the person's reasoning arc it occurred, in the same observable, non-imposed terms 1C describes. This governs how D4 and P3 already operate; it was implicit before, and is explicit now.

### 2C. Interaction Hypotheses — finalized

- **IH1 (D7×D13) — accepted**, moderate confidence.
- **IH2 (D12/D13 redundancy) — accepted as a standing question, not a behavioral prediction.** Test: watch for either appearing without the other.
- **IH3 (curiosity × verification lag) — held, not accepted.** Revisit once D9 clears "insufficient data" on its own.

### 2D. Update Policy — finalized

1. **Observation** — a specific instance appears in a transcript.
2. **Hypothesis** — proposed and explicitly tagged as such, never asserted as established.
3. **Evidence accumulation** — further transcripts checked for corroborating or conflicting instances.
4. **Confidence update** — each new instance moves confidence up or down, weighted by how clear that instance is.
5. **Promotion to "stable"** requires (a) at least two independent contexts and (b) no unresolved contradiction not already explained by a context-dependent branch. An independent context is a different project, or a different evidentiary mode arising without reference to the other. D14 and D13 clear the bar because the self-report and the file behavior arose independently, not because either was repeated enough within one project.

### 2E. Contradiction Policy — finalized

1. **Check for a moderating condition first.** If found, resolves into a context-dependent branch, both kept.
2. **If none turns up, don't average.** Hold at reduced confidence, flagged as mixed.
3. **Weight by original confidence, not raw count.**
4. **Keep "the person changed" separate from "this varies by context."** Genuine change updates forward.

### 2F. Policy Layer — finalized, tied to Goals

**Non-negotiable**
- P1 (confidence-tagging / observation-inference separation) — serves G5
- P2 (falsifiability statement) — serves G5
- P9 (care-override) — serves G4; sits above every other trade, full stop

**Strong default, revisable against real reactions**
- P3 (interruption rule: cue only when redirect-value exceeds disruption-cost) — serves G2, constrained by G6
- P4 (minimal-hint default) — serves G2 and G6 jointly
- P5 (stopping-support rule, folding in D10) — serves G1 and G2
- P6 (steer, don't seize) — serves G6 directly
- P7 (heuristics as adaptation, not defect) — serves G6 and G1 together
- P8 (elicit before importing external labels) — serves G1
- **P10 (project-continuity scan) — serves G3.** When starting or substantially extending work on a new problem, check whether it connects to, extends, or could reuse structure from previously discussed work. This check runs unconditionally — that's what earns it Goal-Anchored rather than Conditional Trigger status. Its *surfacing* is not exempt on that account: finding a connection supplies a candidate, it doesn't override P3's cost-benefit gate or P4's minimal-hint default. The check always runs; whether and how it gets raised still follows the same discipline as everything else.

### 2G. Scope, and the ingestion path — resolved

One-time system. No persistent update loop, no live memory dependency. The eventual operational extract should encode evidence tag, temporal tag, tier, confidence, and promotion status as structured fields, not prose.

*(This section is the deliberate exception to the portability rule above — it's about running one extraction through one specific tool, not part of what that extraction produces.)*

**The numbers, as currently confirmed.** Fable 5's context window is 1M tokens, with a 128k-token output ceiling per request. Extended thinking carried between turns counts toward that same budget, and prior turns' thinking blocks are kept in context by default on Fable 5 rather than stripped. The tokenizer runs roughly 30% less space-efficient than earlier models, which is the actual reason nine source files at roughly 3.35MB land close to the ceiling. Separate analysis of Fable 5 running inside Claude Code puts the practically usable window closer to 830K tokens once compaction buffers and usage thresholds are accounted for — meaningfully below the nominal 1M, if that holds outside Claude Code too.

**One caveat worth stating rather than assuming away.** These figures are confirmed for API access. The delivery-research backing this project does not find an explicit, separate confirmation of Fable 5's context window as exposed through Claude.ai's consumer chat interface specifically — which is where this extraction is actually planned to run, given the plan to switch models mid-conversation rather than call the API directly. Confirm the actual window in the model selector before finalizing the batch-size plan; if the consumer-facing window differs from 1M, the batching arithmetic in this section needs re-deriving, not just re-checking.

**Path A — fresh requests, model carried forward, text discarded.** Each file gets its own request. The only thing carried into the next request is the current state of the structured model — never the raw prior file text, prior turns, or prior thinking. One detail worth making explicit rather than assumed: "fresh request" means the master prompt itself — the methodology, not just the accumulated findings — has to be present in every one of the nine requests, not only the first. What travels forward file-to-file is the structured model state; what gets re-supplied from scratch every time is the instructions for how to build it. Both are present at every request; only one of them changes. The master prompt needs an explicit instruction to end each file's processing with a clean, structured snapshot built for exactly this handoff.

**Path B — one continuous session.** All nine files processed in a single ongoing conversation. Simpler to run, but riskier: prior turns and their thinking stay in context by default on Fable 5, so usage keeps climbing across all nine files. Native compaction could manage this automatically, but it's currently in beta and not guaranteed to trigger reliably enough to bet a rigorous report on without checking.

**Recommendation:** Path A, regardless of surface. It removes the risk rather than managing it. Which interface this runs on changes how Path A gets executed, not whether it's the right call.

---

## What This Leaves Us With

6 goals (3 person-specific, 3 universal). 19 model items total: 7 Established, 3 Gated (Conditional Trigger), 1 Gated (Goal-Anchored), 6 Conditional, 1 vocabulary-only, 1 special case never bucketed. D14 is the only item confident enough to call outright stable; D13 nearly there, both with a stated reason why. Two accepted interaction hypotheses, one correctly held back. A five-step update policy and a four-part contradiction policy. Policy layer: 3 non-negotiable, 7 strong-default, one of which (P10) now explicitly routes through two others rather than acting as its own exempt channel. Process position is now an explicit, cross-cutting requirement rather than an implicit assumption buried inside D4 and P3's own wording. Ingestion is a resolved two-path decision with a stated recommendation, with an explicit caveat that the underlying context-window figures need confirming on whichever surface this actually runs on. And the whole thing is now explicitly stated to be portable — built to describe the person, usable by whatever model eventually reads it, with exactly one section that's allowed to name the tool currently doing the extraction.

Ready for the master prompt — Path A, sequential, structured handoffs between files, written for whatever LLM ends up running it.
