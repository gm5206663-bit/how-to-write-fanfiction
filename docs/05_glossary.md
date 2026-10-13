# 05 · Glossary — the working vocabulary

**Guide v3.0 · Law revision v5.4 · updated 2026-10-13.** Terms are grouped by where you meet them. Laws are numbered in [`01`](01_the_laws.md); tools in [`06`](06_automation.md).

---

## Craft and prose

- **Band** — the chapter's word window: **2,400–3,400 words**. In band is a pass; outside is a stop.
- **Avg (14–18)** — average sentence length, in words, measured across the chapter. The clean-and-clear target.
- **Over 60** — a sentence longer than 60 words. Count must be **0**.
- **The-way** — a construction family banned outright from prose (a mechanical tic, policed by the banned-token sweep). Count must be **0**.
- **Bare** — bare fragments (verbless stubs used as sentences) as a style crutch. Count must be **0**.
- **Clean and clear** — the prose law: natural prose, no nonsense repetition, no repetitive skill lists in the body, mastery shown by daily-life action, lore kept to the footer or the status file.
- **Panel line** — a line printed from the character's status panel inside prose. **F22** governs when panels may print in full: only on update or gain; **0 panel lines is legal and deliberate** for ordinary chapters.
- **Footer / apparatus** — the mechanical line(s) at a chapter's end (state stamps, receipts). Apparatus lives in the chapter *file* only where the law allows, and never leaks end-state into early chapters.
- **Ore** — raw canon material fetched from primary text before drafting. Secondary sources are ore, never law.
- **Butterfly** — a change the story causes in the world, *felt, not footnoted*. Every butterfly is born with its **open obligation** in the butterfly ledger; logged only where the tracks make contact on the page (dual-track) or where the change is shown (single-track).
- **Priced experience** — a world rule delivered through a character who pays for the knowledge, rather than stated by the narrator (craft law 3).

## State and truth

- **Status panel** — the serial's **single source of truth**: identity card, live edge, ranks, locks, bans, relationships, exact figures, next beat. *If a number isn't in it, the number doesn't exist yet.* Rebuilt from chapters freely; **never rebuilt from memory**.
- **Exact figures** — the panel section that is the *single cultivation authority* for every number: levels, meters, ring years, talent stacking.
- **Meter** — a growth quantity with **its own pace law** (pages, thrusts, meals, sparring…). Meters are infusion-fed — they advance because life happened.
- **Locks** — decisions fixed by the author (F0–F26 in the Grey Wolf) — "not up for renegotiation by a later draft".
- **Bans** — things that must never appear: the-way, bare, over-60, any valid "MASTERED terminal", resource-buying, shop/quest/points, voice/intelligence theft, memory-write. Enforced by the banned-token sweep.
- **Drift guard** — the check that fails the build when a meter freezes or a printed number goes stale against the authority file.
- **Authority order** — when two files disagree, the ranked list that decides: the author's words first, then the project's locked documents, then the kit laws, then receipts.
- **Handoff file** — the cold-start brief: what is true *now*, the authority order, and which file wins on conflict.

## Gates and checks

- **Gate** — an automated check that can fail the run. Laws need gates; a law without a gate is a wish.
- **Battery** — one command that runs every layer (`checks/run_all.sh` or `tools/run_all.py`). **Must exit 0.**
- **Selftest** — a gate's own proof: injected defects must be caught and named. A gate that never failed is untested.
- **Coverage line** — the "N of M checks ran" statement. **A coverage line is a claim — it gets checked like one.** A check that silently skips is a check that lies.
- **Fail loud** — the design rule: a missing precondition is a FAIL, never a skip.
- **Sentinel** — the shelf's independent health scan: 26 checks (2026-10-13: 26 of 26 ran, 26 pass) including the coverage line itself.
- **Drift scan (independent)** — a scan that re-verifies a project *without trusting the project's own checker* (StoryOS ships one; sha256 on every file).
- **Zero-digit / zero-CJK** — MCU gate rules: numbers written out in prose; no CJK glyphs in an English text.
- **ACCEPTED_HASH** — a stored acceptance of a chapter text. When accepted text changes, the hash *must* fail — the failure is true, and the fix is a new acceptance, never a rewritten hash.

## Canon and receipts

- **Receipts** — the fetched, quoted, dated canon evidence for a claim. Receipts are read-only: never edited, never silently corrected; conflicting readings are kept side by side with the variance logged.
- **Canon spine** — the ordered list of source chapters a serial consumes, with a per-beat confidence tag.
- **Knowledge firewall** — the file stating **what the OC knows, and when** — the map that prevents accidental omniscience.
- **T-registry** — the MCU (film-order) registry of every canon touch: which beat, which panel, which change.
- **False FAIL** — a gate failing for the wrong reason (e.g. a hard-coded assumption). Worth ten false PASSes: it teaches the check was never general.

## Structure and patterns

- **Dual-track (canon-parallel)** — canon on the page, complete and unskipped; the OC parallel on the same clock and streets; butterflies only where the tracks touch on the page.
- **Film order** — for film/TV: canon consumed and retold in the work's own release order, staged scene-by-scene.
- **Camera law (P12)** — *the camera goes where canon goes*: canon scenes shown from canon's own angles; the OC's line parallel, never a substitute.
- **Plural panels** — several canon-side panels in one chapter: what each canon perspective sees.
- **Foundation docset** — the ~20 files a serial holds before chapter one: the source of truth chapters are written *out of*.
- **Open ruling** — a numbered decision only the author can make. Any open ruling **locks drafting**.
- **Stage 0 (foundation stage)** — rulings first, prose second; zero chapters until ruled is a *success state*.
- **One copy of one thing** — the account law (from the two-copies disaster): a text exists in exactly one authoritative place; a document kept in two places will be wrong in one of them.
- **Park** — a deliberate, documented hold on a serial (receipts intact, files archived under the park), not a failure.

## Publishing

- **Reading shelf (Soul Library)** — the public collection: one static page, no frameworks, no tracking, full-text search, 18 serials · 312 chapters · 1,351,161 words (2026-10-13).
- **Control Centre** — the account console: state lives in `state/`; the site and a plain-text bootstrap are **generated** — change the state, not the site.
- **StoryOS** — the reader + agent console: every file with its sha256, an independent drift scan, standard library only.
- **Ship Law** — shipping is a printed checklist: mechanical 80% (measure → gate → sync → commit → push → stamp), authored 20% (the chapter's own final read), exit 0 on every automated step.
- **Status generation** — the one command that rebuilds the serial's inventory file from the tree; never hand-edited; an unregistered file surfaces itself with a marker.
- **Live edge** — the current frontier of a serial (chapter shipped / chapter next), stamped in the README and the panel in the same turn as the ship.

---

## The version axes (short form)

- **Guide edition** — the shape of *this repository* (docs, templates, examples). Current: **v3.0**, 2026-10-13.
- **Law revision** — the F-series itself. Current: **v5.4** (the footwork-fusion revision). The full history — including the retired v2.1 tag chain — is in [`../VERSION_OF_RECORD.md`](../VERSION_OF_RECORD.md).

---

*Rebuilt 2026-10-13 from the compressed originals; every term and receipt preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
