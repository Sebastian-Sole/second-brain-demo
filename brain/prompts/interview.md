# interview — the brain asks *them*

Every other command answers a question. This one works out what the vault **needs to know**, and
asks for it. It's the difference between a filing cabinet and an assistant: nothing gets collected
unless somebody asks.

Optional argument — a source to focus on (`followups`, `assumptions`, `gaps`, `stalled`),
`dry-run` to build the queue and show it without asking anything, or `big-five` to run the
personality inventory instead of the queue (see **Topic path — the profile instrument**, below).

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

Read `cortex/index.md`, `cortex/03_Resources/About me.md`, the last ~10 daily notes, active `cortex/01_Projects/`, and
`cortex/03_Resources/Assumptions.md` if it exists.

Read the spoke `cortex/03_Resources/What I'm into.md` too, **where it would sharpen a question** —
`AGENTS.md` names this command as one of its readers. It's what turns "anything on the reading
pile?" into a question about the thing they actually care about, and it's often what breaks a tie
between two candidates of equal rank. **If it doesn't exist, that's normal** in a young vault —
spokes appear when there's something real to put in them. Build the queue without it, don't block
on it, and don't ask them to fill it in.

Six sources. Each yields candidates; each candidate carries its citation:

| # | Source | What to look for | Shape of the question |
| --- | --- | --- | --- |
| 1 | **Perishable follow-up** | A dated thing that has now happened with no outcome recorded — a deadline, a meeting, a shipped thing, a reply that was due | *"You had X on Tuesday — how did it go?"* |
| 2 | **Open assumption** | `open` rows in the register, ranked as in `review-assumptions` | *"I've been assuming X — right, wrong, or nearly?"* |
| 3 | **Blank dimension** | An empty dimension in the register, especially one that blocked an answer you gave | *"The vault knows nothing about X — <one concrete question>"* |
| 4 | **Stalled commitment** | A project untouched for >14 days, a task carried forward repeatedly, a question rotting in `cortex/00_Inbox/` | *"X hasn't moved in N days — dead, blocked, or want me to take it?"* |
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

**Then the correction footer**, per `AGENTS.md`. Their answers became notes and every question went
into the daily note, and neither of those is visible from the conversation:

```
Captured: [[Note title]] · logged 2 questions to cortex/Daily/2026-08-18.md
(say "that's not what I meant" and I'll rewrite it)
```

One line, at the end, naming the actual notes. **A run that asked nothing wrote nothing and gets no
footer** — silence stays silent, which is the whole point of section 4. A run they disengaged from
still gets it if you already captured an answer.

Don't commit — whatever invoked you handles that.

## Topic path — the profile instrument

`AGENTS.md` says that when the profile gets built by interviewing them, **the human picks the
instrument**: the ordinary preferences interview, or a Big Five inventory. This is where that choice
lives — `setup` mentions it in one line on its way out and deliberately runs neither, because a
first run has to stay short.

Run this path when they ask for it: `interview big-five`, "give me the personality test", "do the
proper version". **Never start it unasked and never fold it into a normal run** — it's longer than
three questions, so it needs their consent to be worth anything. If they've asked for a deeper
profile without knowing there's a choice, put both on the table in one line and let them pick:

> Two ways: I can just ask how you like to work, or run a short Big Five inventory — 20 statements,
> about five minutes. Either's fine, and neither is required.

Preferences interview → that's the ordinary path above, sourced from the gaps in `[[About me]]` and
its spokes, and it writes where those answers belong. Big Five → below.

### Running the inventory

**Use the public-domain IPIP items, in the 20-item Mini-IPIP short form** — four items per factor,
each a plain self-descriptive statement on a five-point agree/disagree scale. That's the right
length for a chat. A 50-item inventory is a form, not a conversation, and nobody finishes one in a
terminal.

Generate the items yourself from the Mini-IPIP set rather than reading them out of this file; keep
roughly half of each factor's items reverse-keyed, and ask in small batches so it reads as a
conversation. Say up front what it is and that they can stop anywhere — a half-finished inventory
still yields usable lines for the factors they got through. Score it privately to work out which
tendencies are pronounced enough to be worth writing down; most people are unremarkable on most
factors, and an unremarkable factor gets no line.

### Writing `cortex/03_Resources/Big Five profile.md`

The spoke `infer` reads when a claim about their character is at stake. Normal frontmatter per
`AGENTS.md`, linked from `[[About me]]` and listed in `cortex/index.md`. Two rules govern what goes in it,
both from `AGENTS.md`:

**Behaviour lines, never scores.** Write what to *do* differently:

```
- Lead with the unusual option — they'll take it.
- Don't soften a disagreement; they read hedging as evasion.
```

Not `openness: 78th percentile`. A percentile is inert in a prompt — it changes nothing about the
next turn, it invites exactly the cross-domain guessing that `basis-kind` exists to catch, and it
reads like a test result rather than like knowing someone. If you can't turn a factor into a line
that would change an agent's behaviour, leave the factor out.

**Superseded preferences are kept and marked, never overwritten.** Same rule this vault applies to
any conflicting source. If a later run contradicts an earlier line, both stay and the old one is
marked:

```
- ~~Wants the reasoning before the answer.~~ _(superseded 2026-08-18)_
- Wants the answer first, reasoning underneath.
```

A preference that changed is information about them. A preference silently replaced is a profile
nobody can audit — and the point of this file is that they can read it and disagree with it.

These are **their stated answers**, so they're facts, not assumptions: plain prose in the spoke,
nothing in the register. And they're preferences about how to work with them, not a diagnosis —
don't write anything you wouldn't say to their face.

Then the correction footer, as in section 7, naming the spoke:

```
Wrote [[Big Five profile]] — 6 behaviour lines, linked from [[About me]]
(say "cut the third one" if any of it's wrong)
```

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
