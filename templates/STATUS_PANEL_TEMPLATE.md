# STATUS_PANEL.md — the single source of truth

**Template · guide v3.0 · law revision v5.4.** Copy to `foundation/STATUS_PANEL.md` (or `STATUS.md` if your project generates its inventory; the names are interchangeable — the *shape* is not).

**How to use:** replace every *example* value (they come from the workshop's reference serial, the Grey Wolf) and keep the section shapes. **The panel may be rebuilt from the chapters; it may never be rebuilt from memory** (F7). **If a number isn't in this file, the number doesn't exist yet.**

**Machinery warning:** the §0 block between the `LIVE-EDGE` markers is parsed by tools. Keep the markers and field names exactly as they are; replace only the values.

---

## §0 — Live edge (machine block)

```
<!-- LIVE-EDGE-START
LIVE_EDGE: {{Chapter NN — Title}}
LIVE_EDGE_FILE: {{chapters/Chapter_NN_Title.md}}
LIVE_EDGE_WORDS: {{0000}}
LIVE_EDGE_AVG: {{00.0}}
LIVE_EDGE_BAND: {{IN 2400-3400 | OUT — reason}}
LIVE_EDGE_OVER60: {{0}}
LIVE_EDGE_THE_WAY: {{0}}
LIVE_EDGE_BARE: {{0}}
LIVE_EDGE_PANEL_LINES: {{0 | N}}
LIVE_EDGE_GATE: {{PASS — battery name, steps, panel rows IN SYNC}}
LIVE_EDGE_DATE: {{YYYY-MM-DD}}
NEXT_BEAT: {{Chapter NN+1 — the beat, in one line}}
LIVE-EDGE-END -->
```

**LIVE EDGE:** {{one rendered line — chapter, words, avg, caps, panel lines, gate, date}}
**NEXT BEAT:** {{the next chapter's beat, in one line}}

---

## §1 — The OC — full status card

- **Name:** {{OC name}} — *example: Ye Cang*
- **Origin:** {{who they are and why they are here, one line}} — *example: an Earth mind reborn, full meta, silent, innate rank 1, beside the canon lead (F0)*
- **Age / Level:** {{age}} · {{rank}} — *example: 12 · rank 30, Great Soul Master*
- **Martial soul:** {{the soul and its grade line — every grade a different name}} — *example: Grey Wolf → Storm Frost Ghost Wolf (ice + wind)* — see F2/F16/F17
- **Rings:** {{count}} — {{years, color, concealed state}} — *example: 2 · 1,350y / 1,850y, true purple shown as yellow by Ring Veil* — see F10/F11
- **Body:** {{state}} — *example: ~500 kg, robust for age* — see F18
- **Spirit Sea / equivalent:** {{value}} — *example: 850 — perception 10–100 m*
- **Appearance & tells:** {{the canon's own marks, from your beast/source study — not invented poetry}} — see F20

## §2 — Exact figures (the single cultivation authority)

Every number the prose may use lives here. A chapter that prints a number not on this list is wrong.

- **Level:** {{nn}}
- **Rings:** {{years / colors / concealment}}
- **Body:** {{value}}
- **Spirit Sea / equivalent:** {{value}} — {{effective talent stacking, if the serial uses one}}
- **Meters** — each with its grade line and current %:
  - Walking — Low {{n}}% → Silent Wind Step (Mid)
  - Running — Low {{n}}% → Wind Stride (Mid)
  - Body Control — Low {{n}}% → Flowing Body (Mid)
  - Soul Power Control — Low {{n}}% → Flowing Control (Mid)
  - Five Senses — Low {{n}}% → Keen Senses (Mid)
  - Reading — Low {{n}}% → Fluent Reading (Mid)
  - Understanding — Low {{n}}% → Deep Understanding (Mid)
  - Spearmanship — Low {{n}}% → Spear Flow (Mid)
  - Cooking — Low {{n}}% → Camp Cooking (Mid)
  - Combat Style — Low {{n}}% → Grey Ridge Hunt (Mid→High) — *the fusion of everything that feeds it*
- **Fusion ledger:** {{three-Low fusions in flight and their progress}} — *example: Walking + Running + Body Control (three Low at 100%) fuse → Silent Wind Step (Mid) at 1% — movement + movement + footwork = movement.*
- **Skills:** {{names + ring + age}} — full descriptions live in `SKILLS_CANON.md`.

## §3 — Pace laws (every meter on its own fuel)

Each meter advances because life happened — never because the plot needs a number (F8). *Examples in brackets.*

- Walking — paced by steps · Running — by distance · Mountain Stride — by distance
- Body Control — by control events · Soul Power Control — by flow events
- Five Senses — by sensing · Observation — by looking · Hunter's Sense — by tracking
- Stillness — by held quiet · Tally — by counting · Plain Speech — by conversations
- Reading — by pages · Understanding — by comprehension events
- Spearmanship — by thrusts · Cooking — by meals · Combat Style — by sparring (fusion of many)
- **Everything that grows feeds every open meter. 100% is the evolution trigger — never a resting terminal.**

## §4 — Working notes

- **The prose law:** band 2,400–3,400 · avg 14–18 · over-60 = 0 · the-way = 0 · bare = 0 · no repetitive skill lists in the body — mastery shown by daily-life action; lore in the footer or this file.
- **F22 (panel prose rule):** a full panel prints in a chapter **only on update or gain**; ordinary chapters may print **0 panel lines** and that is legal and deliberate. *Example: Ch6 — The Hem Road, 0 panel lines, daily life, no fights yet.*
- **Current working preference:** {{e.g. road craft, hem roads, villages — the texture this arc lives in}}.

---

*The evolution chain in one breath: every technique has a grade (Low · Mid · High · Top) and 1–100% within it; at 100%, that second, it evolves into the next technique of its lineage — every grade a different name; suitable techniques fuse (2–3 Lows → one Mid); footwork fuses to **one** line — Basic Walking + Basic Running + Mountain Stride → Silent Wind Step (Mid) — never three separate Highs. There is no such thing as 100% MASTERED. The full law and the per-technique map: [`docs/01_the_laws.md`](../docs/01_the_laws.md) (F14 · F23 · F26 · Appendix B).*
