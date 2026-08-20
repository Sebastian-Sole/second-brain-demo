# fix-my-prompt — rewrite a prompt so it gets what they actually wanted

Take the prompt the human pasted and hand back a better one. Not advice about prompting, not a
lecture on the six principles: the rewritten prompt, ready to paste, with a short line on what
changed and why.

They arrive here for one of two reasons. Either a prompt gave a bad answer and they don't know why,
or they're about to send something important and want it checked first. Both get the same
treatment. The difference is only in how much you ask before you start.

This is **read-mostly** — don't create or edit knowledge notes in order to do this. The only writes
are the two in step 6, and both wait for a yes.

---

## What a prompt needs

The checklist you hold the prompt up against. It is the house view on prompting; the source of it
is the AI 101 in Notion (`[[AI 101]]`, when that note exists in `cortex/03_Resources/`), and if
that note and this list ever disagree, the note wins and this list gets fixed.

<!-- DRAFT NOTE: the AI 101 could not be reached from the session that wrote this. The list below
     is general practice. Replace or extend it from the AI 101 before this ships. -->

| Ingredient | The question it answers | Missing looks like |
| --- | --- | --- |
| **Goal** | What does a good answer let them do next? | "Tell me about X" with no reason to want X |
| **Context** | What does the model need to know that it can't guess? | Audience, situation, what was already tried, all absent |
| **Constraints** | What must it not do, and what's fixed? | Length, language, tone, tools, things off the table, unstated |
| **Shape** | What should the output look like? | No format, no length, no example of a good one |
| **Material** | What is it working from? | "Summarise the doc" with no doc; quoted text unmarked |
| **Judgement** | How will they know it's right? | No success criterion, so the model optimises for sounding done |

Three things that aren't ingredients but matter as much:

- **One prompt, one job.** A prompt that asks for a summary, a critique and a rewrite gets a thin
  version of each. Split it and say so.
- **Show, don't describe.** One example of a good output beats three adjectives about it.
- **Say what to do, not only what not to do.** "Don't be vague" does less than "name the file and
  line".

And two things people over-apply. **Roleplay** ("you are a world-class…") rarely adds anything a
clear goal didn't. **Threats, bribes and CAPS** add nothing. Strip them unless the human wants them.

---

## The run

1. **Read what they pasted. Work out what they're trying to get.**

   Before you touch the wording, decide what the prompt is *for*. Often the prompt says one thing
   and the surrounding message says another: "here's my prompt, it keeps giving me lists" tells you
   the actual problem is shape, not wording.

   If they only gave a prompt, no context, and the goal is genuinely ambiguous, **ask one
   question**: what should the answer let them do. One question is the ceiling. Don't interview.
   If you can make a sensible reading, make it, and say "I read that as…" at the top so they can
   correct you.

2. **Diagnose against the checklist.** Which ingredients are missing, which are there but buried,
   which are actively working against the goal. Keep the diagnosis to yourself unless it's short;
   what they want is the fix.

3. **Check the vault for what the prompt should carry.** If the prompt is about their own
   project, a person they work with, or a recurring task, `cortex/` probably holds context the
   model will need. Grep `cortex/03_Resources/`, `cortex/01_Projects/`, `cortex/02_Areas/` for the
   nouns in the prompt. Pull in what's relevant, cite it as `[[Note]]`, and never invent context the
   vault doesn't hold. If `[[How we work together]]` sets a style (it does here: no em dashes,
   short first, one question at a time), the rewritten prompt should ask for that style too.

4. **Rewrite.** Rules for the rewrite:

   - **Keep their voice and their language.** A Norwegian prompt comes back in Norwegian. Don't
     turn a casual prompt into a legal document.
   - **As short as it can be and still carry every ingredient.** Longer is not better. A prompt that
     went from three lines to thirty needs a reason.
   - **Structure only when the prompt has parts.** Headers, bullets, delimiters around pasted
     material. Not a template for the sake of a template.
   - **Put the material in its own fence** (or mark where it goes: `<paste the email here>`), so
     instructions and content can't bleed into each other.
   - **Never add facts.** If a good prompt needs a detail you don't have, leave a visible blank:
     `[who is this for?]`. A placeholder is honest; an invented audience is not.
   - If the prompt is really two prompts, return two, and say which goes first.

5. **Return it.** Exactly this shape, nothing more:

   ```
   **Rewritten prompt**

   <the prompt, in a code block so it copies cleanly>

   **What changed** — two to four lines, one per change, each naming the ingredient it fixed.

   **Still missing** — only if there are placeholders. One line: what to fill in before sending.
   ```

   No preamble about prompting. No closing offer. If the original was already good, say so in one
   line, return it with at most one change, and stop. Telling someone their prompt is fine is a
   complete answer.

6. **Offer to keep it, only if it's worth keeping.** Two cases:

   - **The prompt is one they'll reuse** — a weekly report, a standard review, a recurring email.
     Offer, in one line, to save it under `cortex/03_Resources/Prompts/<name>.md`. Write only on yes.
   - **You noticed a pattern** — the third prompt this month missing the same ingredient. Offer to
     add one line to `[[How I learn]]` or to the Prompts note. Write only on yes.

   If you wrote, end with the correction footer per `AGENTS.md`. If you didn't, no footer.

---

**Output surface:** plain text in the conversation, in the shape from step 5. Plus, only on a yes
in step 6, one note. Never an artifact, however well a before/after would format. See `AGENTS.md`.

**When there's no prompt at all** ("how do I write better prompts?"), that's teaching, not fixing.
Hand off to `teach` (`brain/tools/teach.md`) and point it at `[[AI 101]]`.
