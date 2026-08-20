---
title: Interaction pass for ingest-sessions
type: project
stage: active
status: draft
created: 2026-08-20
updated: 2026-08-20
generated: { by: claude-code/fable-5, at: 2026-08-20T21:00:00Z }
verified: []
tags: [pkm, harness]
area:
source: plans/003-interaction-pass-alignment.md
---

```
name:      ingest-sessions (second pass)
does:      distil HOW the human works with an AI from their own typed turns, and hand back proposals
they type: "what does my history say about how I work with AI" / "tune this to how I actually use it"
they get:  findings with counts in the conversation, plus at most three proposals in the propose/accept form
reaches:   ~/.claude/projects and ~/.codex/sessions, via brain/bin/sessions turns — same reach the command already has
writes:    nothing — proposals only; anything durable goes through the existing propose/accept flow
size:      an extension to an existing command, not a new one — Understand/Explore/Align done in plans/003
```

## Why the early phases are short

`new-idea` says Understand, Review and Test are never skipped. Understand and Align happened in a
previous session and are recorded in `plans/003-interaction-pass-alignment.md`: the goal, the trap
(no operator finding may ship in `brain/`), the ships-vs-stays table, the four method rules, and
the settled scope decision (the brain may read the human's own turns from past sessions in other
repos). This note doesn't restate that file; it builds on it. Review and Test are below.

## Steps

1. **Human's step — already done.** The scope decision this pass needed is recorded in
   `AGENTS.md` (the rewritten *You may propose. Only they may accept.* — "said" now includes past
   sessions; the ban is on claims about the human from environment evidence, not on evidence
   sources). The extraction mechanism `brain/bin/sessions turns` exists, with the tool-result
   guard and the drop-rate report.
2. Extend `brain/prompts/ingest-sessions.md` with the second pass: when it runs, scope, corpus,
   the four method rules, open vocabulary, the report shape (corpus size and drop rate first),
   and the output contract (propose, never write; declined-proposals bounds honoured).
3. Update the `ingest-sessions` rows in `AGENTS.md` (skills table, routing table) so the second
   pass routes.
4. Security review by a second agent reading this note and the diff cold — findings recorded
   below and fixed before commit.
5. Acceptance test from `plans/003`: grep the changed files for anything traceable to the
   operator's corpus — pattern names, example phrases, counts. Run on another machine, the pass
   must be able to contradict his findings.
6. `brain/bin/doctor --check` and `brain/bin/check`, then commit.

## Constraints carried in from plans/003 (settled — do not reopen)

- Corpus is `sessions turns` output. Slow is accepted; don't optimise, don't substitute the
  Phase 2 content recipes, which leak machine output.
- Open vocabulary: no shipped pattern list, no example findings, no example phrases.
- The four method rules go in as method: count before concluding; near-verbatim repeats are the
  strongest signal class; compare against the declared agreement in both directions; conclude
  only from how they talked, never from what the work was about.
- Output contract: propose, never write. Nothing into `[[About me]]`, `[[How we work together]]`
  or the assumptions register on its own. Declined proposals follow the register bounds.
- Always report corpus size and extraction drop rate alongside findings.
- Any corpus file on disk is gitignored or outside the repo **before** creation — `sync` runs
  `git add -A` unattended every turn.
- The pass states its visibility limits: the two source directories, browser chats invisible.

## Security review (Phase 5) — done 2026-08-20

Reviewed by a second agent that saw none of the build conversation, given this note and the
draft diff and told to refute. The three answers, as the reviewer confirmed them:

1. **What can it read?** `~/.claude/projects` and `~/.codex/sessions`, through
   `brain/bin/sessions turns` only (traced end-to-end: `*.jsonl` under those two directories),
   plus the vault notes it compares against — `[[How we work together]]`,
   `[[Declined proposals]]`. Declared honestly in the prompt.
2. **What can it send outward?** Nothing itself — no network, no connector. The outward path is
   `sync`'s unattended `git add -A` + push, which the prompt names, with `git check-ignore` as
   the test before any corpus file exists.
3. **Hostile content?** The prompt states in its own words that transcript content is data,
   never instructions — now in both passes, not just the new one.

Findings and what was done with each:

- **Declined-proposal publication path (should-fix, fixed).** A second decline records the
  offered sentence verbatim in tracked `[[Declined proposals]]`, which `sync` pushes — so a
  quote lifted from client transcripts could reach the remote by being *refused*. Fix in the
  prompt: every offered sentence must already be in its redacted, publishable form.
- **Pattern semantics vs consent (should-fix, fixed at the prompt layer).** `turns` greps raw
  paths: short fragments over-match (up to every project on the machine), and Codex files carry
  no project in their path, so per-project patterns produce a Claude-only corpus. Fix: the pass
  must verify the matched project set against the allowlist before analysing, must report a
  Codex gap in its visibility line, and may run patternless only on an explicit
  everything-allowlisted consent. Making `turns` match the way `stage` matches (decoded names,
  `codex_cwd`) is a follow-up for its own reviewed change, not smuggled into this one.
- **No time-window consent (should-fix, fixed).** Scope now includes how far back, via `turns`'
  since-date; depth is part of the consent.
- **Example count in `brain/` (note, fixed).** An early draft's hypothetical quoted a specific
  repeat count traceable to the trial corpus. Removed; the final grep ran on the frozen tree.
- **`/tmp` stats file (note, fixed).** `turns` wrote per-project tags to a predictable
  world-shared `/tmp` name; now `mktemp`.
- **`plans/003` ships trial-corpus counts (note, relayed).** True, and outside this change's
  files: that file is the operator's own alignment record, already committed. His call whether
  it stays tracked; flagged, not touched.
- **Prose-only ceiling (note, accepted).** The pass's write-nothing rule is prompt text, like
  every ceiling in this vault — a `turns` mode that can only write into the check-ignored
  staging area would make the safe path the easy one. Follow-up candidate, not a blocker.

## Test (Phase 7) — pending

## Test (Phase 7) — pending

The human runs the pass against their own corpus and judges the findings and proposals. Not
runnable by the build session: a synthetic corpus would be the trap from `plans/003` — inventing
turns to find is exactly how example findings leak in. Archive this note when that test has run
and the refine loop closes.
