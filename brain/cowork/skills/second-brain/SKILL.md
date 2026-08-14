---
name: second-brain
description: Operating manual for a markdown second-brain vault. Use whenever the attached folder contains an AGENTS.md and folders like 00_Inbox/, 03_Resources/ and brain/prompts/ — i.e. any time you are reading, writing, filing, linking or maintaining notes in that vault, including when the human just talks about something they want remembered rather than naming a command.
---

# Second brain — read the vault's own manual first

The folder attached to this project is a personal second brain: markdown notes in a git repo, with
its own operating manual.

**Read `AGENTS.md` at the vault root now, and follow it.** It is the single source of truth — the
folder map, the frontmatter schema, the provenance rules, the voice rules, and the command table.
Everything below is only what Cowork needs that the other surfaces get for free.

Do not improvise a filing system. If `AGENTS.md` isn't there, the wrong folder is attached; say so.

## Why this skill exists

Cowork doesn't read `AGENTS.md` or `CLAUDE.md` from an attached folder the way Claude Code does,
and it doesn't read the `.claude/` directory in the repo. So the manual that loads automatically
everywhere else does not load here. This skill's only real job is to make you go read it.

That makes this the weakest seam in the vault's model-agnostic design, and it's worth being honest
about rather than papering over. If the human wants the manual loaded on *every* session without
depending on this skill triggering, they can paste the pointer in `brain/cowork/README.md` into the
project's **Instructions**. That's vendor metadata living outside git — which is exactly what this
repo argues against — so it's offered as a fix, not a recommendation.

## Talking counts as capturing

Per `AGENTS.md`: if the human just talks to you without naming a command, treat it as `capture`.
They should not have to learn six commands to use their own notes.

## Saving your work — the part Cowork doesn't do for you

Claude Code commits after every turn via a `Stop` hook. **Cowork has no equivalent, and it does not
read the repo's `.claude/settings.json` where that hook is defined.** So nothing here commits
itself.

At the end of a working session, run the vault's sync script:

```sh
brain/bin/sync
```

If you cannot run shell commands against the attached folder, **say so plainly and tell the human
their work is unsaved to git** — their notes are on disk but there is no commit to revert to, and
git-as-undo is the thing that makes an agent writing into someone's notes safe. Do not quietly skip
this step, and do not claim the vault was saved when it wasn't.

## What not to do here

- **No HTML artifacts, PDFs, or canvas documents.** Everything lands as markdown in the vault plus
  plain text in the conversation. A brief the human has to download is worse than one they can
  already read, and a file that isn't markdown in git isn't searchable, linkable or revertable.
- **Don't write into `brain/`.** It's the harness, not knowledge.
- **Don't copy transcripts or large binaries into the vault.** See `AGENTS.md`.
