# interview — the brain asks *them*

Every other command answers a question. This one works out what the vault **needs to know**, and
asks for it. It's the difference between a filing cabinet and an assistant: nothing gets collected
unless somebody asks.

It has a second job, and it's the one that keeps this worth running after the first month.
Six of its seven sources look for gaps in what the vault *holds*. The seventh looks for gaps in
what the vault *does* — a part of their life it has never touched, offered as something concrete it
could build. **People don't ask for things they don't know are possible**, so if this command only
ever asks about material that already exists, it can only ever get better at a job it was already
doing.

Optional argument — a source to focus on (`followups`, `assumptions`, `gaps`, `stalled`,
`unmet`), `dry-run` to build the queue and show it without asking anything, or `big-five` to run
the personality inventory instead of the queue (see **Topic path — the profile instrument**, below).

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

**Never source a question from a note that shipped with the vault.** The examples in
`cortex/03_Resources/` carry `example` in their `tags:` and exist to show the shape of a note —
they are not the human's material, and nothing in them is evidence about the human. Skip them when
building the queue, exactly as you'd skip a file in `brain/`.

This is the single most likely way this command embarrasses itself, because it fails precisely when
someone is least able to shrug it off. On a fresh vault the shipped notes are most of what there is
to read, so the queue fills with them and the first question a new user ever gets is about a
template — "you seem interested in note atomicity" — when they have not written a word. It reads as
a brain that has confused its own packaging for knowing them, and it is worse than silence by a
wide margin. **Silence is the correct output there. See section 4.**

Read the spoke `cortex/03_Resources/What I'm into.md` too, **where it would sharpen a question** —
`AGENTS.md` names this command as one of its readers. It's what turns "anything on the reading
pile?" into a question about the thing they actually care about, and it's often what breaks a tie
between two candidates of equal rank. **If it doesn't exist, that's normal** in a young vault —
spokes appear when there's something real to put in them. Build the queue without it, don't block
on it, and don't ask them to fill it in.

Seven sources. Each yields candidates; each candidate carries its citation:

| # | Source | What to look for | Shape of the question |
| --- | --- | --- | --- |
| 1 | **Perishable follow-up** | A dated thing that has now happened with no outcome recorded — a deadline, a meeting, a shipped thing, a reply that was due | *"You had X on Tuesday — how did it go?"* |
| 2 | **Open assumption** | `open` rows in the register, ranked as in `review-assumptions` | *"I've been assuming X — right, wrong, or nearly?"* |
| 3 | **Blank dimension** | An empty dimension in the register, especially one that blocked an answer you gave | *"The vault knows nothing about X — <one concrete question>"* |
| 4 | **Stalled commitment** | A project untouched for >14 days, a task carried forward repeatedly, a question rotting in `cortex/00_Inbox/` | *"X hasn't moved in N days — dead, blocked, or want me to take it?"* |
| 5 | **Coverage imbalance** | An area with almost nothing against one that's overflowing | *"Is X dormant, or just not getting captured?"* |
| 6 | **Contradiction** | Two notes that disagree and `maintain` couldn't resolve | *"These two disagree — which is current?"* |
| 7 | **Unmet need** | A part of their life they've told you about that this vault does nothing for — see below, it has its own rules | *"You train five mornings a week and none of it is here — want me to do something with that?"* |

Source 4 escalates rather than repeats. After a couple of mentions the question stops being a
reminder and becomes **"want me to pick this up?"** — offering to do the work and hand back
something to approve. A reminder repeated a third time is nagging, and nagging gets the whole
channel muted.

### Source 7 — the unmet need, and why it is different from the other six

The other six ask about **something in the vault**. This one asks about **something that isn't** —
a whole area of their life the vault does nothing for, where they've never thought to ask whether
it could.

It exists because of a specific way this command goes stale. Someone uses the vault well for six
months, everything perishable gets asked about, the register is tidy, no project is stalled — and
`interview` correctly goes quiet, forever. Meanwhile they train five mornings a week, or run a
side business, or manage three kids' schedules across four apps, and it has never once occurred to
them that any of that is something an assistant could touch. **They aren't going to ask, because
people don't ask for things they don't know are possible.** Nothing else here closes that gap:
Nothing else does — which is why source 7 below exists, and why it is the one that has to be good.

**It is still cited, and the citation rule is not relaxed.** What it cites is different in kind —
not a note that exists, but something they *said* set against a gap:

