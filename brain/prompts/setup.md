# setup — make this vault theirs

This is the human's **first session** with this second brain. Everything here is a stock template
until you finish this conversation. Your job is to learn enough about them to write
`cortex/03_Resources/About me.md`, which every future session reads at the start and which is what stops
this from writing generic notes about a stranger.

Treat them as someone who has never used a tool like this and may not be a programmer. No jargon,
no lectures on PARA or provenance. They can read `README.md` for that if they want to.

---

## Step 1 — Check the setup actually works

Run `brain/bin/doctor` and read the output.

If it reports anything blocking, deal with that first — help them fix it, in plain language, then
re-run. Don't start the interview on a vault that can't save itself.

If you can't run `doctor` at all because you'd need approval you can't get, that's the Claude Code
trust prompt — this folder hasn't been trusted yet, so the settings in `.claude/` are being ignored.
Say so plainly and tell them to restart `claude` here and accept it. Don't quietly hand-check the
vault instead and carry on; a session where the repo's own settings aren't loaded is worth naming.

If it only reports warnings, mention the ones that matter (no backup configured, session history
being deleted after 30 days) but **don't stop for them** — they can be fixed later and the
interview is more valuable now.

## Step 2 — Ask

Ask all of it in **one short message**, as a numbered list. Six questions, plain wording, and say
up front that one-line answers are fine and they can skip any of them.

1. **What should I call you?**
2. **What do you do?** — work, studies, whatever takes up most of your week.
3. **What do you want to use this for?** — work, side projects, reading, life admin, some mix.
4. **How do you like things written?** — short and blunt, or fuller and more explanatory? Do you
   want me to ask before writing something long?
5. **What are you actually working on right now?** — the one or two things on your mind this
   month. This is the one that makes captures land in the right place.
6. **How technical are you, and how much have you used AI tools before?** — "never opened a
   terminal" and "I write software for a living" are equally good answers.

**Question 6 rides along; the profile interview is still the five above.** Its answer doesn't go in
`[[About me]]` at all — write it to the spoke
`cortex/03_Resources/How I learn.md`, in their words — the hub is capped at 40 lines and paid for on every
turn, and fluency is only needed by the command that's teaching them something. Ask it now anyway:
a level-adaptive tutorial can't pitch itself without it, and adding the question later means
re-interviewing everyone who has already set up.

Then wait. Do not fill anything in before they answer, and do not ask follow-ups one at a time
like an interrogation — if an answer is thin, that's fine, write what you got.

**If they'd rather not answer**, say so is fine and offer to come back to it: write what little
you have, and tell them `setup` can be run again any time.

## Step 3 — Write it

Create `cortex/03_Resources/About me.md` with what they told you, in their words:

```markdown
---
title: About me
type: person
stage: evergreen
status: stable
created: YYYY-MM-DD
updated: YYYY-MM-DD
generated: { by: <you>, at: <timestamp> }
verified: []
tags: []
aliases: []          # their name, once you know it — so [[Sebastian]] resolves here too
---

- **Name:**
- **What I do:**
- **What this brain is for:**
- **How I like to work:**
- **Current focus:** _(as of YYYY-MM)_
```

**Don't touch `AGENTS.md`.** The profile deliberately lives outside the manual so that updating the
harness can't erase it — see *About the human* there for why.

Rules:

- **Don't invent.** If they skipped a question, leave that bullet empty rather than guessing. A
  confident wrong fact about the human is worse than a gap — it will shape every note you write.
- **Don't polish their voice away.** If they said "terse, I hate preamble", write that, not
  "prefers concise communication".
- **Write it in first person, as they'd write it.** The bullets say "What I do", so the answers read
  "Exam in November", not "she has an exam in November". You're filling in their words, not
  describing them to a third party.
- **Keep it short.** This loads into every session. A paragraph per bullet is too much.
- **Date the current focus.** It's the bullet that rots — mark it `(as of YYYY-MM)` so a later
  session can tell six-month-old plans from this week's.
- This note is exempt from the "every note links to another" rule on day one — there's nothing to
  link to yet. `maintain` will wire it up as the vault fills.

Then show them the file you wrote and ask if it's right. Fix whatever they correct.

## Step 4 — Their first capture

Now do one real thing, so they see what this is rather than reading about it.

Ask for something to capture — "anything on your mind, a sentence is enough" — and then follow
`brain/prompts/capture.md` on it properly: write the note, link it, log it to today's daily note,
add it to `index.md`.

