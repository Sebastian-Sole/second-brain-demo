# explain — teach it at their level

Teach the human the thing they asked about, pitched at *them*: what they already know, how they
like to learn, what they're working on this week.

If they didn't name a topic, teach whatever they were just puzzling over in conversation. If
there's nothing, ask what they want to understand.

**This is not `ask`.** `ask` interrogates the vault — "what did I decide about X", "what do I know
about Y" — and answers from their own notes; `explain` teaches something new mostly from general
knowledge, and touches the vault only to calibrate the pitch. If what they actually want is their
own past thinking played back, stop and hand off to `ask` rather than lecturing them about a
subject they've already written notes on.

This is **read-only**. It creates and edits nothing.

1. **Read one spoke: `[[How I learn]]`.** Per `AGENTS.md`, `[[About me]]` is a hub read every
   session and the detail lives in linked spokes. Read that one. Don't walk the rest — each spoke
   costs context on a turn that needs exactly one of them.

   **If it doesn't exist, that's normal**, especially in a young vault — spokes appear when
   there's something real to put in them. Pitch sensibly and get on with it. Afterwards, *once*,
   offer to record how they'd have preferred it:

   ```
   Want me to start [[How I learn]] with "worked example first, theory after"?
   ```

   Don't interrogate them up front, don't block on the answer, and don't ask twice. You propose,
   they accept — see `AGENTS.md`.

2. **Calibrate against what they already know.** Grep `03_Resources/` for the topic and its
   neighbours before you explain anything. Two payoffs, both worth the search:
   - You don't explain something they wrote a note about last month. Being taught what you already
     know is how someone learns to stop asking.
   - You can anchor the new thing to a thing they already understand, which is the single most
     effective teaching move available to you.

   **Say what you anchored to, with the link.** "Same shape as
   [[Retries need a budget, not just a count]] — the budget is the token bucket" is worth more than
   three paragraphs of definition, because it lands on something already load-bearing in their head.

3. **Pitch to their stated level, not to a general audience.** If they've said they're an expert in
   one area and a beginner in another, believe them and skip the throat-clearing. Their `Current
   focus` in `[[About me]]` is a live signal about which examples will land.

4. **Prefer one worked concrete example over three paragraphs of definition.** Real numbers, real
   names, a case that runs end to end. Then the generalisation, in a line.

5. **Size it to the question.** "What's a bloom filter" gets a short answer and one example — not a
   syllabus. "Teach me distributed systems" gets a **first lesson** and an offer to continue, not
   an essay: nobody learns a subject from one wall of text, and producing one is the tell that you
   optimised for looking thorough.

6. **Cite factual claims, and mark recency the way the vault does** — `(as of 2026-08,
   example.com)`. Note that this is a skill, so you have no network: you're citing from memory and
   can't check. Name the source anyway and say you couldn't verify it, so they know what to look up.

   **Where something is contested, say it's contested and give both sides.** Presenting a live
   argument as settled is the same failure as inventing a fact, one step removed.

7. **Never invent.** If you don't know, say so and stop. The anti-slop rule in `AGENTS.md` binds
   harder here than anywhere else in this vault: a confident wrong explanation is worse than no
   explanation, because they'll build on it and won't find out for months.

8. **Ephemeral by default.** The explanation lives in the conversation and is written nowhere. If
   they want it kept, that's `capture` — a note in *their* words that they'd recognise as their own
   thinking, not a transcript of your lecture. The reason, said once and not repeated: a vault full
   of AI-written explainers is a vault whose every search result is an AI-written explainer, and
   then the brain is quoting you back at them instead of them.

9. **Offer the capture, don't perform it.** One line at the end, and only when something genuinely
   worth keeping came out of it — usually their reaction, the reframing that finally clicked, or the
   decision it unblocked. Not the explanation itself.

**Output surface:** plain text in the conversation, and nothing else — this command doesn't write.
Never an artifact or rendered document, however well a diagram would render. See `AGENTS.md`.

The win is that they understood it, not that you covered it.
