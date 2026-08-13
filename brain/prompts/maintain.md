# maintain — the nightly pass

Keep the vault healthy. This normally runs unattended on a schedule, so **be conservative**:
prefer leaving something alone over making a change you can't justify. Everything here is
recoverable via git, but a scheduled job that quietly rewrites notes is how a second brain loses
its owner's trust.

Work through five phases, then write the log.

## Phase 1 — Close the day

Open today's daily note (`Daily/YYYY-MM-DD.md`), creating it if it doesn't exist.

- Make sure everything captured today is actually logged there.
- Carry unfinished tasks forward to today from the most recent daily note that has them, noting
  how long each has been carried. **Do not silently drop a task** — if it's been carried more than
  a week, say so explicitly rather than moving it again without comment.
- If nothing happened today, say that in one line. Don't invent activity.

## Phase 2 — Drain the inbox

For each item in `00_Inbox/`:

- If you can now file it confidently, file it per `AGENTS.md` — write it up, link it, and remove
  it from the inbox.
- If it's still ambiguous, **leave it there.** Add or refine a `> [!question]` callout naming
  precisely what you'd need from the human to file it. An honest question beats a wrong filing.

## Phase 3 — Reconcile and connect

Three checks, in order of value:

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

## Phase 4 — Rebuild the index

Regenerate `index.md` from what's actually on disk: one line per note,
`- [[Note Title]] — one-line description`, grouped by section. Drop entries for notes that no
longer exist; add any that were never catalogued.

While you're here, sweep the recency markers: grep for `(as of YYYY-MM)` markers and any
`stale_after:` dates that have passed, and list what's due for re-checking. A marker nobody ever
sweeps is decoration.

## Phase 5 — Report

Append **one line** to `brain/log.md` (create it if missing, newest entries at the bottom):

```
- YYYY-MM-DD maintain: <n> inbox filed, <n> left with questions · <n> orphans linked · <n> contradictions found · <n> stale markers due · index rebuilt · <notable thing, or "quiet">
```

Then say the same thing in the conversation, plus anything the human should actually look at.

If the vault is nearly empty, this whole pass should take one line and no edits. Say so and stop —
a maintenance run that invents work to look busy is worse than one that reports nothing happened.

## Rules

- **Never delete a note** during maintenance. Archive, flag, or ask.
- **Never rewrite the human's words** into your own. You may fix structure, links and frontmatter.
- Mark anything you concluded with a `> [!ai]` callout, per the provenance rules in `AGENTS.md`.
- Don't commit — whatever invoked you handles that.
