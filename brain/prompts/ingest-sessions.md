# ingest-sessions — turn past AI coding sessions into notes you can search

Your agent CLIs already record every session you've ever had with them, on disk, in full. That is
months of your own decisions and reasoning sitting in files you can't search. This turns them into
short notes the vault can answer from.

**The rule that governs everything below: distil, never ingest.** A single transcript can be 74 MB;
a whole history is gigabytes. A vault is megabytes of markdown. Copying transcripts in would bury
every real note underneath them — the exact retrieval failure `AGENTS.md` warns about, at a
thousand times the scale. Transcripts stay where they are. You write short notes *about* them.

---

## Phase 0 — Scope, before you read anything

**Ask the human which projects to ingest, and default to none.** Do not skip this and do not guess.

List the projects you can see (the recipe is below), show them the list, and have them pick. Their
history almost certainly contains client work, employer code, and other people's confidential
material, and a second brain is a git repo that gets pushed. Ingesting the wrong project is not a
tidiness problem.

Write their answer to `06_Sessions/scope.md` as an allowlist of path fragments, so later runs don't
re-ask. Anything not matching the allowlist is skipped silently.

**Then agree a window.** Default to the **last 30 days**. Never attempt an entire history in one
run — it's thousands of sessions and it will cost more than it's worth. Report what remains at the
end so they can run it again.

## Phase 1 — Find and stage the sessions

**You cannot read the transcripts directly.** Every agent CLI sandboxes itself to the working
directory, so `~/.claude/projects` and `~/.codex/sessions` are out of reach no matter how you're
invoked. Don't fight this and don't ask for a permission escalation. Use the helper:

```sh
brain/bin/sessions list                    # every project with sessions on this machine
brain/bin/sessions list <pattern>          # just the ones matching
brain/bin/sessions stage <pattern> [n]     # copy the n newest into raw/sessions/transcripts/
brain/bin/sessions clean                   # delete them again when you're done
```

`list` is what you show the human in Phase 0. `stage` copies transcripts into a gitignored folder
inside the vault, where you can read them with your normal tools. **Always `clean` at the end**,
even if the run failed — leaving gigabytes of transcripts in the working tree is how one of them
eventually gets committed.

Note that Claude Code's project directories are a lossy encoding of the path (`/` and `-` both
become `-`), so `list` output is for matching and display, not for constructing paths.

**Tell the human about retention on the first run.** Claude Code deletes transcripts older than
**30 days** at startup unless `cleanupPeriodDays` is raised in `~/.claude/settings.json`. If theirs
is unset or low, say so before you do anything else — everything outside that window is already
gone, and this command cannot get it back.

Skip any session already ingested — `grep -rl "session-id" 06_Sessions/` is enough, no state file.
Skip trivial ones too: a session under ~10 KB or a handful of turns is someone opening a CLI and
closing it, and it does not deserve a note.

## Phase 2 — Read cheaply

Never read a whole transcript into context. Pull the shape of it:

The recipes below use `jq`, which is not installed everywhere — check with `command -v jq` before
relying on it (`brain/bin/doctor` reports it too). Without it, `grep`/`sed` over the JSONL works
fine for pulling user turns; it's just noisier. Don't ask the human to install anything.

- **Claude Code**: `jq -r 'select(.type=="user") | .message.content | if type=="array" then .[0].text else . end'`
  gives you the human's turns — usually enough on its own. `select(.type=="ai-title") | .aiTitle`
  sometimes has a pre-made title; use it when it's there, don't rely on it. `.cwd` and `.gitBranch`
  appear on message records.
- **Codex**: `session_meta` for cwd and timestamp; `response_item` records carry the conversation.

Strip the noise: `<local-command-caveat>`, `<command-name>`, system reminders and hook output are
harness plumbing, not thinking. If the human's turns alone don't tell you what happened, sample the
last few assistant turns — not the middle.

## Phase 3 — Write one note per session

Into `06_Sessions/`, named `YYYY-MM-DD <project> — <what happened>.md`:

```yaml
---
title: "Moelven — reworked the invoice import retry logic"
type: session
stage: active
status: draft
created: 2026-02-14        # the session's date, not today's
updated: 2026-08-13
generated: { by: <your agent>/<your model>, at: <now> }
verified: []
tags: [session]
area:                      # work | code | …
source: "codex:019b6f93-2e12-7573-89b0-f9f17c5de9cd"
transcript: "~/.codex/sessions/2025/12/30/rollout-2025-12-30T15-04-35-019b6f93.jsonl"
---
```

Four headings, and nothing else:

- **What I was working on** — two sentences.
- **What I decided** — the durable part. Decisions and the reasons for them. If nothing was
  decided, say so; plenty of sessions decide nothing.
- **What I learned** — things that would still be true in six months. Not "fixed a typo."
- **Where it connects** — `[[wikilinks]]` to existing notes and projects. Search the vault first.

**The note must stand on its own.** The `transcript:` path is for verification, not for the answer —
transcripts get pruned, machines get replaced, and a note that only says "see session 019b6f93" is
worthless the day that file disappears. Write the actual conclusion down.

Write in the human's voice, past tense, their words where you have them. These are *their* sessions;
don't turn them into changelog entries.

## Phase 4 — Catalogue

Write `06_Sessions/index.md`: one line per session, newest first —
`- YYYY-MM-DD · project · [[Note Title]] — one line`. Group by month once there are more than ~30.

Add **one** line to the root `index.md` pointing at it. Do not list individual sessions there; a
thousand session lines would destroy the catalog that makes retrieval work.

## Phase 5 — Report

**Output surface:** session notes as markdown in `06_Sessions/`, plus a plain-text summary in the
conversation. No artifact, no rendered report, and never a transcript copied into the vault.

Say how many sessions you scanned, ingested, and skipped (and why), how many remain outside the
window, and name the two or three notes most worth reading. Then stop.

---

## Rules that matter here

- **Nothing staged ever gets committed.** `raw/sessions/transcripts/` is gitignored and temporary.
  Run `brain/bin/sessions clean` when you finish, and never move a transcript out of there into a
  tracked folder — not into `raw/`, not anywhere. The notes are the deliverable; the transcripts are
  scaffolding you borrowed for ten minutes.
- **Scan every note you write for secrets before saving it.** You are summarising files full of
  API keys, tokens and pasted credentials, and a faithful summary of a credential is still a
  credential. At minimum check for `sk-`, `ghp_`, `xox[baprs]-`, `AKIA`, `-----BEGIN .* PRIVATE KEY`,
  `Bearer [A-Za-z0-9._-]{20,}`, and anything shaped like `password=` or `secret=`. Redact to
  `[redacted]`. When in doubt, leave it out — the transcript still has it if it's ever needed.
- **A regex will not catch confidentiality.** "Migrating Acme off their legacy billing system"
  matches no pattern and is still not yours to publish. That's what the Phase 0 allowlist is for,
  and it's why the default is deny.
- **Never invent what a session was about.** If the transcript is too fragmentary to summarise, skip
  it and say so. A wrong session note is worse than a missing one, because it will be cited later.
- Mark anything you inferred rather than read with an **AI synthesis** callout, per `AGENTS.md`.

Session notes are **not** part of the default retrieval order. `ask` reads them when the question is
about past work — "what did I decide about X", "when did I last touch Y" — and otherwise leaves them
alone, for the same reason it leaves `raw/` alone: there are thousands of them and they will
out-match your real notes on any keyword.
