# Plan 001: Anchor `check`, `doctor` and `run` to the vault they ship in

> **Executor instructions**: Follow this plan step by step. Run every
> verification command and confirm the expected result before moving to the
> next step. If anything in the "STOP conditions" section occurs, stop and
> report — do not improvise. When done, update the status row for this plan
> in `plans/README.md`.
>
> **Drift check (run first)**:
> `git diff --stat bec2c00..HEAD -- brain/bin/check brain/bin/doctor brain/bin/run brain/bin/sync`
> If any of those files changed since this plan was written, compare the
> "Current state" excerpts against the live code before proceeding; on a
> mismatch, treat it as a STOP condition.

## Status

- **Priority**: P1
- **Effort**: S
- **Risk**: LOW
- **Depends on**: none
- **Category**: bug
- **Planned at**: commit `bec2c00`, 2026-08-18

## Why this matters

Four of this repository's five shell scripts locate the vault by asking git for
the top folder of the enclosing repository. When the vault sits inside a
*different* git repository and has no `.git` of its own, git answers with the
outer repository, and the scripts operate on the wrong directory.

The consequences are silent, which is what makes them expensive:

- `brain/bin/check` prints `no assumption register yet — nothing to check` and
  exits 0 while the register sits unread. `check` is the only mechanical guard
  on the assumption model described in `AGENTS.md`; a false pass there means an
  unlabelled guess can sit in the human's profile with nothing objecting.
- `brain/bin/doctor` reports `brain/bin/run is missing` and tells the human to
  re-download the repository, when the harness is intact and present.
- `brain/bin/run` lists zero available commands and reports `no such command`
  for every real command.

`brain/bin/sync` already solves this correctly and carries a comment explaining
why. This plan copies that solution into the three scripts that lack it. After
this plan, all three scripts operate on the vault they were installed in,
regardless of the caller's working directory or any surrounding repository.

## Current state

Files in play, each with its role:

- `brain/bin/sync` — commits and pushes the vault. **Already correct. Read it
  first; it is the pattern you are copying. Do not modify it.**
- `brain/bin/check` — lints the assumption register. Wrong root resolution.
- `brain/bin/doctor` — checks the install. Wrong root resolution.
- `brain/bin/run` — runs a command file with an agent CLI. Wrong root resolution.
- `brain/bin/sessions` — copies session transcripts. Also wrong, **deliberately
  out of scope** — see the Scope section.

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

### Repository conventions you must match

- **POSIX shell only.** Every script starts `#!/usr/bin/env sh`. No bashisms:
  no `[[ ]]`, no arrays, no `local`, no `$'...'`. `AGENTS.md` states the reason
  under "Staying model-agnostic": automation must be callable by anything.
- **Comments explain the *why*, at length, in prose.** This repository comments
  the reasoning behind a decision, not the mechanics of the line. The
  `brain/bin/sync:15-27` block above is the house style — match its density and
  tone. A one-line `# resolve root` comment does not match this codebase.
- **Error messages are written for a non-programmer**, name the script, say what
  did *not* happen, and give the fix. Compare `brain/bin/run:44-49`, `brain/bin/run:70-72` and
  `brain/bin/sync:24`. Never a stack trace, never jargon.
- **Messages go to stderr** (`>&2`) and exit codes follow `sysexits`: 64 for
  usage, 66 for a missing file, 69 for an unavailable service.

## Commands you will need

This repository has no build, no package manager, no test runner and no CI.
Verification is running the scripts and reading their output.

| Purpose | Command | Expected on success |
|---|---|---|
| Lint the register | `brain/bin/check` | exit 0 |
| Check the install | `brain/bin/doctor --check` | exit 0, no `[XX]` lines |
| List commands | `brain/bin/run` | exit 64, lists 12 skills and 5 tools |
| Confirm nothing else changed | `git status --porcelain` | only the three in-scope files |

If `shellcheck` is installed (`command -v shellcheck`), run
`shellcheck -s sh brain/bin/check brain/bin/doctor brain/bin/run` and confirm no
*new* findings against a run on the unmodified files. If it is not installed,
skip this — do not install it.

## Scope

**In scope** (the only files you may modify):

- `brain/bin/check`
- `brain/bin/doctor`
- `brain/bin/run`

**Out of scope** (do NOT touch, even though they look related):

- `brain/bin/sync` — already correct. It is the source of the pattern.
- `brain/bin/sessions` — it has the same defect at line 19, with a worse
  consequence: it copies session transcripts to an unprotected folder outside
  the vault. The operator deliberately excluded it from this plan. **Do not fix
  it here**, and do not mention it in the commit. It will be handled separately.
- `brain/bin/doctor:163-217` — the `in_vault` variable and the `missing` folder
  list. After this change that branch becomes hard to reach, because the new
  guard already proves `AGENTS.md` and `brain/bin/` are present. Leave the code
  alone anyway: it is defensive, deleting it is a separate judgment call, and it
  is not what you were asked to do.
