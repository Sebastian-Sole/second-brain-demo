# routing-eval — does plain English reach the right command?

The vault routes natural language to a command **silently**: the human types "whats it like out",
never `/weather`, and never sees a line saying which prompt fired. Silent routing is the right
call — nobody wants a tour of the machinery — but it means a misroute looks exactly like a correct
route until something wrong gets written. This file is the only thing standing between those two.

The routing table under **"### Routing — what to run when nobody names a command"** in
[`AGENTS.md`](../AGENTS.md) is what's under test. This file is the test set.

Every utterance below is written the way somebody actually types: lowercase, abbreviated, no
command vocabulary. That's deliberate. A test set written in the words of the routing table proves
only that the table contains its own words.

---

## How to run this

1. **Open a fresh session** in this vault — a new agent that has *not* read this file.
   This is the whole method. An agent that just read the expected answers will route correctly for
   the wrong reason, and you'll have measured its reading comprehension instead of its routing.
   If you're the agent that just wrote or read this file, you cannot run it. Hand it off.
2. Paste **one utterance, verbatim**, as the entire message. No preamble, no "testing routing", no
   file path. Any framing you add is a hint that won't exist in real use.
3. Note **which command it actually ran**. Routing is silent, so you'll be inferring it from
   behaviour: what it read, what it wrote, the shape of the answer, and the correction footer that
   any write leaves behind. `git status` after the turn is the cheapest evidence for writes.
4. Compare against **Expected**. Score it: pass, or fail with what it did instead.
5. **Undo the writes** before the next utterance — `git checkout .` / `git clean -fd`, or run the
   whole pass on a scratch branch. Test 7 opens a real task file; test 17 writes a real digest.
6. One fresh session **per utterance** where you can afford it. Conversation history is context,
   and context routes. At minimum, start fresh whenever the previous utterance wrote something.

**Scoring the tools.** `email`, `calendar`, `news` and `weather` may be unconfigured on the machine
you're testing. That's still a pass: the command was reached, and its declared `fallback:` firing
("No calendar connector is configured…") is proof it was reached. A pass is *the right command was
chosen*, never *the answer was good*.

**Scoring an empty vault.** This vault is close to empty. `ask` rows still expect `ask` — routing
to `ask` and honestly reporting "nothing here about that" is a pass. Routing to `teach` and
teaching the topic instead is a **fail**, and it's the exact failure the `ask`/`teach` rows exist
to catch. Likewise `infer`: its own gate makes it decline under ten human-written notes. Reaching
`infer` and watching it decline is a pass.

**Scoring "ask the human".** Four rows expect no routing at all — the correct move is one short
clarifying question. Routing anywhere without asking is a fail, *including* routing to `capture`.

**Scoring "say it can't".** Row 41 also expects no routing, but it isn't a question to the human:
the table instructs the router to *say* the vault can't do this. A short "I can't search for places
from here" passes. Running `location` passes nothing, even if it volunteers the same caveat after —
the table's wording is "say that **rather than routing here**".

---

## The set

60 utterances. `Hard` marks a known collision — two table rows that both plausibly match. Those are
the rows worth reading the reason column on, because a failure there is a table problem, not a
model problem.

