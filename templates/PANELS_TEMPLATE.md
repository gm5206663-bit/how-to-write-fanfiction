# PANELS.md — panel grammar and the ledger of every line ever printed

**Template · guide v3.0 · law revision v5.4.** Copy to `foundation/PANELS.md`. Replace the *example* rows (reference serial: the Grey Wolf).

**The law behind this file:** the panel is the story's relationship with its own numbers. Two rules run it — **the exact-figures section of the status panel is the single cultivation authority** (a number not there does not exist), and **F22: a full panel prints in a chapter only on update or gain** — ordinary chapters may print **0 panel lines**, deliberately. This file records **every line the panel has ever printed**, so that zero is a measured zero, not a forgotten one.

---

## §1 — The grammar

- **Authority:** every printed line must trace to `STATUS_PANEL.md` §2 (Exact figures). If the panel file and a chapter disagree, the build fails the same turn.
- **F22 — when panels print:** on update or gain only — a level, a ring, a bloodline beat. *Example: Ch6 — The Hem Road printed 0 panel lines — daily life, no fights yet — and the ledger still says IN SYNC.*
- **The drift guard:** a frozen meter — a number that stopped moving while its feeders grow — **fails the build.** The guard is why F22 is safe: chapters may go quiet precisely because this ledger is machine-checked.
- **The prose the panels live in:** clean and clear — avg 14–18, band 2,400–3,400, over-60 = 0, the-way = 0, bare = 0, no repetitive skill lists in the body. The rejected style for contrast: avg 6.8, median 5, the same phrases repeated per sentence — *never that.*

## §2 — The ledger — every line ever printed

| # | Source file | Section | Text | Chapter | Status |
|---|---|---|---|---|---|
| 1 | STATUS_PANEL.md | §2 | Level: 30 — Great Soul Master | — | IN SYNC |
| 2 | STATUS_PANEL.md | §2 | Rings: 1,350y / 1,850y, true purple, shown yellow (Ring Veil) | — | IN SYNC |
| 3 | STATUS_PANEL.md | §2 | Body: ~500 kg robust | — | IN SYNC |
| 4 | STATUS_PANEL.md | §2 | Spirit Sea: 850 — effective talent ~3.5× — perception 10–100 m | — | IN SYNC |
| 5 | SKILLS_CANON.md | §2 | Ghost Wolf facts — identifier, paradox, behavior | — | IN SYNC |
| 6 | SKILLS_CANON.md | §4 | Storm Frost Ghost Wolf line — breakthrough evolution | — | IN SYNC |
| 7 | SKILLS_CANON.md | §4 | Ring Veil — concealment state | — | IN SYNC |
| 8 | chapters/Chapter_01_*.md | footer | Level {{n}} — full panel on update only | Ch1 | IN SYNC |
| 9 | chapters/Chapter_02_*.md | footer | Level {{n}} — Walking Low → Silent Wind Step Mid | Ch2 | IN SYNC |
| 10 | chapters/Chapter_03_*.md | footer | Level {{n}} | Ch3 | IN SYNC |
| … | … | … | … | … | … |
| 80 | chapters/Chapter_06_*.md | — | **0 panel lines** — no update/gain — F22 | Ch6 | IN SYNC |

**Total: {{N}} rows — all IN SYNC** — the count is printed on every run; a row that leaves sync is a build stop, not a warning.

## §3 — Using this file

1. **After every chapter**, add its rows (or its measured zero) the same turn — never "later" (Ship Law).
2. **Before shipping**, the drift guard re-checks every row against the panel's exact figures.
3. **When a number changes**, the panel §2 changes first, then the chapters that print it, then this ledger — one turn, three files, no drift.

---

*The evolution chain note that belongs beside every number: every technique has a grade and 1–100%; at 100% it evolves the same second — every grade a different name; footwork fuses to one line. Full law: [`docs/01_the_laws.md`](../docs/01_the_laws.md) (F7 · F14 · F22 · F26).*
