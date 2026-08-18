# Plan 001: Anchor all four scripts to the vault they ship in, and refuse to stage transcripts git would commit

> **Executor instructions**: Follow this plan step by step. Run every
> verification command and confirm the expected result before moving to the
> next step. If anything in the "STOP conditions" section occurs, stop and
> report — do not improvise. When done, update the status row for this plan
> in `plans/README.md`.
>
> **Drift check (run first)**:
> `git diff --stat bec2c00..HEAD -- brain/bin/check brain/bin/doctor brain/bin/run brain/bin/sessions brain/bin/sync`
> If any of those files changed since this plan was written, compare the
> "Current state" excerpts against the live code before proceeding; on a
> mismatch, treat it as a STOP condition.

## Status

- **Priority**: P1
- **Effort**: M
- **Risk**: LOW
- **Depends on**: none
- **Category**: bug, security
- **Planned at**: commit `bec2c00`, 2026-08-18

## Why this matters

Four of this repository's five shell scripts locate the vault by asking git for
the top folder of the enclosing repository. When the vault sits inside a
*different* git repository and has no `.git` of its own, git answers with the
outer repository, and all four scripts operate on the wrong directory.

Every consequence is silent, which is what makes them expensive:

- **`brain/bin/sessions` is the dangerous one.** It copies AI session
  transcripts into `cortex/raw/sessions/transcripts/`, a path that
  `.gitignore:35` excludes from git. `.gitignore:31-34` describes those files
  as "enormous (gigabytes) and full of credentials, client code and pasted
  secrets", and `brain/prompts/ingest-sessions.md:48` promises the human that
  `stage` puts them "into a gitignored folder inside the vault". With the wrong
  root, the copies land *outside* the vault, where the vault's `.gitignore`
  cannot reach them — and the script prints a success message naming a relative
  path that reads as though they went to the right place.
- **`brain/bin/check`** prints `no assumption register yet — nothing to check`
  and exits 0 while the register sits unread. `check` is the only mechanical
  guard on the assumption model in `AGENTS.md`; a false pass there means an
  unlabelled guess can sit in the human's profile with nothing objecting.
- **`brain/bin/doctor`** reports `brain/bin/run is missing` and tells the human
  to re-download the repository, when the harness is intact and present.
- **`brain/bin/run`** lists zero available commands and reports
  `no such command` for every real command.

`brain/bin/sync` already solves this correctly and carries a comment explaining
why. Steps 2 to 5 copy that solution into the four scripts that lack it.

Step 6 then adds a second, independent guard to `sessions` alone: before it
copies anything, it asks git whether the destination is actually ignored, and
refuses if it is not. The path fix and this guard catch the same failure from
two different directions, which is the right shape for the one script in this
repository that moves credentials around. The guard also covers cases the path
fix does not — a vault whose `.gitignore` was edited, or replaced by a harness
update that dropped the line.

### This is preventive, not an active fire — read before you panic

Verified on 2026-08-18: the defect **does not trigger in this repository**.
This vault has its own `.git`, so `git rev-parse --show-toplevel` answers with
the vault and all four scripts currently behave. The fault needs a vault nested
inside another git repository with no `.git` of its own — the state
`brain/bin/sync:32-44` already detects and refuses.

That does not make this plan optional. It means you are removing a trap rather
than putting out a fire, so **prefer a careful diff over a fast one**. If a
verification disagrees with this plan, stop and report; nothing here is urgent
enough to justify guessing.

The same reasoning applies to Step 6. Its guard is not repairing a live leak in
this repository — `.gitignore:35` is doing its job here today. It is making the
promise in `brain/prompts/ingest-sessions.md:48` enforced rather than merely
written down, which matters because the operator is about to start using that
feature regularly.

## Current state

Files in play, each with its role:

- `brain/bin/sync` — commits and pushes the vault. **Already correct. Read it
  first; it is the pattern you are copying. Do not modify it.**
- `brain/bin/check` — lints the assumption register. Wrong root resolution.
- `brain/bin/doctor` — checks the install. Wrong root resolution.
- `brain/bin/run` — runs a command file with an agent CLI. Wrong root resolution.
- `brain/bin/sessions` — copies session transcripts in and out. Wrong root
  resolution, and no check on the destination.

### The correct pattern, as it exists today in `brain/bin/sync:15-27`