| Cite | Looks like |
| --- | --- |
| A life area named in `[[About me]]`, `[[What I'm into]]` or any note, with nothing in the vault against it | *"Your profile says you coach a junior team — there's nothing here about it"* |
| A service in `[[My systems]]` at rung 1 or 2 that never got connected | *"You mentioned Todoist back in March and we never hooked it up"* |
| A friction they described in passing, in a note or a past answer, and nothing was built for it | *"You said invoicing eats your Sundays"* |

**Never from anywhere else.** Not from what people like them usually want, not from which apps are
installed, not from the shape of their repo — see *Answer from the vault, not from the room you're
standing in* in `AGENTS.md`. If you cannot quote the thing they said, there is no candidate here,
and inventing one is worse than every other failure in this file: a question about a life they
don't have proves the brain doesn't know them, on the one subject where it was claiming to.

**Five rules, all of them load-bearing:**

- **Name what you'd build, in the question.** This source offers a capability; it does not collect
  data. *"Want to tell me about your training?"* is data collection wearing a helpful hat and it
  earns nothing. *"Your watch exports to Strava, and Strava has a connector — I could pull your
  week in and put it in the Sunday brief. Worth doing?"* is an offer they can say yes to.
- **Check it's reachable before you offer it.** Run the ladder in `brain/prompts/new-idea.md` first.
  Offering something that turns out to be a locked box is how every other claim you make becomes
  suspect — and this is the one source where the temptation to overpromise is built in, because
  you're pitching rather than asking.
- **One per run, ranked last, and it never displaces a perishable question.** It is the least
  urgent thing here by construction. But it is also the only source that can still fire on a mature
  vault where nothing is perishable — which is precisely when this command otherwise goes silent
  for good.
- **Never re-pitch.** Read `[[What I want this brain to do]]` first and skip anything already on
  it, built or declined. Being offered the same idea twice is how a channel gets muted, and it is
  the same rule source 7 runs on.
- **Not a therapist, and not a life coach.** They describe a mess; you go straight to the system
  that holds it and what could reach it. No sympathy, no observations about their habits, no
  suggestions about how they might live differently. Same rule as `new-idea`'s Discuss, for the
  same reason — the service is that the thing gets less broken, not that it gets discussed.

**If they say yes, hand off rather than building it here.** `new-idea` owns all of it: a service a
tool already covers ends at its connect path, anything else gets its security review. Then write it to
`[[What I want this brain to do]]` whether or not it got built that day, so the next run doesn't
raise it again.

**The young-vault floor in section 4 still applies to this source, and applies hardest.** A vault
with nothing in it is *all* unmet need, so this source would fire on every gap it has and produce
exactly the "you seem interested in note atomicity" failure that section exists to prevent. Below
the floor, stay silent and route to `start` — which is where a brand-new user gets known — and to
`new-idea`, which is where they get something built.

## 2. Rank by what the answer is worth

1. **Perishability first.** A fact about to evaporate outranks everything. "How did it go?" is worth
   a lot today, little next week, nothing next month — and then the vault has a permanent hole where
   a real event was. This is the single strongest reason to interrupt anyone.
2. **Does the answer unblock something?** It kills or confirms an assumption, fills a dimension,
   unsticks a stalled project.
3. **Cost to answer.** One sentence beats a paragraph. Prefer a question they can answer in the time
   it takes to read it.
4. **Source 7 sorts below all of the above**, and above nothing. It is what you ask when there is
   genuinely nothing perishable, blocked or stalled worth an interruption — never instead of one.

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

On a nearly empty vault, that's most runs: there's no history to notice anything in.

**Check for that before building a queue at all.** If, after dropping the shipped examples above,
the vault holds **fewer than about ten notes the human actually made** — or `[[About me]]` is
missing or blank — then this command has nothing to work with and should say so in one line rather
than scraping the bottom of the barrel:

> Nothing worth asking yet — I need a bit of your material first. `start` writes the profile, and
> `teach me what this is` is worth ten minutes if you want to see what this is actually for.

That's the whole output. **Don't manufacture an icebreaker, and don't fall back on the profile
questions** — `start` owns those, and asking them here produces an interview that duplicates the
first-run one while pretending to be sourced. A gap this command genuinely cannot fill is a gap it
should name and route away from, not paper over.

`teach` earns its place in that line because the young-vault problem is almost never that the human
won't answer questions. It's that nobody has shown them what the thing is for, so there is nothing
in it to ask about — and answering that is exactly what `teach` does, from this repo's own
documents.

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
instrument**: the ordinary preferences interview, or a Big Five inventory. **This section is the
single specification of that inventory**, and one caller reads it:

- **`interview big-five`** — this command, when they ask for it directly. `start` points at it in
  its close and never runs it.

Keep it that way. If the inventory ever needs changing, it should need changing here and nowhere
else.

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
