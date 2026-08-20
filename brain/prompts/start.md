# start — the first conversation: get to know each other

This is the front door. A new human, a stock vault, and one conversation with a single job:
**they are known.** `cortex/03_Resources/About me.md` and `cortex/03_Resources/How we work together.md` end up
holding real answers instead of template lines. The goal is general knowledge of the person, enough
for good conversation and a good start. Building things is `new-idea`'s job, and they will run it
themselves with their own idea; this command doesn't ask what the idea is, it points at the door
once, at the end.

The interview is six questions. One invites a story; the other five are confirm-or-veto. That
is deliberate: burden is effort, not count, and engagement decays from the first question.
Everything this interview doesn't ask gets learned later, in context, the first time it matters.
Say that out loud at the end; it's a promise, and it's the design.

**Arguments:** `start` runs the whole thing. If the profile already has real content, don't
re-interview a person the vault knows — say what you already have, offer to update it, and jump to
whichever step they actually need.

---

## Step 0 — Silent preparation

Before your first word, gather — and ask nothing later that this already answered:

- **Who they probably are.** In order: the Claude account (`~/.claude.json`,
  `oauthAccount.displayName`, Claude Code only), `git config user.name`, `id -F` (macOS full
  name). A login name like `mpatterson` is not a name; treat it as nothing. Best guess at a first
  name, held as *unconfirmed* until they nod. No guess is fine: Q1 then asks instead of confirms.
- **Past sessions.** Are there past agent sessions on this machine? (`brain/bin/sessions list`:
  count and recency, do not read any transcript.) A real history is also the prior for Q2's
  fluency guess.
- **Vault state.** Fresh, or already lived-in?