```sh
# Anchor to the script's own location, never to the working directory. Asking
# git for the toplevel walks *up*: clone this vault inside any other repo and
# every turn would commit that repo instead — its .env, its keys, all of it,
# with nobody watching.
root=$(cd "$(dirname "$0")/../.." 2>/dev/null && pwd -P) || root=''

# The same guard doctor uses for in_vault: structure is what proves we are in
# the vault, rather than in some directory that merely contains one.
if [ -z "$root" ] || [ ! -f "$root/AGENTS.md" ] || [ ! -d "$root/brain/bin" ]; then
  echo "sync: ${root:-$0} is not a vault — AGENTS.md and brain/bin/ should both be there. Nothing was committed." >&2
  exit 1
fi
cd "$root" || exit 1
```

### The defect, as it exists today

`brain/bin/check:17-18`

```sh
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root" || exit 1
```

`brain/bin/doctor:31-32`

```sh
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root" || exit 1
```

`brain/bin/run:16-17`

```sh
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root"
```

`brain/bin/sessions:19-20`

```sh
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root"
```

### How `sessions` uses that root

`brain/bin/sessions:22` — a **relative** path, resolved against whatever `cd`
above landed on:

```sh
stage_dir="cortex/raw/sessions/transcripts"
```

It is used in five places: `mkdir -p` at line 78, two `cp` destinations at lines
143-144, the success message at line 157, and `rm -rf` at line 163. Fixing the
root therefore repairs `stage` and `clean` together — no other change is needed
for the path defect.

### Repository conventions you must match

- **POSIX shell only.** Every script starts `#!/usr/bin/env sh`. No bashisms:
  no `[[ ]]`, no arrays, no `local`, no `$'...'`. `AGENTS.md` states the reason
  under "Staying model-agnostic": automation must be callable by anything.
- **Comments explain the *why*, at length, in prose.** This repository comments
  the reasoning behind a decision, not the mechanics of the line. The
  `brain/bin/sync:15-27` block above is the house style — match its density and
  tone. A one-line `# resolve root` comment does not match this codebase.
- **Error messages are written for a non-programmer**, name the script, say what
  did *not* happen, and give the fix. Compare `brain/bin/run:44-49`,
  `brain/bin/run:70-72` and `brain/bin/sync:24`. Never a stack trace, never
  jargon, never a lecture.
- **Messages go to stderr** (`>&2`) and exit codes follow `sysexits`: 64 for
  usage, 66 for a missing file, 69 for an unavailable service.

### The `set -e` trap you will hit in step 6

`brain/bin/sessions:17` sets `set -eu`. A command that exits non-zero therefore
ends the script immediately. `git check-ignore` exits **1** on the normal
"not ignored" answer, so you must never call it bare. Use this form, which is
safe under `set -e`:

```sh
rc=0
git check-ignore -q "$stage_dir/probe.jsonl" 2>/dev/null || rc=$?
```

## Commands you will need

This repository has no build, no package manager, no test runner and no CI.
Verification is running the shell scripts and reading their output.

| Purpose | Command | Expected on success |
|---|---|---|
| Lint the register | `brain/bin/check` | exit 0 |
| Check the install | `brain/bin/doctor --check` | exit 0, no `[XX]` lines |
| List commands | `brain/bin/run` | exit 64, lists 12 skills and 5 tools |
| List transcripts | `brain/bin/sessions list` | exit 0 |
| Confirm scope | `git status --porcelain` | only the four in-scope files |

If `shellcheck` is installed (`command -v shellcheck`), run
`shellcheck -s sh brain/bin/check brain/bin/doctor brain/bin/run brain/bin/sessions`
and confirm no *new* findings against a run on the unmodified files. If it is
not installed, skip this — do not install it.

## Scope

**In scope** (the only files you may modify):

- `brain/bin/check`
- `brain/bin/doctor`
- `brain/bin/run`
- `brain/bin/sessions`

**Out of scope** (do NOT touch, even though they look related):

- `brain/bin/sync` — already correct. It is the source of the pattern.
- `.gitignore` — line 35 already excludes the stage directory. Step 6 adds a
  check that this is true at run time; it does not change the rule itself.
- `brain/prompts/ingest-sessions.md` — it describes `sessions` correctly. It is
  the *script* that fails to keep the promise, not the prompt that makes it.
- `brain/bin/doctor:163-217` — the `in_vault` variable and the `missing` folder
  list. After this change that branch becomes hard to reach, because the new
  guard already proves `AGENTS.md` and `brain/bin/` are present. Leave the code
  alone: it is defensive, deleting it is a separate judgment call, and it is not
  what you were asked to do.
