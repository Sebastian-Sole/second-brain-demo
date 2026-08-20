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

The checklist you hold the prompt up against. It is a condensed copy of the Prompting page in the
[AI 101](https://app.notion.com/p/AI-101-3c24dc662c22815e84d3d5b97733af81) (Notion, public), which
in turn draws on Anthropic's AI Fluency course. If this list and that page ever disagree, the page
wins and this list gets fixed.

The one-sentence version, from that page: prompting is briefing a new colleague. What you want,
why, and what good enough looks like. Everything below is a variant of that.

**Before anything else: does the prompt say what good enough looks like?** "A dinner suggestion" is
not a criterion. "Three dishes, under 30 minutes, not what we ate yesterday, and tell me which
ingredients I'm missing" is. Most answers that feel bad are answers to a prompt with no criterion.
Check this first, every time.

Then the six techniques. A good prompt doesn't need all six; it needs the ones its job calls for.

| # | Technique | What it looks like | Missing looks like |
| --- | --- | --- | --- |
| 1 | **Context** | What they want, why, and who they are | "Tell me about climate change" with no interview in Indonesia behind it |
| 2 | **Examples** | One or more input → wanted-output pairs, covering different cases | Three adjectives about the style and no sample of it |
| 3 | **Shape** | Format, length, language, sections, hard requirements | No format, so the model picks one |
| 4 | **Steps** | The order to work in, when many valid routes exist | "Analyse the sales data" with no sequence |
| 5 | **Think first** | Ask it to weigh factors, constraints, alternatives before answering | Only worth adding for judgement calls; newer models often do it anyway |
| 6 | **Role** | Expertise, perspective or tone | "Explain X" when "as an experienced teacher to a smart ten-year-old" was the point |

The six mistakes, which are what you are actually looking for in the pasted prompt:

- **Assuming it reads minds.** What they didn't say, it guesses. Make them say it.
- **Five unrelated jobs in one message.** One thing at a time. If the prompt is two prompts, return
  two and say which goes first.
- **Vague about good enough.** See above.
- **Saying "don't".** "Don't use bullet lists" describes what they don't want. "Write it as three
  short paragraphs" describes what they do. Rewrite every negative as a positive where you can.
- **Contradictory instructions.** "Short but thorough", "creative but stick to the facts". Pick one,
  or make the trade-off explicit ("short; if something had to go, say what").
- **Not giving feedback.** Not a prompt-writing error, but if they pasted a whole failed exchange,
  the fix may be "reply: no, shorter, drop point two", or "start a fresh conversation". Say so
  instead of rewriting the opening prompt.

**Calibration, not rules.** The page is explicit about this and so should you be: nearly every
mistake comes in a pair. Too vague or too detailed. Too little context or everything they have. The
skill is knowing which side this prompt is on right now. A prompt that is already thirty lines does
not need more structure; it probably needs the criterion pulled to the top and half the rest cut.

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
Hand off to `teach` (`brain/tools/teach.md`) and point it at the [AI 101 Prompting page](https://app.notion.com/p/AI-101-3c24dc662c22815e84d3d5b97733af81).
