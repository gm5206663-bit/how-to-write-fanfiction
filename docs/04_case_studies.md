# 04 · Case Studies — real numbers, real lessons

Every law in this guide was paid for. These are the receipts.

---

## The Adaptive Prodigy — Soul Land 3 (OC Lin Hao)

**116 chapters · ~354,700 words · the serial that built the system.**

- Started as a free-written fic with a character bible written as eternal truth.
- The bible went stale around chapter 30 → the **Unfixed Law** (dated states, baselines not ceilings).
- Mid-run continuity cracks forced a **full-spectrum repair pass** — every chapter re-audited against canon. It passed green, and the repair *itself* became the template for the rebuild protocol in the workflow doc.
- Its mirror-copy of the codex was retired under the **TWO-COPIES LAW** — with a staleness layer that now *fails if a second copy reappears*.

**Lesson:** a 350K-word serial is a state machine. Respect the state or rebuild the machine.

## Blue Silver — pre-canon (*Home*, a Blue Silver Emperor grass)

**15 chapters · 34,711 words · Book One complete · all seven gates passing.**

- The proof that "small" and "gated" coexist: a quiet pre-canon story about a grass named Home, rebuilt chapter set and all, ending with every gate green.
- The **seven-gate** structure (canon, panel, ledger, firewall, prose, continuity, selftest) matured here.

**Lesson:** gates are not for epics only. The smaller the story, the more embarrassing a continuity bug.

## Fire Phoenix — Soul Land 4 (OC Yan Shuo)

**52 chapters · the serial that taught duplication and pacing.**

- **The five-copies disaster:** at one point this project existed in *five* places. Two copies were frozen at Chapter 31 while the live edge was Chapter 52 — and one stale file inside them presented banned values (`Dawnflame 1,120`, `Dawn-Iron 2,040`) as current. The fix took a full day, a dated archive with `git mv` receipts (345 renames, all R100, zero deletions), and `README_STALE_ARCHIVED.md` markers in every archived copy.
- **The pacing law:** early chapters mapped one canon chapter to one fic chapter — the fic became a slow-motion replay. The fix is now Law 8: compress routine beats, expand only what the butterfly changes.

**Lesson:** copies don't stay identical. And canon-speed is not a virtue.

## Devouring Dragon — Soul Land (reincarnator, Holy Spirit Cult)

**21 chapters · the plain-language serial.**

- Session ruling **s40 (PLAIN LANGUAGE LAW)**: early chapters buried simple events under heavy prose. The re-carve to plain words made every later chapter faster to write *and* to gate.

**Lesson:** ornament is a tax you pay twice — once writing it, once auditing it.

## The Golden Lion — Soul Land 2 (OC Jin Yang, Golden Lion martial soul)

**Foundation → Chapter 3 in one day, every step gated.**

- Founded with the full docset: authors' law (L-01…), canon ledger (001…), status panel, the Lion Module (protagonist bible), two pointer ores, and its own gate `sl2-goldenv1`.
- **The author-strike pattern in action:** Chapter 1 was written, and the author rejected the entire opening venue as canon-illogical ("if she wants she choose in starting; who gives her first ring?"). Chapter 1 was **rebuilt** same-day on a canon-logical footing; every ledger re-synced. A later strike produced the CANON-FIRST default: follow canon, ask never.
- **Possession carding:** the author flagged a missed power-state reveal; the panel versioned (v4 → v5) with the base-form card, stack order, and ring-orbit exposure — the fix went into the panel *and* the gate.

**Lesson:** the system's job is to make author overrides cheap. Rulings logged same-turn, rebuilds gated same-day.

## Dragon Prince Yuan — native-OC (Zhou Xu)

**The gate that cried FAIL — and was right to.**

- The scanner reported FAIL. The project looked fine. The truth: **the scanner was right for the wrong reasons** — it hard-coded 11 SL4-specific firewall filenames, so a project declaring firewalls in a differently-named file read as "zero firewalls" (scanner bug, made generic after), *and* the project genuinely lacked a machine-readable live-edge manifest (authored after). Two stale "do not write Chapter 1 yet" headers were also found sitting above their own contradicted later sections.

**Lesson:** when a gate fails and you're sure the work is fine — investigate the gate too. Then fix both. A false FAIL you investigate is worth ten false PASSes you never see.

## Seed of Creation · The Second Heartbeat · Holy Spirit — foundation-stage serials

- *Seed of Creation* (SL2.5 era): scaffolded, four rulings pending, **zero chapters until ruled**. 
- *The Second Heartbeat* (SL5): Tang San's twin brother — foundation with a butterfly registry and ripple rules before a word of prose.
- *Holy Spirit* (SL2): 4 chapters, governed by the NO-MISTAKE KIT.

**Lesson:** foundation-stage is a *stage*, not a failure to start. Rulings first, prose second — always.

---

## The scoreboard

| Serial | Chapters | Words/state | One-line legacy |
|---|---|---|---|
| The Adaptive Prodigy | 116 | ~354,700 | built the system |
| Fire Phoenix | 52 | live (private) | two-copies + pacing laws |
| The Unraveled Tide | 24 | active | multi-panel law |
| Devouring Dragon | 18 | live | plain-language law |
| Blue Silver | 15 | Book One complete | seven-gate maturity |
| The Golden Lion | 3+ | hottest serial | one-day gated launch |
| Holy Spirit | 4 | live | no-mistake kit |
| Dragon Prince Yuan | 1+ | live | the gate that cried FAIL |
| The Second Heartbeat | 0 | foundation | rulings-before-prose |
| Seed of Creation | 0 | foundation | same |
| SL1 Gu Yuan · new-SL3 branch | — | archived / frozen | provenance kept |

**Combined: 400,000+ words, every shipped chapter gate-checked.** The method scales down (a 4-chapter serial) and up (a 116-chapter monster) with the same loop.
