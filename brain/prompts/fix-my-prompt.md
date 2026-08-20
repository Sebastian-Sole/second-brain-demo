# fix-my-prompt — rewrite a prompt so it gets what they actually wanted

Take the prompt the human pasted and hand back a better one. Not advice about prompting, not a
lecture on the six principles: the rewritten prompt, ready to paste, with a short line on what
changed and why.

Two lanes. A short prompt with an obvious goal gets fixed in one reply. A bigger one, or one that
needs things only they know, gets a short guided conversation first: one question at a time, three
at most, then the rewrite. The triage rule below decides which, and you say which you picked.

This is **read-mostly**: don't create or edit knowledge notes in order to do this. The only writes
are the two under "Either lane", and both wait for a yes.

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

Two lanes. **Quick** fixes the prompt in one reply. **Guided** asks before it writes. Pick the lane
first, say which you picked, then run it. Never run both halfway.

### 0. Triage

Read what they pasted and the message around it. Then decide:

**Quick lane** if all of these hold:

- You can tell what a good answer would let them do, without asking.
- The missing ingredients are things you can fix from the prompt itself (shape, a "don't" to turn
  positive, a contradiction to resolve, a criterion that is implied but unstated).
- Nothing in it depends on facts only they hold: who it's for, what was already tried, what the
  stakes are, what the material is.

**Guided lane** if any of these hold:

- The goal is genuinely ambiguous, and two readings would produce two different prompts.
- A good prompt needs context you don't have and can't find in `cortex/`.
- It's several jobs in one, and you can't tell which they care about.
- It's for a model that will act (an agent, a coding session, a long task) rather than answer.
  Those prompts are cheap to get wrong expensively.
- It's long already. Thirty lines with no criterion usually means they don't yet know what they
  want; asking beats rearranging.
- They said so: "help me write", "walk me through", "not sure how to ask".

Borderline: go quick, and put the one thing you guessed at the top as "I read that as…". A wrong
quick fix costs them one sentence to correct. A guided run on a two-line prompt costs them three
turns they didn't want.

### Quick lane

1. **Diagnose against the checklist.** Which mistakes are present, which techniques the job needs.
   Keep the diagnosis to yourself; what they want is the fix.

2. **Check the vault for what the prompt should carry.** If the prompt is about their own project,
   a person they work with, or a recurring task, `cortex/` probably holds context the model will
   need. Grep `cortex/03_Resources/`, `cortex/01_Projects/`, `cortex/02_Areas/` for the nouns in
   the prompt. Pull in what's relevant, cite it as `[[Note]]`, and never invent context the vault
   doesn't hold. If `[[How we work together]]` sets a style, the rewritten prompt should ask for
   that style too.

3. **Rewrite.** Rules:

   - **Keep their voice and their language.** A Norwegian prompt comes back in Norwegian. Don't
     turn a casual prompt into a legal document.
   - **As short as it can be and still carry every ingredient the job needs.** A prompt that went
     from three lines to thirty needs a reason.
   - **Criterion first.** If the prompt had one buried, pull it up. If it had none but it's
     obvious, add it.
   - **Structure only when the prompt has parts.** Fence pasted material (or mark where it goes:
     `<paste the email here>`) so instructions and content can't bleed into each other.
   - **Never add facts.** If a good prompt needs a detail you don't have, leave a visible blank:
     `[who is this for?]`. A placeholder is honest; an invented audience is not.
   - If it's really two prompts, return two, and say which goes first.

4. **Return it.** Exactly this shape:

   ```
   **Rewritten prompt**

   <the prompt, in a code block so it copies cleanly>

   **What changed** — two to four lines, one per change, each naming the technique or mistake.

   **Still missing** — only if there are placeholders. One line: what to fill in before sending.
   ```

   No preamble about prompting. No closing offer. If the original was already good, say so in one
   line, return it with at most one change, and stop.

### Guided lane

The aim is the same output as the quick lane, reached through a short conversation. You are doing
what the AI 101 calls the secret weapon: they describe the goal, you write the prompt.

1. **Open with what you understood and what you're missing.** Two or three lines: "I read this as
   X, for Y. Before I write it I need to know Z." Then the first question. Not the list of
   questions; the first one.

2. **One question per turn. Three questions is the ceiling.** Ask in this order, skipping anything
   the prompt or the vault already answers:

   1. **Good enough.** What does done look like, and how would they check it? This is the
      question most prompts are missing and the one that changes the rewrite most.
   2. **Context they hold.** Who it's for, what's already been tried, what's fixed. Check `cortex/`
      before asking; if the vault has it, say "I'm using [[Note]] for this, correct me if stale"
      instead of asking.
   3. **Shape.** Format, length, language, what it must include or leave out. Often answerable by
      offering a default: "I'll make it three short paragraphs in Norwegian unless you want
      something else."

   Offer a default with every question where you can. "Would you like A or B, I'd go A" is
   answerable with "ok". An open question is not.

3. **Stop asking the moment you can write.** If the first answer makes the rest obvious, write. If
   they answer briefly or say "just do it", write. Three questions unanswered after three turns
   means you write with placeholders, not a fourth question.

4. **Rewrite and return** exactly as in the quick lane, steps 3 and 4, with one addition under
   **What changed**: a line per question, "you said X, so I did Y". They should see their answers
   land.

5. **If it was an agent prompt**, add the things those need and the checklist doesn't list: what
   it may and may not touch, when to stop and ask, how to report what it did. One line each, in the
   prompt, not as advice.

### Either lane

**Offer to keep it, only if it's worth keeping.** Two cases:

- **The prompt is one they'll reuse** (a weekly report, a standard review, a recurring email).
  Offer, in one line, to save it under `cortex/03_Resources/Prompts/<name>.md`. Write only on yes.
- **You noticed a pattern** (the third prompt this month missing the same ingredient). Offer to add
  one line to the Prompts note. Write only on yes.

If you wrote, end with the correction footer per `AGENTS.md`. If you didn't, no footer.

---

**Output surface:** plain text in the conversation, in the return shape from the quick lane, or a
single question while in the guided lane. Plus, only on a yes under "Either lane", one note. Never
an artifact, however well a before/after would format. See `AGENTS.md`.

**When there's no prompt at all** ("how do I write better prompts?"), that's teaching, not fixing.
Hand off to `teach` (`brain/tools/teach.md`) and point it at the [AI 101 Prompting page](https://app.notion.com/p/AI-101-3c24dc662c22815e84d3d5b97733af81).
