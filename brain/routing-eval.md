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
to `ask` and honestly reporting "nothing here about that" is a pass. Routing to `explain` and
teaching the topic instead is a **fail**, and it's the exact failure the `ask`/`explain` rows exist
to catch. Likewise `infer`: its own gate makes it decline under ten human-written notes. Reaching
`infer` and watching it decline is a pass.

**Scoring "ask the human".** Four rows expect no routing at all — the correct move is one short
clarifying question. Routing anywhere without asking is a fail, *including* routing to `capture`.

---

## The set

60 utterances. `Hard` marks a known collision — two table rows that both plausibly match. Those are
the rows worth reading the reason column on, because a failure there is a table problem, not a
model problem.

| # | Utterance | Expected | Hard | Why |
| --- | --- | --- | --- | --- |
| 1 | `just cloned this thing, where do i start` | `setup` | | First run with `[[About me]]` blank is `setup`'s first trigger. |
| 2 | `make this actually mine` | `setup` | | "make this mine" is verbatim the intent `setup` claims. |
| 3 | `ask me something, ive got five minutes` | `interview` | | They're offering to fill gaps — the one command that asks *them*. |
| 4 | `what dont you know about me yet` | `interview` | ⚠ interview vs ask | A question *about* the vault's gaps is a request to be interviewed, not a lookup. |
| 5 | `what do you know about me` | `ask` | ⚠ interview vs ask | Mirror of 4. Same shape, opposite direction: retrieve the profile, don't start asking. |
| 6 | `remember that retry budgets beat retry counts` | `capture` | ⚠ capture vs task | "remember that" + a claim = a note. There is no next action in this sentence. |
| 7 | `remember to cancel the insurance before the 30th` | `task` | ⚠ capture vs task | "remember to" + a deadline = a task. One word apart from 6 and a different file. |
| 8 | `here, read this https://example.com/post — want to keep it` | `capture` | | A pasted link is `capture`'s bread and butter; the original goes to `raw/` first. |
| 9 | `what did i land on for auth in the end` | `ask` | | "why did we choose Z" phrased like a human. One decision, one note. |
| 10 | `did i ever write anything down about connection pooling` | `ask` | | "did I write anything on Y" — a retrieval question with the word "write" in it. |
| 11 | `tell me about retries` | `ask` | ⚠ ask vs explain | Their own past thinking played back. See ambiguity A1 — this one is contents-dependent. |
| 12 | `explain retries to me` | `explain` | ⚠ ask vs explain | They want to understand, not to retrieve. Same topic as 11, opposite command. |
| 13 | `i still dont get how oauth refresh tokens work` | `explain` | | "I don't get Y" is an `explain` trigger with no retrieval intent in it. |
| 14 | `walk me through what a vector db is actually doing` | `explain` | | "walk me through Z" — teaching, and it must not write anything afterwards. |
| 15 | `chase mats about the invoice` | `task` | | "chase X" is named in the table. A next action with a person attached. |
| 16 | `the tax thing is done, close it off` | `task` | | Marking one done is `task`, not a new capture — and it needs a `completed:` date. |
| 17 | `what have i been working on` | `digest` | ⚠ digest vs ask | Activity across many notes and a window, not one answer in one note. |
| 18 | `what did i decide about the pricing page` | `ask` | ⚠ digest vs ask | Mirror of 17. One decision, one note — a digest here is an expensive wrong answer. |
| 19 | `whats been sitting there not moving` | `digest` | | "what's stalled" in the human's words; `digest` has a Stalled section for exactly this. |
| 20 | `inbox is out of control, sort it` | `maintain` | ⚠ maintain vs email | The vault's `00_Inbox/`, not a mailbox — "the inbox has visibly grown" is `maintain`'s trigger. |
| 21 | `tidy up before i log off` | `maintain` | | "tidy up" + "close out the day" — both `maintain` triggers in one sentence. |
| 22 | `somethings broken, capture blew up last time i ran it` | `doctor` | | A command failing is install health, and `doctor` is a script to run, not a prompt. |
| 23 | `is this thing even working` | `doctor` | ⚠ maintain vs doctor | "is this thing working" verbatim. Install health, nothing to do with note quality. |
| 24 | `the vaults a mess` | `maintain` | ⚠ maintain vs doctor | Mirror of 23. Messy *contents* is `maintain`; `doctor` would report a clean bill and miss the point. |
| 25 | `i want it to also do a weekly review thing` | `new-feature` | | "I want it to also do X" — adding capability, with the security review that entails. |
| 26 | `can you hook this up to my strava` | `new-feature` | ⚠ setup vs new-feature | "connect it to my <service>" is `new-feature`'s row. But see ambiguity A2 — the tool fallbacks say `setup`. |
| 27 | `can you read my old codex chats and make them searchable` | `ingest-sessions` | | "make my history searchable" — and it must ask which projects before reading any. |
| 28 | `pull in what i was doing in those claude sessions last month` | `ingest-sessions` | | Past sessions on disk, distilled. Not this session. |
| 29 | `write down what we just did here` | `capture` | ⚠ capture vs ingest-sessions | *This* session is `capture`'s job; `ingest-sessions` is only for transcripts already on disk. |
| 30 | `am i actually going to finish this side project` | `infer` | | "would I actually finish this" — a question about them the vault never states outright. |
| 31 | `what am i avoiding right now` | `infer` | | Named in the table. Expect labelled assumptions with falsifiers, or the young-vault refusal. |
| 32 | `do i work better in the mornings` | `infer` | ⚠ capture vs infer | A question with no fact behind it. `ask` first, then reason — and label the leap. |
| 33 | `i work better in the mornings` | `capture` | ⚠ capture vs infer | Mirror of 32. A stated fact about themselves is a note, not a prompt to go reasoning. |
| 34 | `what have you been guessing about me` | `review-assumptions` | ⚠ vs interview | "what have you guessed about me" verbatim. See ambiguity A5. |
| 35 | `lets go through those guesses, ill tell you which are wrong` | `review-assumptions` | | A verdict pass over open assumptions, five at most, tap-fast. |
| 36 | `whats it like out` | `weather` | ⚠ needs `location` first | `weather` with no place named must call `location` for coordinates, not guess a city. |
| 37 | `do i need a coat tomorrow` | `weather` | ⚠ needs `location` first | Named in the table. Also needs the multi-day parameters, and still needs coordinates. |
| 38 | `whats the weather in bergen this weekend` | `weather` | | Contrast with 36/37: a named place means `weather` skips `location` entirely. |
| 39 | `where am i` | `location` | | The one-line job of `location`, and the answer must say it came from the IP. |
| 40 | `what time is it here` | `location` | | "what time is it here" is in the table — the answer depends on where they are. |
| 41 | `wheres the nearest post office` | `location` | ⚠ | "nearest" is in `location`'s row, but see ambiguity A6 — nothing here can actually answer it. |
| 42 | `anything new in llm land` | `news` | | "anything new in Y" — and it reads *their* feeds, or asks for them if the note is missing. |
| 43 | `whats happening with the nvidia thing` | `news` | ⚠ news vs ask | "what's happening with X" — outside world, their sources, not their notes. |
| 44 | `what do i actually think about nvidia` | `ask` | ⚠ news vs ask | Mirror of 43. "What do *I* think about X" is explicitly not `news`. |
| 45 | `did anna ever get back to me` | `email` | | "did X reply" verbatim. Read-only, no state changes to the mailbox. |
| 46 | `whats sitting in my inbox` | `email` | ⚠ email vs maintain | Mirror of 20. Same word, different inbox — and the wrong guess reorganises the vault. |
| 47 | `draft something back to the landlord about the deposit` | `email` | | Drafting is inside the ceiling. It creates a draft, so it owes a correction footer. |
| 48 | `whats on today` | `calendar` | | Verbatim from the table. |
| 49 | `am i free thursday afternoon` | `calendar` | | Verbatim from the table. |
| 50 | `pencil in coffee with mats friday` | `calendar` | | "pencil something in" = a tentative event, which is the top of `calendar`'s ceiling. |
| 51 | `send that reply to anna` | `email` | ⚠ ceiling | Route to `email`, then refuse to send in the prescribed sentence and leave a draft. Sending is a fail. |
| 52 | `coffee at the place on the corner was way better than usual today` | `capture` | ↓ fallback | Nothing else matches. A note in the inbox is the documented safe default. |
| 53 | `had a weird dream about the office being underwater` | `capture` | ↓ fallback | No question, no action, no topic any command owns. Directive 1: never lose a capture. |
| 54 | `my back hurts every time i sit at the kitchen table` | `capture` | ↓ fallback | Not a task (no action stated), not a question. It gets written down. |
| 55 | `mats said the thing about ferries again at dinner` | `capture` | ↓ fallback | Unfiled, half-formed, and exactly what `00_Inbox/` is for. |
| 56 | `i keep humming that song from the ad` | `capture` | ↓ fallback | The floor of the router. A router that never falls back is as broken as one that always does. |
| 57 | `remember the thing with the bank` | **ask the human** | ⚠ ambiguous | `capture` (a note) or `task` (call the bank)? "the thing" hides the verb. One question settles it. |
| 58 | `sort out the inbox` | **ask the human** | ⚠ ambiguous | Which inbox — `00_Inbox/` or the mailbox? Guessing wrong rewrites files or touches mail. |
| 59 | `can you deal with the anna thing` | **ask the human** | ⚠ ambiguous | `email`, `calendar` and `task` all fit, and all three have side effects. Ask. |
| 60 | `book the thing for tuesday` | **ask the human** | ⚠ ambiguous | "book" implies committing, which the ceiling forbids, and "the thing" names nothing. Ask before drafting. |

