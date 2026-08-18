# Plan 002: Correct five places that still promise mail and calendar never write

> **Executor instructions**: Follow this plan step by step. Run every
> verification command and confirm the expected result before moving to the
> next step. If anything in the "STOP conditions" section occurs, stop and
> report — do not improvise. When done, update the status row for this plan
> in `plans/README.md`.
>
> **Drift check (run first)**:
> `git diff --stat bec2c00..HEAD -- .claude/commands/email.md .claude/commands/calendar.md README.md AGENTS.md`
> If any of those files changed since this plan was written, compare the
> "Current state" excerpts against the live text before proceeding; on a
> mismatch, treat it as a STOP condition.

## Status

- **Priority**: P1
- **Effort**: S
- **Risk**: LOW
- **Depends on**: none
- **Category**: docs
- **Planned at**: commit `bec2c00`, 2026-08-18

## Why this matters

Commit `bec2c00` ("brain: mail and calendar act on approval, not prohibition")
changed the rule for the `email` and `calendar` tools. They used to be described
as never writing anything. They now read freely, draft by default, and perform a
send or create an event when the human asks for it in that turn **and** approves
the permission prompt.

That commit updated eleven files. It missed five lines, which still state the
old, stronger promise. They fall into two groups, and both matter for a
different reason:

- **Two are the `description:` of a slash command** — the one sentence the human
  reads in the command menu at the moment they invoke the tool. That is the worst
  possible place for this error: a person who believes the tool cannot send is a
  person who reads an approval prompt less carefully.
- **Two are rows in the routing table in `AGENTS.md`**, which is what the agent
  itself reads to decide how to behave. Both rows now contradict themselves in a
  single sentence: they say an action happens "never", then point the reader at
  "the ceiling", which permits that same action on two gates. An agent reading
  the word "never" may refuse a send the human legitimately asked for and
  approved — the rule failing in the opposite direction, but still failing.

The fifth is a line in `README.md`.

`brain/bin/doctor` cannot catch any of this. Its wrapper check at lines 451-467
only confirms that a wrapper points at a file that exists; it has no view of
whether the wrapper's prose is true. This class of error is invisible to the
harness, so it must be corrected by hand.

## Current state

Five lines in four files. All wrong in the same way.

### 1. `.claude/commands/email.md:2`

```
description: Read your mailbox and answer from it — reads and drafts, never sends.
```

### 2. `.claude/commands/calendar.md:2`

```
description: Read your schedule and answer from it — reads and drafts, never responds or reschedules.
```

### 3. `README.md:270`

```
2. **Connect your mail and calendar.** The `email` and `calendar` tools are already here and read-only by design; connecting them turns everything already written down about your week into free context. Highest-leverage move available.
```

The wrong phrase is `read-only by design`.

### 4. `AGENTS.md:891` — the `email` row of the routing table

```
| `email` | "what's in my inbox" meaning the mail account, "did X reply", "draft a reply to Y", "email X about Z" — they want the text composed now | `cortex/00_Inbox/`, the vault folder — that's `maintain`. An intention to deal with someone later, with no text wanted yet — `task`. Sending, replying, forwarding, deleting or labelling — never, see the ceiling. |
```

The wrong phrase is the final sentence of the third column:
`Sending, replying, forwarding, deleting or labelling — never, see the ceiling.`

### 5. `AGENTS.md:892` — the `calendar` row of the routing table

```
| `calendar` | "what's on today", "am I free Thursday", "pencil something in" | Accepting, declining, moving or cancelling anything — never, see the ceiling. |
```

The wrong phrase is the whole third column:
`Accepting, declining, moving or cancelling anything — never, see the ceiling.`

### The true rule, as the repository now states it

You must match this. Quote from these sources; do not invent new wording.

`AGENTS.md:754-755`, the tools table — **already correct**, updated by `bec2c00`:

```
| `email` | `brain/tools/email.md` | The connected mailbox — read, draft, and send when asked | Drafts always; sends and mailbox changes only on an explicit request |
| `calendar` | `brain/tools/calendar.md` | The connected calendar — read, and write when asked | Nothing, unless the human asks for an event |
```

`brain/tools/email.md:5` and `brain/tools/calendar.md:5`, the frontmatter the
tools actually run on — **already correct**:

```yaml
writes: drafts; sends and mailbox changes only when asked
writes: events, and only when asked
```

`AGENTS.md:808-826`, the section titled "Mail and calendar act only when asked",
states the two gates in full, plus one further rule you must preserve:

> **Never propose a destructive action.** Trash, delete, mark spam, archive a
> thread, remove a label — carry one out if the human names it, and never be the
> one to raise it.

That restraint is real and must survive your edit. What changes is the claim
that these actions never happen; what stays is that the agent never offers them.

### Repository conventions you must match

- **A wrapper file is thin and stays thin.** Every file in `.claude/commands/`
  is a four-line pointer at the real prompt, each ending with an HTML comment
  reading "Don't add instructions here". You are editing one line of frontmatter.
  Change nothing else.
- **The `description:` is one sentence and appears in a menu.** Every existing
  description is a single line under about 110 characters, shaped as: what it
  does, then a spaced em-dash, then the limit. Compare the other 16 files in
  `.claude/commands/`.
