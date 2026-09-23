# 01 · The Laws of Record

Ten laws. Each one exists because a real serial really failed without it. Each one has a **rule** (what you do) and a **check** (how it's enforced — by hand or by machine).

> Order matters less than this: **a law without a check is a wish.**

---

## Law 1 — The Canon-First Creation Law

> **Check canon before inventing. Butterfly-check everything. Personality-first. Style-match canon. Self-audit every chapter.**

- **Rule:** Before writing any scene, find out what canon actually says. If canon covers the beat, follow canon by default — *follow canon by default, ask never* (a late addition to my own law set: the author follows canon unless they deliberately choose otherwise, and never asks permission to be canon-faithful). If you invent something, trace the ripple: what else changes, and does it break a canon fact downstream?
- **Why:** My first long serial drifted from canon so quietly that by mid-book the timeline was unrecoverable. The rebuild cost more than the writing.
- **Check:** the canon ledger — every chapter lists which canon chapters it consumes and every butterfly it introduces. The gate scans for contradictions.

## Law 2 — The Multi-Panel Law

> **Canon always shown, never skipped. The OC is added, never centered.**

- **Rule:** Canon events happen on the page. You may not skip a canon scene because it's inconvenient; your OC may not replace a canon character's moment. The OC stands *beside* canon, not on top of it.
- **Why:** Readers come for the world they love. The fastest way to lose them is to bend the world around your OC — canon characters becoming cheerleaders, canon crises resolving because the OC exists.
- **Check:** per-chapter panel audit: which canon beats appear in this chapter, and whose arc owns the emotional center?

## Law 3 — The Unfixed Law

> **For AT holders nothing is fixed — traits are dated states; power is a baseline, never a ceiling.**

- **Rule:** Every character sheet entry is a **dated state**, not a permanent fact. "Rank 39 (as of ch 52)". Power written in the foundation is the *floor* the story starts from, not a cage the story must respect.
- **Why:** Character bibles written as eternal truths go stale by chapter 30, and then writers either ignore their own bible (state rot) or obey it (dead characters).
- **Check:** the status panel carries dates; the gate's banned-value scan catches prose that states numbers the panel has superseded. (This law caught a real bug: two stale copies of a project presented `Dawnflame 1,120` as current while the live panel banned that exact value.)

## Law 4 — The Natural-Ripple Principle

> **Nothing pre-decided — romance included. Canon spine; bends only when earned and logged.**

- **Rule:** No fixed ending, no planned pairing, no reserved plot twist. The canon spine is the river; your fic is one boat on it. When you bend canon, the bend must be *earned* by the story so far and *logged* in the ledger.
- **Why:** Pre-decided arcs force characters off their own logic. Readers can smell the rails.
- **Check:** the butterfly registry — every bend has an entry: cause, first divergence chapter, downstream effects.

## Law 5 — The Two-Copies Law

> **A fact maintained in two places will be wrong in one of them, and the check reads the other.**

- **Rule:** Every fact lives in exactly ONE authoritative place. Mirrors are either banned, or dated and archived. When a project needs a copy for convenience, the copy must be marked generated and the check must fail if the two drift.
- **Why:** One of my projects existed in **five copies** at once. Two were frozen at Chapter 31 while the live edge was Chapter 52 — and someone almost read the stale one as truth. The cleanup took a full day and a dated receipt file.
- **Check:** the staleness layer — a check that fails if a second copy reappears; the independent drift scanner (never trust only the project's own checker).

## Law 6 — The Use Everything Protocol

> **Read all files → research canon from primary text → run every law and test → update every file after.**

- **Rule:** Before drafting: read the whole docset. After drafting: update *everything* — codex, status panel, continuation prompt, chapter footer, ledger, serial log, index. Same-turn. Never "later".
- **Why:** A docset that is 95% synced is a docset that lies 5% of the time.
- **Check:** the gate's sync check — every chapter file carries a ledger footer; the panel's chapter counter must equal the highest chapter on disk.

## Law 7 — The Plain Language Law

> **Plain words. Say the thing.**

- **Rule:** Prose favors plain, direct language. Ornament must earn its place. Dialogue carries scenes; description serves the beat.
- **Why:** Born from the devouring-dragon serial (session ruling s40): early chapters hid simple events behind heavy prose and readers bounced.
- **Check:** the prose-method doc per serial — registers, dialogue floor (e.g. ≥3 dialogue exchanges per scene), word floor per chapter, banned "purple" constructions.

## Law 8 — The Pacing / Compression Law

> **Do not map one canon chapter to one fic chapter by default. Compress routine beats; expand only what the butterfly changes.**

- **Rule:** Canon's routine chapters (travel, class, minor training) compress into brief passages. Expand only where your OC's presence genuinely changes the outcome — butterfly, character, system, tactics, relationships.
- **Why:** Born on Fire Phoenix: 1:1 pacing made the fic a slow-motion replay of canon. The fix is now structural.
- **Check:** each chapter footer lists canon chapters consumed; a 1:1 ratio across consecutive chapters triggers review.

## Law 9 — The Author-Rulings Law

> **Author rulings outrank every file. Including the laws.**

- **Rule:** When the human author decides, the decision is recorded verbatim in the rulings file and takes precedence over every document, including these laws. Agents do not override it; they log it.
- **Why:** Tools exist to serve the story, not to trap it. A rules system with no override valve becomes the thing it was built to prevent.
- **Check:** rulings file with numbered, dated entries; serial log records every ruling the same turn it's made.

## Law 10 — The Gate Law

> **No chapter ships without the gate passing. No gate is trusted until its selftest passes.**

- **Rule:** Every serial ships with a checker (`verify.py`-style). The gate must exit 0 before a chapter is committed. And the gate itself must be tested: feed it known defects and prove it catches them (mine run 10/10 defect classes).
- **Why:** A check that has never caught anything is decoration. A gate that has never failed a selftest is a rubber stamp.
- **Check:** the selftest — see [`examples/minigate.py`](../examples/minigate.py) for a working minimal version.

---

*Compressed form of all ten — print it, pin it above the desk:*

```
canon first, ask never        · canon shown, OC beside
traits dated, power floor     · nothing pre-decided, bends logged
one truth, zero copies        · read everything, update everything
plain words                   · compress routine, expand butterfly
author outranks the files     · no gate, no ship
```
