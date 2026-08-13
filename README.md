# second-brain-demo

A personal second brain that an AI agent maintains for you.

It's a folder of markdown files — that's the whole thing. You dump something into it — a thought, a
link, a decision you just made, what you did today — and an agent files it, writes it up in your
words, links it to what's already there, and keeps the whole thing tidy. Later you ask it questions
and it answers from your own notes. It can also read back through the AI coding sessions you've
already had and turn *those* into notes, so work you did six months ago becomes searchable.

No database. No SaaS. No proprietary format. No app you have to install. **And no vendor lock-in** —
it runs on Claude Code, Codex, Cursor, Copilot, Aider, or whatever comes next, because nothing here
is written in any one tool's dialect.

---

## Setup (about five minutes)

**1. Get the repo.**

```bash
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
```

*(The `rm -rf .git` gives you your own history instead of this repo's. For backup and phone access,
create an empty private repo on GitHub and
`git remote add origin <your-url> && git push -u origin main`.)*

**2. Start an agent** in the folder — `claude`, `codex`, or anything else that reads `AGENTS.md`.

**3. Make it yours.** Open `AGENTS.md` and fill in the **About the human** section at the top —
your name, what you do, what you're working on now. Two minutes here changes everything
downstream, because that file loads into every session.

**4. Dump something.**

```
capture I keep rewriting the same auth boilerplate on every project. Worth extracting into a package?
```

Watch where it goes.

