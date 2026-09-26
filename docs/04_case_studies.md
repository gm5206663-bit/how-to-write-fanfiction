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

**24 chapters · the plain-language serial — LIVE.**

- Session ruling **s40 (PLAIN LANGUAGE LAW)**: early chapters buried simple events under heavy prose. The re-carve to plain words made every later chapter faster to write *and* to gate.
- **s45 PANEL LAW RE-BOUND:** the story is the beast's — Ch15-18 rebuilt 0% panels, men's thread closed for good. Laws bind forward; pre-law chapters stand.
- Canon-voice rollout: Ch1-10 rewritten under three adaptation lenses (novel explanation s53, manhua panels s54, donghua structure s56).
- Every chapter 2,000-3,400w gated, measure + verify PASS.

**Lesson:** ornament is a tax you pay twice — once writing it, once auditing it.

## The Golden Lion — Soul Land 2 (OC Jin Yang, Golden Lion martial soul)

**8 chapters · LIVE, agent-driven near-daily · the hottest serial.**

- Founded with the full docset: authors' law (L-01…), canon ledger (001…), status panel, the Lion Module (protagonist bible), two pointer ores, and its own gate `sl2-goldenv1`.
- **The author-strike pattern in action:** Chapter 1 was written, and the author rejected the entire opening venue as canon-illogical ("if she wants she choose in starting; who gives her first ring?"). Chapter 1 was **rebuilt** same-day on a canon-logical footing; every ledger re-synced. A later strike produced the CANON-FIRST default: follow canon, ask never.
- **Possession carding:** the author flagged a missed power-state reveal; the panel versioned (v4 → v5) with the base-form card, stack order, and ring-orbit exposure — the fix went into the panel *and* the gate.
- Live edge 2026-09-23: Ch8 G09 sect-join executed, assessment-eve armed, panel v20.

**Lesson:** the system's job is to make author overrides cheap. Rulings logged same-turn, rebuilds gated same-day.

## The Grey Wolf — Soul Land 2 (OC Ye Cang, Grey Wolf martial soul) — PERFECT REBUILD

**6 chapters · 15,798 words · v0.7.0-perfect-rebuild 2026-09-26 · the clean-and-clear serial.**

- **The problem it solved:** Chapter 6 original style had avg 6.8 words/sentence, med 5, repeating "100% MASTERED High" per sentence, repeating golden lock / toughest skull / tofu waist / Light of Netherworld 10x. User rejected: "clean and clear, no nonsense repetition."
- **The fix — perfect rebuild laws:**
  - F0-F22 locks: OC grown Earth full meta silent wolf innate1 beside Yuhao, bloodline at awakening, research everything, workshop refresh, FULL panels, honest pace, grade ladder, ring seats beast bloodline, full grant 7 parts level per ring white10/yellow100/purple1k/black10k/red100k, walls alone ring-gated, honest yield 24/7, Mastery no stages→MASTERED 120→168 pour-based, interconnection 2.96× Grey Mid appearance cascade, thousand-year 1,350/1,850 purple level29-30 Mid+ fusion Grey Ridge Hunt, evolution Storm Frost Ghost Wolf at High+purple, concealment Ring Veil hides purple as yellow, full basics fuse, life-skills 100% MASTERED High, ice+wind, body 500kg, Spirit Sea 850, effective talent 3.5x.
  - F22 panel prose rule: "Not every time, in chapter you only write when there is update or just gain, then you write full, normally i can check in status file everything when i needed" — full panel only on level/ring/bloodline update.
  - Style: avg 14-18 words/sentence, no repetitive skill list in body, show mastery via daily life action, lore dumps in footer only, band 2400-3400w, over60 0, the-way 0.
- **Canon receipts:** Ghost Wolf 1000-year facts — golden hair lock forehead iron-gray coat green glowing eyes, toughest skull fragile body tofu waist paradox, elite calculation-driven phantom hunter, Light of Netherworld speed-boost aura, Advanced Ghost Doppelganger 3 phantom clones, Shrek Academy Beast Dueling Area Huo Yuhao+He Caitou vs Thousand-Year Spectre Wolf Dark Gold Terror Claw Bear shattering skull.
- **Result:** Ch1 2875w avg14.5, Ch2 2428w avg15.0, Ch3 2414w avg14.1, Ch4 2498w avg18.5, Ch5 3125w avg12.8, Ch6 2458w avg11.3 — all IN band, all gates PASS, 80 panel rows IN SYNC, release v0.7.0-perfect-rebuild 293K zip.