- **The routing table's third column is the "Not for" column.** `AGENTS.md:886`
  calls it "the load-bearing one" and says every row must say whose territory a
  request *isn't*. Keep that job. Your edit must still tell the router what to
  send elsewhere; it must stop claiming the tool cannot act.
- **Punctuation.** This repository uses a spaced em-dash (` — `). Copy the
  character from the existing line rather than typing one.
- **`README.md` is written for a non-programmer.** Short clauses, no jargon, the
  promise in the second person. `GUIDE.md:321-323` already says it correctly for
  a reader of that document — use it as the model.

## Commands you will need

This repository has no build, no package manager and no test runner.
Verification is grep, plus one script.

| Purpose | Command | Expected on success |
|---|---|---|
| Check the install | `brain/bin/doctor --check` | exit 0, no `[XX]` lines |
| Find stale claims | see Step 5 | no matches in the in-scope lines |
| Confirm scope | `git status --porcelain` | only the four in-scope files |

## Scope

**In scope** — five lines, in four files. Modify **only these lines**:

- `.claude/commands/email.md` — line 2 only
- `.claude/commands/calendar.md` — line 2 only
- `README.md` — line 270 only
- `AGENTS.md` — lines 891 and 892 only

**Out of scope** (do NOT touch):

- `brain/tools/email.md` and `brain/tools/calendar.md` — already correct, and
  they are the source of truth. `AGENTS.md:758` says that where the table and a
  tool's frontmatter disagree, the frontmatter wins. You are correcting the
  documentation to agree with it, never the other way round.
- **`AGENTS.md:784`** — contains the words "never sends" and is **correct**,
  because it is qualified in the same sentence: "never sends, changes or deletes
  anything the human did not ask for in that turn". Leave it exactly as it is.
- **`AGENTS.md:808-826`**, the ceiling section itself — already correct.
- **`AGENTS.md:804`** — "a tool never sends vault content to a third party without
  saying so in the same reply". A different rule about disclosure, correct, out of
  scope.
- **`GUIDE.md:322`** — contains "it never sends unless you ask it to and then
  approve it". Qualified, correct, out of scope.
- The rest of `README.md`. Item 2 of that numbered list is the only wrong line.
- `.claude/settings.json` — the `ask` list is already correct.
- `brain/bin/doctor` — teaching it to check that a wrapper's prose stays true is
  a real idea and deliberately not part of this plan. See Maintenance notes.

## Git workflow

- Branch: `advisor/002-correct-stale-mail-and-calendar-promises`
- One commit. Message style, from `git log`: a short lowercase subject naming
  the effect, e.g.
  `brain: correct five places that still say mail and calendar never write`
- Do NOT push and do NOT open a pull request.

## Steps

### Step 1: Correct the `email` wrapper

In `.claude/commands/email.md`, replace line 2 with exactly:

```
description: Read your mailbox and answer from it — drafts always; sends only when you ask and approve.
```

**Verify**:

```sh
sed -n '2p' .claude/commands/email.md
wc -l < .claude/commands/email.md
```

→ the new line exactly, then `10`.

### Step 2: Correct the `calendar` wrapper

In `.claude/commands/calendar.md`, replace line 2 with exactly:

```
description: Read your schedule and answer from it — creates an event only when you ask and approve.
```

**Verify**:

```sh
sed -n '2p' .claude/commands/calendar.md
wc -l < .claude/commands/calendar.md
```

→ the new line exactly, then `10`.

### Step 3: Correct `README.md`

In `README.md`, replace line 270 with exactly:

```
2. **Connect your mail and calendar.** The `email` and `calendar` tools are already here — they read freely and draft by default, and a send or a new event needs you to ask for it and then approve the prompt; connecting them turns everything already written down about your week into free context. Highest-leverage move available.
```

**Verify**:

```sh
grep -c 'read-only by design' README.md
sed -n '270p' README.md | grep -c 'approve the prompt'
```

→ `0`, then `1`.

### Step 4: Correct the two routing-table rows in `AGENTS.md`

These are single-line markdown table rows. Keep all four pipe characters and
both other columns byte-identical. Only the third column's wording changes.

Replace line 891 with exactly:

```
| `email` | "what's in my inbox" meaning the mail account, "did X reply", "draft a reply to Y", "email X about Z" — they want the text composed now | `cortex/00_Inbox/`, the vault folder — that's `maintain`. An intention to deal with someone later, with no text wanted yet — `task`. Sending, replying, forwarding, deleting and labelling belong here too, but only on an explicit request plus an approved prompt, and you never raise a destructive one yourself — see the ceiling. |
```

Replace line 892 with exactly:

```
| `calendar` | "what's on today", "am I free Thursday", "pencil something in" | Accepting, declining, moving and cancelling belong here too, but only on an explicit request plus an approved prompt, and you never raise one yourself — see the ceiling. |
```

**Verify** — the table must still parse as a table, and the rows must still
have four pipes each:

```sh
awk 'NR==891 || NR==892 { print NR": "gsub(/\|/,"|") }' AGENTS.md
```