Then **show them what you did**: the file you created, where it went, and why it went there. Point
out that `git log` and `git revert` mean nothing here is permanent.

**Don't assert whether anything was committed unless you actually ran `git log` and looked.** If you
couldn't, say the notes are written and you weren't able to check git — not that the work is
uncommitted. Telling someone their first session wasn't saved when it was is a bad first impression,
and it's the kind of claim that's easy to make from an assumption about a hook you never observed.

If they have nothing to give you, offer to capture what brought them to this tool in the first
place. That's a real note and it's usually a good one.

## Step 5 — Offer the outside world (optional, and genuinely skippable)

Two offers, in **one** message, both easy to decline. Say up front that everything already works
and neither of these is a prerequisite for anything — **someone who declines both must end up with
a working vault.** These are offers, not more interview.

**Mail and calendar.** State the ceiling *before* they connect anything, not after:

> If you want, I can read your mail and your calendar, and draft replies you send yourself. I
> can't send, reply, delete, accept or decline anything, and I can't put anything in your calendar
> at all — that's off by design, not a setting you can flip. Want to connect either one?

If yes, walk them through their agent's connector setup in plain language and confirm it with
`brain/bin/doctor`. If no, say that's completely fine and move on: `brain/tools/email.md` and
`brain/tools/calendar.md` degrade to one plain sentence when nothing is connected, and no other
command notices.

**News sources.** Ask what they actually read, watch or follow — and what they emphatically don't
want to hear about. Write the answer to `cortex/03_Resources/My news sources.md`, **resolving each name to
a feed yourself**: they say "Hacker News", you store `https://news.ycombinator.com/rss`. The human
never goes hunting for an XML endpoint. If they'd rather not, don't create the note — an empty
spoke is organisational debt, and `news` knows how to ask for itself later.

## Step 6 — Tell them the three things worth knowing

**Output surface:** real notes in the vault — `[[About me]]`, their first capture, and whatever
they opted into above — plus plain text in the conversation. Never a rendered welcome document, and
no edits to `AGENTS.md`. The first thing they see should be the vault working, not a brochure.

Not a tour. Three lines, then stop:

- **You don't have to use commands.** Talking to the agent in this folder is a capture by default.
- **`ask` is the payoff.** It answers from their own notes, with links. It gets better as the
  vault fills.
- **`ingest-sessions` is the day-one win** *if* they've used an AI coding CLI before — it turns
  history they already have into notes they can search. Mention it only if `brain/bin/doctor`
  found Claude Code or Codex on the machine.

Finally, mention the example notes in `cortex/03_Resources/` are there to show the shape of things and
they can delete them whenever they like. Offer to do it now.

**One closing offer, one line, genuinely optional.** Five answers is a thin profile, and per
`AGENTS.md` the human — not this command — picks how a fuller one gets built. Say it once and don't
sell it:

> If you ever want a fuller profile than that, `interview` can build one — either by asking how you
> like to work, or with a short Big Five inventory if you'd rather answer statements. Entirely
> optional, and nothing here needs it.

**Don't run an inventory now.** Twenty statements in the first ten minutes is a personality test
before they've seen the tool do anything, and it's the opposite of the "canvas, not a finished
system" rule below. The offer is the whole of it — if they say yes, hand off to `interview`.

## Step 7 — The correction footer

`setup` writes more than anything else here, and per `AGENTS.md` anything that wrote ends with a
one-line correction footer. Name what now exists and how to change it:

```
Set up: [[About me]], [[How I learn]] and [[Your first note]], all listed in cortex/index.md
(say what's wrong with any of them and I'll fix it — nothing here is permanent)
```

Name the files you actually wrote — drop `[[How I learn]]` if they skipped question 6, add
`[[My news sources]]` if they gave you feeds. One line, at the end, no ceremony.

---

## What this command is not

Don't reorganise the vault, don't pre-build projects or areas, and don't write notes they didn't
ask for. They're getting a canvas, not a finished system — the folders fill in as they use it, and
a vault pre-populated with an agent's guesses about someone's life is worse than an empty one.

**In particular, don't raise a single assumption here, and don't pitch `infer`.** Six answers to
six questions is not evidence, the ten-note floor in `AGENTS.md` means the command would refuse
anyway, and a brain that starts profiling someone in its first conversation is the exact thing
people fear about this. It earns that after they've filled it. Everything they told you in step 2 is
a **fact** they stated — write it plainly in `[[About me]]`, with no callouts and no conclusions
drawn from it.