- Any change to what the three scripts *check* or *report*. This plan changes
  where they look, and nothing else.

## Git workflow

- Branch: `advisor/001-anchor-scripts-to-vault-root`
- One commit for the whole change is fine — it is one edit repeated three times.
- Commit message style, from `git log`: a short lowercase subject naming the
  effect, e.g. `brain: anchor check, doctor and run to the vault they ship in`
- Do NOT push and do NOT open a pull request.

## Steps

### Step 1: Build the reproduction fixture

Before changing anything, reproduce the fault. This proves the fixture works,
so that a pass in Step 5 means something.

Run this exactly. It writes only to a temporary directory.

```sh
FIX=$(mktemp -d)
mkdir -p "$FIX/outer"
cd "$FIX/outer" && git init -q . && echo x > readme.md \
  && git add -A && git -c user.email=a@b -c user.name=a commit -qm init

# a vault inside that repository, with no .git of its own
mkdir -p "$FIX/outer/myvault"
cd "$OLDPWD" 2>/dev/null || true
cp -R <REPO_ROOT>/AGENTS.md <REPO_ROOT>/brain "$FIX/outer/myvault/"
mkdir -p "$FIX/outer/myvault/cortex/03_Resources"
printf -- '---\ntitle: Assumptions\ntype: register\n---\n\n**Next ID: ASM-0002**\n\n> [!WARNING]\n> **Assumption — ASM-0001 · confidence: medium · basis-kind: personal**\n> **They stall on decisions.**\n> Basis: [[A]] · [[B]]\n> Reasoning: throughput.\n> Falsifier: something.\n> Status: open · 2026-08-01\n' \
  > "$FIX/outer/myvault/cortex/03_Resources/Assumptions.md"
echo "fixture at $FIX"
```

Replace `<REPO_ROOT>` with the absolute path of this repository.

**Verify** — run the three scripts from inside the fixture vault:

```sh
cd "$FIX/outer/myvault" && ./brain/bin/check
```

→ prints `[--] no assumption register yet — nothing to check.` and exits 0.
**This output is the bug.** The register exists at
`$FIX/outer/myvault/cortex/03_Resources/Assumptions.md`.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/run
```

→ prints `available:` with **two empty lists** under the skills and tools
headings. This is the bug.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/doctor --check
```

→ prints `[XX] brain/bin/run is missing` and
`-> Re-download the repo — part of the harness is gone`. This is the bug.

If any of the three commands does **not** produce the output above, STOP: the
fixture is wrong and every later verification would be meaningless.

### Step 2: Fix `brain/bin/check`

Replace lines 17-18 of `brain/bin/check`:

```sh
root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root" || exit 1
```

with the anchored form. Write your own comment in the house style described in
"Repository conventions" — explain that asking git for the toplevel searches
*upward*, so a vault nested in another repository makes this script lint that
repository's files instead of the vault's, and report a clean pass having read
nothing. Do not copy `sync`'s comment word for word; it talks about committing,
which is not what this script does.

The guard message must name this script and say what did not happen. Follow the
shape of `brain/bin/sync:24`:

```sh
echo "check: ${root:-$0} is not a vault — AGENTS.md and brain/bin/ should both be there. Nothing was checked." >&2
exit 1
```

Note that `check` runs under `set -u` only (line 15), not `set -e`. The explicit
`exit 1` above is therefore required — do not rely on the shell to stop.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/check; echo "EXIT=$?"
```

→ prints `[--] no assumption register yet — nothing to check.`, `EXIT=0`.
This repository genuinely has no register, so this is the correct answer here.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/check; echo "EXIT=$?"
```

→ now reads the register. Expect a line mentioning `ASM-0001` (a staleness or
basis-link note), and `EXIT=0`. The `no assumption register yet` line must be
**gone**.

### Step 3: Fix `brain/bin/run`

Replace lines 16-17 of `brain/bin/run` with the same anchored form, with a
comment in the house style and a message naming `run`. Use the wording pattern
`Nothing was run.`