- Any change to what the scripts *check*, *report*, or *copy*. This plan changes
  where they look, plus one new refusal in `sessions`. Nothing else.

## Git workflow

- Branch: `advisor/001-anchor-scripts-to-vault-root`
- Two commits is the clearest split: one for steps 2-5 (the repeated path fix),
  one for step 6 (the new guard). One commit is acceptable.
- Commit message style, from `git log`: a short lowercase subject naming the
  effect, e.g. `brain: anchor check, doctor, run and sessions to their own vault`
  and `brain: refuse to stage transcripts git is not ignoring`
- Do NOT push and do NOT open a pull request.

## Steps

### Step 1: Build the reproduction fixture

Before changing anything, reproduce the faults. This proves the fixture works,
so that a pass later means something.

Run this exactly. It writes only to temporary directories.

```sh
FIX=$(mktemp -d)
FAKEHOME=$(mktemp -d)
REPO=<REPO_ROOT>            # absolute path of this repository

# an unrelated git repository
mkdir -p "$FIX/outer"
( cd "$FIX/outer" && git init -q . && echo x > readme.md \
  && git add -A && git -c user.email=a@b -c user.name=a commit -qm init )

# a vault inside it, with no .git of its own
mkdir -p "$FIX/outer/myvault/cortex/03_Resources"
cp -R "$REPO/AGENTS.md" "$REPO/.gitignore" "$REPO/brain" "$FIX/outer/myvault/"
printf -- '---\ntitle: Assumptions\ntype: register\n---\n\n**Next ID: ASM-0002**\n\n> [!WARNING]\n> **Assumption — ASM-0001 · confidence: medium · basis-kind: personal**\n> **They stall on decisions.**\n> Basis: [[A]] · [[B]]\n> Reasoning: throughput.\n> Falsifier: something.\n> Status: open · 2026-08-01\n' \
  > "$FIX/outer/myvault/cortex/03_Resources/Assumptions.md"

# a fake transcript to stage
mkdir -p "$FAKEHOME/.claude/projects/-Users-me-secretproj"
printf '{"cwd":"/Users/me/secretproj"}\n' \
  > "$FAKEHOME/.claude/projects/-Users-me-secretproj/abc.jsonl"

echo "fixture=$FIX  fakehome=$FAKEHOME"
```

**Verify** — run all four scripts from inside the fixture vault. Each must show
its fault.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/check
```
→ prints `[--] no assumption register yet — nothing to check.`, exit 0.
**This is the bug**; the register exists two directories down.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/run
```
→ prints `available:` with **two empty lists**. This is the bug.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/doctor --check
```
→ prints `[XX] brain/bin/run is missing` and
`-> Re-download the repo — part of the harness is gone`. This is the bug.

```sh
cd "$FIX/outer/myvault" && HOME="$FAKEHOME" ./brain/bin/sessions stage secretproj
find "$FIX/outer" -name 'claude--abc.jsonl'
( cd "$FIX/outer" && git check-ignore -q cortex/raw/sessions/transcripts/claude--abc.jsonl; echo "ignored? exit $?" )
```
→ the script reports
`staged 1 transcript(s) matching 'secretproj' into cortex/raw/sessions/transcripts`.
`find` shows the file at **`$FIX/outer/cortex/raw/...`** — outside the vault.
`check-ignore` exits **1**, meaning **not ignored**. This is the bug, and it is
the reason this plan is tagged `security`.

If any of the four does not produce the output above, STOP: the fixture is
wrong and every later verification would be meaningless.

Reset the staged file before continuing: `rm -rf "$FIX/outer/cortex"`

### Step 2: Fix `brain/bin/check`

Replace lines 17-18 of `brain/bin/check` with the anchored form from "The
correct pattern". Write your own comment in the house style — explain that
asking git for the toplevel searches *upward*, so a vault nested in another
repository makes this script lint that repository instead, and report a clean
pass having read nothing. Do not copy `sync`'s comment word for word; it talks
about committing, which is not what this script does.

The guard message must name this script and say what did not happen:

```sh
echo "check: ${root:-$0} is not a vault — AGENTS.md and brain/bin/ should both be there. Nothing was checked." >&2
exit 1
```

`check` runs under `set -u` only (line 15), not `set -e`. The explicit `exit 1`
is therefore required — do not rely on the shell to stop.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/check; echo "EXIT=$?"
```
→ `[--] no assumption register yet — nothing to check.`, `EXIT=0`. This
repository genuinely has no register, so that is the correct answer here.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/check; echo "EXIT=$?"
```
→ now reads the register. Expect a line mentioning `ASM-0001`, and `EXIT=0`.
The `no assumption register yet` line must be **gone**.

### Step 3: Fix `brain/bin/run`

Replace lines 16-17 with the same anchored form, a house-style comment, and a
message naming `run`. Use the wording pattern `Nothing was run.`

`run` sets `set -eu` at line 14. Keep the explicit `exit 1`.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/run; echo "EXIT=$?"
```
→ exit 64, with 12 names under `skills (brain/prompts/)` and 5 under
`tools (brain/tools/)`.

