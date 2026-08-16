# Design notes

Why this vault is built the way it is. **You don't need any of this to use it** — [`README.md`](README.md)
is the manual, [`AGENTS.md`](AGENTS.md) is what the agent reads. This file is for the person
deciding whether to adopt the design, or about to change it.

---

## How it stays model-agnostic

This is the part worth stealing even if you never use the rest.

Every agent has its own dialect — `CLAUDE.md`, `.cursorrules`, proprietary command formats, hook
configs. Write your system in one of those and you've married that vendor. So: **the substance
lives in a portable core, and each tool gets a thin adapter.**

```
AGENTS.md          the operating manual — read natively by 20+ agents
CLAUDE.md          three lines: "read AGENTS.md". No instructions of its own.
GEMINI.md          same three lines, because Gemini only opts in to AGENTS.md

brain/prompts/     the commands, as plain markdown. Any agent can read them.
brain/bin/sync     commit + push, in POSIX shell. Callable by a hook, cron, CI, or you.
brain/bin/run      runs a prompt with whichever agent CLI is installed.
brain/bin/doctor   checks the install and says what to fix, in plain language.
brain/bin/sessions finds and stages AI transcripts that agents can't reach themselves.

.claude/commands/  six-line wrappers pointing at brain/prompts/
.claude/settings.json  a hook that calls brain/bin/sync, plus a read-only permission allowlist
```

Teaching the vault a new agent means adding **one case** to `brain/bin/run` and one pointer file.
Nothing else changes. Delete the whole `.claude/` directory and the vault still works.

The seams aren't perfectly symmetrical, and pretending otherwise would be a lie: Claude Code has a
`Stop` hook, so it commits after every turn on its own. Codex, Cursor and Gemini have no equivalent,
so with those you run `brain/bin/sync` yourself — `AGENTS.md` tells them to. Codex also loads custom
prompts only from `~/.codex/prompts`, not from the repo, so its slash commands are per-machine
rather than per-vault. The portable layer is genuinely portable; the conveniences on top vary by
what each vendor gives you to hook into.

The same rule applies to automation: `brain/bin/sync` is a shell script, not a hook, so a hook, a
cron job, and a CI workflow can all call the identical code path.

### Where the thesis actually breaks: Cowork

Every adapter above is thin because every one of those agents reads instructions *from the folder*.
Claude Cowork doesn't. Its standing context is per-project **Instructions** stored in Cowork's own
metadata — not in the repo, not in git, not shareable, and deleted when the project is archived.
It also ignores the repo's `.claude/` directory, so the auto-commit hook never fires.

That is the vendor-metadata failure this document argues against, arriving on the surface with the
least technical audience.

**An adapter was built and then deleted, which is the more useful story.** Cowork supports plugins,
plugins are file-based and installable straight from a git repo, and the six commands ported over
cleanly as thin wrappers — the same shape as `.claude/commands/`. That part worked. What didn't:

- **Plugins have no always-on component.** The operating manual would ride on a skill that fires
  when its description looks relevant, not on every session. The reliable alternative is pasting a
  pointer into project Instructions, which is the unversioned vendor metadata this whole document
  argues against.
- **No auto-commit.** Whether a Cowork plugin hook can run `brain/bin/sync` against a local folder
  isn't answerable from Anthropic's docs, which describe Cowork both as working directly on your
  computer and as running in an isolated VM that writes to your filesystem.

So the honest statement is: **the commands are portable to Cowork; the operating manual is not.**
That's half a seam — and half a seam, on the surface whose users are least equipped to notice when
the manual didn't load and nothing got committed, is worse than an honest "not supported here."

The generalisable lesson is the one worth keeping: **this design travels exactly as far as the
convention that an agent reads its instructions from the folder it's working in.** Every agent that
honours it costs one pointer file and one `run` case. The first agent that doesn't costs the whole
thesis, and no amount of adapter cleverness buys it back — because what fails to port isn't the
commands, it's the manual that makes the commands mean anything.

---

## Why PARA, with a caveat

**PARA** (Projects / Areas / Resources / Archives) for the top level, plus atomic notes as the
thinking layer. PARA sorts by *how actionable something is right now*, not by subject, which is
why one vault can hold your work, your side projects and your life without becoming a filing
cabinet.

> **PARA is here because it's familiar, not because it's proven.** There are no controlled trials
> of PARA, Zettelkasten, LYT, ACCESS or Johnny Decimal — not mixed evidence, none at all. The
> widely-quoted "40% improvement" is self-reported confidence from paying customers with no control
> group. What *is* measured is much duller: shallow trees beat deep ones, and folders start paying
> for a split at around 21 items. So this layout is one reasonable answer, not the right one — and
> `type:` in frontmatter, not the folder, is what actually routes a note. Swap the folder map in
> `AGENTS.md` and every command still works.
>
> The genuinely evidence-backed part of this repo is `digest` and `maintain` — the review loop.
> The robust finding in the note-taking literature is that *revisiting* notes helps; how you filed
> them doesn't.

