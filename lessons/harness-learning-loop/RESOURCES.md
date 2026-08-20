# Resources

## Primary

- **[Claude Code hooks reference](https://code.claude.com/docs/en/hooks)** — the authority for the
  31 events, which three can inject context, matcher values, and hook stdin fields. Fetched
  2026-08-20. Trust: high (vendor docs for the exact runtime in use). Caveat: the stdin field names
  were read via a summariser, so confirm against one real hook run before depending on them.

## In-repo, and higher trust than any external source for this project

- `AGENTS.md:21-167` — profile, agreement, the propose/accept protocol, both budget caps.
- `AGENTS.md:565-700` — the assumptions register: the one-way rule, the block format, confidence
  rubric, the four gates. The pattern decision 7 should copy rather than reinvent.
- `brain/bin/agreement` — the working example of a context-injecting hook, with its house rules in
  its own comments.
- `brain/bin/check` — how a prose rule gets turned into a mechanical one. The precedent for
  enforcing anything new.
- `.gitignore` — five separate entries exist because `sync` commits and pushes within one turn. Read
  before choosing where a friction log lives.

## Not yet consulted

- Whether Codex or Gemini expose a pre-prompt hook equivalent. Unresolved, and it bounds how strong
  the portability claim can be on stage.
