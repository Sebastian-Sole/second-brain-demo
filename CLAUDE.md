# CLAUDE.md

**The operating manual for this vault is [`AGENTS.md`](AGENTS.md). Read it now and follow it.**

This file exists only because Claude Code reads `CLAUDE.md` by name. It deliberately contains no
instructions of its own — everything lives in `AGENTS.md` so that Codex, Cursor, Copilot, Aider
and the rest read exactly the same manual. Don't add rules here; add them there.

Claude-specific conveniences, all of which are thin wrappers over the portable layer:

- `.claude/commands/*.md` — slash commands that point at `brain/prompts/*.md`
- `.claude/settings.json` — a `Stop` hook that runs `brain/bin/sync` after each turn, plus an
  allowlist for the vault's own scripts and read-only inspection commands

If the human seems new here, or `AGENTS.md`'s **About the human** section is still blank, offer
`/setup` before anything else.