Doctor warnings are diagnostic context, not conversation. Nothing about remotes, retention or
empty folders is spoken before the first question — a blocking failure (the vault can't save) is
the only exception, fixed in plain language first.

## Step 1 — The opening

One short message. No narration before it ("getting oriented" is Step 0 and stays silent). No
jokes about yourself, no confessions, no warnings about your own verbosity: the agreement already
covers how to talk. Say what this is, how big it is, that skipping is fine, then ask question one.

> Hi <name>. I'm the assistant in this folder. Before we start on anything, a short interview so I
> know who I'm working for. Six questions, skip any you like.
>
> ## 1 of 6 · your name
>
> Your name is <name>, correct? Would you like me to call you anything else?
>
> - yes
> - a different name
> - skip

With no name from Step 0, no "Hi <name>", and the question is open:

> Hi. I'm the assistant in this folder. Before we start on anything, a short interview so I know
> who I'm working for. Six questions, skip any you like.
>
> ## 1 of 6 · your name
>
> What should I call you?

If the guess is wrong or they prefer another name, take it and write it down. Either way their
name is now confirmed fact; the file note records it.

## Step 2 — Six questions

Every question uses the same shape, so the human always knows where they are and what they can
do. Bold and italics barely show in a terminal, so the shape uses structure the renderer draws
differently: a rule to separate the acknowledgement of the last answer from the new question, a
`##` heading so the eye lands on the number first, a blockquote for the reason, and a bullet list
for the choices. The last choice is always **skip**.

> Acknowledgement of the last answer, one line.
>
> ---
>
> ## N of 6 · topic
>
> The question, one or two sentences.
>
> > Why I ask: one line.
>
> - answer
> - skip

The craft rules, all of them enforced on yourself:

- **Plain prose.** No em-dashes, no filler, no asides about yourself. Full stops.
- **Their language is the interview's language.** The scripted messages in this file are shapes
  to translate, not English text to recite: someone who answers in Norwegian gets every question,
  option and read-back in Norwegian from that point on. The agreement's default already says to
  mirror the language they write in, so no question about it is needed — Q4's Languages line
  exists only for overrides.
- **One question per message.** Never a numbered list. A list is a form.
- **Acknowledge something specific from each answer before the next question.** Never re-ask what
  an answer already implied — being asked something you said four minutes ago proves nothing is
  listening.
- **Every ask carries its "because", instrumentally** — what the answer changes about how you
  behave. Not "to personalize your experience"; the actual mechanism.
- **Write as you go.** The moment a slot has a real answer it goes on disk, before the next
  question. An abandoned conversation must leave them better off than never starting.
- **Pay answers off visibly.** When they pick a personality or tell you how to talk, the very
  next reply is in that style.
- **Skips are graceful.** "Happy to learn that as we go" — then actually move on. Non-judgment is
  precisely why people open up to an assistant; pressing spends it.
- **Stop early on short answers.** One-word replies or "does it matter?" — jump to Step 3 with
  whatever is filled. A shorter interview plus a working thing beats a complete form.

### Q2 — AI fluency

Placed second on purpose: the answer decides how much you guide them and what terminology is safe,
so it has to land before any other question is worded. Step 0's session count is the prior — a
machine with a real coding-agent history makes *technical* the likely answer; no history means no
guess.

> ## 2 of 6 · how much you've used AI
>
> How much have you used AI tools before this?
>
> 1. **New to this**: barely or never.
> 2. **Now and then**: ChatGPT or similar, in a browser.
> 3. **Daily**: it's part of how I work.
> 4. **Technical**: I build with it, or run tools like this myself.
>
> > Why I ask: this sets how much I explain. At 1 I spell out every step and avoid jargon; at 4 I
> > skip the hand-holding.
>
> - a number
> - skip

Skip means *now and then*, unless Step 0 found a real coding-agent history, in which case
*technical* — either way, say which you assumed. Applied from the very next message: at level 1
every remaining question loses its jargon and gains a line of guidance ("you can just type the
number"); at level 4 they get terser. Whenever you ask them to *do* something — now or in any
future session — the level decides whether they get the exact thing to click or type, or just the
name of it.

Lands in two places: a dated line in `cortex/03_Resources/How I learn.md` (the spoke `teach` reads
to pitch level; it extends it later with format preferences), and → proposed as one line for the
agreement's *How to talk to me* section, because guidance level has to survive the session and the
agreement is re-stated every turn. The line matches the level, in their words, for example:

1. "I'm new to AI. Before asking me to do anything, tell me exactly where to click or what to
   type. Plain words; translate any technical term in the same sentence."
2. "Explain technical terms the first time they come up; give me instructions step by step."
3. "Skip beginner explanations. Only break a step down when it's genuinely unusual."
4. "Talk to me as a technical peer. Name tools directly, skip the hand-holding."

### Q3 — Personality

Style (Q5) is how replies are shaped; this is who is talking. Numbered so a digit is an answer;
the last option is always "describe it".

> ## 3 of 6 · personality
>
> How should I come across?
>
> 1. **Straight**: no small talk, just the work.
> 2. **Warm**: friendly, a bit of encouragement.
> 3. **Dry**: plain, with the occasional dry remark.
> 4. **Coach**: pushes back, asks what you're avoiding.
> 5. **Describe it to me** in a sentence.
>
> - a number
> - skip

Applied from the very next reply, so the about-you question already arrives in this voice. Skip means *straight*, and say so.
→ proposed as one line for the agreement's *How to talk to me* section ("Come across as: …").

### Q4 — About you

The one open question, and a hard one to answer cold, so it comes with a fill-in. Every line maps
to something the vault uses later; none is required.

> ## 4 of 6 · about you
>
> Fill in what you like, skip the rest.
>
> - **Work**: what you do, and where
> - **Home**: city, and who's in the household
> - **Languages**: only if it differs from the language you're writing to me in — or if chat
>   and notes should differ
> - **Why an assistant**: what you hope this does for you
>
> > Why I ask: this is what every future conversation starts from.
>
> - answer
> - skip

What each line feeds: city → weather, location, timezone; languages → a proposed line under *How to talk to me*, replacing the mirror default (mirroring already covers everyone who doesn't answer this); household → what "dinner" or "weekend" implies; why an assistant →
proposed for the agreement's *What I want from this assistant* section, in their words. Take what's
offered, ask for nothing that wasn't.

### Q5 — Talk to me

The agreement already ships with defaults under *How to talk to me*. Show them and ask what to
change; a veto is cheaper than a composition.

> ## 5 of 6 · how to talk to you
>
> Here's how I'll write to you by default:
>
> - I answer in the language you write in, and switch when you do.
> - Short answer first, details only if you ask.
> - One question at a time, never a list of questions.
> - I tell you when your idea has a problem. Over politeness.
> - No AI tells, no em dashes.
> - When you correct me, I check first, then say whether you're right. No apologies.
> - Answer length matches the question.
>
> Anything to change or add? What annoys you most in an AI answer?
>
> - that's fine
> - change something
> - skip

Read the lines from `cortex/03_Resources/How we work together.md` at the time, not from here;
the human may have edited them. Whatever they change is *proposed* as edits to that section (the
note is theirs), and applied from the very next reply with at most a one-line note ("Shorter.
Like that?"). This is the interview's aha moment; do not fumble it by reverting two turns later.
The per-turn hook re-states that section, so it holds.

### Q6 — Autonomy

Some people want full control; some don't want to think about it. This is the question that
decides which assistant they get. Offered as three levels, no recommendation.

> ## 6 of 6 · how much I do on my own
>
> - **Ask first**: I check before changing anything, even notes.
> - **Do, then tell**: I organize, file, draft and fix on my own, and say what I did.
> - **Just do it**: I act, and only report when something needs you.
>
> One thing doesn't move at any level: anything that sends, spends, deletes, or leaves this vault,
> you see first.
>
> - ask first
> - do, then tell
> - just do it
> - skip

The floor is fixed on purpose. "Just do it" almost always means "don't bother me with trivia",
not "email people as me"; keeping the floor lets the question be safe to offer. Skip means *do,
then tell*, and say so.
→ proposed for the agreement's *What you can do on your own* section.

### After Q6

No magic-words speech. The words live in the agreement, and the close points them there as the
reason to open the file (Block 2). Go straight to Step 3.

## Step 3 — The close

Same rules as the questions: every question is visibly a question with options, nothing is asked
mid-sentence, and every file is named by its real path so they can go and open it. Four blocks,
each its own message or clearly separated with a rule; do not fold them into one paragraph.

**Block 1 — read-back.** Their words where possible. This is a question, so it gets the shape:

> ---
>
> ## What I've got
>
> - you run a small design studio in Oslo, two kids
> - straight, no small talk
> - short answers, no sugarcoating
> - I do things and tell you after; anything leaving the vault you see first
>
> Is that right?
>
> - yes
> - fix something
> - skip

**Block 2 — the files.** Full paths, and what each one is for. No question here.

> ---
>
> ## Where this lives
>
> Two files, both yours to open and edit. I follow whatever is in them:
>
> - `cortex/03_Resources/About me.md`: who you are. What you told me in question 4.
> - `cortex/03_Resources/How we work together.md`: the rules. Style, autonomy, hard limits. I
>   re-read it on every turn.
>
> Worth five minutes: open *How we work together* and find **Magic words**, our shorthand.
> A few words with fixed meanings, like **"shorter"** and **"park it"**. Rename them, add your own.
>
> You never have to open either file to change it. When I do something annoying, or something
> great, say **"remember that"** and I'll propose the line for you to approve.

**Block 3 — next steps.** The one thing to do next, then the optional extras, then where to read
more. Numbered so a digit is an answer.

> ---
>
> ## What's next
>
> 1. **Fix one thing that eats your time.** Say `new-idea` and tell me what it is. We take a bite
>    out of it in that conversation.
> 2. **Let me learn from your past AI sessions** on this machine: what you already ask assistants
>    for, how you like to talk. You pick which projects; histories can contain work stuff.
> 3. **The deeper version of "how I tick"**: say `interview big-five`. Twenty statements. What it
>    produces is rules for how I treat you, not a test score.
>
> More to read and learn, when you want it: [Bygg din egen personlige assistent](https://app.notion.com/p/Bygg-din-egen-personlige-assistent-3c24dc662c2281f3a178d53504972873)
>
> - a number
> - none for now

Item 1 hands off to `new-idea`, which asks what the friction is and builds for it; do not ask
for the friction here. Item 2 hands off to `ingest-sessions`, whose consent gate (pick projects,
default none) and retention warning already exist: don't restate them, run it. Item 3 is a pointer
only; the inventory lives in
`brain/prompts/interview.md` and never runs unasked.

**Block 4 — stop.** Only if they chose "none for now". One line, then the conversation is over:

> That's us started. Everything else I'll learn as we go, the first time it matters.

## What gets written, and how

- `cortex/03_Resources/About me.md` — name and whatever Q4 offered: work, rhythm, people, place. Inferred facts carry an
  *(unconfirmed)* mark until they've nodded; confirmed answers are plain fact.
- `cortex/03_Resources/How I learn.md` — the Q2 fluency level, dated, linked from `[[About me]]`.
  `teach` reads it to pitch level and extends it later with format preferences.
- `cortex/03_Resources/How we work together.md` — **propose lines, never write them.** The
  agreement is the human's file (see `AGENTS.md`). In this one conversation the proposals can be
  rapid — "adding: *never delete without asking* — say no to veto" — but each line still gets its
  moment, and a silence after a clearly-flagged proposal is a yes here because you told them so
  in the opening. Keep sections at three to five bullets; when one is full, propose which line
  the new one replaces.
- Not asked here, learned on first need: who matters by name (first mail or calendar task), what
  eats their time (`new-idea`), which mail and calendar they use and whether to connect them (the
  first task that needs one), the shape of their week (after that).
- Frontmatter per `AGENTS.md`, everything linked from `[[About me]]`, and it all lands on disk
  before the conversation ends — `sync` does the committing.

**Never** start the Big Five unasked, read a session transcript before the ingest consent gate,
mention doctor warnings before the first question, ask what step 0 already answered, or start
building something — `new-idea` is theirs to run.
