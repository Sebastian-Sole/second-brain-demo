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

Copy this repo, then cut it loose from its history so the notes you write are yours:

```bash
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
```

The `rm -rf .git` deletes *this repo's* history so you start with your own. It doesn't touch a
single note.

<details>
<summary>Want it backed up and readable from your phone? (recommended, 2 minutes)</summary>

Create an empty **private** repo on [github.com/new](https://github.com/new) — no README, no
`.gitignore` — then:

```bash
git remote add origin https://github.com/<you>/<your-repo>.git
git push -u origin main
```

Now every change is backed up, and github.com renders your notes on any device. `brain/bin/doctor`
warns you until this is set up, because a vault that exists on one laptop is one spilled coffee from
gone.
</details>

**2. Check it works.**

```bash
./brain/bin/doctor
```

It'll tell you what's missing and exactly how to fix it. Fix anything marked `[XX]`.

**3. Start your agent** in that folder — type `claude`, or `codex`, or whatever you installed.
Prefer not to use a terminal? See [Which app to use](#which-app-to-use) below.

Claude Code will ask whether you trust this folder the first time. **Say yes** — until you do, it
ignores the settings that ship with this repo and will pester you for permission on routine things.

**4. Say `setup`.**

It asks one question at a time — what you use AI for now, what annoys you about it, where that
problem actually lives — and each question follows from your last answer instead of marching through
a list. Then it connects what can be connected and **builds you one thing that works before you're
finished**, aimed at whatever you said was annoying, and runs it in front of you. **Don't skip
this** — it's the difference between notes about you and notes about a generic person, and it's the
part where you find out what this is actually for.

**5. If you're not sure what you've just installed, say `teach me how this works`.**

It explains what this actually is — the agent, the harness around it, and the vault — pitched at
wherever you are, from never-having-used-AI upward. It teaches it a piece at a time, each ending
with something real happening rather than a summary, and it can turn the whole thing into a lesson
you keep. It's the same command you'd use to learn anything else; this repo just happens to be a
subject it has the documents for.

That's it. From here you just talk to it.

---

## Using it

Everything day-to-day is in [**`GUIDE.md`**](GUIDE.md) — that's the file to read once you're
installed. The summary:

**Talk to it in plain sentences.** You don't have to learn any commands; it works out what you meant
and does that, silently. Anything that wrote something ends with one line naming what it made, so a
wrong guess is visible and one sentence to correct.

If you'd rather name a command, there are about twenty, in two kinds — **skills**, which touch only
the vault and work in every agent as shipped, and **tools**, which reach outside it and usually need
connecting first:

| | |
| --- | --- |
| **Getting things in** | `capture` anything at all · `task` for things with a next action |
| **Getting things out** | `ask` your own notes · `teach` you something new · `digest` recent activity |
| **Reasoning past your notes** | `infer` what you never wrote down · `review-assumptions` to confirm or kill its guesses |
| **The outside world** | `weather` · `location` · `news` · `email` · `calendar` |
| **Keeping it healthy** | `doctor` for the install · `maintain` for the notes |
| **Making it yours** | `setup` · `interview` · `new-idea` |
| **Working out what to do with it** | `teach` for what this is and how to use it · `interview` for what to build next |
| **Your history** | `ingest-sessions` |

`digest` surprises people: it names themes across unrelated notes that you never wrote down,
including the things you keep avoiding. `infer` is the one a general chat model can't do, because it
doesn't know you — and every guess it makes is labelled, evidenced, falsifiable, and promotable to a
fact only by you. **Mail and calendar read and draft. They send only when you ask and then
approve** — that rule is written into the tools themselves, and on Claude Code an `ask` list in
`.claude/settings.json` makes the harness stop and ask you, for the mail and calendar connectors it
names. Under another agent, a connector it doesn't name, or any mode that turns prompts off, the
rule is the prompt and nothing else.

The vault itself is markdown organised by [PARA](https://fortelabs.com/blog/para/) — `cortex/00_Inbox/`,
`cortex/01_Projects/`, `cortex/02_Areas/`, `cortex/03_Resources/`, `cortex/04_Archive/`, plus `cortex/Tasks/`, `cortex/Daily/` and `cortex/raw/`.
**You mostly won't think about it.** The structure is for the agent to reason over, not for you to
maintain. Two example notes ship in `cortex/03_Resources/` so it isn't empty on day one; delete them
whenever you like. github.com renders the vault for free, and [Obsidian](https://obsidian.md) reads
this layout as-is if you want something nicer — **open `cortex/` as the vault, not the repo root**,
or your graph fills up with the manual instead of your notes.

> **Tip for Claude Code:** you'll be asked to approve each file the agent writes. Once you've
> watched it a few times and trust it, press `shift+tab` to switch to accept-edits mode and it
> stops asking. Everything it does is still a git commit you can revert.

---

## Which app to use

The vault is markdown in a folder, so anything that reads a folder and runs an agent works. Not
everything works equally well, and pretending otherwise would be the exact vendor-neutrality
theatre this repo is against.

| App | Works? | Notes |
| --- | --- | --- |
| **Claude Code — terminal** | Yes | Reference surface. Everything works. |
| **Claude Code — desktop app** | Yes | **Best option if you don't want a terminal.** Same engine, reads the manual natively, auto-commits. No caveats. |
| **Codex — CLI or app** | Yes | Reads `AGENTS.md`. You run `brain/bin/sync` yourself. |
| Cursor / Aider / Windsurf / Zed | Yes | Read `AGENTS.md`. Sync yourself. |
| Gemini CLI | Yes | Reads `GEMINI.md`, which points at `AGENTS.md`. |
| **Claude Cowork** | Not out of the box | See below. Use the desktop app instead. |
| claude.ai chat / mobile | No | No access to a folder on your computer. |

### Cowork is the honest exception

Cowork is the friendliest of these for someone who never opens a terminal, and it's the one place
this repo's "works with any agent" claim doesn't hold. Two documented facts cause it:

- **Cowork doesn't read `AGENTS.md` or `CLAUDE.md` from a folder you attach.** Its standing context
  is per-project *Instructions*, which live in Cowork's own metadata on your machine — not in your
  repo, not in git, not shared with anyone, and [deleted when you archive the project](https://claude.com/docs/cowork/guide/projects).
- **It doesn't read the repo's `.claude/` directory either**, so the auto-commit hook never fires
  and nothing gets committed unless you ask for it.

Point Cowork at a clone and the operating manual is inert. That's worth stating plainly because it's
the exact failure this repo argues against everywhere else: the instructions that govern your notes
living in a vendor's metadata, outside git, unversioned and unshareable.

**So there's no Cowork adapter here.** One could be built — Cowork supports plugins, and plugins are
file-based and installable straight from a git repo — but it would ship with the operating manual
riding on a skill that fires on relevance rather than on every session, and with no working
auto-commit. Half a seam, on the surface whose users are least able to notice when it slips. Not
worth it while **Claude Code's desktop app is also GUI-only, reads the manual natively, and has none
of these problems.**

<details>
<summary>If you want to use Cowork anyway</summary>

Attach your vault folder to a Cowork project, then paste this into the project's **Instructions**:

> The attached folder is a second-brain vault. Read `AGENTS.md` at its root at the start of every
> session and follow it — it is the operating manual. If I talk about something without naming a
> command, treat it as a capture; if I name one, read `brain/prompts/<name>.md` and follow it. Never
> produce HTML artifacts, PDFs or canvas documents; notes go in the vault as markdown and answers
> go in the conversation as text. Run `brain/bin/sync` before you finish, and tell me if you can't.

That works, and it's the thing to know you're accepting: those Instructions aren't in your repo,
aren't versioned, aren't shared, and vanish when the project is archived. Check `git log`
occasionally — nothing here commits itself.

</details>

## Your history, made searchable

This is the thing worth doing on day one, and the reason a fresh vault isn't empty.

Your agent CLIs have been recording every session you've ever had with them — Claude Code in
`~/.claude/projects/`, Codex in `~/.codex/sessions/`. On a machine that's seen a year of work
that's several gigabytes of your own decisions and reasoning, sitting in files you cannot search.
`ingest-sessions` reads them and writes a short note per session — what you were doing, what you
decided, what you learned — into `cortex/06_Sessions/`, wired into the rest of the vault.

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

## Keeping it running

`brain/bin/doctor` is the first thing to run whenever something feels broken — it checks the install
and prints the command that fixes each problem. `maintain` is the equivalent for your notes rather
than the install; both are in [`GUIDE.md`](GUIDE.md).

**You run them.** This repo ships no cron job and no background agent on purpose — an agent with
unattended access to your notes, before you've watched what it does, is how you stop trusting it in
week two. Scheduling `maintain` later is one line in whatever scheduler you already use; see
[`DESIGN.md`](DESIGN.md#why-nothing-runs-on-a-schedule).

### Updating the harness

Setup cut you loose from this repo's history, so `git pull` won't reach it. When you want a newer
version of the manual and the commands, take the harness and leave your notes alone:

```bash
git remote add upstream https://github.com/Sebastian-Sole/second-brain-demo.git
git fetch upstream
git checkout upstream/main -- AGENTS.md CLAUDE.md GEMINI.md GUIDE.md README.md DESIGN.md brain/ .claude/
git checkout HEAD -- brain/log.md   # your run log lives in brain/ — put yours back
git diff --stat            # look before you commit
./brain/bin/doctor
```

Those paths are the harness — your notes, your daily notes and `cortex/index.md` aren't in the list, so
they can't be touched. The one exception is `brain/log.md`, the history of your own maintenance
runs: it sits inside `brain/`, so the update would overwrite it with the empty version this repo
ships. That's what the second line is for — it puts your copy back from your last save. (Your vault
saves itself after every turn, so "your last save" is a few minutes ago at worst.)

**Your profile is a note (`cortex/03_Resources/About me.md`), not part of the manual, and this is why.**
Anything personal stored inside `AGENTS.md` would be overwritten by the command above without a
word, and you'd find out from an agent that had quietly stopped knowing who you are. If you ever
suspect that happened, `doctor` checks for it specifically and prints the one line that restores it
from git.

---

## Where to take it next

1. **Write your own command** — run `new-idea` when you catch yourself thinking *I wish it could…*. It is the only way this vault grows one. It takes the problem in your words, decides whether the new thing stays inside the vault (`brain/prompts/`) or reaches outside it (`brain/tools/`), and writes a security review into the file before it writes the file. That review is the step you'd skip by copying a prompt by hand, and it matters most for the things that reach outside, because those run with your connectors attached. Fastest way to make the system yours.
2. **Connect your mail and calendar.** The `email` and `calendar` tools are already here — they read freely and draft by default, and a send or a new event needs you to ask for it and then approve the prompt; connecting them turns everything already written down about your week into free context. Highest-leverage move available.
3. **Schedule something, once you trust it** — `maintain` nightly, a morning brief, a weekly review.
4. **Put a real interface on it.** The vault exposes exactly two operations: *write a file into `cortex/00_Inbox/`*, and *run `brain/bin/run <prompt>`*. Every UI is a thin client over those two — a Slack bot, a Telegram bot, an iOS Shortcut, an email address.

---

## Why it's built this way

The design decisions — how it stays vendor-neutral, why provenance is tracked the way it is, why
PARA comes with a caveat, and what the vault looks like after a few months of use — are in
[**`DESIGN.md`**](DESIGN.md). None of it is required reading.

The one rule worth knowing without reading that file: **anything the agent concluded rather than
heard from you stays marked as such, permanently — and only you can promote it to a fact.** A read
across your notes is marked *AI synthesis*; a guess about *you* becomes a numbered assumption with
a falsifier attached. That's what keeps a second brain from turning into a pile of confident AI
text you slowly stop trusting.

---

## License

MIT. Take it, change it, make it yours.
