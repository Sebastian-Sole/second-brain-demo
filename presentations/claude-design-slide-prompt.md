# Prompt for Claude Design — "Personal Assistant" deck, Sebastian's sections

You are extending an existing slide deck for a live presentation. The Intro slides (Mike Patterson's opening section) already exist. Your job is to create the slides for Sebastian Sole's sections, matching the existing deck's look and feel.

**Use the template slides at "Deck A - Template Slides"** as the visual foundation. Reuse their layouts, fonts, colours, and spacing. New slides must feel like they were always part of this deck, not bolted on.

## What the presentation is

A talk about building a personal AI assistant on top of a plain-text "second brain": an Obsidian vault (a git repo of markdown notes) that an AI agent reads, writes, and maintains through slash commands, scheduled runs, and connections to real services (calendar, weather, news, Notion). The audience is colleagues who will get access to a starter template afterwards and are meant to leave wanting to build their own.

Two presenters alternate: Mike (intro, one demo, closing hand-off) and Sebastian (the demos and features below). You are only making Sebastian's slides, plus the closing "key takeaways" and "get started" slides he also presents.

## Tone of voice

Write in the register of Oliver Burkeman (Four Thousand Weeks), at the length of Mark Manson, without Manson's contempt. Warm, plain-spoken, a little wry. Not a corporate AI pitch; no hype, no robot clichés.

Rule for every line: concede something, then land the point, in under 15 words.

Do:
- Admit the audience's skepticism inside the line itself. The humour is only the delivery vehicle for that concession.
- Prefer questions over claims. "What's the one thing that always gets in your way? Dinner. Again."
- Say "everyone has this problem", never "you have a weakness".
- Use self-deprecating specifics from real failures, not generic jokes. "It confidently told me the weather for the wrong city. Great formatting, though."
- Short, clear sentences. Few commas.

Don't:
- State opinions as laws of nature (the James Clear aphorism voice). "For years the problem was the machine. Now the problem is the relationship." is the voice to avoid.
- Be blunt more than once per piece. One Manson line is seasoning; two is a mood.
- Moralise, lecture, or promise.

Reference rewrite of the line to avoid:
"We've been promised a digital assistant roughly every three years since the nineties. This time might actually be different, and annoyingly, the reason it might work is you."

## Slides to create, in order

### 1. Demo 1 — The digest
- A slide introducing the morning digest: the assistant compiles a daily digest on its own schedule and delivers it to Notion. Leave a large placeholder for a screenshot of a real digest.
- A follow-up slide titled around "What just happened?" that unpacks the digest, with these points (keep each to a short label plus one line):
  - **The harness** — skills the assistant runs, output lands in Notion
  - **Connections** — calendar, news, weather, and other live sources
  - **It knows my preferences** — the digest is shaped by notes about me, not a generic template
  - **It ran itself** — a scheduled run; nobody typed anything
  - **Persistent notes** — what it learns stays in the vault and compounds

### 2. Demo 2 — /ingest
- One slide introducing `/ingest`: the assistant reads your past AI coding sessions and distils them into short notes the vault can answer from. The theme is *self-improving AI interaction* — it learns how you work with it from how you've already worked with it.

### 3. Demo 3 — "How do I actually do this?"
- One near-black slide with white text, minimal: this is the backdrop for a ~20 minute live demo. Something like the section title and the two commands being demoed:
  - `/start` — the first conversation; it gets to know you
  - `/new-idea` — turn "I wish it could…" into a working command: understand, plan, build
- No other content. It sits on screen while Sebastian works live.

### 4. Other features
- One slide, a simple vertical list. Each row: the command name on the left, a short one-line description to its right.
  - `/teach <any-subject>` — your own personal teacher: knows how you like to learn, and what you already know
  - `/explore` — wander the vault and see what it's connected
  - `/fix-my-prompt` — paste a prompt, get it back rewritten; it can read the docs once so you never have to again
  - `/interview` — the brain interviews *you*: spots gaps in what it knows, or add something new (`/interview me about my music taste` — music, movies, food, travel)

### 5. What it can look like (Mike's demo)
- One near-black slide with white text, same treatment as Demo 3. Section title plus three short labels:
  - Taste engine
  - Assumptions
  - Push to talk

### 6. Forced key takeaways
- One slide, maximum two messages, big type:
  - **Ask.** You can do anything with this — the only failure mode is not asking.
  - **You're in charge.** Don't like how it does something? Change it. It's your assistant.
- Keep the tone rules especially tight here; this is the emotional close, not a corporate summary slide.

### 7. Get started
- Final slide: point the audience to Notion, where they'll find:
  - Ideas you can implement today
  - AI 101
  - The harness docs
- One warm closing line in the tone above.

## Constraints

- Match the existing deck: same template family ("Deck A - Template Slides"), same type scale, same colour palette. The two demo slides (Demo 3 and Mike's demo) are the deliberate exception: near-black background, white text.
- All slide copy follows the Tone of voice section. Every line concedes something, then lands the point, in under 15 words. At most one blunt line in the whole set.
- Slides support a live talk; they don't replace it. Prefer one idea per slide, short lines, generous whitespace. No paragraphs, no bullet walls.
- Keep command names in monospace (`/start`, `/new-idea`, etc.).
- Leave clearly marked placeholders wherever a screenshot is expected (the digest slide).
