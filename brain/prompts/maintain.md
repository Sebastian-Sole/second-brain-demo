# maintain — the health pass

Keep the vault healthy. **Be conservative**: prefer leaving something alone over making a change
you can't justify. Everything here is recoverable via git, but an agent that quietly rewrites
someone's notes is how a second brain loses its owner's trust.

Assume this may one day be running unattended on a schedule, with nobody reading the output until
morning. Write every judgement call so it survives that: if you weren't sure, the vault should say
so in the file, not only in the conversation.

Work through five phases, then write the log.

## Phase 1 — Close the day

Open today's daily note (`Daily/YYYY-MM-DD.md`), creating it if it doesn't exist.

- Make sure everything captured today is actually logged there.
- **Surface what's open in `Tasks/` — don't copy any of it anywhere.** Tasks are notes now (see
  `brain/prompts/task.md`); nothing moves between daily notes, so there is no carry-forward and no
  way for one to breed duplicates. Read `Tasks/`, give each open task its age from `id:`, and
  **say so out loud** when something has been open a long time — "*Call the bank* has been open six
  weeks — still want it?" — rather than listing it silently for the tenth time.
- If nothing happened today, say that in one line. Don't invent activity.

## Phase 2 — Drain the inbox

For each item in `00_Inbox/`:

- If you can now file it confidently, file it per `AGENTS.md` — write it up, link it, and remove
  it from the inbox.
- If it's still ambiguous, **leave it there.** Add or refine an **Open question** callout naming
  precisely what you'd need from the human to file it. An honest question beats a wrong filing.

## Phase 3 — Reconcile and connect

Five checks, in order of value:

1. **Contradictions.** Look for notes making claims that disagree. When you find a pair, don't
   delete either — keep both, add recency markers `(as of YYYY-MM, source)`, and state plainly in
   the newer note what it supersedes and why. If you can't tell which is right, say so and flag it
   for the human. This is the single most valuable thing this pass does: an AI-maintained vault
   fails by accumulating quiet inconsistencies, not by running out of space.
2. **Orphans.** Find notes with no inbound or outbound links. For each, either wire it to
   something genuinely related, or — if it's stale and unconnected — suggest archiving it. Never
   manufacture a link that isn't real just to clear the count.
3. **Broken links.** `[[wikilinks]]` pointing at notes that don't exist. Some are intentional
   ("worth writing later") — leave those. Fix the ones that are clearly typos or renames.
4. **Assumptions.** Skip this entirely if `03_Resources/Assumptions.md` doesn't exist. Otherwise,
   for each `open` block: does anything captured since it was raised **satisfy its falsifier**? If
   so, refute it — `Status: refuted · <date>`, naming the note that did it, moved to **Refuted &
   withdrawn**, never deleted. This is the one verdict you may reach without the human, because a
   falsifier they already wrote is a test they already agreed to; anything short of that stays
   open. Mark anything open more than 90 days as `stale`, recount the header, and run
   `brain/bin/check` — fix every `[XX]` it reports. Never promote an assumption to a fact here, no
   matter how much evidence has piled up. Only the human does that.
5. **The task invariant.** `completed:` must be present whenever `task:` is `done` or `dropped`,
   and absent while it's `open` — that's what makes "how long was this open" computable from `id:`
   and `completed:`. **`brain/bin/doctor` checks this mechanically**, so run it and report what it
   found rather than re-walking `Tasks/` and `04_Archive/` by hand. Fix what it names: the missing
   date belongs in the file, not in your reply.

## Phase 4 — Rebuild the index

Regenerate `index.md` from what's actually on disk: one line per note,
`- [[Note Title]] — one-line description`, grouped by section. Drop entries for notes that no
longer exist; add any that were never catalogued.

**Rebuild the `Open tasks` section too** — one line per `task: open` note in `Tasks/`, linked by
title, newest-relevant first. Archived tasks stay out: `04_Archive/` is outside the default search
set, and a catalog listing a thousand finished tasks defeats the point of having one.

**Do not enumerate `06_Sessions/` here.** It has its own `index.md` and there can be thousands of
session notes; listing them in the root catalog would drown the notes it exists to surface. One
line pointing at `06_Sessions/index.md` is all the root index gets. If session notes are present,
refresh their own index while you're here.

While you're here, sweep the recency markers: grep for `(as of YYYY-MM)` markers and any
`stale_after:` dates that have passed, and list what's due for re-checking. A marker nobody ever
sweeps is decoration.

## Phase 5 — Report

Append **one line** to `brain/log.md` (create it if missing, newest entries at the bottom):

```
- YYYY-MM-DD maintain: <n> inbox filed, <n> left with questions · <n> orphans linked · <n> contradictions found · <n> assumptions refuted, <n> stale · <n> stale markers due · index rebuilt · <notable thing, or "quiet">
```

Leave the assumptions figures out of the line entirely if there's no register.

Then say the same thing in the conversation, plus anything the human should actually look at.

If the vault is nearly empty, this whole pass should take one line and no edits. Say so and stop —
a maintenance run that invents work to look busy is worse than one that reports nothing happened.

## Rules

- **Never delete a note** during maintenance. Archive, flag, or ask.
- **Never rewrite the human's words** into your own. You may fix structure, links and frontmatter.
- Mark anything you concluded with an **AI synthesis** callout, per the provenance rules in
  `AGENTS.md`.
- Don't commit — whatever invoked you handles that.