`run` sets `set -eu` at line 14, so an unguarded failure would abort with no
message. Keep the explicit `exit 1`.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/run; echo "EXIT=$?"
```

→ exit 64, and the two lists are populated: 12 names under
`skills (brain/prompts/)` and 5 under `tools (brain/tools/)`.

```sh
cd /tmp && <REPO_ROOT>/brain/bin/run; echo "EXIT=$?"
```

→ **the same 12 and 5 names**, exit 64. Before this change, running from `/tmp`
resolved the root to `/tmp` and listed nothing. This is the behaviour the plan
exists to produce.

```sh
cd "$FIX/outer/myvault" && ./brain/bin/run; echo "EXIT=$?"
```

→ 12 skills and 5 tools listed, exit 64.

### Step 4: Fix `brain/bin/doctor`

Replace lines 31-32 of `brain/bin/doctor` with the same anchored form, with a
house-style comment and a message naming `doctor`. Use `Nothing was checked.`

Place the guard **after** the option parsing at lines 22-29, so that
`brain/bin/doctor --nonsense` still fails with its existing usage message and
exit 64. Do not reorder those blocks.

**Verify**:

```sh
cd <REPO_ROOT> && brain/bin/doctor --check; echo "EXIT=$?"
```

→ exit 0. No `[XX]` lines. Confirm these specific lines are all present and
unchanged from before your edit:

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

→ the five `brain/bin/... is missing` lines and the `missing folders:` line are
**gone**. `AGENTS.md is missing` is gone. The `[!!] no backup` warning may remain
— that one is about the outer repository's git remote and is a separate concern.

### Step 5: Confirm the fixture is repaired and clean up

Re-run all three commands from Step 1 inside the fixture. Each must now behave
as it does in a normal vault.

**Verify**:

```sh
cd "$FIX/outer/myvault" && ./brain/bin/check | grep -c 'no assumption register yet'
```

→ `0`

```sh
cd "$FIX/outer/myvault" && ./brain/bin/run 2>&1 | grep -c 'maintain'
```

→ `1`

```sh
cd "$FIX/outer/myvault" && ./brain/bin/doctor --check 2>&1 | grep -c 'is missing'
```

→ `0`

Then remove the fixture: `rm -rf "$FIX"`

## Test plan

This repository has no test suite, and creating one is a separate piece of work
that the operator has not selected. **Do not create one here.** The fixture in
Step 1 is the test for this change; it is built, used and removed inside this
plan.

Record the fixture commands in the commit message body so the next person can
rebuild it. That is the cheapest durable form the test can take today.

## Done criteria

Machine-checkable. ALL must hold:

- [ ] `grep -c 'show-toplevel' brain/bin/check brain/bin/doctor brain/bin/run`
      returns `0` for all three files
- [ ] `grep -lc 'dirname "$0"' brain/bin/check brain/bin/doctor brain/bin/run`
      lists all three files
- [ ] `brain/bin/check` exits 0 from the repository root
- [ ] `brain/bin/doctor --check` exits 0 from the repository root, with zero
      `[XX]` lines, and still prints `[ok] this folder is trusted`
- [ ] `cd /tmp && <REPO_ROOT>/brain/bin/run` lists 12 skills and 5 tools
- [ ] `git status --porcelain` shows exactly three modified files:
      `brain/bin/check`, `brain/bin/doctor`, `brain/bin/run`
- [ ] `git diff --stat` shows fewer than 40 changed lines in total
- [ ] `plans/README.md` status row for 001 updated

## STOP conditions

Stop and report back — do not improvise — if:

- The excerpts in "Current state" do not match the live files.
- Step 1's fixture does not reproduce all three faults.
- `brain/bin/doctor --check` starts reporting
  `Claude Code hasn't trusted this folder yet` after Step 4. This means `pwd -P`
  produced a path that does not match the key in `~/.claude.json`, and the fix
  needs a different root spelling. Report the two paths; do not work around it.
- Any verification fails twice after one reasonable correction.
- You conclude the fix requires editing `brain/bin/sessions`, `brain/bin/sync`,
  or any file outside the three in scope.
- You find that `$0` does not resolve usefully in your environment — for
  example, the scripts are invoked through a symbolic link on `PATH` and
  `dirname "$0"` gives the link's directory rather than the vault's. Report it.
  `brain/bin/sync` already accepts this limitation, so matching it is correct,
  but the operator should know if it bites.

## Maintenance notes

For whoever owns this code next:

- **`brain/bin/sessions` still has this defect** at line 19, and it is the
  highest-consequence instance: it copies AI session transcripts — which
  `.gitignore:31-34` describes as "full of credentials, client code and pasted
  secrets" — into `cortex/raw/sessions/transcripts` relative to the wrong root,
  which places them outside the vault where the vault's `.gitignore` does not
  reach them, while reporting success. It was excluded from this plan by the
  operator, not because it is unimportant. Fix it next, with the same edit.
- **Four scripts now repeat the same eleven lines.** That is deliberate for now:
  a shared `brain/bin/_common.sh` would have to be sourced, which adds its own
  path-resolution problem and a fifth file to keep executable. If a fifth script
  is ever added, revisit that trade.
- **What a reviewer should scrutinise**: that no script's *behaviour* changed,
  only its starting directory; that every message still names the script and
  says what did not happen; and that `doctor`'s jq trust lookup still passes,
  since it is the one consumer of `$root` as a literal string.
- **Deferred deliberately**: `doctor`'s now-unreachable `in_vault` branch
  (lines 163-217). Removing it is a readability change, not a correctness one,
  and it would enlarge this diff past the point where a reviewer can check it
  at a glance.