| # | Utterance | Expected | Hard | Why |
| --- | --- | --- | --- | --- |
| 1 | `just cloned this thing, where do i start` | `start` | | First run with `[[About me]]` blank is `start`'s first trigger. |
| 2 | `make this actually mine` | `start` | | "make this mine" is verbatim the intent `start` claims. |
| 3 | `ask me something, ive got five minutes` | `interview` | | They're offering to fill gaps — the one command that asks *them*. |
| 4 | `what dont you know about me yet` | `interview` | ⚠ interview vs ask | A question *about* the vault's gaps is a request to be interviewed, not a lookup. |
| 5 | `what do you know about me` | `ask` | ⚠ interview vs ask | Mirror of 4. Same shape, opposite direction: retrieve the profile, don't start asking. |
| 6 | `remember that retry budgets beat retry counts` | `capture` | ⚠ capture vs task | "remember that" + a claim = a note. There is no next action in this sentence. |
| 7 | `remember to cancel the insurance before the 30th` | `task` | ⚠ capture vs task | "remember to" + a deadline = a task. One word apart from 6 and a different file. |
| 8 | `here, read this https://example.com/post — want to keep it` | `capture` | | A pasted link is `capture`'s bread and butter; the original goes to `cortex/raw/` first. |
| 9 | `what did i land on for auth in the end` | `ask` | | "why did we choose Z" phrased like a human. One decision, one note. |
| 10 | `did i ever write anything down about connection pooling` | `ask` | | "did I write anything on Y" — a retrieval question with the word "write" in it. |
| 11 | `tell me about retries` | `ask` | ⚠ ask vs teach | Their own past thinking played back. See ambiguity A1 — this one is contents-dependent. |
| 12 | `explain retries to me` | `teach` | ⚠ ask vs teach | They want to understand, not to retrieve. Same topic as 11, opposite command. |
| 13 | `i still dont get how oauth refresh tokens work` | `teach` | | "I don't get Y" is a `teach` trigger with no retrieval intent in it. |
| 14 | `walk me through what a vector db is actually doing` | `teach` | | "walk me through Z" — teaching, and it must not write anything afterwards. One question, so no course offer either. |
| 15 | `chase mats about the invoice` | `task` | | "chase X" is named in the table. A next action with a person attached. |
| 16 | `the tax thing is done, close it off` | `task` | | Marking one done is `task`, not a new capture — and it needs a `completed:` date. |
| 17 | `what have i been working on` | `digest` | ⚠ digest vs ask | Activity across many notes and a window, not one answer in one note. |
| 18 | `what did i decide about the pricing page` | `ask` | ⚠ digest vs ask | Mirror of 17. One decision, one note — a digest here is an expensive wrong answer. |
| 19 | `whats been sitting there not moving` | `digest` | | "what's stalled" in the human's words; `digest` has a Stalled section for exactly this. |
| 20 | `inbox is out of control, sort it` | `maintain` | ⚠ maintain vs email | The vault's `cortex/00_Inbox/`, not a mailbox — "the inbox has visibly grown" is `maintain`'s trigger. |
| 21 | `tidy up before i log off` | `maintain` | | "tidy up" + "close out the day" — both `maintain` triggers in one sentence. |
| 22 | `somethings broken, capture blew up last time i ran it` | `doctor` | | A command failing is install health, and `doctor` is a script to run, not a prompt. |
| 23 | `is this thing even working` | `doctor` | ⚠ maintain vs doctor | "is this thing working" verbatim. Install health, nothing to do with note quality. |
| 24 | `the vaults a mess` | `maintain` | ⚠ maintain vs doctor | Mirror of 23. Messy *contents* is `maintain`; `doctor` would report a clean bill and miss the point. |
| 25 | `i want it to also do a weekly review thing` | `new-idea` | | "I want it to also do X" — adding capability, with the security review that entails. |
| 26 | `can you hook this up to my strava` | `new-idea` | | `new-idea` owns "connect it to my <service>" at every rung; whether a tool exists only decides where inside the run it ends (the connect path in Discuss), not which command fires. |
| 27 | `can you read my old codex chats and make them searchable` | `ingest-sessions` | | "make my history searchable" — and it must ask which projects before reading any. |
| 28 | `pull in what i was doing in those claude sessions last month` | `ingest-sessions` | | Past sessions on disk, distilled. Not this session. |
| 29 | `write down what we just did here` | `capture` | ⚠ capture vs ingest-sessions | *This* session is `capture`'s job; `ingest-sessions` is only for transcripts already on disk. |
| 30 | `am i actually going to finish this side project` | `infer` | | "would I actually finish this" — a question about them the vault never states outright. |
| 31 | `what am i avoiding right now` | `infer` | | Named in the table. Expect labelled assumptions with falsifiers, or the young-vault refusal. |
| 32 | `do i work better in the mornings` | `infer` | ⚠ capture vs infer | A question with no fact behind it. `ask` first, then reason — and label the leap. |
| 33 | `i work better in the mornings` | `capture` | ⚠ capture vs infer | Mirror of 32. A stated fact about themselves is a note, not a prompt to go reasoning. |
| 34 | `what have you been guessing about me` | `review-assumptions` | ⚠ vs interview | "what have you guessed about me" verbatim, and `interview` now cedes the register to it explicitly. |
| 35 | `lets go through those guesses, ill tell you which are wrong` | `review-assumptions` | | A verdict pass over open assumptions, five at most, tap-fast. |
| 36 | `whats it like out` | `weather` | ⚠ needs `location` first | `weather` with no place named must call `location` for coordinates, not guess a city. |
| 37 | `do i need a coat tomorrow` | `weather` | ⚠ needs `location` first | Named in the table. Also needs the multi-day parameters, and still needs coordinates. |
| 38 | `whats the weather in bergen this weekend` | `weather` | | Contrast with 36/37: a named place means `weather` skips `location` entirely. |
| 39 | `where am i` | `location` | | The one-line job of `location`, and the answer must say it came from the IP. |
| 40 | `what time is it here` | `location` | | "what time is it here" is in the table — the answer depends on where they are. |
| 41 | `wheres the nearest post office` | **say it can't** | ⚠ | `location`'s **Not for** now excludes this outright: "nothing in this vault searches for places, **so say that rather than routing here**." Routing to `location` and reciting the city is a fail. See A10. |
| 42 | `anything new in llm land` | `news` | | "anything new in Y" — and it reads *their* feeds, or asks for them if the note is missing. |
| 43 | `whats happening with the nvidia thing` | `news` | ⚠ news vs ask | "what's happening with X" — outside world, their sources, not their notes. |
| 44 | `what do i actually think about nvidia` | `ask` | ⚠ news vs ask | Mirror of 43. "What do *I* think about X" is explicitly not `news`. |
| 45 | `did anna ever get back to me` | `email` | | "did X reply" verbatim. Read-only, no state changes to the mailbox. |
| 46 | `whats sitting in my inbox` | `email` | ⚠ email vs maintain | Mirror of 20. Same word, different inbox — and the wrong guess reorganises the vault. |
| 47 | `draft something back to the landlord about the deposit` | `email` | | Drafting is inside the ceiling. It creates a draft, so it owes a correction footer. |
| 48 | `whats on today` | `calendar` | | Verbatim from the table. |
| 49 | `am i free thursday afternoon` | `calendar` | | Verbatim from the table. |
| 50 | `pencil in coffee with mats friday` | `calendar` | ⚠ | "pencil something in" is a calendar sentence, so `calendar` is still the right route — but the ceiling now says read-only, so a pass is reaching `calendar` **and** being told it can't create the event. Making one is a fail; so is routing to `task`. |
| 51 | `send that reply to anna` | `email` | ⚠ ceiling | Route to `email`, then refuse to send in the prescribed sentence and leave a draft. Sending is a fail. |
| 52 | `coffee at the place on the corner was way better than usual today` | `capture` | ↓ fallback | Nothing else matches. A note in the inbox is the documented safe default. |
| 53 | `had a weird dream about the office being underwater` | `capture` | ↓ fallback | No question, no action, no topic any command owns. Directive 1: never lose a capture. |
| 54 | `my back hurts every time i sit at the kitchen table` | `capture` | ↓ fallback | Not a task (no action stated), not a question. It gets written down. |
| 55 | `mats said the thing about ferries again at dinner` | `capture` | ↓ fallback | Unfiled, half-formed, and exactly what `cortex/00_Inbox/` is for. |
| 56 | `i keep humming that song from the ad` | `capture` | ↓ fallback | The floor of the router. A router that never falls back is as broken as one that always does. |
| 57 | `remember the thing with the bank` | **ask the human** | ⚠ ambiguous | `capture` (a note) or `task` (call the bank)? "the thing" hides the verb. One question settles it. |
| 58 | `sort out the inbox` | **ask the human** | ⚠ ambiguous | Which inbox — `cortex/00_Inbox/` or the mailbox? Guessing wrong rewrites files or touches mail. |
| 59 | `can you deal with the anna thing` | **ask the human** | ⚠ ambiguous | `email`, `calendar` and `task` all fit, and all three have side effects. Ask. |
| 60 | `book the thing for tuesday` | **ask the human** | ⚠ ambiguous | "book" implies committing, which the ceiling forbids, and "the thing" names nothing. Ask before drafting. |

