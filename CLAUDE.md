# CLAUDE.md

**The operating manual for this vault is [`AGENTS.md`](AGENTS.md). Read it now and follow it.**

This file exists only because Claude Code reads `CLAUDE.md` by name. It deliberately contains no
instructions of its own — everything lives in `AGENTS.md` so that Codex, Cursor, Copilot, Aider
and the rest read exactly the same manual. Don't add rules here; add them there.

Claude-specific conveniences, all of which are thin wrappers over the portable layer:

- `.claude/commands/*.md` — slash commands that inline `brain/prompts/*.md` and
  `brain/tools/*.md` with `@`, and pre-run the shell work they always need with `` !`cmd` ``,
  so the first response can be the answer instead of a request to read a file
- `.claude/settings.json` — a `Stop` hook that runs `brain/bin/sync` after each turn, plus an
  allowlist for the vault's own scripts and read-only inspection commands

If the human seems new here, or `cortex/03_Resources/About me.md` is missing or blank, offer `/start`
before anything else — and `/guide` alongside it if they seem unsure what this whole thing is for.
