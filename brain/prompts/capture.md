# capture — file a raw dump into the vault

Capture what the human gave you: a thought, a link, a decision, a transcript, whatever it is.

If they gave you nothing specific, capture what you just did or discussed in this session. If
there's nothing to capture at all, ask what they want to put in.

Follow the workflow in `AGENTS.md`. Concretely:

1. **Triage.** Decide what each piece is — a thought, external source material, a task, a journal
   entry, or a project update. One dump can be several of these; split it.

2. **Preserve first.** If any of it is external material (an article, a transcript, a pasted
   thread, a PDF), write the original verbatim into `raw/` as
   `raw/YYYY-MM-DD-<short-slug>.md` **before** you write anything else. Never edit that file
   afterwards.

3. **Search before writing.** Grep the vault for the concepts involved — titles, `aliases`, and
   body text, plus obvious synonyms. If a note on this already exists, **extend it** rather than
   creating a near-duplicate. Note what you found.

4. **Write atomically.** One idea per note in `03_Resources/`, with the full frontmatter block
   from `AGENTS.md`. Titles are claims, not labels. Write it in the human's voice — their idea
   sharpened, not replaced by a neutral summary. A big dump becomes several small linked notes,
   not one long one.

   If you generated a synthesis or an inference the human didn't say, mark it:

   ```
   > [!NOTE]
   > **AI synthesis** — …
   ```

5. **Link.** Every new note links to at least one other note and to its Area. Add the reverse
   link where it reads naturally. A link to a note that doesn't exist yet is fine.

   **If what they just told you settles an open assumption**, say so and record it now. A dump
   that contradicts one is a refutation — `Status: refuted`, their words as the reason, moved to
   **Refuted & withdrawn** in `03_Resources/Assumptions.md` and never deleted. One that confirms
   one is *not* a confirmation you can make on their behalf; note that it adds evidence and leave
   the verdict to `review-assumptions`. Most verdicts will arrive this way rather than in a review
   pass, so don't let one slide past unrecorded. Run `brain/bin/check` if you touched the register.

6. **Log and catalog.** Add a one-line entry to today's daily note (`Daily/YYYY-MM-DD.md`) so
   there's a timeline — create the note if it doesn't exist. Then add each new note to `index.md`
   under the right section as `- [[Note Title]] — one-line description`. Keeping the catalog
   current is what lets the next session find this without searching for it.

7. **Report.** Tell them briefly what you created, updated, and linked — and surface anything you
   left in `00_Inbox/` as an explicit question.

Rules that matter here:
- **Never lose anything.** If you can't process a piece, it goes to `00_Inbox/` with an
  **Open question** callout describing what you were unsure about. Don't silently drop it.
- **Don't pad.** Five well-linked atomic notes beat one sprawling essay. If the dump only
  contains one idea, write one note.
- Don't invent facts to make a note feel complete.

**Output surface:** markdown notes in the vault, plus a short plain-text report in the
conversation. Never an artifact, PDF or rendered document — see `AGENTS.md`.

The `Stop` hook commits for you — you don't need to run git.
