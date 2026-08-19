# setup — make this vault theirs

This is the human's **first session** with this second brain. Everything here is a stock template
until you finish this conversation. Your job is to learn enough about them to write
`cortex/03_Resources/About me.md`, which every future session reads at the start and which is what stops
this from writing generic notes about a stranger.

Treat them as someone who has never used a tool like this and may not be a programmer. No jargon,
no lectures on PARA or provenance. They can read `README.md` for that if they want to.

---

## Step 1 — Check the setup works, and say nothing about it

Run `brain/bin/doctor` and read the output. On Claude Code the wrapper has already run it and
pasted the result into your context — either way, **the checkup is for you, not for them.** It is
diagnostic context. It is not the first thing they hear.

**Warnings do not get mentioned here. Not one, not briefly, not as a friendly preamble.** No
backup remote, transcripts expiring in 30 days, an empty vault — none of it is spoken in the
opening message. They can all be fixed in a minute, none of them stops anything, and step 6 is
where they belong.

This rule exists because it is the easiest one in the file to break and the most expensive. You
have a checkup sitting in your context, it has findings in it, and reporting findings feels like
being useful. It isn't: **the first sentence someone ever reads from their second brain decides
whether it feels like an assistant or like a build pipeline.** "Your branch doesn't push to the
remote yet — one command, `git push -u origin main`" is a fine sentence in the wrong place, and
someone who came here to have their notes organised has just been handed homework about git before
being asked their name. Open with the question. Nothing else.

**Two things — and only these two — earn a word before the first question:**

- **Something blocking.** The vault can't save itself. Deal with it first, in plain language, then
  re-run. Don't start an interview on a vault that will lose the answers.
- **You couldn't run `doctor` at all** because you'd need approval you can't get. That's the Claude
  Code trust prompt — the folder hasn't been trusted, so everything in `.claude/` is being ignored.
  Say so plainly and tell them to restart `claude` here and accept it. Don't quietly hand-check the
  vault instead and carry on; a session where the repo's own settings aren't loaded is worth naming.

Everything else: stay silent and go to step 2. **If the checkup was clean, don't announce that
either** — "everything checks out, the vault works" is still a status report about machinery, and
they didn't ask. The proof that it works is step 4, where they watch it file a real note.

## Step 2 — Ask which depth, then ask

**This is your first message to them, and it opens cold.** No status report, no summary of what
you just checked, no "great news". One line of context if you like — *"Let's make this yours"* —
and then the fork. Per step 1, nothing from the checkup appears here.

**Offer two depths, in one short message, before any question.** Both are real options and neither
is the "proper" one — say that plainly, because a fork where one branch is obviously the good one
isn't a choice, it's a nudge:

> Two ways to do this. **Quick** is six questions, about two minutes, and gets you a working vault —
> most people start here. **In depth** takes fifteen to twenty and gets a much sharper profile: the
> same six, then how you like things written, what you're into, and a short research-backed
> personality inventory if you want one. You can start quick and deepen it any time — nothing is
> locked in either way.

Then take the answer at face value. **Don't sell the deep one and don't apologise for it**, and if
they don't pick, run quick — the reversible option is the right default, and it's reversible in one
sentence (`setup deep`, or `interview`, whenever they like).

An explicit argument skips the question entirely: `setup quick` and `setup deep` mean what they say.

**Both paths run the six questions below.** Deep is a superset, not a different interview — it
continues at *The in-depth path* near the end of this file, after they've seen the vault do
something real.

### The six

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
add it to `cortex/index.md`.

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

> If you want, I can read your mail and your calendar and answer from them. Reading never
> interrupts you. Writing always does: I draft by default, and I only send a mail or put something
> in your calendar if you ask me to and then say yes to the prompt. I'll never suggest deleting or
> declining anything. Want to connect either one?

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

**Then one more line, and it matters most for the people least likely to ask for it:**

> If you want to know what this actually is — what the thing in your terminal is, what it can be
> wired into, what people build on top of it — say `guide`. It's pitched wherever you are, from
> never-used-AI upward, and `guide expand` is the part with the ideas in it.

Say it once. Someone who has just watched their first note get filed is at the exact moment where
"what else can this do" is a live question, and `guide` is the answer to it — but a first run that
turns into a tour is a first run nobody finishes, so **offer it and stop.** Don't run it here.

Finally, mention the example notes in `cortex/03_Resources/` are there to show the shape of things and
they can delete them whenever they like. Offer to do it now.

### Now — and only now — the checkup warnings

**This is where step 1's warnings come out.** They've watched the vault file a real note, so
"you've got no backup yet" is now a sentence about *their notes* rather than a sentence about a
stranger's git config. Same fact, completely different weight.

**At most two, one line each, each with the fix attached and no explanation of why it matters** —
they can ask. The two that are ever worth saying:

> Two things worth a minute sometime: this isn't backed up anywhere yet (`git push -u origin main`
> once you've made a repo for it), and Claude Code deletes its session history after 30 days unless
> you change that — which matters only if you ever want `ingest-sessions` to read it.

**Skip any that don't apply, and skip the whole block if none do.** Don't read the checkup out.
Don't list warnings that fix themselves — "no notes yet" stopped being true four steps ago, and
repeating a stale finding is how someone learns the report isn't looking at their actual vault.
And **don't offer to fix the backup for them**: it needs a repo that doesn't exist yet and a
decision about where their private notes get hosted, which is theirs to make.

**On a quick run, one closing offer, one line, genuinely optional.** Five answers is a thin
profile, and per `AGENTS.md` the human — not this command — picks how a fuller one gets built. They
already declined once in step 2, so this is a reminder that the door is open, not a second pitch.
Say it once and drop it:

