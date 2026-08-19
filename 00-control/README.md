# ARTOS Control Layer

This directory governs how ARTOS is maintained. It is intentionally separate from project content so repository rules remain easy to find and are not confused with architecture or research claims.

## Control files

| File | Purpose |
|---|---|
| `repository-manifest.md` | What each ARTOS area contains and which evidence role it serves. |
| `file-placement-policy.md` | Where new conversations, research, decisions, code, tests, outputs, and continuity updates belong. |
| `continuity/working-continuity-state.md` | Durable state for resumption after context loss or session change. |

## Authority order

For resuming the project, use the continuity state and operational extract first, then the latest canonical architecture/lifecycle baselines, then the relevant review and project evidence. The original archive is preserved for provenance and should not be silently rewritten to match later interpretations.

## Change discipline

Every material change should identify its evidence state, preserve provenance, avoid duplicate canonical copies, and update the continuity record when it changes the project’s current state, decisions, assumptions, or next action. Generated files belong in a clearly labelled output or release location and must not replace their source artefacts.