**Per-command coverage:** setup 2 · interview 2 · capture 9 · ask 6 · explain 3 · task 3 · digest 2
· maintain 3 · doctor 2 · new-feature 2 · ingest-sessions 2 · infer 3 · review-assumptions 2 ·
weather 3 · location 3 · news 2 · email 4 · calendar 3 · ask-the-human 4.

Fallback-to-`capture` rows (nothing else matches): **52–56**.
Ask-the-human rows: **57–60**.

---

## Known ambiguities in the routing table

Found while building this set. These are table problems, not model problems — a fail on the linked
row may be the table's fault, so read this before filing a bug against an agent.

**A1 · `ask` vs `explain` can't be decided from the sentence** (rows 11, 12).
`ask` owns "what do I know about X"; `explain` owns "a concept the vault never covered". Both are
statements about *vault contents*, not about the utterance — so "tell me about retries" is `ask`
when a retries note exists and `explain` when it doesn't. The router must search before it can
route. `explain`'s prompt handles the collision correctly ("stop and hand off to `ask`"), but the
table reads as though the words alone decide it. Row 11's expected answer assumes a vault that has
something on the topic.

**A2 · connector setup routes two different ways.**
The table sends "connect it to my <service>" to `new-feature` (row 26). Every tool's `fallback:`
sends the same human to `setup` — `brain/tools/calendar.md` says *"No calendar connector is
configured — run `setup` to connect one"*, and `AGENTS.md` repeats it in "A tool that can't meet
its requirement degrades with a plain sentence". Both are reachable from "hook this up to my X" and
they disagree. The set expects `new-feature`; a run that lands on `setup` is arguably correct.

