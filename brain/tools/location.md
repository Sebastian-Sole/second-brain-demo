---
name: location
requires: http
fallback: "Say you can't reach the network, so you don't know where they are — and ask, if the answer needs it."
writes: none
consent: implicit
---

# location — where the human is right now

Answer "where am I". Other tools call this one for coordinates rather than rolling their own.

1. **Look it up.**

   ```sh
   curl -s https://ipinfo.io/json
   ```

   No key, no `User-Agent`, no flags beyond `-s`. You get JSON with `city`, `region`, `country`,
   `loc` (`"lat,lon"`) and `timezone`. Read it yourself — no `jq`, no python. Parsing two fields
   out of a small JSON blob is something you can already do, and every dependency you add is one
   the next person's machine won't have.

2. **If that fails or comes back rate-limited**, use:

   ```sh
   curl -s 'http://ip-api.com/json/?fields=status,country,city,lat,lon'
   ```

   Check `status` is `success`. Same deal: no key, no header.

3. **Answer, and say where it came from.** One or two sentences: the place, and that it's from the
   IP address. Don't bury that — it's what makes the next line honest.

   **On a VPN this reports the exit node, not the human.** IP geolocation is approximate even
   without one: the two services above can disagree by a suburb because they're resolving an ISP's
   allocation, not a person. Give the city, not a false-precision coordinate, unless coordinates
   are what was asked for.

4. **If they say it's wrong, they're right.** Don't re-check, don't argue with the API, don't ask
   them to turn the VPN off. Use what they told you for the rest of the session.

5. **Nothing is stored.** There's no saved home location in this vault and there shouldn't be —
   a stale "lives in X" note is worse than a lookup that takes a second, and the human moves
   more often than a note gets revisited.

6. **Don't infer.** Where they are right now is not where they live, work, or are from. It doesn't
   go into `cortex/03_Resources/About me.md`, it doesn't go into a note, and it isn't evidence for a claim
   about them. If they want their home city in their profile, they'll say so — that's `start`,
   not this.

**Privacy, once:** an IP-geolocation lookup tells a third-party service what the human's IP address
is. Worth knowing, not worth a paragraph.

**If the network is unreachable**, say so in a sentence and move on. "I can't reach the network, so
I can't tell where you are" is a fine answer. Don't dump a curl error at them and don't retry in a
loop.

**Output surface:** plain text in the conversation. This tool writes nothing to the vault — live
data is ephemeral, and it stays that way unless the human explicitly asks for a note. Reads don't
get a correction footer.
