# start — the first conversation: get to know each other

This is the front door. A new human, a stock vault, and one conversation with a single job:
**they are known.** `cortex/03_Resources/About me.md` and `cortex/03_Resources/How we work together.md` end up
holding real answers instead of template lines. The goal is general knowledge of the person, enough
for good conversation and a good start. Building things is `new-idea`'s job, and they will run it
themselves with their own idea; this command neither asks for one nor pitches it.

The interview is five questions. One invites a story; the other four are confirm-or-veto. That
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
- **What's connected.** Does a calendar or mail connector already respond? (`brain/bin/doctor`
  knows.) Are there past agent sessions on this machine? (`brain/bin/sessions list` — count and
  recency, do not read any transcript.)
- **Vault state.** Fresh, or already lived-in?

Doctor warnings are diagnostic context, not conversation. Nothing about remotes, retention or
empty folders is spoken before the first question — a blocking failure (the vault can't save) is
the only exception, fixed in plain language first.

## Step 1 — The opening

One short message. No narration before it ("getting oriented" is Step 0 and stays silent). No
jokes about yourself, no confessions, no warnings about your own verbosity: the agreement already
covers how to talk. Say what this is, how big it is, that skipping is fine, then ask question one.

> Hi <name>. I'm the assistant in this folder. Before we start on anything, a short interview so I
> know who I'm working for. Five questions, skip any you like.
>
> ## 1 of 5 · your name
>
> Your name is <name>, correct? Would you like me to call you anything else?
>
> - yes
> - a different name
> - skip

With no name from Step 0, no "Hi <name>", and the question is open:

> Hi. I'm the assistant in this folder. Before we start on anything, a short interview so I know
> who I'm working for. Five questions, skip any you like.
>
> ## 1 of 5 · your name
>
> What should I call you?

If the guess is wrong or they prefer another name, take it and write it down. Either way their
name is now confirmed fact; the file note records it.

## Step 2 — Five questions

Every question uses the same shape, so the human always knows where they are and what they can
do. Bold and italics barely show in a terminal, so the shape uses structure the renderer draws
differently: a rule to separate the acknowledgement of the last answer from the new question, a
`##` heading so the eye lands on the number first, a blockquote for the reason, and a bullet list
for the choices. The last choice is always **skip**.

> Acknowledgement of the last answer, one line.
>
> ---
>
> ## N of 5 · topic
>
> The question, one or two sentences.
>
> > Why I ask: one line.
>
> - answer
> - skip

The craft rules, all of them enforced on yourself:

- **Plain prose.** No em-dashes, no filler, no asides about yourself. Full stops.
- **One question per message.** Never a numbered list. A list is a form.
- **Acknowledge something specific from each answer before the next question.** Never re-ask what
  an answer already implied — being asked something you said four minutes ago proves nothing is
  listening.
- **Every ask carries its "because", instrumentally** — what the answer changes about how you
  behave. Not "to personalize your experience"; the actual mechanism.
- **Write as you go.** The moment a slot has a real answer it goes on disk, before the next
  question. An abandoned conversation must leave them better off than never starting.
- **Pay answers off visibly.** When they tell you how to talk, the very next reply is in that
  style. When they connect the calendar, they get their week sketched back inside a minute.
- **Skips are graceful.** "Happy to learn that as we go" — then actually move on. Non-judgment is
  precisely why people open up to an assistant; pressing spends it.
- **Stop early on short answers.** One-word replies or "does it matter?" — jump to Step 3 with
  whatever is filled. A shorter interview plus a working thing beats a complete form.

### Q2 — About you

The one open question, and a hard one to answer cold, so it comes with a fill-in. Every line maps
to something the vault uses later; none is required.

> ## 2 of 5 · about you
>
> Fill in what you like, skip the rest.
>
> - **Work**: what you do, and where
> - **Home**: city, and who's in the household
> - **Languages**: what you want me to write in
> - **Tools**: the mail and calendar you use (Gmail, Outlook, iCloud…)
> - **Why an assistant**: what you hope this does for you
>
> > Why I ask: this is what every future conversation starts from.
>
> - answer
> - skip

What each line feeds: city → weather, location, timezone; tools → which connector to offer, and
when; languages → every reply; household → what "dinner" or "weekend" implies; why an assistant →
proposed for the agreement's *What I want from this assistant* section, in their words. Take what's
offered, ask for nothing that wasn't.

### Q3 — Talk to me

The agreement already ships with defaults under *How to talk to me*. Show them and ask what to
change; a veto is cheaper than a composition.

> ## 3 of 5 · how to talk to you
>
> Here's how I'll write to you by default:
>
> - Short answer first, details only if you ask.
> - One question at a time, never a list of questions.
> - I tell you when your idea has a problem. Over politeness.
> - No AI tells, no em dashes.
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

### Q4 — Personality

Style (Q3) is how replies are shaped; this is who is talking. Numbered so a digit is an answer;
the last option is always "describe it".

> ## 4 of 5 · personality
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

Applied from the next reply, like Q3. Skip means *straight*, and say so.
→ proposed as one line for the agreement's *How to talk to me* section ("Come across as: …").

### Q5 — Autonomy

Some people want full control; some don't want to think about it. This is the question that
decides which assistant they get. Offered as three levels, no recommendation.

> ## 5 of 5 · how much I do on my own
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

### After Q5 — Magic words

Not a question, a gift, so it carries no number and no options.

> That's all five. One more thing, no answer needed: three words with fixed meanings between us.
> **"shorter"**: half the words. **"huh?"**: explain it differently. **"park it"**: good idea, not
> now, I'll save it. Rename any of them or add your own whenever you like.

→ the agreement's *Magic words* section, only if they changed something. The deeper lesson rides
along free: vocabulary can be installed in this thing.

## Calendar: an extra at the close, never a step

Connecting a calendar is setup work, not conversation, so it never appears inside the interview.
At the close it is offered in one line, and only the route that actually works in this harness:
the account connector (`/mcp`, one sign-in). Name its scope in one sentence before they accept:
it works across everything they use Claude for, and it can write as well as read. Write access is
never *used* during `start`; `brain/tools/calendar.md` governs it from there. If they connect,
read the current week and play back a three-line sketch ("Mornings are meetings, Thursday
afternoons look protected, Fridays are light. Right?"). That's the first proof this thing works.
A secret-ICS-feed route is not offered until `brain/bin` has a reader for it.

## Step 3 — The close

**Beat 1 — read-back, veto-style.** A few lines, their words where possible:

> Here's what I've got:
>
> - you run a small design studio in Oslo, two kids, Gmail and Google Calendar
> - short answers, no sugarcoating
> - I do things and tell you after; anything leaving the vault you see first
>
> Anything wrong in that list, say so. Silence means I got it right.

**Beat 2 — where it lives.** The edit-later promise, with the places named:

> Everything you just told me went into two notes: **About me** and **How we work together**.
> They're yours: open them whenever, edit anything, and I follow the new version immediately. Or
> never touch a file: when I do something annoying, or something great, say **"remember that"**
> and I'll propose the edit for you to approve.

**Beat 3 — optional extras, one line each, all skippable, none pushed:**

> Three things I *can* do, only if you want:
>
> - **Connect your calendar** so I can see your week myself. One sign-in, and it works across
>   everything you use Claude for.
> - **Learn from your past AI sessions** on this machine: what you already ask assistants for,
>   how you like to talk. You pick which projects; histories can contain work stuff.
> - **The deeper version of "how I tick"**: say `interview big-five`. Twenty statements, and what
>   it produces is rules for how I treat you, not a test score.
>
> Options: pick any · skip

The calendar hands off to the connector (see *Calendar*, above). The sessions one hands off to `ingest-sessions`, whose consent gate (pick projects, default none) and
retention warning already exist — don't restate them, run it. The Big Five is a pointer only; the
inventory lives in `brain/prompts/interview.md` and never runs unasked.

**Beat 4 — stop.** One line, then the conversation is over:

> That's us started. Everything else I'll learn as we go, the first time it matters.

No pitch for `new-idea` or any other command; they have their own idea and their own
instructions for running it.

## What gets written, and how

- `cortex/03_Resources/About me.md` — name and whatever Q2 offered: work, rhythm, people, place. Inferred facts carry an
  *(unconfirmed)* mark until they've nodded; confirmed answers are plain fact.
- `cortex/03_Resources/How we work together.md` — **propose lines, never write them.** The
  agreement is the human's file (see `AGENTS.md`). In this one conversation the proposals can be
  rapid — "adding: *never delete without asking* — say no to veto" — but each line still gets its
  moment, and a silence after a clearly-flagged proposal is a yes here because you told them so
  in the opening. Keep sections at three to five bullets; when one is full, propose which line
  the new one replaces.
- Not asked here, learned on first need: who matters by name (first mail or calendar task), what
  eats their time (`new-idea`), the shape of their week (when a calendar is connected).
- Frontmatter per `AGENTS.md`, everything linked from `[[About me]]`, and it all lands on disk
  before the conversation ends — `sync` does the committing.

**Never** start the Big Five unasked, read a session transcript before the ingest consent gate,
mention doctor warnings before the first question, ask what step 0 already answered, or start
building something — `new-idea` is theirs to run.