```sh
cd /tmp && <REPO_ROOT>/brain/bin/run; echo "EXIT=$?"
```
→ **the same 12 and 5 names**, exit 64. Before this change, running from `/tmp`
resolved the root to `/tmp` and listed nothing.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/run; echo "EXIT=$?"
```
→ 12 skills and 5 tools listed, exit 64.

### Step 4: Fix `brain/bin/doctor`

Replace lines 31-32 with the same anchored form, a house-style comment, and a
message naming `doctor`. Use `Nothing was checked.`

Place the guard **after** the option parsing at lines 22-29, so that
`brain/bin/doctor --nonsense` still fails with its existing usage message and
exit 64. Do not reorder those blocks.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/doctor --check; echo "EXIT=$?"
```
→ exit 0, no `[XX]` lines. Confirm these four lines are present and unchanged:

- `[ok] all folders present`
- `[ok] the scripts can run`
- `[ok] all 18 command wrappers point at prompts that exist, and all 5 tools declare what they need`
- `[ok] this folder is trusted, so its settings actually apply`

**The last one is the sensitive check.** `doctor` passes `$root` to `jq` at
lines 494-497 to look this repository up by path in `~/.claude.json`. Your change
alters how `$root` is spelled — `pwd -P` resolves symbolic links. If that line
now reports `Claude Code hasn't trusted this folder yet`, the key no longer
matches and you have introduced a regression. Treat it as a STOP condition.

```sh
cd <REPO_ROOT> && brain/bin/doctor --nonsense; echo "EXIT=$?"
```
→ `doctor: unknown option '--nonsense' — usage: brain/bin/doctor [--check]`,
exit 64.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/doctor --check
```
→ the five `brain/bin/... is missing` lines, the `missing folders:` line and
`AGENTS.md is missing` are all **gone**. A `[!!] no backup` warning may remain;
that is about the outer repository's remote and is a separate concern.

### Step 5: Fix `brain/bin/sessions`

Replace lines 19-20 with the same anchored form, a house-style comment, and a
message naming `sessions`. Use `Nothing was copied.`

Say in the comment what makes this script's version of the fault different from
the others: it writes files, and the files are transcripts.

`sessions` sets `set -eu` at line 17. Keep the explicit `exit 1`.

Change nothing else in this step. `stage_dir` at line 22 stays a relative path;
it is now relative to the right directory.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/sessions list | head -3; echo "EXIT=$?"
```
→ runs and exits 0 (or 69 with
`No agent session directories found on this machine.` if you have none — both
are correct here).

```sh
cd "$FIX/outer/myvault" && HOME="$FAKEHOME" ./brain/bin/sessions stage secretproj
find "$FIX/outer" -name 'claude--abc.jsonl'
```
→ the file is now at
**`$FIX/outer/myvault/cortex/raw/sessions/transcripts/claude--abc.jsonl`** —
inside the vault. There must be **no** `$FIX/outer/cortex/` directory.

```sh
cd "$FIX/outer/myvault" && HOME="$FAKEHOME" ./brain/bin/sessions clean
ls "$FIX/outer/myvault/cortex/raw/sessions/" 2>&1
```
→ `clean` removes the staged folder from inside the vault.

### Step 6: Make `sessions stage` refuse a destination git is not ignoring

This is the security guard, and it is independent of steps 2-5. Even with the
right root, a vault whose `.gitignore` lost line 35 — by hand, or by a harness
update — would let `sync` commit and push gigabytes of credentials on the next
turn.

In `brain/bin/sessions`, inside the `stage)` branch, insert the guard
**immediately before** `mkdir -p "$stage_dir"` at line 78, and **after** the
`[ -n "$pattern" ] ||` usage check. It must run after the `cd "$root"` from
step 5, because git answers this question relative to the current directory.

