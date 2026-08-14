# second-brain-demo

A personal second brain that an AI agent maintains for you.

It's a folder of markdown files — that's the whole thing. You dump something into it — a thought, a
link, a decision you just made, what you did today — and an agent files it, writes it up in your
words, links it to what's already there, and keeps the whole thing tidy. Later you ask it questions
and it answers from your own notes. It can also read back through the AI coding sessions you've
already had and turn *those* into notes, so work you did six months ago becomes searchable.

Your notes stay plain files in your own git repo. No database, no SaaS, no proprietary format — and
no lock-in to any one AI vendor.

---

## Before you start

Three things, and the first two are the real cost:

| You need | Why | Roughly |
| --- | --- | --- |
| **An AI coding agent, installed** | It's the thing that does the work. [Claude Code](https://claude.com/claude-code) is the best-supported here; Codex, Cursor and Gemini CLI also work. | 5 min |
| **A paid plan for it** | These agents need a subscription or API billing. This vault doesn't add any cost of its own, but it can't run for free. | from ~$20/mo |
| **Git, and a terminal** | Git is your undo button — it's what makes an agent writing into your notes safe rather than alarming. On a Mac, `git` may already be there; if not, run `xcode-select --install`. | 5 min |

A GitHub account is optional but recommended — it's what backs the vault up and lets you read your
notes from your phone.

**You don't need to know git, or how to program.** You need to be willing to type a few commands
once. If something goes wrong later, `brain/bin/doctor` tells you what's broken in plain language.

---

## Setup

**1. Get your own copy.**

The easy way: click **[Use this template](https://github.com/Sebastian-Sole/second-brain-demo/generate)**
at the top of this repo to create your own private copy on GitHub, then clone it:

```bash
git clone https://github.com/<you>/<your-repo>.git my-brain
cd my-brain
```

<details>
<summary>No GitHub account? Do it locally instead.</summary>

```bash
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
```

That `rm -rf .git` deletes this repo's history so you start with your own. It doesn't touch your
notes. You can add a backup later with `git remote add origin <url> && git push -u origin main`.
</details>

**2. Check it works.**

```bash
./brain/bin/doctor
```

It'll tell you what's missing and exactly how to fix it. Fix anything marked `[XX]`.

**3. Start your agent** in that folder — type `claude`, or `codex`, or whatever you installed.

**4. Say `setup`.**

It asks you five questions about who you are and what you're working on, writes the answers into
`AGENTS.md`, and walks you through your first capture. **Don't skip this** — it's two minutes and
it's the difference between notes about you and notes about a generic person.

That's it. From here you just talk to it.

---

## The commands

| Command | What it does |
| --- | --- |
| `setup` | First run: checks the install, learns who you are, walks you through your first capture |
| `capture <anything>` | Files a raw dump — triages it, writes it up in your voice, links it to related notes, logs it to today's daily note |
| `ask <question>` | Answers from what's in your vault, with links to the notes it used |
| `digest [window]` | Rolls up recent activity: what happened, patterns across it, what's stalled |
| `maintain` | Health pass — close the day, drain the inbox, reconcile contradictions, link orphans, rebuild the index |
| `ingest-sessions` | Distils your past AI coding sessions into notes you can search |

In Claude Code these are slash commands (`/capture`). In any other agent, just say the word.

**You don't have to use them at all.** Talking to the agent in this folder counts as a capture —
`AGENTS.md` tells it to treat whatever you say that way by default.

`digest` is the one that surprises people. It doesn't just summarise — it reads across unrelated
notes and names themes you never wrote down, including the things you keep avoiding.

> **Tip for Claude Code:** you'll be asked to approve each file the agent writes. Once you've
> watched it a few times and trust it, press `shift+tab` to switch to accept-edits mode and it
> stops asking. Everything it does is still a git commit you can revert.

---

## Your history, made searchable

This is the thing worth doing on day one, and the reason a fresh vault isn't empty.

Your agent CLIs have been recording every session you've ever had with them — Claude Code in
`~/.claude/projects/`, Codex in `~/.codex/sessions/`. On a machine that's seen a year of work
that's several gigabytes of your own decisions and reasoning, sitting in files you cannot search.
`ingest-sessions` reads them and writes a short note per session — what you were doing, what you
decided, what you learned — into `06_Sessions/`, wired into the rest of the vault.

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
>
> `brain/bin/doctor` checks this for you and will nag until you fix it.

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

**You mostly won't think about this.** The structure is there for the agent to reason over, not for
you to maintain — it decides where things go, and `maintain` keeps it tidy. The layout is
[PARA](https://fortelabs.com/blog/para/) plus atomic notes; if you'd rather use something else,
change the folder map in `AGENTS.md` and every command keeps working.

Two example notes ship in `03_Resources/` so the vault isn't empty on day one. Delete them whenever
you like — nothing depends on them.

**Want to browse it visually?** You don't need to — your agent is the primary interface, and
github.com renders it for free. But [Obsidian](https://obsidian.md) reads this layout as-is and is
the nicest option. Logseq, Foam and VS Code also understand `[[wikilinks]]`.

---

## Maintenance

`maintain` is the health pass: it closes out the day, drains the inbox, reconciles notes that
contradict each other, links up orphans, and rebuilds `index.md`. It appends one line to
`brain/log.md` so you can see what it did without reading a single note.

**You run it.** This repo ships no cron job and no background agent on purpose — an agent with
unattended access to your notes, before you've watched what it does, is how you stop trusting it in
week two. Run it by hand a few times first. Scheduling it later is one line in whatever scheduler
you already use; see [`DESIGN.md`](DESIGN.md#why-nothing-runs-on-a-schedule).

---

## Where to take it next

1. **Write your own command.** Copy `brain/prompts/digest.md`, change it, add a row to the table in `AGENTS.md`. Fastest way to make the system yours.
2. **Connect something that already records you** — email, calendar, your codebase. Anything already written down somewhere a machine can reach is free context; everything else you have to type. Highest-leverage move available.
3. **Schedule something, once you trust it** — `maintain` nightly, a morning brief, a weekly review.
4. **Put a real interface on it.** The vault exposes exactly two operations: *write a file into `00_Inbox/`*, and *run `brain/bin/run <prompt>`*. Every UI is a thin client over those two — a Slack bot, a Telegram bot, an iOS Shortcut, an email address.

---

## Why it's built this way

The design decisions — how it stays vendor-neutral, why provenance is tracked the way it is, why
PARA comes with a caveat, and what the vault looks like after a few months of use — are in
[**`DESIGN.md`**](DESIGN.md). None of it is required reading.

The one rule worth knowing without reading that file: **anything the agent inferred rather than
heard from you gets marked as an AI synthesis, permanently.** That's what keeps a second brain from
turning into a pile of confident AI text you slowly stop trusting.

---

## License

MIT. Take it, change it, make it yours.
