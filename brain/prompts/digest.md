# digest — roll up recent activity

Produce a digest of recent activity in the second brain.

**Window:** if the human named one, interpret it loosely (`week`, `month`, `since Tuesday`, a date
range). Default to the **last 7 days** if nothing is given. State the window you used at the top.

Read the daily notes in that window, everything in `00_Inbox/`, and any notes whose `created` or
`updated` frontmatter falls inside it. Then write the digest to
`Daily/YYYY-MM-DD — Digest.md` (dated today) and show it in the conversation.

Structure it in four sections:

### 1. Shipped / Captured
What actually happened, grouped by project or area. Every line links to the note it came from.
Be specific — "merged the auth refactor" beats "made progress on the backend". If nothing
happened in a group, leave the group out rather than padding it.

### 2. Patterns
**This is the section that earns the digest.** Look across the window for themes the human never
stated explicitly:
- the same idea arriving from two unrelated directions
- a kind of work that keeps recurring
- something they keep starting and not finishing
- a shift in what they're spending attention on

Two or three real observations. If there genuinely isn't a pattern, say so — a fabricated theme is
worse than a short section. Mark these as yours:

```
> [!ai] Synthesis — not stated anywhere explicitly; this is a read across N notes.
```

### 3. Stalled
A table: **what · how long · the smallest next action.** Anything open in a project note, any task
carried across multiple daily notes, any question left in `00_Inbox/`.

The "smallest next action" column must be genuinely small and specific — the actual first move,
not a restatement of the goal.

> Be direct here. If something has been open for weeks, say the number of weeks. A digest that
> softens this is useless — the whole point is that the vault notices what the human is avoiding.

### 4. Open loops
Threads waiting on someone else, unanswered questions, things half-decided.

---

Then, in the conversation (not the file), close with **one line**: the single thing most worth
doing next, and why it's that one.

Notes:
- If the vault is nearly empty (a fresh install), say so plainly and show what little there is
  rather than inventing content. It'll get better as they use it.
- The `Stop` hook commits for you.