Write it in this shape:

```sh
rc=0
git check-ignore -q "$stage_dir/probe.jsonl" 2>/dev/null || rc=$?
if [ "$rc" -eq 1 ]; then
  echo "sessions: git is NOT ignoring $stage_dir, so anything copied there would be committed and pushed on the next turn." >&2
  echo "          Transcripts hold credentials, client code and anything you ever pasted into a session." >&2
  echo "          Nothing was copied. Check that .gitignore still has the line: cortex/raw/sessions/transcripts/" >&2
  exit 1
fi
```

Three behaviours, and your comment must explain why each is right:

| `rc` | Meaning | Action | Why |
|---|---|---|---|
| `0` | git ignores the destination | continue | The promise in `ingest-sessions.md:48` holds. |
| `1` | git does **not** ignore it | refuse, exit 1 | A copy here becomes a commit, then a push. |
| `128` | no git repository at all | continue | Nothing can be committed, so nothing can leak this way. `sync` already reports this state. |

Note the probe filename. `git check-ignore` is asked about a **file inside** the
directory, not the directory itself. The pattern in `.gitignore` ends in a
slash, so it matches directories only, and git cannot tell that a path is a
directory when that path does not exist yet. Asking about a file inside is both
the reliable form and the question that actually matters. Do not create the
probe file; `check-ignore` does not need it to exist.

**Verify** — the guard allows a correct vault:

```sh
cd <REPO_ROOT> && brain/bin/sessions stage nothing-matches-this 2>&1 | head -2
```
→ `sessions: nothing matches 'nothing-matches-this' — try: brain/bin/sessions list`.
It reached the pattern check, so the guard let it through.

**Verify** — the guard refuses when the destination is not ignored. Break the
fixture's `.gitignore` on purpose:

```sh
grep -v 'cortex/raw/sessions/transcripts/' "$FIX/outer/myvault/.gitignore" > "$FIX/gi" \
  && mv "$FIX/gi" "$FIX/outer/myvault/.gitignore"
cd "$FIX/outer/myvault" && git init -q . 2>/dev/null
HOME="$FAKEHOME" ./brain/bin/sessions stage secretproj; echo "EXIT=$?"
```
→ prints the three-line refusal, `EXIT=1`, and **no file is copied**:

```sh
find "$FIX/outer/myvault/cortex/raw" -name '*.jsonl' | wc -l
```
→ `0`

**Verify** — a vault with no git at all is still allowed. Note that removing
the vault's own `.git` is **not enough**: Step 1's `outer` repository still
encloses it, so git finds that one and answers about it instead. Both must go:

```sh
rm -rf "$FIX/outer/myvault/.git" "$FIX/outer/.git"
cd "$FIX/outer/myvault" && HOME="$FAKEHOME" ./brain/bin/sessions stage secretproj; echo "EXIT=$?"
```
→ stages the file, exit 0. There is no repository anywhere above this
directory, so there is nothing to commit into, and `rc` is 128.

> **Corrected 2026-08-18.** An earlier version removed only the vault's `.git`
> and expected exit 0. That is not a no-repository state, and the guard
> correctly refused. The executor of this plan diagnosed it and removed the
> outer `.git` as well, which is the right test.  

### Step 7: Clean up

```sh
rm -rf "$FIX" "$FAKEHOME"
```

Confirm your own repository is untouched apart from the four scripts:

```sh
cd <REPO_ROOT> && git status --porcelain
```
→ exactly four modified files under `brain/bin/`, plus `plans/`.

## Test plan

This repository has no test suite, and creating one is separate work the
operator has not selected. **Do not create one here.** The fixture in Step 1 is
the test: it is built, used across five steps, and removed in Step 7.

Record the Step 1 fixture commands in the commit message body so the next person
can rebuild it. That is the cheapest durable form this test can take today.

## Done criteria

Machine-checkable. ALL must hold:

- [ ] `grep -c 'show-toplevel' brain/bin/check brain/bin/doctor brain/bin/run brain/bin/sessions`
      returns `0` for all four files
- [ ] `grep -l 'dirname "$0"' brain/bin/check brain/bin/doctor brain/bin/run brain/bin/sessions`
      lists all four files
