# 10 · Publishing — StoryOS, Control Centre, and the Soul Library

**Guide v3.0 · Law revision v5.4 · updated 2026-10-13.** A gated serial deserves a public face. The workshop runs three publishing systems, each with one job: **the shelf** shows readers the prose; **the Control Centre** shows collaborators the account's state; **StoryOS** shows agents and auditors everything, signed.

---

## The Soul Library — the reader's shelf

**One static page. No frameworks, no CDN, no tracking.** The library publishes the serials as a readable site: covers, full-text search, reading progress saved in the reader's own browser (`localStorage`) — nothing phoned home.

- **Built from the chapters, measured, not typed.** The shelf's own tools re-measure every word and sentence from the files: analytics, continuity recaps ("The Story So Far"), a cross-chapter continuity lint, and a **sentinel** — the independent health scan that runs **26 checks** including its own coverage line (2026-10-13: **26 of 26 ran, 26 pass**).
- **Synced by a tool with a spine.** The shelf's sync script copies from each source repo, re-measures everything, rebuilds every machine surface (index, search index, sitemap, recaps, analytics), and **refuses to finish unless a fresh byte comparison finds zero differences.** Every file on the shelf is byte-identical to its source — that is a checked claim, not a hope.
- **Current state:** **18 serials · 312 chapters · 1,351,161 words**, live at [gm5206663-bit.github.io/soul-library](https://gm5206663-bit.github.io/soul-library/).

## The Control Centre — the account's console

**You do not edit the site. You change the state.** The Control Centre holds the account's machine-readable state (`state/` — workspace, projects registry, laws, firewalls, log) and *generates* everything a visitor or collaborator reads: the site (`index.html` — GENERATED, never hand-edited) and a **plain-text transfer bootstrap** (`TRANSFER_BOOTSTRAP.txt` — also GENERATED) that carries the same state with no access to the repository at all.

- **One command rebuilds it:** selftest → measure → bootstrap → build.
- **Why a bootstrap:** hand a fresh agent the text file and it reaches correct state in one read — the same promise the serial handoff files make, at account scale.
- **Receipts in the state:** counts in the Control Centre are **measured, never typed** — the same rule as the register and the shelf.

## StoryOS — the console that signs everything

The reader + agent console: browsers for the projects, the live gate, character locks, knowledge firewalls, and an audit trail — with one distinguishing discipline: **every file carries its sha256**, and a separate **drift scanner re-verifies the workspace without trusting the project's own checker.** Standard library only; no build step at runtime.

- **The parts:** a scanner that builds `data/` from the projects (hashes included), the independent drift scan, a small server (static app + JSON API + proposal inbox + key-gated writes + audit log), and a single self-contained UI file (no external assets).
- **Why it matters to this guide:** it is the purest expression of the workshop's oldest rule — *never trust only the project's own checker.* A gate inside the project can be consistently wrong; a signed, independent scan cannot stay wrong quietly.

## How the three fit together

```
 chapters/ ──► serial state files (panel, meters, inventory — generated)
     │                       │
     │                       ▼
     │            Control Centre state/ ──► site + transfer bootstrap (generated)
     │
     └──► Soul Library build ──► one index.html reading site (+ sentinel 26 checks)
                     │
              StoryOS: sha256 everything, drift-scan independently, serve + console
```

- **Status generation** (`status_gen.py`) rebuilds a serial's inventory from its tree — never hand-edited; an unregistered file surfaces itself with a marker instead of hiding.
- **The ship checklist** (`ship_chapter.py`) runs the mechanical pipeline and refuses to say "shipped" until every automated step verifies — that is where publishing *begins*, not where it ends.

## What publishing is *for* in this method

Not vanity and not backup. Publishing is **the forcing function for honesty**: a public shelf that re-measures byte-for-byte, a console that states its counts, and a scanner that signs every file make silent drift impossible to hide. The workshop's rule from the audits applies here at full strength — **a coverage line is a claim; it gets checked like one** — and a public site is a coverage line the whole world can check.

---

*Rebuilt 2026-10-13 from the compressed originals; every system, tool, and receipt preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
