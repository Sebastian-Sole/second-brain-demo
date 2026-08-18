---
name: weather
requires: http
fallback: "Say the forecast service is unreachable in one sentence — don't guess the weather."
writes: none
consent: implicit
---

# weather — the weather where the human is

1. **Get coordinates from `brain/tools/location.md`.** Follow that file; don't reimplement it. If
   the human named a place, use that place instead and skip the lookup entirely.

2. **Fetch the current conditions.**

   ```sh
   curl -s 'https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&current=temperature_2m,weather_code,wind_speed_10m&timezone=auto'
   ```

   Substitute the real latitude and longitude. No API key and no `User-Agent` — that's why this is
   Open-Meteo and not MET.no, which 403s without an identifying `User-Agent` and would make every
   user of this vault configure one before they could ask what the weather is.

   `timezone=auto` makes the returned times local to the coordinates. Read the JSON yourself —
   POSIX `curl` and your own eyes, nothing else.

3. **Only if they asked for more than one day**, add:

   ```
   &daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code&forecast_days=3
   ```

4. **Translate `weather_code`.** It comes back as a bare integer. Use this table — don't recall it:

   | Code | Meaning |
   | --- | --- |
   | 0 | Clear sky |
   | 1 | Mainly clear |
   | 2 | Partly cloudy |
   | 3 | Overcast |
   | 45 | Fog |
   | 48 | Depositing rime fog |
   | 51 | Drizzle, light |
   | 53 | Drizzle, moderate |
   | 55 | Drizzle, dense |
   | 56 | Freezing drizzle, light |
   | 57 | Freezing drizzle, dense |
   | 61 | Rain, slight |
   | 63 | Rain, moderate |
   | 65 | Rain, heavy |
   | 66 | Freezing rain, light |
   | 67 | Freezing rain, heavy |
   | 71 | Snowfall, slight |
   | 73 | Snowfall, moderate |
   | 75 | Snowfall, heavy |
   | 77 | Snow grains |
   | 80 | Rain showers, slight |
   | 81 | Rain showers, moderate |
   | 82 | Rain showers, violent |
   | 85 | Snow showers, slight |
   | 86 | Snow showers, heavy |
   | 95 | Thunderstorm, slight or moderate |
   | 96 | Thunderstorm with slight hail |
   | 99 | Thunderstorm with heavy hail |

   Say it the way a person would — "overcast", "light rain" — not "WMO code 61". Codes 96 and 99
   are only forecast reliably in Central Europe; elsewhere a thunderstorm generally arrives as 95.

5. **Answer at the size of the question.** "What's the weather" gets a sentence or two: the
   temperature, the condition, and wind only if it's worth mentioning. Build a day-by-day breakdown
   only when they asked for one. A table for a one-line question is slop.

6. **Units follow the human.** Open-Meteo returns Celsius, km/h and mm by default, which is right
   for most of the world. If `03_Resources/About me.md` states a preference, honour it — add
   `&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch` rather than
   converting in your head.

**Privacy, once:** the forecast request tells Open-Meteo which coordinates you asked about, plus a
unit preference if step 6 added one — nothing else from the vault leaves.

**If the request fails**, say the forecast service is unreachable and stop. Never estimate the
weather from the season, the location, or yesterday — a plausible invented forecast is the one
failure mode here that the human can't detect.

**Output surface:** plain text in the conversation. Nothing is written to the vault. A note saying
"12°C, rain from 14:00" is worthless within hours but competes with real notes in keyword search
forever — that's the reason, and it applies to every live-data tool here. If the human explicitly
wants the weather recorded (a trip log, a training diary), that's a `capture`, and it goes in
today's daily note with the date attached. Reads don't get a correction footer.