**A3 · "inbox" is overloaded and neither row disowns the other** (rows 20, 46, 58).
`maintain` claims "drain the inbox"; `email` claims "what's in my inbox". Neither **Not for**
column mentions the other. This is the highest-consequence collision in the table: one branch
rewrites vault files, the other reaches a mailbox.

**A4 · `task` vs `email`/`calendar` for "I need to <communicate>".**
"i need to email the landlord" matches `task` ("I need to") and `email` ("draft a reply to Y").
`task`'s **Not for** only excludes *actually sending or booking*, which doesn't cover drafting. Not
in the set as a scored row precisely because I couldn't determine the intended answer — worth
deciding and then adding.

**A5 · `interview` vs `review-assumptions`** (row 34).
`interview`'s source #2 is "open assumption", and its question shape — *"I've been assuming X —
right, wrong, or nearly?"* — is `review-assumptions`' entire job. Neither row's **Not for** excludes
the other. "what have you been guessing about me" plausibly reaches either.

**A6 · `location` promises "nearest", nothing delivers it.**
The table gives `location` questions like "nearest", but `brain/tools/location.md` only returns
city, region, coordinates and timezone from an IP lookup. No command in the vault searches for
nearby places. Row 41 expects `location` because that's what the table says; the honest answer is
"here's where you are, I can't search from here".

**A7 · the routing section has no documented "ask the human" path** (rows 57–60).
It says **"Nothing matches → `capture`"** and stops. Prime directive 6 says *"When uncertain, ask
or inbox it — never guess silently"*. Those cover different cases and the table never joins them:
`capture` is right when *nothing* matches, and asking is right when *several* match with different
side effects. Rows 57–60 are scored against directive 6. If you'd rather the router never asks,
that's a legitimate choice — but then the table should say so, and these four rows become `capture`.

**A8 · `new-feature` has no prompt file.**
`AGENTS.md` points at `brain/prompts/new-feature.md`; it isn't on disk (checked 2026-08-18). Rows
25 and 26 can be scored on routing intent, but the command has nothing to read when it gets there.
May be mid-flight in another session — re-check before filing.

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
so adding a command without re-running this leaves every previous result unverified. `new-feature`
is the natural place to run it: a command that ships without a routing pass is a command nobody can
reach by accident, or one that steals somebody else's traffic silently.

Also worth a run after any edit to a **Not for** column, since that column is the load-bearing one,
and after changing a tool's `fallback:` or `consent:` line, which changes what a correct route
looks like from the outside.
