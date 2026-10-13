# CANON_LEDGER.md — receipts, butterflies, and the checks that keep canon true

**Template · guide v3.0 · law revision v5.4.** Copy to `foundation/CANON_LEDGER.md`. Replace the *example* rows (references: Stark Heir and MCU Eternal for the MCU shapes; Lan Shen for date arithmetic; Devouring Dragon for the canon-voice rollout).

**The law behind this file:** nothing enters a chapter unverified (F3). Every canon beat the story consumes is **fetched, quoted, and filed** — receipts, not memory. This file is where the receipts, the butterflies, and the date arithmetic live.

---

## §1 — The canon spine (receipted)

| # | Canon chapter / film beat | Date / time in source | Receipt (source + location) | Confidence | Our chapter | Notes |
|---|---|---|---|---|---|---|
| 1 | {{e.g. canon ch1 / film beat 1}} | {{date}} | {{quote + where it was fetched}} | {{High / Mid / Low}} | Ch{{n}} | {{anything the chapter must honor}} |
| 2 | {{e.g. canon ch2 / film beat 2}} | {{date}} | {{receipt}} | {{High}} | Ch{{n}} | {{e.g. a named artifact introduced, with its origin-stage queued}} |
| 3 | {{…}} | | | | | |

**Receipt discipline:** receipts are read-only — never edited, never silently corrected. If two readings of a passage exist, **both are kept and the variance is logged.** Secondary sources (wikis, summaries) are **ore, never law.**

## §2 — The butterfly registry (T-registry)

Every touch of canon by the story is registered the moment it lands — nothing touches canon unlogged.

| T-# | Our chapter | Canon beat touched | What changed | Why it is logged | Status |
|---|---|---|---|---|---|
| T-14 | Ch4 | {{film beat / canon chapter}} | {{what the OC did}} | {{the tracks made contact on the page}} | DELIVERED |
| T-15 | Ch5 | {{beat}} | {{what changes downstream}} | {{contact}} | OPEN — obligation tracked |
| {{T-…}} | | | | | |

**The ripple law:** a butterfly is logged only where the tracks make contact **on the page** (dual-track) — and once logged, it carries an **open obligation**: every registered change must be shown landing, or the registry says why not.

## §3 — Date arithmetic — the highest-yield check

Every "N days ago / N days later" in a chapter is **recomputed by hand** against the day map in `TIMELINE.md`:

| Our chapter | Phrase in prose | Computed against the day map | Result |
|---|---|---|---|
| Ch9 *(example)* | "three months ago" | day map: Ch6 = Day 45, Ch9 = Day 135 → 90 days = 3 months | **PASS** |
| {{…}} | | | |

**Receipt:** this single check caught **nine month-count errors in one chapter alone** and four stale year counts in another (Lan Shen) — it costs a minute and pays more than any other manual check. Never ship a chapter with a relative-time phrase unverified.

## §4 — The canon-voice rollout (three lenses)

When canon material is retold, it is checked through three adaptation lenses (Devouring Dragon's s53/s54/s56):

- **Novel lens (s53):** every fact in the source's own order; causes held exactly; panels held verbatim except retired-word easings, each recorded in the chapter footer; gates green (floors retired, zero tics in cap, no sentence over 60).
- **Manhua lens (s54):** the panel-by-panel reading — what a comic adaptation would show.
- **Donghua lens (s56):** the structural reading — what an animated episode would keep, cut, and reorder.
- **Receipts:** every finding from the three lenses preserved with sources and quotes; each became a named law in the serial's `RAILS.md`.

## §5 — Forbidden future (the denylist)

The present-tense fence: nothing may appear in prose before its time in the source. Write the denylist here and add to it with every chapter.

- *Example — Stark Heir (M2):* `Chitauri · Ultron · Extremis · Vibranium · Sokovia · Blip · Thanos · Avengers · Infinity` — absent from prose.
- *Example — MCU Eternal (M2):* `Uni-Mind · Tiamut · Emergence · Blip · Thanos · Kro` — absent from prose.
- **Your denylist:** {{…}}

## §6 — The machine laws (film/TV serials)

The checks the gate runs on MCU-style texts — keep their receipts here:

- **G1 — CJK:** scanned per line; zero hits in an English text. *(example receipt: 22 files scanned, 0 hits)*
- **G2 — backslash-n:** a literal `\n` surviving into any value is rejected.
- **G3 — digits in prose:** zero digits outside fences (numbers are written out).
- **G4 — dialogue floor:** every chapter at or above the floor *(example: Ch1 96 lines · Ch2 83 · Ch3 67 · Ch4 72)*.
- **G5 — anchor order:** single-anchor order only; span contiguity needs start–end panels.
- **G6 — placeholders:** zero in shipped files (foundation TBDs are out of scope by name).
- **G7 — marker discipline:** markers only inside fences; at most one card, and last.
- **M1 — manifest edge:** the manifest edge matches the file count. **M2 — forbidden future:** the denylist is absent.

---

*The receipts law in one line: **nothing enters a chapter unverified; a claim without its receipt is a wish.** Full law texts: [`docs/01_the_laws.md`](../docs/01_the_laws.md) (F3 · F19 · P12 and the receipt family).*
