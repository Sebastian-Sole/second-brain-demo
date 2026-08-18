# infer — answer what the vault has no facts for

The human is asking something this brain probably can't answer from stored facts alone. Your job is
to **reason to the best available answer anyway** — from adjacent facts about them — and to make the
line between what's known and what you concluded impossible to miss.

If they gave you no question, use whatever they just asked in conversation.

**Read the Assumptions section of `AGENTS.md` before answering.** It's the contract; this is the
procedure.

---

## 1. Check the gates first

Four things stop this command before it starts, per `AGENTS.md`:

- **Under ten notes the human actually wrote** (excluding the `pkm, example` ones and
  `[[About me]]`), don't reason about them at all. Say so plainly — *"there are four notes here and
  three are about the vault itself; I'd be making it up"* — answer whatever the facts support, and
  offer to capture what would change that. This is not a failure; it's the honest answer to a
  question asked of a young brain.
- **Notes about this vault are not evidence about the person.** Its setup, structure and commands
  describe the software.
- **Your session's environment is not evidence.** Connectors, skills, other repos on the disk,
  shell history. Every basis link is a note in this vault.
- **A fact beats an assumption.** If step 3 finds one, stop and answer as `ask` would.

Run `brain/bin/check` if the register already exists — inheriting a broken one and adding to it is
how the ids drift.

## 2. Orient

Read `index.md`, then `cortex/03_Resources/About me.md` (the stated facts), then
`cortex/03_Resources/Assumptions.md` if it exists — **including the refuted section**. If they already
refuted this claim, don't re-raise it: say it was refuted, when, and by what. New evidence can
reopen it, but only explicitly and citing the old row.

**If the claim in play is about their character or disposition** — how they're wired, rather than
what they did last Tuesday — read the spoke `cortex/03_Resources/Big Five profile.md` as well. It holds
behaviour lines they answered for themselves, and a line they stated outranks anything you'd infer
from three notes; it can also kill a candidate assumption outright, which is the cheapest possible
outcome here. **If it doesn't exist, that's normal** — spokes appear when there's something real to
put in them. Reason without it and don't mention it. Don't read it for a question about their work,
their projects or their week: it costs context on every turn and answers nothing there.

## 3. State the target, then retrieve

Write the claim that would actually answer the question as **one falsifiable sentence** before you
gather anything. Vague targets produce horoscopes.

Then search the retrieval order from `AGENTS.md` — `cortex/03_Resources/`, `cortex/01_Projects/`, `cortex/02_Areas/`,
`Tasks/`, `Daily/`, plus `cortex/00_Inbox/` for anything captured but not yet processed — for the topic,
its synonyms, and the entities involved, and follow `[[wikilinks]]` out from the best hits. Sort
what you find into:

- **direct** — facts that answer the question outright, and
- **adjacent** — facts about neighbouring dimensions: how they work, what they've chosen before,
  where their attention goes.

If the question is about past work, `cortex/06_Sessions/` is fair evidence — but note the bias when you
use it. A vault of session notes is a record of someone's *work*, and "they're relentless about
correctness" may be a fact about what gets written down rather than about them.

## 4. Build the chain, explicitly

For each candidate conclusion:

- name the adjacent facts it rests on, as `[[links]]`;
- state **the mechanism** in one sentence — *why* that evidence implies this for *this* person. No
  mechanism, no assumption: you have a vibe;
- pick the **basis-kind** honestly — `personal`, `population`, or `mixed`. Cross-domain taste
  prediction is nearly always `population`. Label it that way even when it feels insightful;
  especially then.

## 5. Try to kill it

Before you state it, search for evidence *against* — a note that cuts the other way, an occasion
they did the opposite. Then apply the counting rules:

- Two facts pointing the same way is a coincidence. Three, with a mechanism, is a claim.
- **Independent means independent.** Three notes from one session, or three restatements of one
  belief, are *one* piece of evidence.
- Name the sampling bias when it applies. What's in the vault is what got captured, not what's true.

## 6. Grade it

`high` / `medium` / `low` against the rubric in `AGENTS.md`. Be stingy — a `medium` you can defend
is worth more than three `high`s you can't. Built on another open assumption? Capped at `low`, and
name the parent id.

## 7. Answer in three blocks, never mixed

