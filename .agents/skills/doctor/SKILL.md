---
name: doctor
description: Check this vault's install and say exactly what to fix.
---

If you have not read `AGENTS.md` at the repository root yet this session, read
it first — it is this vault's operating manual and this skill assumes it.

Run `brain/bin/doctor --check` and relay its report in its own plain
language. If something is fixable and the human wants it fixed, run
`brain/bin/doctor` without `--check`, which repairs missing folders and
`.gitkeep`s rather than only reporting them.

<!-- Thin adapter for Codex (doctor is invoked as $doctor). The real prompt is
     brain/bin/doctor, shared by every agent — same pattern as .claude/commands/.
     Don't add instructions here; edit brain/bin/doctor instead. -->
