# 003 — Alignment: the interaction pass in `ingest-sessions`

Status: **ALIGNMENT ONLY. Do not implement from this file yet.**
Written 2026-08-20 to survive a context switch. Supersedes nothing.

## The one-line goal

`ingest-sessions` gains a second pass. Today it distils **what the human worked on**. It should
also distil **how the human works with an AI**, and hand back proposals for tuning this vault to
that person.

## The trap this plan exists to prevent

The method was proven by running it by hand against the operator's own corpus (287 transcripts,
1532 of his turns, 2026-06-29 onward). That run produced a table of recurring patterns and a
handful of specific findings about him.

**None of those findings may enter `brain/`.** Not as examples, not as a checklist, not as
"patterns to look for". If they do, every person who clones this repo is told they have the
operator's habits, and the command becomes a horoscope that confirms itself.

This is the same line the vault already draws elsewhere: `AGENTS.md` is harness and gets replaced
wholesale on update, while `About me` and `Assumptions.md` belong to the human and are never
shipped at those paths. Findings are the second kind.

### Acceptance test

Grep `brain/` after implementation. If any pattern name, example phrase, or finding traceable to
the operator's transcripts appears there, the implementation is wrong. Run on a different person's
machine, the pass must be able to produce findings that **contradict** his.

## What ships, and what never ships

| Ships in `brain/` | Stays on the human's machine |
| --- | --- |
| The extraction mechanism (`sessions turns`) | Any specific pattern found |
| The machine-chatter filter | Any count, any percentage |
| The method: count, compare, report | Any proposed agreement line |
| The output contract: propose, never write | Any assumption raised |

## The method, stated so it generalises

Open vocabulary is the requirement, not a preference. The pass reads the human's turns and reports
what actually recurs, **including things nobody predicted**. It must not carry a list of patterns
to hunt for.

Four method rules earned from the trial run. All four are about *how to look*, none is about *what
was found*:

1. **Count before concluding.** A pattern is a pattern when it appears across many sessions, not
   when it is memorable. Report turns and sessions, not adjectives.
2. **Near-verbatim repeats are the strongest signal class.** A sentence typed almost identically
   many times is a magic word the human already invented and never declared. Look for repetition
   of form, not of topic.
3. **Compare against the declared agreement.** The most useful output is the mismatch in both
   directions: rules in `[[How we work together]]` that never fire, and rules fired constantly that
   were never written down.
4. **Conclude only from how they talked, never from what the work was about.** Subject matter is
   the banned evidence class at `AGENTS.md:302`. This is also what keeps the pass safer than the
   content pass: it needs the human's own sentences and nothing else.

## Scope decision, already made

**Settled 2026-08-20:** the brain may read the human's own turns from past AI sessions in other
repos, in order to learn how they work with AI.

This is a widening of "something they *said*" at `AGENTS.md:159`, which today silently means "said
in this session". **`AGENTS.md` must say so out loud before the pass ships.** A record the human
knows about is memory; the same record kept quietly is the thing people are right to object to.

## Build state as of 2026-08-20

`brain/bin/sessions` has an uncommitted `turns` subcommand. It reads transcripts from the source
directories, emits only human-typed turns, and writes nothing anywhere. It runs and its filter
catches every machine category it names. **Two known defects, so it is not finished:**

- **Too slow.** The full corpus ran past two minutes. Fixable: one `awk` pass over all files
  rather than one invocation per file, and drop the per-file `date -r`.
- **It leaks tool results.** Pasted terminal output appears as if the human typed it. `awk` regex
  cannot reliably tell a `tool_result` block from a text block. **Open decision:** require `jq`
  and degrade with a plain sentence when it is missing, or stay pure POSIX and accept a lossy
  corpus.

The filter list is empirical, drawn from one machine, and therefore incomplete. The strings
themselves are Claude Code and Codex harness output, so they generalise, but a user with no
subagents never emits `<task-notification>` and a Codex-heavy user has different noise. Treat the
list as extensible and **always report the drop rate**, so an unfamiliar corpus shows up as a
strange number rather than as silent coverage.

## Open harness question this raised

`[[How we work together]]` ships with starter magic words. The trial run showed at least one
shipped default that never fired for its owner in seven weeks of real use. That is a finding about
him and stays with him, but it poses a general question worth answering in the design:

**Should shipped agreement defaults be marked provisional until the interaction pass confirms
them?** An unconfirmed default costs tokens on every prompt and teaches the human that writing
preferences down does not work.

## Decided elsewhere in the same session, recorded so it is not relitigated

- Suggestion 11 (tools all point outward) is **dropped**. It read a split by reach as a split by
  subject matter.
- Suggestions 5 and 6 (relationship assumptions; a spoke for how they work with AI) are accepted
  and need no design work. This pass is what fills them.
- `AGENTS.md` is not too long, it is uniform: 226 bold spans across 878 non-blank lines and no
  priority structure. The fix is stratification into a small always-read core plus spokes, which
  is the pattern the file already prescribes for `[[About me]]` and does not apply to itself.
  After the workshop.
- `AGENTS.md:48` and `:112` use "paid for" in two senses. One sentence. Not done.
