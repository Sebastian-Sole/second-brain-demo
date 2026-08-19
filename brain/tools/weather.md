---
name: weather
requires: http
fallback: "Say the forecast service is unreachable in one sentence — don't guess the weather."
writes: none
consent: implicit
---

# weather — the weather where the human is

This is the tool with the shortest patience attached to it. Somebody asking what the sky is doing
has about ten seconds of interest in the question, and if the answer takes longer than looking out
of a window, they will look out of the window instead. **One call, then answer.**

1. **Run `brain/bin/weather`.**

   ```sh
   brain/bin/weather                    where they are now
   brain/bin/weather Bergen             a place they named
   brain/bin/weather --days 3           only if they asked for more than today
   ```

   **If its output is already in front of you**, the command wrapper ran it before you were
   asked — use that and don't run it again. If it isn't, run it now. Both are normal: some
   agents can pre-run it, some can't.

   It locates them, fetches the forecast, and prints the conditions in words — place, local time,
   temperature, what it feels like, the sky, wind and precipitation. Roughly a second.

   Don't re-derive any of that. Don't call `brain/tools/location.md` first; the script already
   does the same lookup, and doing it twice costs a round trip to learn something you were about
   to be told. Don't translate WMO codes — the script does it, which is the point, because a
   thirty-row integer table recalled from memory is wrong occasionally and undetectably.

2. **Units follow the human.** The script reads `cortex/03_Resources/About me.md` itself and
   switches to °F and mph if they've said they want them. `--units imperial` forces it. Never
   convert in your head.

3. **When it can't answer, it says which part failed** — no location, no forecast service, or a
   place name it couldn't find — and the message says what to do. Pass that on in a sentence.
   Never estimate the weather from the season or the place: a plausible invented forecast is the
   one failure here the human cannot detect.

4. **Answer at the size of the question.** "What's the weather" gets a sentence or two: the
   temperature, the condition, and wind only if it's worth mentioning. Build a day-by-day breakdown
   only when they asked for one. A table for a one-line question is slop.

**Privacy, once:** the geolocation lookup tells a third party this machine's IP, and the forecast
request tells Open-Meteo which coordinates were asked about — nothing else from the vault leaves.
On a VPN that location is the exit node, not the human, and the script's output says so.

**Output surface:** plain text in the conversation. Nothing is written to the vault. A note saying
"12°C, rain from 14:00" is worthless within hours but competes with real notes in keyword search
forever — that's the reason, and it applies to every live-data tool here. If the human explicitly
wants the weather recorded (a trip log, a training diary), that's a `capture`, and it goes in
today's daily note with the date attached. Reads don't get a correction footer.