```
**Known** — what the vault actually holds, with [[links]]. Say plainly what's missing.
**Assumed** — the claim · confidence · basis-kind · because <the leap, one line>.
**Would change my mind** — the falsifier, and the one thing worth capturing to settle it.
```

In their voice: concrete, terse, no hedging-as-filler. Never open with an unlabelled guess — if the
first sentence is a conclusion, it starts with **Assumption:**. Cap at three. If there's no basis at
all, say the vault doesn't know and offer to research or capture it. Never pad.

## 8. Name the gap

Every assumption marks something this brain should have known. End with the **single question** that
would convert it to a fact — one question, answerable in a sentence, not a survey.

## 9. Persist only what's durable

An assumption that would change a future answer gets registered. A throwaway guess stays in the
conversation — don't grow the register for the sake of it.

To register one:

1. Take the next id from **Next ID** in `cortex/03_Resources/Assumptions.md`, then bump it.
2. Append the full block under a `### ASM-nnnn — <short title>` heading, in the section for its
   dimension, followed by a `_Subject: <who> — <where the pointer lives>_` line.
3. Add the **one-line pointer** where it belongs — never a copy of the reasoning, and never in a
   `## Facts` section or in `[[About me]]`:
   - about the human → nowhere else; the register's dimension section *is* the self-model here
   - about another person → that person's note, under `## Inferred (not stated)`
   - about a project → that project note, under `## Assumptions`
4. Update the status counts in the register header.
5. Run `brain/bin/check` and fix every error it reports.
6. **End with the correction footer.** Registering an assumption is a write, and routing is silent,
   so the last line names what went into the register and how to take it back out:

   ```
   Registered: ASM-0012 in [[Assumptions]] — open until you rule on it
   (say "drop it" if that's not worth keeping)
   ```

   If you created the register in this run, say that instead: `Started [[Assumptions]] and
   registered ASM-0001`. One line, at the end, no ceremony. **An answer that registered nothing
   wrote nothing and gets no footer** — the three blocks are the whole reply.

### Creating the register

If `cortex/03_Resources/Assumptions.md` doesn't exist, create it now — with the full skeleton below, not
just the one block you have. The blank dimensions are the point: **a dimension with nothing in it is
the most useful line in the file**, because it tells the next session what to ask about and stops a
leap quietly resting on nothing.

```markdown
---
title: Assumptions
type: register
stage: evergreen
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
generated: { by: <agent>/<version>, at: <timestamp> }
verified: []
tags: [meta]
area:
aliases: [assumptions, assumption register, self-model]
---

# Assumptions

What this brain has concluded about me that **I never said**. Facts I stated live in
[[About me]]; this is the layer above them, and every claim here is open until I confirm it.

> [!WARNING]
> Nothing in this file is a fact while it is open. The rules are in `AGENTS.md`. Never quote an
> open line from here back to me without its label, and never copy one into [[About me]] or into a
> spoke. Only I promote one, and only through `review-assumptions`.

**Next ID: ASM-0001**

| Status | Count |
| --- | --- |
| open | 0 |
| confirmed | 0 |
| refuted | 0 |
| stale | 0 |
| withdrawn | 0 |

Confirm or kill these with `review-assumptions`.

---

## How they work

## How they decide

## What they value

## Taste

## Attention & follow-through

## Other people & projects

---

## Blank — nothing recorded at all

Don't infer across these; ask instead.

_(list the dimensions with no evidence — social energy, money, health, risk appetite, how they
handle conflict with people, whatever this vault has never touched)_

> [!WARNING]
> **Sampling bias, permanent caveat.** This vault holds what got captured, not what's true. If
> most of it is work, then most of the above describes a worker. Discount accordingly.

## Refuted & withdrawn

Kept forever. A wrong guess, recorded, is what stops the same wrong guess next month.

_(none yet)_
```

Add it to `index.md` under **People & concepts**, and log a line to today's daily note.

## What this command must never do

- State an assumption as a fact, in the answer or in a note.
- Promote one to fact on its own. Only the human does that, via `review-assumptions`.
- Act on one. It informs *their* decisions; it never authorises sending, booking, buying, or
  changing anything.
- Infer about another person as though the conclusion were something they said.
- Pad a thin vault. "There isn't enough here yet" is a complete, correct answer.

**Output surface:** plain text in the conversation, plus the register if you wrote to it. Never an
artifact or rendered document — see `AGENTS.md`.
