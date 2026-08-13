# second-brain-demo

A personal second brain that an AI agent maintains for you — including while you're asleep.

It's a folder of markdown files. You dump things into it — a thought, a link, a decision you just
made, what you did today — and an agent files it, writes it up in your words, links it to what's
already there, and keeps the whole thing tidy. Later you ask it questions and it answers from your
own notes. Every night it tends the vault on its own.

No database. No SaaS. No proprietary format. **And no vendor lock-in** — it runs on Claude Code,
Codex, Cursor, Copilot, Aider, or whatever comes next, because nothing here is written in any one
tool's dialect.

---

## Setup (about five minutes)

**1. Get the repo.**

```bash
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
```

*(The `rm -rf .git` gives you your own history instead of this repo's. For backup, phone access,
and the nightly job, create an empty private repo on GitHub and
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

**5. (Optional) Open the folder in [Obsidian](https://obsidian.md)** to browse and see the graph.
It's just a viewer — the vault works fine without it.

---

## The four commands

| Command | What it does |
| --- | --- |
| `capture <anything>` | Files a raw dump — triages it, writes it up in your voice, links it to related notes, logs it to today's daily note |
| `ask <question>` | Answers from what's in your vault, with links to the notes it used |
| `digest [window]` | Rolls up recent activity: what happened, patterns across it, what's stalled |
| `maintain` | The nightly pass — close the day, drain the inbox, reconcile contradictions, link orphans |

In Claude Code these are slash commands (`/capture`). In any other agent, just say the word —
`AGENTS.md` tells it which prompt file to read. You don't have to use them at all: talking to the
agent in the folder works, because `AGENTS.md` says to treat what you say as a capture by default.

`digest` is the one that surprises people. It doesn't just summarise — it reads across unrelated
notes and names themes you never wrote down, including the things you keep avoiding.

---

## The nightly job

The vault maintains itself on a schedule. This is the difference between a notes folder and a
system, so it's set up out of the box.

**On GitHub** — `.github/workflows/nightly.yml` runs at 03:00 UTC. Two things to set:

1. A repository **variable** `BRAIN_AGENT` = `claude` or `codex` (defaults to `claude`).
2. The matching repository **secret**:
   - `claude` → `ANTHROPIC_API_KEY`, or `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`
   - `codex` → `OPENAI_API_KEY`

**Locally instead** — no GitHub, no secrets in the cloud:

```bash
# every night at 03:00, using whichever agent CLI you have installed
0 3 * * * cd ~/my-brain && ./brain/bin/run maintain && ./brain/bin/sync
```

Either way, `maintain` appends a line to `brain/log.md` so you can see what it did without
reading a single note.

> **Worth knowing:** GitHub runs scheduled workflows only from your default branch, and on public
> repos it disables the schedule after 60 days of no activity. A nightly commit counts as
> activity, so an active vault keeps itself alive.

---

## How it stays model-agnostic

This is the part worth stealing even if you never use the rest.

Every agent has its own dialect — `CLAUDE.md`, `.cursorrules`, proprietary command formats, hook
configs. Write your system in one of those and you've married that vendor. So: **the substance
lives in a portable core, and each tool gets a thin adapter.**

```
AGENTS.md          the operating manual — read natively by 20+ agents
CLAUDE.md          three lines: "read AGENTS.md". No instructions of its own.

brain/prompts/     the commands, as plain markdown. Any agent can read them.
brain/bin/sync     commit + push, in POSIX shell. Callable by a hook, cron, CI, or you.
brain/bin/run      runs a prompt with whichever agent CLI is installed.

.claude/commands/  four-line wrappers pointing at brain/prompts/
.claude/settings.json  a hook that calls brain/bin/sync
```

Teaching the vault a new agent means adding **one case** to `brain/bin/run` and one pointer file.
Nothing else changes. Delete the whole `.claude/` directory and the vault still works.

The same rule applies to automation: `brain/bin/sync` is a shell script, not a hook, so a hook, a
cron job, and a CI workflow can all call the identical code path.

---

## How it's organised

```
00_Inbox/        anything unprocessed or ambiguous
01_Projects/     active efforts with a goal and an end
02_Areas/        ongoing responsibilities with no end date
03_Resources/    atomic notes — the actual knowledge
04_Archive/      finished and dormant things
05_Attachments/  images, PDFs, binaries
Daily/           daily notes: journal + capture log
raw/             immutable originals of anything external
brain/           the harness: prompts, scripts, run log
```

**PARA** (Projects / Areas / Resources / Archives) for the top level, plus atomic notes as the
thinking layer. PARA sorts by *how actionable something is right now*, not by subject, which is
why one vault can hold your work, your side projects and your life without becoming a filing
cabinet.

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
| When it works | Every night, on a schedule | Only while you're typing |
| What it can do | Anything an agent CLI can — read files, run scripts, commit to git | Produce text |
| If it's wrong | `git revert` | Hope |
| Vendor | Swap the agent; the vault doesn't notice | Migration means losing it |

Same model in both columns. The difference is entirely the harness around it.

---

## Where to take it next

1. **Write your own command.** Copy `brain/prompts/digest.md`, change it, add a row to the table in `AGENTS.md`. Fastest way to make the system yours.
2. **Connect something that already records you** — email, calendar, your codebase. Anything already written down somewhere a machine can reach is free context; everything else you have to type. Highest-leverage move available.
3. **Add more scheduled passes** — a morning brief, a weekly review. `nightly.yml` is the template.
4. **Put a real interface on it** — the vault is a git repo and the commands are plain prompts, so a Slack bot, a Telegram bot or a custom UI is a thin client that runs a prompt and commits the result.

---

## A note on AI-written notes

The main failure mode of an AI-maintained vault is **slop** — generic, hedge-filled prose you stop
trusting, and gradually losing track of which thoughts were yours.

`AGENTS.md` carries explicit guardrails: capture *your* thinking rather than a neutral summary of
the topic, stay concrete, and mark anything the agent inferred with a `> [!ai]` callout so
authorship stays clear permanently. That last rule matters more than it looks — an inference that
gets mistaken for a fact will be cited as evidence for the next inference.

Keep those rules. They're the difference between a second brain and a pile of AI text.

---

## License

MIT. Take it, change it, make it yours.
