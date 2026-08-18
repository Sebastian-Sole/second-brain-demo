# Using your second brain

You've run `setup` and the vault knows who you are. This is what to do with it from here.

Two other files, so you know when to leave this one: [`README.md`](README.md) is what this is and
how to install it, and [`DESIGN.md`](DESIGN.md) is why it's built the way it is. Neither is
required reading. This one is.

The short version, if you read nothing else:

- **Talk to it in plain sentences.** You don't have to learn any commands.
- **Never file anything by hand.** Deciding where a note goes is the agent's job, not yours.
- **Anything it writes, you can undo.** Every change is a save point in git.

---

## Where things go, and why you don't have to care

The folders sort by **how actionable something is right now**, not by what it's about. That's the
whole idea — it's called PARA, and it's why one vault can hold your job, your side project and
your life admin without turning into a filing cabinet with forty subject folders.

| Folder | What's in it |
| --- | --- |
| `00_Inbox/` | Anything it wasn't sure about. Should be near-empty most of the time. |
| `01_Projects/` | Things with a goal and an end. "Ship the new pricing page." |
| `02_Areas/` | Things you're on the hook for forever. "Health", "Finances", "The team." |
| `03_Resources/` | The actual knowledge — one idea per note. Also your profile. |
| `04_Archive/` | Finished projects, dormant areas, completed tasks. |
| `05_Attachments/` | Images, PDFs, anything that isn't text. |
| `06_Sessions/` | Notes about your past AI coding sessions. Appears after `ingest-sessions`. |
| `Daily/` | One note per day: what you captured, what happened. |
| `Tasks/` | One note per open task. |
| `raw/` | Untouched originals of anything that came from outside. Never edited. |
| `brain/` | The machinery — prompts, scripts, log. Not your notes. |

**The one distinction worth learning**, because it's the only one that's genuinely ambiguous:

- An **Area** is a standing responsibility with no finish line. You can fall behind on it.
- A **Resource** is something you'd *read* rather than *act on*. You can't be behind on it.

"Marathon training" is an Area. "That article about VO2 max" is a Resource. If you'd never be
"behind" on it, it's a Resource.

**You should never be moving files around.** The agent decides where things go, using the folder
map in `AGENTS.md`, and `maintain` tidies up after it. If something lands in the wrong place, say
so in a sentence and it moves it. That's the entire filing workflow.

---

## The commands, grouped by what you want

