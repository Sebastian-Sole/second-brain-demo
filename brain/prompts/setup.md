# setup — make this vault theirs

This is the human's **first session** with this second brain. Everything here is a stock template
until you finish this conversation. Your job is to learn enough about them to fill in the
**About the human** section at the top of `AGENTS.md`, which loads into every future session and
is what stops this from writing generic notes about a stranger.

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

Ask all of it in **one short message**, as a numbered list. Five questions, plain wording, and say
up front that one-line answers are fine and they can skip any of them.

1. **What should I call you?**
2. **What do you do?** — work, studies, whatever takes up most of your week.
3. **What do you want to use this for?** — work, side projects, reading, life admin, some mix.
4. **How do you like things written?** — short and blunt, or fuller and more explanatory? Do you
   want me to ask before writing something long?
5. **What are you actually working on right now?** — the one or two things on your mind this
   month. This is the one that makes captures land in the right place.

Then wait. Do not fill anything in before they answer, and do not ask follow-ups one at a time
like an interrogation — if an answer is thin, that's fine, write what you got.

**If they'd rather not answer**, say so is fine and offer to come back to it: write what little
you have, and tell them `setup` can be run again any time.

## Step 3 — Write it

Edit **only** the `## About the human` section of `AGENTS.md`. Replace the blank bullets with what
they told you, in their words. Leave every other line of the file exactly as it is.

Rules:

- **Don't invent.** If they skipped a question, leave that bullet empty rather than guessing. A
  confident wrong fact about the human is worse than a gap — it will shape every note you write.
- **Don't polish their voice away.** If they said "terse, I hate preamble", write that, not
  "prefers concise communication".
- **Write it in first person, as they'd write it.** The bullets say "What I do", so the answers read
  "Exam in November", not "she has an exam in November". You're filling in their words, not
  describing them to a third party.
- **Keep it short.** This loads into every session. A paragraph per bullet is too much.
- Delete the `> **← Start here...**` instruction block above the bullets once it's filled in —
  it's scaffolding for an empty template, and leaving it makes the file look unfinished forever.

Then show them the section you wrote and ask if it's right. Fix whatever they correct.

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

## Step 5 — Tell them the three things worth knowing

**Output surface:** edits to `AGENTS.md`, a real note in the vault, and plain text in the
conversation. Never a rendered welcome document — the first thing they see should be the vault
working, not a brochure.

Not a tour. Three lines, then stop:

- **You don't have to use commands.** Talking to the agent in this folder is a capture by default.
- **`ask` is the payoff.** It answers from their own notes, with links. It gets better as the
  vault fills.
- **`ingest-sessions` is the day-one win** *if* they've used an AI coding CLI before — it turns
  history they already have into notes they can search. Mention it only if `brain/bin/doctor`
  found Claude Code or Codex on the machine.

Finally, mention the example notes in `03_Resources/` are there to show the shape of things and
they can delete them whenever they like. Offer to do it now.

---

## What this command is not

Don't reorganise the vault, don't pre-build projects or areas, and don't write notes they didn't
ask for. They're getting a canvas, not a finished system — the folders fill in as they use it, and
a vault pre-populated with an agent's guesses about someone's life is worse than an empty one.
