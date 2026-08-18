# review-assumptions — confirm, refute, or skip

Open assumptions are worth little until the human rules on them. A confirmed one becomes a fact you
can state back; a refuted one is a permanent correction to the model of them, and the more useful of
the two.

Optional argument: a subject, a dimension, or `stale` to review only the aged ones.

Rules: the Assumptions section of `AGENTS.md`. Register: `03_Resources/Assumptions.md`.

If the register doesn't exist yet, say so in one line and stop — there's nothing to review, and
`infer` is what creates it.

---

## 1. Load the open set

Read the register. Take everything with `Status: open`, filtered by the argument if there is one.

## 2. Rank by leverage, not by age

Put first the ones where a verdict actually changes something:

- it's named as the parent of another assumption (confirming it lifts the child's confidence cap);
- it's `high` or `medium` and shapes how you'd answer a recurring question;
- it's `stale` — open more than 90 days with nothing testing it;
- it sits in a dimension with almost no evidence, so one answer fills a hole.

**Surface at most five per pass.** This has to stay a two-minute job. A review nobody finishes is a
review nobody runs twice.

## 3. Present them for a tap

One block each, numbered, no preamble:

```
1. ASM-0007 · low · personal
   New work displaces unfinished cleanup — the queue orders by momentum, not severity.
   Because: two known-broken things sat for weeks while new work shipped past them.
   Wrong if: you clear something critical the same week it's raised.
```

Then, exactly:

> Reply like `1y 2n 3s` — y = right, n = wrong, s = skip. A few words on any `n` and I'll record why.

Accept anything recognisable — `1y 2n`, "yes to 1 and 3", prose, a correction in their own words.
Never make someone type a paragraph to answer a yes/no. If they answer only some, that's fine; the
rest stay open.

## 4. Record each verdict

In the register, and only there for the reasoning.

**y → confirmed.** Set `Status: confirmed · <date> · by <them>`. Then **promote it**: write the
claim as plain prose where it belongs, carrying its provenance:
`(confirmed 2026-09-01, was ASM-0007)`. Keep the register row; mark the pointer as confirmed.

Where it goes:

- **About them** → the spoke for that subject in `03_Resources/`, named for *them* and not for the
  domain — `[[How I work]]`, `[[How I handle money]]`, `[[How I decide]]`. Create the spoke if it
  doesn't exist yet and link it from `[[About me]]`. A bare domain name like `Money.md` is an
  `02_Areas/` name and collides with it. **Not the hub itself**: `[[About me]]` is capped at 40
  lines and re-read on every turn, so it carries the link, never the claim.
- **About someone else** → that person's note, under `## Facts`.

`brain/bin/check` permits the provenance form in exactly those places, and only while the register
still records that id as `confirmed`. Refute it later and the check will point at the promoted line
so it can come back out.

**n → refuted.** Set `Status: refuted · <date>`, append `Refuted because: <their words>`, and move
the whole block to **Refuted & withdrawn**. **Never delete it.** Remove the pointer from wherever it
was cited — the register keeps the history. If their correction contains a *new fact*, capture that
properly too; it's usually worth more than the assumption was.

**s → skip.** Leave it `open` and add `last surfaced: <date>` so it ranks below fresher ones next
time. Silence is not agreement — an unanswered assumption stays open forever if it has to.

**A correction that reframes rather than kills it** → `withdrawn` with the reason, then raise a new
assumption with a **new id** carrying what they actually said. Never edit an old block into a
different claim; that erases the fact that you were wrong.

## 5. Cascade

If a confirmed assumption was the parent of a chained one, lift that child's confidence cap and say
so. If a refuted one was a parent, mark every child `withdrawn` — they were built on it — and list
them.

## 6. Update the register header

Recount `open` / `confirmed` / `refuted` / `stale` / `withdrawn`. `Next ID` doesn't change — ids are
never reused. Bump `updated:` on every file you touched, and run `brain/bin/check`.

## 7. Report in one block

What's now fact, what got killed, what changed downstream. Then the honest number:

> Survived so far: **confirmed / (confirmed + refuted)**

That ratio is the calibration signal, and it cuts both ways. Near 100% means the assumptions are too
timid to be worth making. Near 0% means the model of them is off and you should be raising fewer,
better ones. Say which one you think it is.

Log a line to today's daily note.

**Then the correction footer.** This pass rewrote the register and, on every `y`, added a line to
a spoke or to someone's `## Facts` — and it may have created that spoke and linked it from
`[[About me]]`. Those are writes the human can't see from the conversation. One line, at the end,
naming every note you touched and how to undo it:

```
Register updated: 2 confirmed, 1 refuted, 2 still open · [[How I work]] gained one line
(say "ASM-0007 was wrong" and I'll reverse that verdict)
```

Name the spoke you actually wrote, not `[[About me]]` — the hub only ever gains a link, and only
the first time a subject gets a spoke. If you created one, say so: that's a new note, and it's the
write the human is least expecting.

A pass where they answered nothing changed nothing, so it gets no footer. Don't commit — whatever
invoked you handles that.

## Guardrails

- **Never confirm on their behalf**, and never read silence as agreement.
- **Never rewrite a claim to fit their answer.** A claim that needed rewording was `withdrawn`, and
  the reworded one is a new id.
- **Don't argue a refutation.** Record it in their words and move on. The whole point of the
  register is that being wrong is cheap and traceable.
- **Don't do a maintenance pass while you're in here.** Verdicts only.

**Output surface:** plain text in the conversation, plus the register and any note a confirmation
promoted a fact into. Never an artifact — see `AGENTS.md`.
