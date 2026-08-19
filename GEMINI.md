# GEMINI.md

**The operating manual for this vault is [`AGENTS.md`](AGENTS.md). Read it now and follow it.**

This file exists only because Gemini CLI reads `GEMINI.md` by name and treats `AGENTS.md` as
opt-in. It deliberately contains no instructions of its own — everything lives in `AGENTS.md` so
that Claude Code, Codex, Cursor, Copilot, Aider and the rest read exactly the same manual. Don't
add rules here; add them there.

Gemini-specific conveniences, all thin wrappers over the portable layer:

- `.gemini/commands/*.toml` — slash commands that inline `brain/prompts/*.md` and
  `brain/tools/*.md` with `@{}`, and pre-run the shell work they always need with `!{}`, so the
  first response can be the answer instead of a request to read a file. They carry no
  instructions of their own — edit the file in `brain/` instead.
