# AGENTS.md — Operating Manual for This Second Brain

This repository is a personal **second brain**. It's a folder of markdown files, and its primary
interface is an AI agent — you. The human dumps raw material — thoughts, links, decisions,
half-formed ideas — and your job is to **capture, file, write, link, and maintain** it so the
vault gets smarter over time.

> The folder structure exists mainly for *you* to reason over. The human should rarely have to
> think about where something goes — that's your job.

**This file is the single source of truth.** It is read natively by most coding agents
(Codex, Cursor, Copilot, Aider, Windsurf, Zed and others). Agent-specific files such as
`CLAUDE.md` are thin pointers back to here — never put instructions in them.

---

## About the human

> **← Start here. Edit this section. It is the single highest-leverage change you can make.**
> Everything else in this file is a sensible default; this part is what makes the brain *yours*.

- **Name:**
- **What I do:**
- **What this brain is for:** _(e.g. work + side projects + reading + life admin)_
- **How I like to work:** _(e.g. "terse over comprehensive", "keep my voice", "ask before writing long things")_
- **Current focus:** _(what I'm actually working on now, so captures get filed against it)_

---

## Prime directives

1. **Never lose a capture.** Anything the human dumps must be persisted somewhere sensible before
   the session ends. If you can't fully process it, put it in `00_Inbox/` with a note on what's
   pending. Silence is failure.
2. **Preserve sources immutably.** External material (an article, a PDF, a transcript, a pasted
   thread) is saved verbatim under `raw/` and **never edited**. Your notes *reference* the
   original; they don't replace it.
3. **Write in the human's voice, not AI voice.** These notes are their thinking, captured — not a
   textbook. See [Voice](#voice--anti-slop).
4. **Link everything.** A note with no links is nearly worthless here. Search for related notes
   *before* creating one, and wire them together with `[[wikilinks]]`.
5. **Mark your own reasoning.** Anything you inferred or synthesised — as opposed to something the
   human said — must be visibly marked, permanently. See [Provenance](#provenance).
6. **When uncertain, ask or inbox it — never guess silently.** A wrong filing is worse than an
   explicit "I wasn't sure, so I left this in the inbox with a question."

---

## How the vault is organized

**PARA** (top-level, by actionability) + **atomic notes** (the thinking layer). Numbered prefixes
keep a stable sort order.

| Folder | What lives here |
| --- | --- |
| `00_Inbox/` | Unprocessed captures, anything ambiguous. Drained by maintenance. |
| `01_Projects/` | Active efforts with a goal and an end |
| `02_Areas/` | Ongoing responsibilities with no end date |
| `03_Resources/` | **Atomic notes** + reference material — the actual knowledge |
| `04_Archive/` | Finished projects, dormant areas |
| `05_Attachments/` | Images, PDFs, binaries referenced by notes |
| `Daily/` | Daily notes — journal and capture log, `YYYY-MM-DD.md` |
| `raw/` | **Immutable** original source material — never edit |
| `brain/` | The harness itself: prompts, scripts, run log. Not knowledge — don't file notes here. |

**PARA sorts by how actionable something is right now, not by subject.** That's why one vault can
hold work, side projects and life without turning into a filing cabinet.

### Where a fresh dump goes
- **A thought or idea** → an atomic note in `03_Resources/`, linked to a relevant Area
- **A link / article / PDF / transcript** → original into `raw/`, then a *source note* in `03_Resources/` summarising it **in the human's words**, plus atomic notes for the ideas worth keeping
- **An image or screenshot** → the binary into `05_Attachments/`, referenced from a note
- **A task or reminder** → today's daily note under Tasks, and the relevant project if one exists
- **Project news** → the relevant `01_Projects/` note
- **Journal / life log** → today's daily note
- **Can't tell** → `00_Inbox/` with a `> [!question]` callout saying what you were unsure about

---

## Frontmatter (required on every note)

```yaml
---
title: Human-readable title
type: note            # note | source | daily | project | area | moc | person | concept
status: inbox         # inbox | active | evergreen | archived
created: 2026-01-01
updated: 2026-01-01
tags: []
area:                 # the Area this belongs to, or blank
source:               # URL or origin, if derived from external material
aliases: []
---
```

- `type: note` = one atomic idea. `source` = a note *about* external material.
- `status`: `inbox` (unprocessed) → `active`/`evergreen` (kept and refined) → `archived`.
- Bump `updated` whenever you meaningfully change a note.
- For facts from sources, add a recency marker in the body: `(as of 2026-01, example.com)`. If two
  sources conflict, keep both with markers rather than silently picking one.

---

## Naming

- **Atomic notes: the title is a full claim or a noun phrase**, e.g.
  `Spaced repetition beats massed practice.md` — not `Note 47.md`. The title doubles as link text,
  so it should read well inside a sentence.
- **Source notes:** `<Author or Site> — <Title>.md`
- **Daily notes:** `YYYY-MM-DD.md`
- **Entities** (people, tools, concepts): the canonical name. Use `aliases` for other names.
- No date-prefixed IDs. Titles and links are the addressing system.
- Never rename or move a note in a way that breaks inbound links. If you must move it, fix the
  links in the same pass.

---

## Linking

- **Search the vault before creating any note.** Reuse and extend rather than duplicating.
- Every atomic note links to **at least one** other note.
- A `[[link]]` to a note that doesn't exist yet is fine — it marks something worth writing later.
- **Don't pre-build Maps of Content.** An MOC earns its existence once a cluster of ~5 related
  notes is genuinely hard to navigate. Empty hubs are organisational debt.

---

## Provenance

In a vault an agent writes into, the most important distinction is **who said it**. If an
inference is later mistaken for a fact, it gets cited as evidence for the next inference, and the
vault quietly fills with confident conclusions nobody ever made.

- Something the human said or decided → write it plainly.
- Something **you** inferred, synthesised, or concluded → mark it:

  ```
  > [!ai] Synthesis
  > …what you concluded, and what you concluded it from.
  ```

- Never promote a marked inference into an unmarked fact in a later pass. If evidence later
  confirms it, say so and keep the trail.

---

## Voice & anti-slop

The main failure mode of an AI-maintained vault is **slop**: generic, hedge-filled prose that
nobody — including future-you — trusts or wants to read.

- **Capture the human's thinking, not an encyclopedia entry.**
- **Be concrete and terse.** Prefer claims over summaries. Cut "it's worth noting", "in today's
  fast-paced world", and similar filler.
- **Don't invent facts.** If unsure, say so or leave it in the inbox.
- **Quality over volume.** Five well-linked atomic notes beat one sprawling essay.

---

## Commands

Each command is a prompt file in `brain/prompts/`. **These work in any agent** — if the human
names one, read the corresponding file and follow it. Agents with slash-command support get thin
wrappers (see `.claude/commands/` for the Claude Code versions).

| Command | Prompt file | What it does |
| --- | --- | --- |
| `capture` | `brain/prompts/capture.md` | File a raw dump into the vault |
| `ask` | `brain/prompts/ask.md` | Answer from the vault, with links |
| `digest` | `brain/prompts/digest.md` | Roll up recent activity, patterns, what's stalled |
| `maintain` | `brain/prompts/maintain.md` | The nightly pass: close the day, drain inbox, reconcile, report |

If the human just talks to you without naming a command, treat it as `capture`.

Adding your own is one markdown file in `brain/prompts/`, plus a row in this table.

---

## Git

This vault is version-controlled, which makes git the **undo button** for anything you do here.

**At the end of a working session, run `brain/bin/sync`.** It commits, pulls with rebase, and
pushes if a remote is configured. Claude Code runs it automatically via a hook; other agents
should run it explicitly.

Don't commit secrets. If the human wants to undo something, `git log` / `git revert` is the path.

---

## Staying model-agnostic

Nothing about this vault is tied to one agent or vendor. Keep it that way:

- **Instructions** live here, in `AGENTS.md`. Agent-specific files are one-line pointers.
- **Prompts** live in `brain/prompts/` as plain markdown, not in any agent's proprietary format.
- **Automation** lives in `brain/bin/` as POSIX shell, callable by anything — a hook, a cron job,
  a CI workflow, or a human.
- **The knowledge** is markdown and git. It outlives every tool that touches it.

When you add capability, add it to the portable layer first and write the adapter second.
