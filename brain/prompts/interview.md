# interview — the brain asks *them*

Every other command answers a question. This one works out what the vault **needs to know**, and
asks for it. It's the difference between a filing cabinet and an assistant: nothing gets collected
unless somebody asks.

Optional argument — a source to focus on (`followups`, `assumptions`, `gaps`, `stalled`), or
`dry-run` to build the queue and show it without asking anything.

**The whole skill is question selection.** Anyone can ask questions. The value is asking the two or
three worth interrupting someone for, right now, and staying quiet otherwise.

> This command is invoked by the human — nothing here runs on a timer, by design (see `AGENTS.md`).
> The silence rules below are written as though it did, because that's the only way it stays worth
> running by hand either. If they later put it on a schedule, it's ready.

---

## 1. Build the queue — never freestyle a question

**Every question must come from something in the vault, and must carry the note, task or record
that produced it.** A question you can't cite is small talk, and small talk is how this channel gets
muted.

Read `index.md`, `03_Resources/About me.md`, the last ~10 daily notes, active `01_Projects/`, and
`03_Resources/Assumptions.md` if it exists.

Six sources. Each yields candidates; each candidate carries its citation:

| # | Source | What to look for | Shape of the question |
| --- | --- | --- | --- |
| 1 | **Perishable follow-up** | A dated thing that has now happened with no outcome recorded — a deadline, a meeting, a shipped thing, a reply that was due | *"You had X on Tuesday — how did it go?"* |
| 2 | **Open assumption** | `open` rows in the register, ranked as in `review-assumptions` | *"I've been assuming X — right, wrong, or nearly?"* |
| 3 | **Blank dimension** | An empty dimension in the register, especially one that blocked an answer you gave | *"The vault knows nothing about X — <one concrete question>"* |
| 4 | **Stalled commitment** | A project untouched for >14 days, a task carried forward repeatedly, a question rotting in `00_Inbox/` | *"X hasn't moved in N days — dead, blocked, or want me to take it?"* |
| 5 | **Coverage imbalance** | An area with almost nothing against one that's overflowing | *"Is X dormant, or just not getting captured?"* |
| 6 | **Contradiction** | Two notes that disagree and `maintain` couldn't resolve | *"These two disagree — which is current?"* |

Source 4 escalates rather than repeats. After a couple of mentions the question stops being a
reminder and becomes **"want me to pick this up?"** — offering to do the work and hand back
something to approve. A reminder repeated a third time is nagging, and nagging gets the whole
channel muted.

## 2. Rank by what the answer is worth

1. **Perishability first.** A fact about to evaporate outranks everything. "How did it go?" is worth
   a lot today, little next week, nothing next month — and then the vault has a permanent hole where
   a real event was. This is the single strongest reason to interrupt anyone.
2. **Does the answer unblock something?** It kills or confirms an assumption, fills a dimension,
   unsticks a stalled project.
3. **Cost to answer.** One sentence beats a paragraph. Prefer a question they can answer in the time
   it takes to read it.

Drop anything that fails all three — most candidates should die here. A queue of twenty means the
bar is too low, not that you have twenty questions.

## 3. The budget

- **At most three questions**, and at most **one per source**. Variety, not an interrogation.
- **One at a time.** Ask, wait, respond to what they actually said, *then* decide whether the next
  one is still worth asking. Never paste a list.
- **Stop at the first sign of disengagement** — a one-word answer, "not now", a change of subject.
  End immediately and cheerfully, no closing summary, and don't raise the channel again this
  session. Pushing past this is how it earns a mute.
- **Cooldowns.** A skipped question comes back no sooner than **7 days**; skipped twice, **30**;
  skipped three times, it's **retired** — record that it isn't worth asking. Never ask the same
  question twice in a week.

Cooldowns are real only if they're written down. Log every question asked to today's daily note in
this exact shape, and grep the last ~30 days of daily notes for `interview:` before you ask
anything:

```
- interview: asked "<the question>" — answered | skipped   [source: <what produced it>]
```

## 4. Silence is the default

End with **no message and no writes** unless at least one question clears the bar. Nothing here
obliges you to speak. A run with nothing behind it trains someone to ignore the next one, and then
the good questions never land either.

On a nearly empty vault, that's most runs: there's no history to notice anything in. Say "nothing
worth asking yet" in one line, or stay quiet, and don't manufacture an icebreaker. `setup` is where
a new vault learns who someone is — not here.

## 5. Ask like an assistant, not a form

Open with the concrete thing, never with process:

> The importer rewrite hasn't been touched in three weeks and it's still your only open project —
> parked, or want me to pull the thread?

Not *"I'd like to ask a few questions to improve the second brain."* Concrete, in their voice, one
question, then stop talking. Follow up on their actual answer before moving on — a real answer
usually contains two more facts than the question asked for, and chasing those beats advancing the
queue.

For assumption questions, use the presentation format and the verdict rules from
`review-assumptions.md`, and record `confirmed` / `refuted` / `withdrawn` exactly as specified there.
Only the human promotes an assumption to fact.

## 6. Capture everything that falls out

**Their answers are the point.** They're first-hand facts, and usually better than anything you'd
have inferred. Run each through the normal `capture` logic: file it, link it, keep their words, and
say where it landed. An interview that produced no note was wasted.

Answers are **facts**, written as plain prose — never as assumptions. If an answer contradicts an
open assumption, refute it on the spot and say so.

## 7. Close

One short block: what you captured, what changed, what's still open. Skip it entirely if they
disengaged. Log each question to today's daily note in the shape above, and run `brain/bin/check` if
you touched the register.

Don't commit — whatever invoked you handles that.

## Guardrails

- **Never invent a premise.** If you can't cite what makes you think something happened, don't ask
  about it. A confidently wrong question — "how was the trip?" when there was no trip — is worse
  than silence: it proves the brain doesn't know what's going on.
- **Never ask what the vault already knows.** Search first. Asking something that's answered in a
  note is the fastest way to look useless.
- **Never stack.** Three is the ceiling, not the target. Two good ones beat three.
- **Never moralise about backlog.** "This has been open five weeks" is a fact. "You really should
  deal with this" is nagging. Offer to do it instead.
- **Don't interview about other people's private business.** Questions about a partner, family or
  colleagues are only worth asking where they serve something the human is actually doing.

**Output surface:** plain text in the conversation, plus whatever notes the answers produce. Never
an artifact — see `AGENTS.md`.
