# Claude Cowork adapter

The vault's commands, packaged as a Cowork plugin so you can use your second brain from Claude
Desktop without opening a terminal.

**This directory is inert unless you install it.** Claude Code, Codex, Cursor, Gemini and everything
else ignore it completely — a marketplace has to be added by hand before anything here loads.
Delete the whole folder and the vault still works.

---

## Install

**If your vault is on GitHub** (or GitLab/Bitbucket, public):

1. Cowork → **Customize → Plugins → Add marketplace**
2. Enter your vault's repo — `owner/repo` or the full `https://github.com/owner/repo` URL
3. Install **Second Brain** from the plugins that appear
4. Create a Cowork project and attach your vault folder to it

**If your vault is local only** (no remote), there's nothing for Cowork to fetch from, so upload the
plugin instead. Zip this directory and select it with the upload option on the Plugins page:

```sh
cd brain/cowork && zip -r ~/second-brain-plugin.zip .claude-plugin commands skills README.md
```

You'll need to re-zip and re-upload after changing anything in here — the marketplace route updates
itself, this one doesn't. If the upload rejects that layout, try zipping the `cowork` directory
itself so the archive contains one top-level folder.

> [!NOTE]
> **Partly unverified.** Anthropic documents sharing a plugin "as a compressed file" but doesn't
> specify the expected archive layout, and the marketplace route is the one that's actually been
> tested here. If you have somewhere to push the repo — a private GitHub repo is free — prefer it.

Then start a **new** session inside that project and type `/` — you should see the commands listed.
Run `/second-brain:setup` first. The bare `/setup` also works unless something else claims the name.

**Attaching the folder is not installing the plugin.** Nothing in this directory loads until you
install it under Customize → Plugins; a vault folder on its own does nothing here. That's deliberate
— it's what keeps this adapter inert for everyone not using Cowork — but it does mean "I attached
the vault and the commands aren't there" is expected, not a bug. If they still don't appear right
after installing, start a fresh session; Claude Code needs an explicit reload after an install and
Cowork's equivalent isn't documented.

## The commands

`/second-brain:setup` · `capture` · `ask` · `digest` · `maintain` · `ingest-sessions`

Same six as everywhere else, namespaced by the plugin. They're thin wrappers — each one reads
`brain/prompts/<name>.md` from your attached vault folder, so editing a prompt in the vault changes
behaviour here too, with no reinstall. **You don't have to use them:** talking to Claude about
something you want remembered counts as a capture.

## Recommended: paste this into the project's Instructions

Cowork does not read `AGENTS.md` from an attached folder. The bundled skill tells Claude to go read
it, but a skill loads *when it looks relevant*, not on every session. Instructions is the only
always-on channel Cowork offers, so paste this in:

> The attached folder is a second-brain vault. Read `AGENTS.md` at its root at the start of every
> session and follow it — it is the operating manual. If I talk about something without naming a
> command, treat it as a capture. Never produce HTML artifacts, PDFs or canvas documents; notes go
> in the vault as markdown and answers go in the conversation as text. Run `brain/bin/sync` before
> you finish, and tell me if you can't.

Worth knowing what you're accepting: those Instructions live in Cowork's own project metadata on
your machine, not in your repo. They aren't versioned, they aren't shared with anyone, and
**archiving the project deletes them** (your folder and files are untouched). That's precisely the
vendor-metadata problem this repo argues against in `DESIGN.md` — it's the least-bad option Cowork
currently offers, not a good one.

## Two things that are worse here than elsewhere

**Nothing commits itself.** Claude Code commits after every turn via a `Stop` hook in
`.claude/settings.json`. Cowork doesn't read that file, and the plugin ships no hook — so the vault
only gets committed when Claude runs `brain/bin/sync`, which the skill tells it to do at the end of
a session. If it can't, it's told to say so rather than pretend. **Check `git log` occasionally
until you trust it.**

> [!NOTE]
> **Unverified.** Whether a Cowork plugin *hook* can run `brain/bin/sync` against your local folder
> is not answerable from Anthropic's docs — Cowork is described both as working directly on your
> computer and as running in an isolated VM that writes to your filesystem, and those imply
> different things for shell access. No hook ships here until someone confirms it on a real
> instance. If it works, this section gets shorter.

**`ingest-sessions` may not work at all.** It shells out to `brain/bin/sessions` to reach
`~/.claude/projects` and `~/.codex/sessions`, which live outside the attached folder. If Cowork's
sandbox can't see them, the command will say so. Run that one from Claude Code.

## If you're choosing a surface

Cowork is the nicest way to use this without a terminal, and the weakest technically. **Claude
Code's desktop app is also GUI-only, reads `AGENTS.md` natively, and has none of the caveats
above** — if you want the full system without a terminal, start there.