**Lesson:** repetition is not emphasis — it is noise. Show mastery through daily life, keep lore in the ledger. The clean-and-clear law scales to any serial.

## Dragon Prince Yuan — native-OC (Zhou Xu)

**The gate that cried FAIL — and was right to.**

- The scanner reported FAIL. The project looked fine. The truth: **the scanner was right for the wrong reasons** — it hard-coded 11 SL4-specific firewall filenames, so a project declaring firewalls in a differently-named file read as "zero firewalls" (scanner bug, made generic after), *and* the project genuinely lacked a machine-readable live-edge manifest (authored after). Two stale "do not write Chapter 1 yet" headers were also found sitting above their own contradicted later sections.

**Lesson:** when a gate fails and you're sure the work is fine — investigate the gate too. Then fix both. A false FAIL you investigate is worth ten false PASSes you never see.

## Lan Shen — Soul Land 3 (dual-track reincarnation)

**V2 epoch — canon-parallel rebuild · 2 chapters live 8,779w · 9 layers ALL GREEN.**

- Doctrine: canon runs *on the page*, complete and unskipped, in Wulin's own close-third. OC lives in parallel — same clock, same streets — butterfly only logged when tracks make contact on the page.
- V1 had 15 chapters, retired 2026-09-23 for canon-parallel doctrine violation (transcribed translation dialogue, 297 verbatim words). Re-voiced Ch1-4 to 0-63 verbatim words each.
- Fix 2026-09-26: README 1->2 chapters, V1/V2 split clarified, status_gen registered Chapter_02, removed ⚠️ marker.

**Lesson:** canon-parallel is not "canon-adjacent" — it is canon *on the page*. If you skip canon, you are not parallel.

## Seed of Creation · The Second Heartbeat · Holy Spirit — foundation-stage serials

- *Seed of Creation* (SL2.5 era): scaffolded, four rulings pending, **zero chapters until ruled**. 
- *The Second Heartbeat* (SL5): Tang San's twin brother — foundation with a butterfly registry and ripple rules before a word of prose.
- *Holy Spirit* (SL2): 4 chapters, governed by the NO-MISTAKE KIT.

**Lesson:** foundation-stage is a *stage*, not a failure to start. Rulings first, prose second — always.

---

## The scoreboard (2026-09-26 audit — 12 repos)

| Serial | Chapters | Words/state | One-line legacy |
|---|---|---|---|
| The Adaptive Prodigy | 116 | ~354,700 | built the system |
| Fire Phoenix | 52 | live (private) | two-copies + pacing laws |
| The Unraveled Tide | 24 | 84K | multi-panel law |
| Devouring Dragon | 24 | 65K | plain-language law · canon-voice rollout |
| Blue Silver | 15 | 34,711 | seven-gate maturity |
| The Golden Lion | 8 | 24K | one-day gated launch · near-daily |
| The Grey Wolf | 6 | 15,798 · perfect rebuild v0.7.0 | clean-and-clear law · F0-F22 locks |
| Holy Spirit | 4 | live | no-mistake kit |
| Dragon Prince Yuan | 1+ | live | the gate that cried FAIL |
| Lan Shen | 2 | 8,779w V2 | canon-parallel doctrine |
| Stark Heir | 4 | 22K | MCU dual-track |
| MCU Eternal | 3 | paused | MCU Eternal OC |
| The Second Heartbeat | 0 | foundation | rulings-before-prose |
| Seed of Creation | 0 | foundation | same |

**Combined: 796K+ words in soul-library (193 chapters), every shipped chapter gate-checked. 12 repos total, 9 public, 1 private, 1 profile, 1 primary. Method proven across 10+ Soul Land serials plus MCU.**

**New 2026-09-26: Grey Wolf perfect rebuild added — clean and clear, no nonsense repetition, avg 14-18, band 2400-3400, over60 0, the-way 0, 80 panel rows IN SYNC.**