→ `891: 4` and `892: 4`

```sh
sed -n '891,892p' AGENTS.md | grep -c 'never, see the ceiling'
```

→ `0`

```sh
sed -n '891,892p' AGENTS.md | grep -c 'see the ceiling'
```

→ `2` — the pointer to the ceiling is kept in both rows.

### Step 5: Confirm no stale claim survives, and nothing correct was over-corrected

**Verify** — no stale phrasing left in the in-scope files:

```sh
grep -nE 'never (sends?|responds?|reschedul)|read-only by design|never, see the ceiling' \
  .claude/commands/email.md .claude/commands/calendar.md README.md AGENTS.md
```

→ no output, exit 1.

**Verify** — the three *correct* statements elsewhere are still there. This
command must still find exactly three lines:

```sh
grep -rn 'never sends' AGENTS.md GUIDE.md
```

→ exactly three lines: `AGENTS.md:784`, `AGENTS.md:804` and `GUIDE.md:322`. All three
are correct and out of scope.

**Verify** — the destructive-action restraint survived:

```sh
grep -c 'Never propose a destructive action' AGENTS.md
```

→ `1`

### Step 6: Confirm the harness still passes

**Verify**:

```sh
brain/bin/doctor --check; echo "EXIT=$?"
```

→ exit 0, no `[XX]` lines, and this line still present:

```
[ok] all 18 command wrappers point at prompts that exist, and all 5 tools declare what they need
```

## Test plan

There is no test suite in this repository and this plan does not create one.
The greps in Step 5 are the test: one proves the wrong text is gone, one proves
the correct text elsewhere was left alone, and one proves the restraint on
destructive actions was not lost in the rewrite.

## Done criteria

Machine-checkable. ALL must hold:

- [ ] `grep -c 'read-only by design' README.md` returns `0`
- [ ] `grep -c 'never sends' .claude/commands/email.md` returns `0`
- [ ] `grep -c 'never responds' .claude/commands/calendar.md` returns `0`
- [ ] `grep -c 'never, see the ceiling' AGENTS.md` returns `0`
- [ ] `grep -rn 'never sends' AGENTS.md GUIDE.md` still returns exactly 3 lines
- [ ] `grep -c 'Never propose a destructive action' AGENTS.md` returns `1`
- [ ] `awk 'NR==891||NR==892{print gsub(/\|/,"|")}' AGENTS.md` returns `4` twice
- [ ] `wc -l < .claude/commands/email.md` returns `10`
- [ ] `wc -l < .claude/commands/calendar.md` returns `10`
- [ ] `wc -l < AGENTS.md` returns `994` — no lines added or removed
- [ ] `brain/bin/doctor --check` exits 0 with no `[XX]` lines
- [ ] `git status --porcelain` shows exactly four modified files
- [ ] `git diff --stat` shows 4 files changed, 5 insertions, 5 deletions
- [ ] `plans/README.md` status row for 002 updated

## STOP conditions

Stop and report back — do not improvise — if:

- The excerpts in "Current state" do not match the live text. In particular, if
  `README.md:270` no longer contains `read-only by design`, someone has already
  fixed part of this; report what you found rather than guessing at the rest.
- `git diff --stat` shows more than 5 changed lines. This plan is exactly five
  one-line replacements; anything larger means you edited something you should
  not have.
- `wc -l < AGENTS.md` does not return `994`. You have wrapped a table row across
  two lines, which breaks the markdown table.
- Step 5's second grep returns anything other than exactly three lines. That means
  you edited `AGENTS.md:784`, `AGENTS.md:804` or `GUIDE.md:322`, all of which are
  correct.
- `brain/bin/doctor --check` reports a new problem after your edits.

## Maintenance notes

For whoever owns this code next:

- **This class of error has no automatic guard.** `brain/bin/doctor:451-467`
  checks that a wrapper points at a file that exists, and nothing more. A
  wrapper whose `description:` contradicts the tool it points at passes every
  check in this repository. Two options if it recurs: teach `doctor` to compare
  each wrapper's description against the `writes:` field of the tool it points
  at, or shorten every wrapper description to name the command and nothing else,
  so it cannot make a promise. The second is cheaper and harder to break.
- **`AGENTS.md` states the mail and calendar rule in four separate places** —
  the tools table (754-755), the ceiling section (808-826), the consent
  paragraph (784) and the routing table (891-892). Commit `bec2c00` updated
  three of the four and missed the fourth. Any future change to this rule should
  grep `AGENTS.md` for both `email` and `calendar` and check every hit, then
  repeat across `.claude/commands/`, `README.md` and `GUIDE.md`.
- **What a reviewer should scrutinise**: that the two menu descriptions now
  state a limit the system actually keeps; that the two routing rows still tell
  the router what to send elsewhere and still forbid *proposing* a destructive
  action; and that `AGENTS.md:784` and `GUIDE.md:322` were not touched.
- **`brain/routing-eval.md` should be re-run** after this lands. Its closing
  section says to re-run any time the routing table changes — and this plan
  changes two of its rows. The eval has never been run at all, so its Results
  table is empty. That work is deliberately not part of this plan.
