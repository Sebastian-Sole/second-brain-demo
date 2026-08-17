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

2. **Answer in their voice, at the size of the question.** Direct answer first, supporting detail
   after. Concrete and terse. No "based on your notes" preamble, no hedging — write it the way
   they'd summarise it back to themselves.

   Match the register they asked in. A question typed in one line gets a few sentences back;
   headers, bold labels and sections are for a question that genuinely has parts. Turning a
   passing question into a document is its own kind of slop.

3. **Cite as you go.** Every claim traces to a note via `[[Note Title]]` so they can click
   through. Keep any recency markers `(as of YYYY-MM, source)` from the source note.

4. **Separate what the vault says from what you're adding — and keep the second part smaller.**
   If you're inferring or synthesising across notes rather than reporting, mark it — an
   **AI synthesis** callout per `AGENTS.md`, or a plain inline note. The human must always be able
   to tell their own past thinking from your commentary.

   Never let the marked half outweigh the sourced half. Per `AGENTS.md`, marking an inference
   doesn't license making it — and a young vault is a trap here, because most of its notes are
   *about the vault*. Reading those as a portrait of the person reads the scaffolding as the human.

   **If the honest answer needs a claim the vault doesn't hold**, don't smuggle it into the prose.
   Switch to the three-block form and keep it short:

   ```
   **Known** — what the vault actually holds, with [[links]].
   **Assumed** — the claim · confidence · basis-kind · because <the leap, one line>.
   **Would change my mind** — the falsifier.
   ```

   Cap it at three, obey the gates in `AGENTS.md` (ten notes, not the scaffolding, not your
   session's environment), and check `03_Resources/Assumptions.md` first so you don't re-raise
   something already refuted. If the question is *mostly* that — a question about them rather than
   about their notes — say so and offer `infer`, which does this properly and registers what's
   worth keeping. `ask` answers from the vault; `infer` reasons past it.

5. **Be honest about gaps, including when the gap is most of it.** If the vault doesn't cover this,
   say so plainly. Don't pad with general knowledge, don't fabricate a citation, and don't
   compensate for a thin vault by inferring harder. "Barely anything yet — here's the little
   there is" is a good answer to a question about a two-day-old brain; four hundred words of
   character analysis off five notes is not.

6. **Offer to capture — don't just do it.** If answering surfaced something worth keeping (a
   synthesis across notes, a missing link you noticed), offer it. Only write if they say yes. You
   may fix an obviously broken `[[link]]` in passing — mention it if you do.

7. **A problem you tripped over is a footnote, not the headline.** If you notice something broken
   while looking — a blanked profile, a stale note, a dead link — answer the question they actually
   asked, in full, and put the problem in a line at the end. Don't open with it, don't go
   reconstruct it from `git log` unless they ask, and don't close by handing back a bundle of
   chores in place of an answer. One offer, phrased so that "no" is a complete reply.

**Output surface:** plain text in the conversation, and nothing else — this command doesn't write.
Never an artifact or rendered document, however well the answer would format. See `AGENTS.md`.

Keep it short enough that they read it rather than skim it. The win is that they got the answer
without opening the vault — not that you produced a document.