- [ ] `grep -c 'check-ignore' brain/bin/sessions` returns `1`
- [ ] `brain/bin/check` exits 0 from the repository root
- [ ] `brain/bin/doctor --check` exits 0 from the repository root, with zero
      `[XX]` lines, and still prints `[ok] this folder is trusted`
- [ ] `cd /tmp && <REPO_ROOT>/brain/bin/run` lists 12 skills and 5 tools
- [ ] `brain/bin/sessions stage nothing-matches-this` reaches the pattern check
      rather than the ignore guard
- [ ] `git status --porcelain` shows exactly four modified files, all under
      `brain/bin/`
- [ ] `git diff --stat` shows roughly 60-80 changed lines. **This is a smell
      test, not a gate.** If your comments are good and the total runs a little
      over, leave them — the "Repository conventions" section asks for prose
      that explains the *why*, and that costs lines. Do not compress a comment
      to hit a number. If the total is far larger, something outside the four
      anchor blocks and the Step 6 guard has changed; that is the real signal.
- [ ] `plans/README.md` status row for 001 updated

## STOP conditions

Stop and report back — do not improvise — if:

- The excerpts in "Current state" do not match the live files.
- Step 1's fixture does not reproduce all four faults, especially the
  `check-ignore` exit of 1 on the staged transcript.
- `brain/bin/doctor --check` starts reporting
  `Claude Code hasn't trusted this folder yet` after Step 4. This means `pwd -P`
  produced a path that does not match the key in `~/.claude.json`, and the fix
  needs a different root spelling. Report both paths; do not work around it.
- The Step 6 guard refuses to run in **this** repository. That would mean
  `.gitignore:35` is not doing its job here, which is a finding in its own
  right, not something to code around.
- Any verification fails twice after one reasonable correction.
- You conclude the fix requires editing `brain/bin/sync`, `.gitignore`, or any
  file outside the four in scope.
- You find that `$0` does not resolve usefully in your environment — for
  example, the scripts are invoked through a symbolic link on `PATH`, so
  `dirname "$0"` gives the link's directory rather than the vault's. Report it.
  `brain/bin/sync` already accepts this limitation, so matching it is correct,
  but the operator should know if it bites.

## Maintenance notes

For whoever owns this code next:

- **Four scripts now repeat the same eleven lines.** That is deliberate: a
  shared `brain/bin/_common.sh` would need to be sourced, which reintroduces the
  same path-resolution problem one level down, and adds a fifth file whose
  executable bit `doctor` would have to police. If a sixth script is ever added,
  revisit that trade.
- **The Step 6 guard is the durable protection, not the path fix.** The path fix
  corrects one way the destination goes wrong. The guard checks the property
  that actually matters — *will git commit this?* — and so it also covers ways
  nobody has thought of yet, including a future harness update that ships a
  `.gitignore` without line 35. If you ever move `stage_dir`, move the guard
  with it.
- **What a reviewer should scrutinise**: that no script's *behaviour* changed
  apart from the new refusal; that every message names its script and says what
  did not happen; that `doctor`'s jq trust lookup still passes, since it is the
  one consumer of `$root` as a literal string; and that the `rc=$?` idiom in
  step 6 is used, because a bare `git check-ignore` under `set -e` would end the
  script silently on the normal "not ignored" answer.
- **Deferred deliberately**: `doctor`'s now-unreachable `in_vault` branch
  (lines 163-217). Removing it is a readability change, not a correctness one,
  and it would enlarge this diff past the point where a reviewer can check it at
  a glance.
- **Related, not fixed here**: `brain/bin/doctor:87-97` reports any git remote
  as `backed up to <url>` without checking whether it is public. That is audit
  finding 4 and is unplanned. It belongs to the same family as the Step 6 guard
  — both ask "where is this actually going?" — and would sit naturally beside it.
  Measured on 2026-08-18: `Sebastian-Sole/second-brain-demo` is **PUBLIC**, and
  while the staged transcripts and `cortex/06_Sessions/scope.md` are both
  ignored, the session notes at `cortex/06_Sessions/<note>.md` are **tracked**,
  committed by the `Stop` hook and pushed. Step 6 stops transcripts reaching a
  remote; nothing yet stops the notes distilled from them reaching a public one.
- **Apply this plan to the operator's working vault too.** The private
  repository `Sebastian-Sole/second-brain` at `~/Documents/Obsidian Vault` was
  not inspected during this audit. Run `brain/bin/doctor` there first; if its
  harness predates `bec2c00`, this plan applies unchanged.