**Per-command coverage:** start 2 · interview 2 · capture 9 · ask 6 · teach 3 · task 3 · digest 2
· maintain 3 · doctor 2 · new-idea 2 · ingest-sessions 2 · infer 3 · review-assumptions 2 ·
weather 3 · location 2 · news 2 · email 4 · calendar 3 · ask-the-human 4 · say-it-can't 1.

Fallback-to-`capture` rows (nothing else matches): **52–56**.
Ask-the-human rows: **57–60**.
Decline-without-routing row: **41**.

---

## Known ambiguities in the routing table

These are table problems, not model problems — a fail on the linked row may be the table's fault,
so read this before filing a bug against an agent.

> **Reconciled against the routing table on 2026-08-18** (`AGENTS.md`, 889 lines). Six of the eight
> items originally recorded here had since been fixed in the table and are gone; the wording that
> resolved each is logged at the bottom, so a reader can tell a fix from a quiet deletion.
>
> **This section means nothing unless it is re-checked every time the routing table changes** — the
> same trigger as [When to re-run](#when-to-re-run), and for the same reason. A resolved ambiguity
> left standing here tells a tester to "fix" the manual backwards; a live one deleted here costs a
> silent misroute nobody is looking for. Reconcile it in the same pass that re-runs the set.
>
> Retired numbers are not reused, so `A1` still means what row 11 says it means, and old entries in
> the Results table stay readable.

**A1 · `ask` vs `teach` can't be decided from the sentence** (rows 11, 12). **Still stands.**
Both rows now cede to each other — `ask` is **Not for** "a concept the vault never covered —
`teach`", and `teach` is **Not for** "handing back what they already wrote — `ask`" — so the
table is no longer silent about the collision. But both of those tests are statements about *vault
contents*, not about the utterance: "tell me about retries" is `ask` when a retries note exists and
`teach` when it doesn't. The router must search before it can route, and the table never says so.
`teach`'s prompt does handle it correctly ("stop and hand off to `ask`"); the table reads as
though the words alone decide it. Row 11's expected answer assumes a vault that has something on
the topic.

**A9 · row 26 is decided by a directory listing, not by the table** (row 26). **Resolved
2026-08-20.** When `setup` was deleted, `new-idea` took "connect it to my <service>" at every
rung: a tool already existing means the run ends at the connect path in Discuss instead of
building, but the *routing* no longer depends on the filesystem. Row 26 stays `new-idea` whether
or not a Strava tool ever ships, so the hard marker is gone and the re-run trigger below no
longer applies to this row.

**A10 · the table has three exits but counts two** (row 41). **New.**
"Two ways out of this table, and they aren't the same" names *nothing matches → `capture`* and
*several match → ask which*. There is a third: `location`'s **Not for** says finding somewhere
nearby is not a routing decision at all — "nothing in this vault searches for places, so say that
rather than routing here" — and `weather`'s says writing the forecast down is refused rather than
handed to `capture`. Both are correct answers and neither is `capture` or a question. Two rows
quietly decline, and the paragraph that enumerates the exits doesn't mention that shape. Row 41 is
scored against the `location` row, not the paragraph. Worth folding into that paragraph as a named
third exit, so a router that has only read the summary doesn't fall through to `capture`.

### Resolved since this set was written

Verified line by line against the current table on 2026-08-18, each against the file rather than a
summary. Kept as a log so nobody re-raises them.

- **A2 · `setup` vs `new-idea` on connecting a service** — fixed. The rows now partition on
  whether a tool exists: `new-idea` takes it "when `brain/tools/` has nothing for that service",
  and its **Not for** reads "connecting a service a tool already exists for — `setup`, which is
  what every tool's `fallback:` sends them to", which is exactly the contradiction that used to
  make this ambiguous. Survives as A9 in a narrower form.
- **A3 · the two inboxes** — fixed. `maintain` is **Not for** "the mail inbox — that's `email`;
  this row owns the vault folder and nothing else"; `email` is **Not for** "`cortex/00_Inbox/`, the vault
  folder — that's `maintain`". Both name the other.
- **A4 · `task` vs `email` on drafting** — fixed. `task` is now **Not for** "composing something
  now: 'draft the mail to the landlord' is `email`, not a task. A task records the intention; it
  doesn't write the text", and `email` claims "they want the text composed now" while ceding "an
  intention to deal with someone later, with no text wanted yet — `task`".
- **A5 · `interview` vs `review-assumptions`** — fixed. `interview` is **Not for** "working the
  open-assumption register for verdicts — `review-assumptions`", and says it borrows that command's
  format when an assumption surfaces; `review-assumptions` is **Not for** "anything the register
  doesn't hold — perishable follow-ups, blank dimensions, stalled work — `interview`".
- **A6 · `location` promised "nearest"** — fixed, and it flipped row 41. The row's triggers are now
  only "where am I", "what time is it here", and its **Not for** disowns nearby search outright.
  Rescored: row 41 expects a decline, not a route. Live residue tracked as A10.
- **A7 · no documented "ask the human" path** — fixed. "Two ways out of this table, and they aren't
  the same" now spells out *several match and they'd do materially different things → ask which, in
  one line, before doing either*, and ties it to prime directive 6. Rows 57–60 are scored against
  the table itself now, not against the directive.
- **A8 · `new-idea` had no prompt file** — stale. `brain/prompts/new-idea.md` exists, 214
  lines. It was mid-flight when this was written, as suspected.

---

## Results

One row per run. Keep the failures specific: the row number and what it did instead, not "some
routing issues".

| Date | Run by / agent | Passed | Failed rows (→ what it ran instead) | Notes |
| --- | --- | --- | --- | --- |
|  |  |  /60 |  |  |
|  |  |  /60 |  |  |
|  |  |  /60 |  |  |
|  |  |  /60 |  |  |

---

## When to re-run

**Any time the routing table in `AGENTS.md` changes, and any time a command or tool is added.**
A new row changes the answer to utterances that already existed — that's what a collision *is* —
so adding a command without re-running this leaves every previous result unverified. `new-idea`
is the natural place to run it: a command that ships without a routing pass is a command nobody can
reach by accident, or one that steals somebody else's traffic silently.

Also worth a run after any edit to a **Not for** column, since that column is the load-bearing one,
and after changing a tool's `fallback:` or `consent:` line, which changes what a correct route
looks like from the outside.
