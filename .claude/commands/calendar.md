---
description: Read your schedule and answer from it — creates an event only when you ask and approve.
---

@brain/tools/calendar.md

The human's input, if any: $ARGUMENTS

<!-- Thin adapter. The real prompt is brain/tools/calendar.md, shared by every agent — `@` inlines it
     here rather than copying it, so there is still one manual. Claude Code and Gemini CLI can
     expand a file and a command's output into the prompt before the agent sees it; Codex and
     Copilot can do neither, and their wrappers still say "read the file", which costs them one
     round trip and nothing else. Don't add instructions here — edit brain/tools/calendar.md instead. -->
