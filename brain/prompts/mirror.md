# mirror — show them what this brain has learned

The one thing a second brain can do that a chat window can't is **show its working**. This command
renders the vault's model of its human back at them — the facts it holds, the guesses still open,
the guesses that died, and the preferences that got replaced — every line naming the note it stands
on. It's the answer to "what do you know about me", and it's answerable at all because everything
here was written down with provenance.

**Strictly read-only, stricter than `ask`.** This command writes nothing, edits nothing, and
proposes nothing — no capture offer, no "want me to update that?", not even a broken `[[link]]`
fixed in passing. If something they see is wrong, the commands that change it already exist and the
close names them once. The restraint is the feature: a mirror that touches up the image is not a
mirror, and this output is only worth trusting because nothing in it was adjusted on the way out.

Optional argument: a subject, to narrow every section to it. No argument renders everything.

---

## 1. Read exactly two places

- **`cortex/03_Resources/About me.md`** — the hub — and **every spoke it links**: `[[How we work
  together]]`, `[[How I learn]]`, and whatever `review-assumptions` has added (`[[How I work]]`,
  `[[How I handle money]]`, …).
- **`cortex/03_Resources/Assumptions.md`** — the register, **including Refuted & withdrawn**.

Nothing else. Not `cortex/Daily/`, not `cortex/raw/`, not the session notes — and never your
session's environment: connectors, installed skills, neighbouring repos and shell history are not
part of the model and must not be rendered as if they were (per `AGENTS.md`, *Answer from the
vault*). The shipped example notes (tagged `pkm, example`) and the vault's own documentation
describe the software, not the person — they never appear here.

A source that doesn't exist is a one-line statement in its section, not a prompt to go searching
for substitutes.

## 2. Render four sections

Every item carries the `[[note]]` it came from. An empty section says so in one plain line and
moves on — never pad a section to look thorough, never soften "nothing" into filler.

**Facts** — what they said, or confirmed. Plain lines from the hub and its spokes, each with the
note it lives in and the date it was learned:

- a promoted assumption carries its own: `(confirmed YYYY-MM-DD, was ASM-nnnn)` — use that date and
  keep the id visible, it's the fact's pedigree;
- otherwise the earliest `verified:` entry; otherwise the note's `created:`;
- if none of those exists, write `date unknown`. Never invent one.

```
**Facts** — what you've told me, or confirmed
- Short answer first, details only if asked — [[How we work together]], learned 2026-01-05
- Does the hard thinking before noon — [[How I work]], confirmed 2026-02-10 (was ASM-0003)
```

Empty: *"No profile yet — `[[About me]]` hasn't been written. `start` is the conversation that
writes it."*

**Open assumptions** — every `Status: open` row, faithfully from the register: id, claim,
confidence, basis-kind, the basis links, the falsifier, and how long it's been open. Don't re-rank
a confidence, reword a claim, or argue for one — this is the register read aloud, not a fresh pass
of reasoning. Raising new ones is `infer`; this renders what exists.

```
**Still guesses** — open, unconfirmed, and labelled that way for a reason
- ASM-0004 · medium · personal — Starts courses and stops at lesson three.
  Based on [[Course notes stop early]] · [[Half-finished playlist]] · wrong if a course gets
  finished end to end · open since 2026-03-01
```

Empty: *"Nothing guessed yet — the register doesn't exist. `infer` is what creates it."*

**Refuted & withdrawn** — the guesses that died, and what killed each one: the `Refuted because:`
line in their own words with its date, or the withdrawal reason. Then the calibration ratio exactly
as `review-assumptions` computes it — **confirmed / (confirmed + refuted)** — because a model that
can't show where it was wrong can't be trusted where it's right. These rows are kept forever for
precisely this moment.

Empty: *"Nothing refuted yet — no guess has faced a verdict. `review-assumptions` is where that
happens."*

**Superseded** — preference and agreement lines that were replaced: the old line, the date it was
marked superseded, and what replaced it, from wherever they sit — `[[How we work together]]` or a
spoke. A preference that changed is information about them; that's why the old lines were kept
marked rather than overwritten, and this is where the trail gets shown.

Empty: *"Nothing superseded — no preference has been replaced yet."*

## 3. Keep the lines you can trace, drop the rest

- **An item that can't name its note doesn't render.** Something you remember from this
  conversation that isn't in a note yet isn't part of the model, and this isn't the command that
  files it.
- **Labels never mix.** An open assumption never renders under Facts, however old or however
  useful — the one-way rule in `AGENTS.md` holds here as everywhere.
- Newest first within each section, so what the brain learned most recently is what they see first.

## 4. Close in two lines, then stop

One line of totals — facts, open, refuted, superseded — and one line naming what changes what they
saw: `review-assumptions` to rule on the guesses, `interview` to fill the gaps, "remember that" to
change an agreement line, `start` to redo the profile. Then stop. No questions, no offers, no
follow-up.

**Output surface:** plain text in the conversation and nothing else. Nothing was written, so no
correction footer — and never an artifact, however well four sections would render. See `AGENTS.md`.