> That's a thin profile on purpose. `setup deep` picks up where this left off whenever you want it —
> or `interview` will fill it in a few questions at a time as you go. Nothing here needs either.

**On a deep run, skip this entirely** — they're doing it now, and offering someone the thing they
are currently in the middle of reads as a system that isn't paying attention.

## Step 7 — The correction footer

`setup` writes more than anything else here, and per `AGENTS.md` anything that wrote ends with a
one-line correction footer. Name what now exists and how to change it:

```
Set up: [[About me]], [[How I learn]] and [[Your first note]], all listed in cortex/index.md
(say what's wrong with any of them and I'll fix it — nothing here is permanent)
```

Name the files you actually wrote — drop `[[How I learn]]` if they skipped question 6, add
`[[My news sources]]` if they gave you feeds, add `[[How I talk]]`, `[[What I'm into]]` and
`[[Big Five profile]]` on a deep run. One line, at the end, no ceremony.

---

## The in-depth path — a fuller profile in one sitting

Run this when they chose **in depth** in step 2, said `setup deep`, or came back for it later.

**It slots in after step 4, not before it.** The ordering is the load-bearing part: by then they
have watched a real note get filed, so they're answering questions about a tool they've seen work
rather than about a folder they were promised. Twenty minutes of profiling before anything has
happened is a personality test administered by a stranger, and it's the surest way to lose someone
in the first ten minutes.

**If they came back later and `[[About me]]` already exists**, don't re-run steps 1–4. Read the
hub, check in one line that it's still true, and start here.

**Three parts, each writing one spoke, each independently skippable.** Say up front that there are
three and they can stop after any one of them — and then make that true by **writing each spoke as
you finish that part**, never batching them to the end. A deep run abandoned halfway has to leave a
better vault than no deep run at all, and it only does if the first spoke is already on disk.

Why spokes and not a longer `[[About me]]`: the hub is capped at 40 lines and paid for on every
single turn, including the turn where someone asked what the weather is. Detail belongs in files
that are read only by the command that needs them — see *A hub, capped at 40 lines* in `AGENTS.md`.

### Part 1 — How they want things written → `[[How I talk]]`

Question 4 in step 2 got one line about this. This gets the detail that actually changes output.
Four questions, one message:

1. **Answer first, or reasoning first?**
2. **Bullets, or prose?**
3. **When I write something in your voice, what should it never sound like?** — the best question
   here by some distance. People struggle to describe how they write and find it very easy to name
   what makes them wince.
4. **How long is too long before you'd rather I just asked you?**

Write **behaviour lines, not adjectives.** "Answer in the first sentence, reasoning underneath"
changes the next turn. "Prefers concise communication" changes nothing — it's a description of a
person rather than an instruction to an agent, and it's the same inert-in-a-prompt failure that
`AGENTS.md` bans percentile scores for.

### Part 2 — What they're into → `[[What I'm into]]`

Read by `digest` and `interview`. This is **taste, not credentials** — not what they're expert in,
what they'd cheerfully lose an evening to.

- What do you actually read, watch or follow?
- What would you happily be interrupted about?
- What do you emphatically not want to hear about?

This overlaps step 5's news sources and the overlap is fine as long as you don't ask twice: **this
spoke is the taste, `[[My news sources]]` is the URLs.** If they name a publication here, carry it
into step 5 and confirm rather than re-asking.

### Part 3 — The inventory → `[[Big Five profile]]`

**Don't restate the instrument here.** It is specified once, in `brain/prompts/interview.md` under
*Topic path — the profile instrument*: the public-domain 20-item Mini-IPIP, five-point scale, half
the items reverse-keyed, scored privately, written as behaviour lines and never as numbers. Read
that file and follow it. Two copies of an inventory spec is two things to keep in sync, and the
second one is always the one that rots.

What this step owns is the offer and the honesty around it:

- **Say what it is, because "personality test" earns scepticism.** Big Five is the model with the
  research actually behind it — decades of it, replicated cross-culturally, the standard instrument
  in the field. People are right to distrust the quizzes they've met before; the fix is naming the
  difference in a sentence, not asserting that this one is serious.
- **Never substitute a pop instrument.** Not MBTI, not the enneagram, not DISC, not love languages.
  They're better known and more fun and they don't replicate — and a profile is *permanent context*
  here, so putting one in means every future session reasons from something that isn't true. If
  they ask for MBTI by name, say what you know in one line, offer the Mini-IPIP instead, and drop
  it if they'd rather not. Don't refuse, and don't lecture them about psychometrics.
- **Say what comes out before they start.** Six or so behaviour lines they can read and argue with.
  Not a score, not a four-letter type, not a label. And say where it's used: `infer` reads it when
  a claim about their character is at stake, and nothing else touches it.
- **Stoppable at any point.** A half-finished inventory still yields usable lines for the factors
  they got through, and this is the part most likely to be declined by someone who wanted the other
  two. Declining it is a normal outcome, not a gap to fill later.

### Rules for the whole path

- **Everything they say here is a fact they stated, not an assumption.** Plain prose in the spokes,
  nothing in the register, no callouts. The one-way rule in `AGENTS.md` still holds without
  exception: you may propose, only they may accept.
- **Show them each spoke as you write it** and fix whatever they correct. This path writes four
  times what quick does, and a profile they never read is one they can't disagree with — which is
  the entire point of keeping it in files they can open.
- **Link every spoke from `[[About me]]` and list it in `cortex/index.md`.** Hub and spokes, per
  `AGENTS.md`. The hub gains a link per spoke and nothing else; it stays under 40 lines.
- **Three parts, then step 5.** Don't let deep grow a fourth part because the conversation was
  going well. If more comes out, that's what `interview` is for, later, in threes.

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
