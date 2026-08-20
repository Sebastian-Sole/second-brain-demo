# Mission

Sebastian is presenting this vault as a harness that genuinely learns its user, positioned against
Claude Desktop and ChatGPT memory, at a workshop. The meeting on 2026-08-20 concluded the demo stays
the Morning Digest but must show what the harness gives beyond out-of-the-box: persistent notes,
feedback loops, own infrastructure, portability across models.

**The learning goal is decision-shaped, not survey-shaped.** He is not learning hooks in general. He
is landing three specific design decisions well enough to build them and defend them on stage:

1. A `SessionStart` hook, so "it knows you" is a harness guarantee rather than a model habit.
2. A friction log, so corrections are observed instead of evaporating at end of session.
7. A home for declined proposals, so signal survives a "not now" without becoming nagging.

Decisions 5 and 6 (assumptions about the working relationship; a spoke for how they want to work
with an AI) are already accepted and need no teaching.

**What good looks like:** each decision has a stated mechanism, a named cost, and a reason it cannot
live anywhere else. If a decision cannot survive the question "why not just put that in a note", it
is not landed.

**Constraint that shapes every answer:** the vault is model-agnostic by design. A hook may only
re-state what a note already holds (AGENTS.md:88). Anything that makes Claude Code the only place a
fact lives breaks the pitch.

Reviewed: 2026-08-20.