Two deliberate omissions:

- **No pre-built Maps of Content.** A hub note earns its place once ~5 related notes are genuinely
  hard to navigate. Shipping empty ones is organisational debt.
- **No pre-made Area or Project notes.** They should appear when you have an area or a project.

### `index.md` and retrieval

`index.md` is the piece that makes retrieval work without an embedding index: the agent reads the
catalog to see what exists instead of guessing at search terms. It's updated on every capture and
fully regenerated by `maintain`.

The retrieval order in `AGENTS.md` exists because of a measured failure, not a theory: long raw
transcripts and append-only logs outrank short canonical notes on keyword match. So `raw/`,
`brain/log.md` and `06_Sessions/` are excluded from default search and read only when the question
is actually about them. Without that rule, a thousand session notes drown the few dozen real ones.

---

## Provenance, and why it's machine-queryable

The main failure mode of an AI-maintained vault is **slop** — generic, hedge-filled prose you stop
trusting, and gradually losing track of which thoughts were yours.

`AGENTS.md` carries explicit guardrails: capture *your* thinking rather than a neutral summary of
the topic, stay concrete, and mark anything the agent inferred with an **AI synthesis** callout so
authorship stays clear permanently. That last rule matters more than it looks — an inference that
gets mistaken for a fact will be cited as evidence for the next inference. The callout is a plain
GitHub alert, so it renders as a real callout on github.com rather than a grey blockquote, and
`grep -rn "AI synthesis"` lists every unverified inference in the vault.

Provenance is also structured, not just a prose convention. Every note carries:

```yaml
generated: { by: human:me, at: ... }   # or { by: claude-code/opus-5, at: ... }
verified: []                            # only a person may add themselves here
status: draft                           # draft | stable | deprecated  — trust
stage: inbox                            # inbox | active | evergreen | archived — workflow
```

So "show me everything the agent wrote that no human has confirmed" is a grep, not a vibe. The
field names follow Google Cloud's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md),
so this isn't a private invention.

`status` (trust) and `stage` (workflow) are separate on purpose — "I haven't processed this" and
"nobody has confirmed this is true" are different claims, and collapsing them is how an unverified
inference quietly becomes a fact.

---

## Why nothing runs on a schedule

Every command is invoked by you. This repo ships **no cron job, no CI workflow and no background
agent**, and that's on purpose. Handing an agent unattended write access to your notes before
you've watched what it does is how you stop trusting it in week two. Run `maintain` by hand a few
times. Read the diffs. `git revert` the ones you don't like.

Once you *do* trust it, scheduling is one line in whatever you already use — `launchd` or `cron`
locally, a GitHub Action, or your own runner:

```bash
0 3 * * * cd ~/my-brain && ./brain/bin/run maintain && ./brain/bin/sync
```

Two things that will bite you if you go the local route: a sleeping laptop runs nothing (`launchd`
catches up on wake, `cron` just misses), and a scheduled job gets a much emptier environment than
your terminal — set `HOME`, `USER` and `PATH` explicitly or your agent CLI will fail to
authenticate in a way that looks nothing like the real problem.

---

## Why not just a chat with memory turned on?

|  | This | A chat product with memory |
| --- | --- | --- |
| Where your data lives | Plain files you own, in your git repo | Inside someone's product, in their format |
| What it remembers | What you decide it remembers, including years of past sessions | What its memory feature happened to save |
| What it can do | Anything an agent CLI can — read files, run scripts, commit to git | Produce text |
| If it's wrong | `git revert` | Hope |
| When it runs | Whenever you run it — or on any schedule you set up | Only while you're typing |
| Vendor | Swap the agent; the vault doesn't notice | Migration means losing it |

Same model in both columns. The difference is entirely the harness around it.

---

## What it looks like once it's been used

A fresh clone is nearly empty, which makes it hard to picture the destination. After a couple of
months of ordinary use it looks roughly like this — no manual filing involved:

```
index.md                    ~60 lines, one per note, grouped
00_Inbox/                   2 items, both with Open question callouts
01_Projects/                Rewriting the billing importer.md
                            Learning Norwegian.md
02_Areas/                   Engineering practice.md
                            Health.md
03_Resources/               ~40 atomic notes — the actual knowledge
                            Retries need a budget, not just a count.md
                            Kaufmann — The Undoing Project.md
04_Archive/                 3 finished projects
06_Sessions/                ~200 distilled session notes + their own index.md
Daily/                      2026-06-14.md … 2026-08-14.md
raw/                        the originals of 12 articles and 3 transcripts
```

The shape to notice: `03_Resources/` is where the value accumulates, `01_Projects/` and
`02_Areas/` stay small, and `00_Inbox/` hovers near zero because `maintain` drains it. If your
inbox is growing, that's the signal to run `maintain` — not to reorganise the folders.
