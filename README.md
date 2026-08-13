# second-brain-demo

A personal second brain that an AI agent maintains for you.

It's a folder of markdown files. You dump things into it — a thought, a link, a decision you just
made, what you did today — and Claude files it, writes it up in your words, links it to what's
already there, and keeps the whole thing tidy. Later you ask it questions, and it answers from
your own notes.

No database. No SaaS. No proprietary format. Your notes are plain text you own, and `git` is the
undo button for anything the AI does to them.

---

## Setup (about five minutes)

**1. Get the repo.**

```bash
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
```

*(The `rm -rf .git` bit gives you your own history instead of this repo's. If you want it backed
up and usable from your phone, create an empty private repo on GitHub and
`git remote add origin <your-url> && git push -u origin main`.)*

**2. Install [Claude Code](https://claude.com/claude-code)** if you don't have it, then start a
session in the folder:

```bash
claude
```

**3. Make it yours.** Open `CLAUDE.md` and fill in the **About the human** section at the top —
your name, what you do, what you're working on right now. Two minutes of work here changes
everything downstream, because it's loaded into every session.

**4. Dump something.**

```
/capture I keep rewriting the same auth boilerplate on every project. Worth extracting into a package?
```

Watch where it goes.

**5. (Optional) Open the folder in [Obsidian](https://obsidian.md)** if you want to browse and see
the graph. It's just a viewer — the vault works fine without it.

---

## The three commands

| Command | What it does |
| --- | --- |
| `/capture <anything>` | Files a raw dump — triages it, writes it up in your voice, links it to related notes, logs it to today's daily note |
| `/ask <question>` | Answers from what's in your vault, with links to the notes it used |
| `/digest [window]` | Rolls up recent activity: what happened, patterns across it, what's stalled |

You don't have to use `/capture` — just talking to Claude in the folder works, because `CLAUDE.md`
tells it to treat what you say as a capture by default.

`/digest` is the one that surprises people. It doesn't just summarise; it reads across unrelated
notes and names themes you never wrote down — including the things you keep avoiding.

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
```

This is **PARA** (Projects / Areas / Resources / Archives) for the top level, plus atomic notes as
the thinking layer — the structure most experienced vaults converge on. PARA sorts by *how
actionable something is right now*, not by subject, which is why one vault can hold your work,
your side projects, and your life without becoming a filing cabinet.

Two deliberate omissions, both of which matter:

- **No pre-built Maps of Content.** A hub note earns its existence once a cluster of ~5 related notes is genuinely hard to navigate. Shipping empty ones is organisational debt.
- **No pre-made Area or Project notes.** They should appear when you actually have an area or a project.

You mostly won't think about folders at all. That's the point — the structure is there for the
model to reason over, not for you to maintain.

---

## What's actually in here

| | |
| --- | --- |
| `CLAUDE.md` | The operating manual. Loaded into **every** session, so you configure behaviour once instead of re-explaining yourself. **This is the file to edit.** |
| `.claude/commands/*.md` | The three commands. Each is just a markdown file — a prompt you *maintain* instead of retyping. Add your own by writing another one. |
| `.claude/settings.json` | A `Stop` hook that commits after every turn (and pushes, if you've set a remote). This is code, not a prompt — it always runs. |

That last distinction is the most useful idea in the repo: **things that must always happen
shouldn't be prompts.** Put them in a hook.

---

## Why not just a chat with memory turned on?

|  | This | A chat product with memory |
| --- | --- | --- |
| Where your data lives | Plain files you own, in your git repo | Inside someone's product, in their format |
| When it works | Whenever you schedule it to | Only while you're typing |
| What it can do | Anything Claude Code can — read files, run scripts, commit to git, reach connected services | Produce text |
| If it's wrong | `git revert` | Hope |
| Vendor | Swap the model; the vault doesn't care | Migration means losing it |

Same model in both columns. The difference is entirely the harness around it.

---

## Where to take it next

This is the **barebones** version — everything here is meant to be understood in one sitting and
changed by you. Natural next steps, roughly in order of payoff:

1. **Write your own command.** Copy `digest.md`, change it, and you have a new one. This is the fastest way to make the system yours.
2. **Put the digest on a schedule** so it runs without you. Waking up to a rollup you didn't ask for is the moment this stops feeling like a notes app.
3. **Connect something that already records you** — email, calendar, your codebase. Anything already written down somewhere a machine can reach is free context; everything else you have to type. This is the highest-leverage move available.
4. **Add a maintenance pass** that runs nightly: close the day, reconcile notes that contradict each other, link up orphans.

---

## A note on AI-written notes

The main failure mode of an AI-maintained vault is **slop** — generic, hedge-filled prose you
stop trusting, and gradually losing track of which thoughts were yours.

`CLAUDE.md` carries explicit guardrails against this: capture *your* thinking rather than a
neutral summary of the topic, stay concrete and terse, and mark anything the model inferred with
a `> [!ai]` callout so authorship stays clear. Keep those rules. They're the difference between a
second brain and a pile of AI text.

---

## License

MIT. Take it, change it, make it yours.
