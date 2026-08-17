# ask — answer from the vault

Answer the human's question from what's in this second brain.

If they didn't give you a specific question, answer whatever they just asked in conversation. If
there's no question at all, ask what they want to know.

This is **read-mostly** — don't create or edit knowledge notes in order to answer.

0. **Start with `index.md`.** It lists what exists. Reading the catalog first is cheaper and more
   accurate than searching blind, and it tells you what *isn't* there — which is how you avoid
   confidently answering from a gap.

1. **Search broadly, then read narrowly.**
   - Grep across `03_Resources/`, `01_Projects/`, `02_Areas/`, `Daily/`, and `00_Inbox/` — titles,
     `aliases`, and body text. Try synonyms and entity names, not just their exact words.
   - Follow `[[wikilinks]]` out from the best hits to pull in neighbours.
   - Then actually open and read the handful that look relevant. Depth on the right 3–6 notes
     beats skimming forty.
   - **If the question is about past work** — "what did I decide about X", "when did I last touch
     Y", "why did we go with Z" — also search `06_Sessions/`, starting from its `index.md`. Don't
     search it otherwise: there may be thousands of session notes and they'll out-match your real
     notes on any keyword.

2. **Answer in their voice.** Direct answer first, supporting detail after. Concrete and terse.
   No "based on your notes" preamble, no hedging — write it the way they'd summarise it back to
   themselves.

3. **Cite as you go.** Every claim traces to a note via `[[Note Title]]` so they can click
   through. Keep any recency markers `(as of YYYY-MM, source)` from the source note.

4. **Separate what the vault says from what you're adding.** If you're inferring or synthesising
   across notes rather than reporting, mark it — an **AI synthesis** callout per `AGENTS.md`, or a
   plain inline note. The human must always be able to tell their own past thinking from your
   commentary.

5. **Be honest about gaps.** If the vault genuinely doesn't cover this, say so plainly. Don't pad
   with general knowledge and don't fabricate a citation. Offer the closest thing that *is*
   captured, and ask whether they want to research it and capture the answer.

6. **Offer to capture — don't just do it.** If answering surfaced something worth keeping (a
   synthesis across notes, a missing link you noticed), offer it. Only write if they say yes. You
   may fix an obviously broken `[[link]]` in passing — mention it if you do.

**Output surface:** plain text in the conversation, and nothing else — this command doesn't write.
Never an artifact or rendered document, however well the answer would format. See `AGENTS.md`.

Keep it a briefing, not an essay. The win is that they get the answer without opening the vault.
