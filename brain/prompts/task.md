# task — open, list, complete, drop or edit a task

CRUD on tasks. This is a **skill**: it touches nothing but the vault, needs no network, and works
in any agent.

**One note per task. There are no inline checkboxes anywhere in this vault.** If you find `- [ ]`
lines in a daily note or a project note, they're legacy or the human's own hand — offer to convert
them into task notes, and don't silently rewrite them either way.

Work out which of the five operations they're asking for, do that one, and stop. Answer at the size
of the question.

---

## The model

Open tasks live in **`Tasks/`** — top-level, unnumbered, alongside `Daily/` and `raw/`. The
`00_`–`05_` prefixes belong to PARA; this isn't a PARA bucket.

**While open, the filename is the title:** `Tasks/Call the bank.md`. It's a linkable note, so a
project can say `[[Call the bank]]`.

Frontmatter, on top of every normal field from `AGENTS.md` (`title`, `stage`, `status`, `created`,
`updated`, `generated`, `verified`, `area`, `tags`, `source`):

```yaml
type: task
id: 2026-08-18T14:22           # immutable. Set once at creation. Never edit it.
task: open                     # open | done | dropped
completed:                     # a date. REQUIRED when task is done or dropped. Absent when open.
recurs:                        # reserved, not yet implemented — leave blank
project: "[[Some project]]"    # quoted wikilink, or blank
```

Four of those look arbitrary without their reasons, so here they are:

- **`task:` is not `status:`.** `status:` already means *trust* (`draft | stable | deprecated`) on
  every note here. Put done-ness in it and you corrupt every "has a human verified this" query in
  the vault. A task can perfectly well be `task: done` and `status: draft`.
- **`id:` is immutable and survives the rename on completion.** The file gets renamed and moved
  when the task closes; `id` is the only thing that still says it's the same task afterwards. It's
  also the start of the clock.
- **`completed:` is required whenever `task:` isn't `open`.** That invariant is what makes "how
  long was this open" computable from `id` and `completed`. `brain/bin/doctor` checks it.
- **There is no priority field, deliberately.** An agent that can read the calendar and the project
  notes ranks better than a letter grade, and a priority written once rots — everything filed
  urgent in March is still urgent in September, at which point nothing is. Work out ordering at the
  moment you're asked.

---

## add

1. **Search `Tasks/` first.** Grep titles and bodies for the thing and its obvious synonyms. If an
   equivalent task is already open, say so and extend it rather than creating a near-duplicate.
2. Write `Tasks/<Title>.md` with the block above: `task: open`, `completed:` blank, `stage: active`,
   `id:` set to now, `area:` filled in, `project:` set if it belongs to one.
3. The body says why it exists and what "done" looks like — one or two lines, in their words. Link
   the project note and add the reverse link there.
4. Log one line in today's daily note (`Daily/YYYY-MM-DD.md`), creating it if needed.
5. **Add it to `index.md` under `## Open tasks`** — `- [[Call the bank]] — one line on what it is`.
   `AGENTS.md` has every session read that catalog first, and `capture` hands tasks straight here
   instead of cataloguing them itself, so if you skip this the task is missing from the catalog
   until somebody runs `maintain`.

**Ask for a due date only if they implied one.** Don't interrogate them; a task with no date is a
perfectly good task, and the fastest way to make someone stop capturing is to make capture cost
five questions.

## list

Reads only — this operation writes nothing.

1. Read every note in `Tasks/`. Default to `task: open`.
2. Order by **relevance**, not by filename: what's due soonest, what belongs to whatever they're
   working on now, what they just mentioned. Say why the top one is on top if it isn't obvious.
3. **Give each one its age**, computed from `id:` — "open 3 days", "open since 14 June".
4. **Flag anything that's been open a long time** instead of listing it silently for the tenth
   time. Say it out loud: "*Call the bank* has been open 6 weeks — still want it?" A list that
   never notices its own dead weight is how a task folder becomes a graveyard.
5. Accept natural filters — "what's due this week", "what's open on the billing project",
   "anything about the flat". Filter on `project:`, `area:`, dates and body text.

Archived tasks aren't in the default set. Search `04_Archive/` only if they ask about finished ones.

## complete / drop

1. **Resolve which task they mean.** If exactly one matches, proceed. **If two match, ask** — name
   both and let them pick. Never guess between two live tasks.
2. **Dropping requires a reason**, recorded in the body. "Dropped: the bank fixed it themselves."
   A dropped task with no reason is indistinguishable from one that was lost.
3. Set `task: done` (or `dropped`), set `completed:` to today's date, set `stage: archived`, bump
   `updated:`. Leave `id:` exactly as it is.
4. **Move the file — never delete it, and let the suffix follow `task:`:**
   `Tasks/Call the bank.md` → `04_Archive/Call the bank (done 2026-08-18).md` when it was completed,
   or `04_Archive/Call the bank (dropped 2026-08-18).md` when it was dropped. A dropped task that
   archives as "done" lies about itself forever, and `id:` is the only identity left to contradict
   it. Update `title:` to match the new filename.
5. **Fix every inbound link in the same pass.** Grep the vault for `[[Call the bank]]` and repoint
   it. This is what makes the rename legal under the vault's never-break-inbound-links rule — and
   you wrote those links, so you know all of them.
6. **Write a pointer line into today's daily note**, and into the project note if the task has one.
   The archived file holds the detail; the log line links to it:

   ```markdown
   - Done: [[Call the bank (done 2026-08-18)]] — opened 2026-08-14
   ```

7. **Take its line out of `## Open tasks` in `index.md`.** That section lists what's open; the
   archived note stays reachable by folder and by the pointer line you just wrote.

Why archive rather than delete: git history is not a recovery path for someone who doesn't know
git. "Where did that task go" has to be answerable by opening a folder. And `04_Archive/` is
already outside the default search set, so a thousand finished tasks pollute nothing.

## edit

Re-title, re-date, re-project, sharpen the body.

- **Re-titling an open task renames the file and fixes inbound links in the same pass** — same
  procedure as step 5 above. A rename that leaves a broken `[[link]]` behind isn't finished.
- Changing `project:` means fixing the link on both project notes, old and new.
- Bump `updated:`.
- **Never edit `id:`.** Not on a re-title, not on a re-date, not to "tidy" it.

---

## Rules

- **Never infer a task the human didn't ask for.** A sentence that mentions an obligation is not a
  task. If it's genuinely ambiguous, ask — or capture it as a note and say that's what you did.
- **Anything you wrote ends with the correction footer**: one line naming what changed and how to
  fix it.

  ```
  Filed as a task: Tasks/Cancel the insurance.md
  (say "make it a note" if that's wrong)
  ```

  A pure `list` created nothing, so it gets no footer.
- Don't write `recurs:` and don't act on one if you find it. It's reserved and not implemented.
- Never delete a task note. Archive it.

Don't commit — whatever invoked you handles that.