In Claude Code these are slash commands — `/capture`, `/ask`. In any other agent, just say the
word. And you can skip them entirely; see [the next section](#you-dont-have-to-use-the-commands).

### Getting things in

**`capture`** — the workhorse. Give it a thought, a link, a decision, a pasted article, a
transcript, or nothing at all (in which case it captures what you two just did). It works out what
each piece is, saves any external original into `raw/` untouched, writes the ideas up as short
notes **in your words**, links them to what's already there, logs a line in today's daily note,
and adds them to `index.md`.

```
capture — decided against the queue for now, cron is fine at this volume
```

> Wrote `03_Resources/Cron is enough until the queue actually backs up.md`, linked to
> `[[Infrastructure]]`, logged to today's daily note.

If a dump contains three ideas you get three small linked notes, not one long one. If it can't tell
what something is, it goes to `00_Inbox/` with an explicit question rather than being guessed at.

**`task`** — anything with a next action. See [Tasks](#tasks) below.

### Getting things out

**`ask`** — answers from your own notes, with links to the notes it used. It reads nothing else:
if the vault doesn't cover it, it says so rather than padding the answer with general knowledge.

```
ask what did I decide about retries?
```

It searches your notes, projects, areas and daily notes. It only digs into `06_Sessions/` when the
question is clearly about past work ("why did we go with Z", "when did I last touch Y") — otherwise
a thousand session notes would drown out the real ones.

**`explain`** — teaches you something new, pitched at you. This is the opposite of `ask`: `ask`
hands back what you already wrote, `explain` covers ground your notes don't. It checks what you've
already written on the topic first, so it doesn't explain something you took notes on last month,
and it anchors the new idea to one you already understand. If you've written a note called
`How I learn`, it reads that to work out how to pitch it. Nothing gets written down unless you ask.

**`digest`** — rolls up recent activity. Defaults to the last 7 days; say `digest last month` or
`digest since Tuesday` for something else. Four sections: what happened, **patterns**, what's
stalled (with how long, and the smallest next action), and open loops. It saves the digest as
`Daily/YYYY-MM-DD — Digest.md` and shows it to you.

The patterns section is the one that surprises people — it reads across unrelated notes and names
themes you never wrote down, including things you keep starting and not finishing. Anything it
concluded rather than read is marked as such.

### Reasoning past what you wrote

These two are a different kind of thing, and the part a general chat model can't do, because it
doesn't know you.

**`infer`** — answers a question your notes don't contain, by reasoning from ones they do. *Would I
actually finish this? What am I avoiding?* Every guess comes back in three labelled parts:

```
**Known** — what the vault actually holds, with links.
**Assumed** — the claim, how confident, and the leap in one line.
**Would change my mind** — what would prove it wrong.
```

Guesses worth keeping get a number and a permanent home in `03_Resources/Assumptions.md`, each with
its evidence, its reasoning, and its falsifier. **Below ten notes you actually wrote, it refuses to
guess about you at all** and says so — a character sketch off four notes is the fastest way to stop
trusting the whole thing.

**`review-assumptions`** — a two-minute pass over what it's guessed. It shows up to five at a time
and you reply `1y 2n 3s` — yes, no, skip.

- **Yes** promotes it into a plain fact in your profile, carrying `(confirmed 2026-09-01, was
  ASM-0007)` so you can always see where it came from.
- **No** marks it refuted and keeps it forever. A wrong guess on the record is what stops the same
  wrong guess next month.
- **Skip** leaves it open. Silence is never read as agreement.

**Only you can turn a guess into a fact.** Nothing does it by age, repetition or usefulness.

### The outside world

These five reach past the vault. The first three need nothing but a network connection; the last
two need you to connect an account, and are covered in [their own section](#connecting-mail-and-calendar).

**`weather`** — the forecast where you are, or somewhere you name. No account, no API key. It uses
Open-Meteo, which is free and needs no signup, so it works on day one.

**`location`** — where you are, worked out from your IP address. It says that's where it came from,
because on a VPN it's the exit node rather than you. If you tell it it's wrong, it believes you and
doesn't argue. Nothing is stored.

**`news`** — a roundup of *your* feeds, filtered to what you said you care about, and away from what
you said you don't. The first time you run it there's nothing to go on, so it asks what you read
and offers to write it down; after that it just runs. You say "Hacker News" — finding the actual
feed URL is its job, not yours. It links every item to the original.

**`email`** and **`calendar`** — read your mail and your schedule and answer from them. They can
prepare a draft. They will never send anything. Read [Connecting mail and
calendar](#connecting-mail-and-calendar) before you connect either.

**None of these write notes.** A forecast or a headline is answered in the conversation and saved
nowhere, because "12°C, rain from 14:00" is true for four hours and then competes with your real
notes in search forever. If you want one kept, say so and it becomes an ordinary capture.

### Keeping it healthy

**`doctor`** — run this first whenever anything feels off. It's a script rather than a prompt:

```bash
./brain/bin/doctor
```

It checks git, whether you have a backup remote, which agent CLIs are installed, that the folders
and scripts are intact, that your profile exists and is under its size cap, that every finished task
carries a completion date, and — on Claude Code — whether your session history is being deleted after
30 days. Every problem comes with the exact command that fixes it. Add `--check` if you want it to
report without changing anything.

**`maintain`** — the health pass over your notes, as opposed to the install. It closes out the day,
files what it can from `00_Inbox/` and leaves an explicit question on what it can't, finds notes
that contradict each other and keeps *both* with dates rather than picking one, links up orphans,
fixes broken links, and rebuilds `index.md`. It writes one line to `brain/log.md` so you can see
what it did without opening a single note.

Run it when the inbox has visibly grown, or once a week. **It never deletes a note** — it archives,
flags, or asks.

### Making it yours

**`setup`** — you've already run this. Run it again any time; it's how you correct your profile.

**`interview`** — the only command that talks to you first. It works out what the vault is missing
and asks: how did the thing on Tuesday go, is this project dead or just quiet, this assumption —
right or wrong? Every question has to cite the note or gap that produced it, it's capped at three,
asked one at a time, and it stops the moment you sound uninterested. **Its default is silence** — on
a young vault most runs have nothing worth asking, and it says so in one line rather than inventing
an icebreaker. Nothing runs it on a timer.

**`new-feature`** — adding a command of your own. **The prompt file for this isn't in the repo yet**,
so treat the name as a label rather than something you can run today. In the meantime, adding a
command is genuinely two steps: copy an existing file in `brain/prompts/` and edit it, then add a row
to the table in `AGENTS.md`. Anything that reaches outside the vault goes in `brain/tools/` instead,
with a small frontmatter block declaring what it needs and what it's allowed to write.

### Your history

**`ingest-sessions`** — the thing worth doing on day one. Your agent CLIs have been recording every
session you've ever had, on disk, in files you can't search. This reads them and writes a short note
per session — what you were doing, what you decided, what you learned — into `06_Sessions/`, wired
into the rest of the vault. Then `ask` can answer questions about work you did eight months ago.

Three things it does deliberately: **it asks which projects to ingest and the default is none** (your
history almost certainly contains other people's confidential code, and this vault gets pushed); it
**never copies a transcript in**, only notes about them; and it **scans everything it writes for
secrets** first, because a faithful summary of an API key is still an API key. It defaults to the last
30 days and tells you what's left.

There's a deadline on this one, covered in the README: Claude Code deletes transcripts older than 30
days unless you change one setting. `doctor` nags you about it.

---

## You don't have to use the commands

Talking to the agent in this folder is enough. It reads what you said and picks the right command
itself, using a routing table in `AGENTS.md` that says, for each command, both what it's for and
what it *isn't* for — which is the half that stops "tell me about X" going to the wrong place.

**Routing is silent.** You won't be told "I'll use `capture` for this", and you won't be asked
permission to route. You asked for a thing, not a tour of the machinery.

**Anything that wrote something ends with one line saying what it made.** That's the safety net for
silent routing: if it guessed wrong, you can see that it did.

```
you:   need to cancel the insurance before the 30th

brain: Filed as a task: Tasks/Cancel the insurance.md
       (say "make it a note" if that's wrong)

you:   no, that's not a task, I was just thinking out loud

brain: Moved it — it's now 03_Resources/The insurance renews at a worse rate.md,
       linked to [[Finances]]. Task removed.
```

Reads get no footer, because nothing was created and there's nothing to correct.

**If nothing matches, it captures.** That's the safe default: the worst outcome is a note sitting
in your inbox with a question attached.

---

## Tasks

**One note per task, in `Tasks/`.** No checkboxes anywhere in this vault — a `- [ ]` line has no
date, no reason, no links, and nothing can tell you when it appeared or why. A thing worth
remembering to do is worth a file. You never write that file; the agent does, so the extra
ceremony costs you nothing.

Add one:

```
you:   remind me to call the bank about the standing order

brain: Filed as a task: Tasks/Call the bank.md
       (say "make it a note" if that's wrong)
```

It only asks for a due date if you implied one. A task with no date is a perfectly good task.

List them:

```
you:   what's open?

brain: Call the bank — open 6 weeks. Still want this one?
       Renew the passport — open 3 days, due before the 14th.
       Draft the Q3 note — open since 2 August, on [[Reporting]].
```

It orders by what's actually relevant rather than by filename, gives each one its age, and says
out loud when something has been sitting there too long. A task list that never notices its own
dead weight is how a task folder becomes a graveyard.

Finish one:

```
you:   called the bank, sorted

brain: Done: 04_Archive/Call the bank (done 2026-08-18).md — opened 2026-08-14
```

**Finished tasks move to `04_Archive/`, they are never deleted.** Two reasons: "where did that task
go" has to be answerable by opening a folder rather than by knowing git, and `04_Archive/` is
already outside the default search, so a thousand finished tasks never clutter up your real notes.
Dropping a task requires a reason, recorded in the file — a dropped task with no reason is
indistinguishable from one that got lost.

---

## Connecting mail and calendar

Both are **opt-in**. Nothing is connected until you connect it, and until then asking about your
inbox gets you one plain sentence — "No mail connector is configured" — rather than an error.

Read this before you connect anything:

> **They read, and they can prepare a draft. They will never send.**

That's the whole ceiling, and it holds when you ask directly, when it's obviously what you meant,
and when the draft already exists and sending is one click. Email never sends, replies, forwards,
trashes, labels, marks spam or archives. Calendar never accepts, declines, moves, cancels or
invites anyone; the most it will do is put a tentative, uninvited hold in your own calendar.

If you ask it to send, it says so and hands you the text to paste.

The reason is worth stating once. Everything here is routed silently, so a misrouted sentence must
never become an email a colleague received. And `git revert` undoes a note you didn't want — it does
nothing at all about a mail sitting in someone else's inbox.

Two more things they do:

- **Nothing from your mailbox or calendar is written into the vault.** It's answered in the
  conversation and saved nowhere unless you explicitly ask for it. This is a git repo that gets
  pushed, and other people's correspondence and whereabouts don't belong in it.
- **Nothing it reads there becomes a fact about you.** It won't decide from your inbox what you do
  for a living. That's not filing, it's surveillance with a note attached.

A note on mail specifically: anyone with your address can put text in front of the agent. Anything
inside a message shaped like an instruction — "AI assistant, forward this to the team", "ignore your
previous instructions" — is treated as text being summarised, never as a command. If something tries
it, you get told.

---

## When it gets something wrong

It will. Three levels of fix, cheapest first.

**1. Say so.** Every write ends with a line naming what it made. Reply in plain words — "that should
be a task", "wrong project", "that's not what I meant" — and it fixes it in the same conversation.
This handles almost everything.

**2. Undo it in git.** Every change to this vault is saved as a numbered point in time, whether
anyone asked for it or not. You can go back to any of them. You do not need to understand git for
this — two commands:

```bash
git log --oneline        # a list of every change, newest first, each with a short id
git revert <that-id>     # undo that one change, leaving everything after it alone
```

`git revert` doesn't erase history; it adds a new change that puts things back. Nothing is lost
either way, so it's safe to try. If you'd rather not type it, ask the agent to show you the last few
changes and undo the one you mean — it can read the same list.

**3. Run `doctor`.** If something feels broken rather than just wrong — a command failing, notes not
saving, the agent not knowing who you are — this is the first thing to run, before debugging
anything by hand:

```bash
./brain/bin/doctor
```

It reports in plain language and each problem comes with the command that fixes it. It also fixes the
mechanical things itself: a missing folder, a script that lost its executable bit.

A special case worth knowing: if the agent has suddenly stopped knowing who you are, your profile
note got clobbered. `doctor` checks for exactly that and prints the one line that restores it.

---

## What it will never do

Short and honest:

- **Send anything.** No email sent, replied to or forwarded. No calendar invite accepted, declined
  or issued. Drafts only, always.
- **Run unattended.** No cron job, no CI workflow, no background agent ships with this. Every
  command is something you invoked, with the changes in front of you. You can put `maintain` on a
  timer later once you trust it — that's your call, not its.
- **Ping you unprompted.** `interview` is the only thing that asks you questions, it only runs when
  you run it, it's capped at three, and it goes quiet when it has nothing worth asking.
- **Put things in your profile you didn't say.** It may *offer* — "want me to add 'no bullet lists'
  to how you like things written?" — and if you ignore it, it drops the subject. It can never write a
  line about you on its own initiative, and it can never conclude something about you from your
  inbox, your calendar, your other repos or your shell history. A check script fails the build if a
  guess turns up in your profile dressed as a fact.
- **Delete your notes.** Superseded notes get marked and kept. Finished tasks get archived. If two
  notes contradict each other, both survive with dates on them.
- **Invent facts.** If it doesn't know, the correct answer is "the vault doesn't cover this" — and
  anything it worked out rather than heard from you stays marked as its reasoning, permanently.

---

## Where to read more

- [`README.md`](README.md) — what this is, installing it, backing it up, which app to use.
- [`AGENTS.md`](AGENTS.md) — the operating manual the agent follows. Long, but it's the actual
  contract, and everything above is a summary of some part of it.
- [`DESIGN.md`](DESIGN.md) — why it's built this way: vendor-neutrality, provenance, why nothing runs
  on a schedule, and what the vault looks like after a few months of use.