**5. (Optional) Pick a viewer.** The vault is plain markdown in a git repo, so it needs none —
your agent is the primary interface and `github.com` renders it for free. If you want to browse and
click links, [Obsidian](https://obsidian.md) is the nicest option and reads this layout as-is;
Logseq, Foam and VS Code also understand `[[wikilinks]]`. Nothing here depends on any of them.

---

## The commands

| Command | What it does |
| --- | --- |
| `capture <anything>` | Files a raw dump — triages it, writes it up in your voice, links it to related notes, logs it to today's daily note |
| `ask <question>` | Answers from what's in your vault, with links to the notes it used |
| `digest [window]` | Rolls up recent activity: what happened, patterns across it, what's stalled |
| `maintain` | Health pass — close the day, drain the inbox, reconcile contradictions, link orphans, rebuild the index |
| `ingest-sessions` | Distils your past AI coding sessions into notes you can search |

In Claude Code these are slash commands (`/capture`). In any other agent, just say the word —
`AGENTS.md` tells it which prompt file to read. You don't have to use them at all: talking to the
agent in the folder works, because `AGENTS.md` says to treat what you say as a capture by default.

`digest` is the one that surprises people. It doesn't just summarise — it reads across unrelated
notes and names themes you never wrote down, including the things you keep avoiding.

---

## Your history, made searchable

This is the thing worth doing on day one, and the reason a fresh vault isn't empty.

Your agent CLIs have been recording every session you've ever had with them. Claude Code keeps
them in `~/.claude/projects/`, Codex in `~/.codex/sessions/`. On a machine that's seen a year of
work that's several gigabytes of your own decisions and reasoning, sitting in files you cannot
search. `ingest-sessions` reads them and writes a short note per session — what you were doing,
what you decided, what you learned — into `06_Sessions/`, wired into the rest of the vault.

Then `ask` can answer "why did we go with the queue instead of cron?" about a session from eight
months ago.

Three things it deliberately does:

- **It asks which projects to ingest, and the default is none.** Your history almost certainly
  contains client work and other people's confidential code, and a second brain is a git repo that
  gets pushed. You allowlist projects once; it remembers.
- **It never copies a transcript in.** Transcripts are gigabytes and vaults are megabytes — dumping
  them in would bury every real note. It writes notes *about* them and leaves them where they are.
- **It scans what it writes for secrets** before saving, because a faithful summary of an API key
  is still an API key.

> [!IMPORTANT]
> **Change one setting before you need this.** Claude Code deletes session transcripts older than
> **30 days**, at startup, by default. So the history you'd most want in six months is being thrown
> away right now, and once it's gone this command can't recover it. Set `cleanupPeriodDays` in
> `~/.claude/settings.json` to something long — `3650` is ten years — and then ingest at your
> leisure. Codex doesn't appear to prune, but don't rely on that.
>
> ```json
> { "cleanupPeriodDays": 3650 }
> ```

## Maintenance, and why nothing here runs on a schedule

`maintain` is the health pass: it closes out the day, drains the inbox, reconciles notes that
contradict each other, links up orphans, and rebuilds `index.md`. It appends one line to
`brain/log.md` so you can see what it did without reading a single note.

**You run it. This repo ships no cron job, no CI workflow and no background agent**, and that's on
purpose. Handing an agent unattended write access to your notes before you've watched what it does
is how you stop trusting it in week two. Run it by hand a few times. Read the diffs. `git revert`
the ones you don't like.

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
brain/bin/sessions finds and stages AI transcripts that agents can't reach themselves.

.claude/commands/  four-line wrappers pointing at brain/prompts/
.claude/settings.json  a hook that calls brain/bin/sync
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

---

## How it's organised

```
index.md         the catalog — what exists. The agent reads this first.
00_Inbox/        anything unprocessed or ambiguous
01_Projects/     active efforts with a goal and an end
02_Areas/        ongoing responsibilities with no end date
03_Resources/    atomic notes — the actual knowledge
04_Archive/      finished and dormant things
05_Attachments/  images, PDFs, binaries
06_Sessions/     distilled notes from past AI sessions (appears once you run ingest-sessions)
Daily/           daily notes: journal + capture log
raw/             immutable originals of anything external
brain/           the harness: prompts, scripts, run log
```

**PARA** (Projects / Areas / Resources / Archives) for the top level, plus atomic notes as the
thinking layer. PARA sorts by *how actionable something is right now*, not by subject, which is
why one vault can hold your work, your side projects and your life without becoming a filing
cabinet.

> **Honest note on the folders: PARA is here because it's familiar, not because it's proven.**
> There are no controlled trials of PARA, Zettelkasten, LYT, ACCESS or Johnny Decimal — not mixed
> evidence, none at all. The widely-quoted "40% improvement" is self-reported confidence from
> paying customers with no control group. What *is* measured is much duller: shallow trees beat
> deep ones, and folders start paying for a split at around 21 items. So this layout is one
> reasonable answer, not the right one — and `type:` in frontmatter, not the folder, is what
> actually routes a note. Swap the folder map in `AGENTS.md` and every command still works.
>
> The genuinely evidence-backed part of this repo is `digest` and `maintain` — the review loop.
> The robust finding in the note-taking literature is that *revisiting* notes helps; how you filed
> them doesn't.

`index.md` is the piece that makes retrieval work without an embedding index: the agent reads the
catalog to see what exists instead of guessing at search terms. It's updated on every capture and
fully regenerated by `maintain`.

Two deliberate omissions:

- **No pre-built Maps of Content.** A hub note earns its place once ~5 related notes are genuinely hard to navigate. Shipping empty ones is organisational debt.
- **No pre-made Area or Project notes.** They should appear when you have an area or a project.

You mostly won't think about folders. The structure is there for the agent to reason over, not for
you to maintain.

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

## Where to take it next

1. **Write your own command.** Copy `brain/prompts/digest.md`, change it, add a row to the table in `AGENTS.md`. Fastest way to make the system yours.
2. **Connect something that already records you** — email, calendar, your codebase. Anything already written down somewhere a machine can reach is free context; everything else you have to type. Highest-leverage move available.
3. **Schedule something, once you trust it** — `maintain` nightly, a morning brief, a weekly review. Whatever scheduler you already use.
4. **Put a real interface on it.** The vault exposes exactly two operations: *write a file into `00_Inbox/`*, and *run `brain/bin/run <prompt>`*. Every UI is a thin client over those two — a Slack bot, a Telegram bot, an iOS Shortcut, an email address. Reaching the vault from a desktop app like Claude Desktop means giving it filesystem access via MCP, or pointing a cloud agent at the repo and letting a "dump" be a commit.

---

## A note on AI-written notes

The main failure mode of an AI-maintained vault is **slop** — generic, hedge-filled prose you stop
trusting, and gradually losing track of which thoughts were yours.

`AGENTS.md` carries explicit guardrails: capture *your* thinking rather than a neutral summary of
the topic, stay concrete, and mark anything the agent inferred with an **AI synthesis** callout so
authorship stays clear permanently. That last rule matters more than it looks — an inference that
gets mistaken for a fact will be cited as evidence for the next inference. The callout is a plain
GitHub alert, so it renders as a real callout on github.com rather than a grey blockquote, and
`grep -rn "AI synthesis"` lists every unverified inference in the vault.

Provenance is also **machine-queryable**, not just a prose convention. Every note carries:

```yaml
generated: { by: human:me, at: ... }   # or { by: claude-code/opus-5, at: ... }
verified: []                            # only a person may add themselves here
status: draft                           # draft | stable | deprecated  — trust
stage: inbox                            # inbox | active | evergreen | archived — workflow
```

So "show me everything the agent wrote that no human has confirmed" is a grep, not a vibe. The
field names follow Google Cloud's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md),
so this isn't a private invention. Note that `status` (trust) and `stage` (workflow) are separate —
"I haven't processed this" and "nobody has confirmed this is true" are different claims, and
collapsing them is how an unverified inference quietly becomes a fact.

Keep those rules. They're the difference between a second brain and a pile of AI text.

---

## License

MIT. Take it, change it, make it yours.
