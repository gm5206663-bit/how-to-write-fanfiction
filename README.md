<p align="center">
  <img src="assets/banner.png" alt="A writing desk at night: a glowing book, five golden spirit rings, a phoenix quill and blue-silver grass" width="100%">
</p>

# How to Write Gated Fan Fiction — The Complete Method

<p align="center">
  <a href="https://github.com/gm5206663-bit/how-to-write-fanfiction/releases/tag/v1.0.0"><img src="https://img.shields.io/badge/release-v1.0.0%20First%20Edition-brightgreen?style=flat-square" alt="v1.0.0"></a>
  <a href="https://github.com/gm5206663-bit/how-to-write-fanfiction/discussions"><img src="https://img.shields.io/badge/discussions-open-9cf?style=flat-square&logo=github" alt="Discussions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT"></a>
</p>

> The system I use to write long-form fan fiction that stays **canon-true for hundreds of thousands of words**.
> Proven on **10+ Soul Land (斗罗大陆) serials** — one of them 116 chapters / ~354,700 words with every chapter machine-checked before shipping.
> Written for **any fandom**, with Soul Land as the working example.

**This is not a vibe guide.** It is a working production system: laws, a foundation docset, a chapter loop, and an audit gate that must pass before anything ships. Treat fan fiction like software: source of truth, tests, and state panels — and your story can grow forever without rotting.

---

## The big idea in 30 seconds

Most fan fiction dies the same five deaths. This method makes each death **structurally impossible** by attaching a rule and a check to every one of them:

| # | How fan fiction dies | The law that kills it | The check that enforces it |
|---|---|---|---|
| 1 | **Canon drift** — the fic contradicts or forgets the source | Canon-First Creation Law | canon spine + canon ledger + gate scan |
| 2 | **OC takeover** — the world bends around the original character | Multi-Panel Law: *canon always shown, never skipped; the OC is added, never centered* | panel audit per chapter |
| 3 | **Power inflation** — the OC becomes a god by chapter 20 | Unfixed Law: *power is a baseline, never a ceiling; traits are dated states* | status panel + banned-value scan |
| 4 | **Voice drift** — canon characters stop sounding like themselves | Style-match + personality-first law | prose method doc + self-audit |
| 5 | **State rot** — notes contradict each other until nobody knows what's true | Two-Copies Law: *a fact maintained in two places will be wrong in one of them, and the check reads the other* | single source of truth + independent drift scan |

---

## The chapter loop

Every chapter, without exception:

```
   ┌─────────────────────────────────────────────────────────┐
   │  1. ORE        read the canon chapters this fic consumes │
   │  2. DRAFT      write the chapter (panels, prose law)     │
   │  3. SELF-AUDIT check every law by hand, fix your own     │
   │  4. GATE       run the machine checks — must exit 0      │
   │  5. SYNC       update EVERY state file same-turn         │
   │  6. SHIP       commit + push, stamp the live edge        │
   └─────────────────────────────────────────────────────────┘
        ↑ repeat. small things become big things if you skip.
```

The full workflow — from empty folder to finished serial — is in [`docs/02_workflow.md`](docs/02_workflow.md).

## What's in this repository

| Path | What it gives you |
|---|---|
| [`docs/01_the_laws.md`](docs/01_the_laws.md) | The ten laws of record — each with *why it exists* and *how to enforce it* |
| [`docs/02_workflow.md`](docs/02_workflow.md) | Foundation → ore → draft → gate → sync → ship, stage by stage |
| [`docs/03_gates_and_audits.md`](docs/03_gates_and_audits.md) | How to build your own audit gate (with a working minimal example) |
| [`docs/04_case_studies.md`](docs/04_case_studies.md) | Real numbers and real lessons from my 10+ serials |
| [`docs/05_glossary.md`](docs/05_glossary.md) | Every term: AT, butterfly, live edge, knowledge firewall, ore… |
| [`examples/minigate.py`](examples/minigate.py) | A working 5-check gate in ~100 lines, stdlib Python, with selftest |
| [`examples/github-actions-gate.yml`](examples/github-actions-gate.yml) | Copy-paste CI: make every push/PR pass the gate selftest on GitHub Actions |
| [`templates/`](templates/) | Copy-paste skeletons: serial foundation, status panel, chapter, canon ledger |

## The living tools (used daily, in their own repos)

| Tool | What it is |
|---|---|
| [`soul-land-universal-kit`](https://github.com/gm5206663-bit/soul-land-universal-kit) | The full public workspace + the portable authoring kit (canon, laws, gates, templates, verify script) |
| [`the-universal-storyline-creation`](https://github.com/gm5206663-bit/the-universal-storyline-creation) | The **Control Centre** — one read and a fresh agent reaches correct state |
| [`storyos-site`](https://github.com/gm5206663-bit/storyos-site) | **StoryOS** — publishes a workspace as a reader + agent console with sha256-level integrity |

> **Two-Copies note:** this repo *teaches* the method; the tools above *are* the method. When they disagree, the tools win.

## Start your first gated serial in 10 steps

1. **Choose your lane** — which era/branch of canon, where you enter, how far you'll follow the spine before diverging.
2. **Write the premise in one paragraph** — protagonist, martial soul / power system hook, and *why canon needs your OC to exist* (if the answer is "it doesn't", good — the OC is added, never centered).
3. **Open the rulings file** — list every decision only the author can make (protagonist identity, relation to canon, entry point, divergence policy). **Drafting is LOCKED until the rulings are answered.**
4. **Build the canon spine** — a dated, sourced list of the canon events your fic will touch. Primary text only; wiki knowledge is ore, not law.
5. **Write the power law** — ranks, ages, costs, ceilings. Then write the **banned-values list**: numbers the prose may never state.
6. **Write the knowledge firewalls** — what your OC must not know yet, and from which chapter they may learn it.
7. **Create the status panel** — the single source of truth for the live edge: ranks, locks, location, relationships, next chapter.
8. **Write the gate** — start from [`examples/minigate.py`](examples/minigate.py), add your serial's banned values and firewalls. **A gate must selftest**: prove it catches defects before you trust it on real chapters.
9. **Write Chapter 1** — canon chapter open, your chapter close. Then run the loop: self-audit → gate → sync every file → ship.
10. **After every chapter, update everything same-turn** — panel, ledger, log, continuation prompt. Never "later". Later is how state rots.

## The laws, compressed

> **Canon always shown, never skipped. The OC is added, never centered.**
> **Check canon before inventing — butterfly-check — personality-first.**
> **Nothing pre-decided, romance included. Bends only when earned and logged.**
> **For AT holders nothing is fixed: traits are dated states, power is a baseline, never a ceiling.**
> **A fact maintained in two places will be wrong in one of them — and the check reads the other.**
> **Author rulings outrank every file. Including this one.**

Full text with commentary: [`docs/01_the_laws.md`](docs/01_the_laws.md).

## Case studies (real numbers)

| Serial | Era | Result |
|---|---|---|
| The Adaptive Prodigy (Lin Hao) | Soul Land 3 | 116 chapters · ~354,700 words · full-spectrum repair pass green |
| Blue Silver (*Home*) | pre-canon | Book One complete — 15 chapters · 34,711 words · all seven gates passing |
| Fire Phoenix (Yan Shuo) | Soul Land 4 | 52 chapters · compression pacing law born here |
| Devouring Dragon | Soul Land | 18 chapters · plain-language law born here |
| The Golden Lion (Jin Yang) | Soul Land 2 | foundation → Chapter 3 in a single day, every step gated |

Full stories and the mistakes that taught each lesson: [`docs/04_case_studies.md`](docs/04_case_studies.md).

---

## ⚖️ Disclaimer

Soul Land (斗罗大陆 / Douluo Dalu) and all related characters, settings, and terms belong to **Tang Jia San Shao (唐家三少)** and the original rights holders. My serials are non-commercial derivative fan work; this guide is my original methodology, released under the [MIT License](LICENSE). No ownership of any source IP is claimed, and the method itself is fandom-neutral — use it with any source material you love.

---

*Built 2026-09-23 by [Gaurav Meena](https://github.com/gm5206663-bit). If this method helps your serial, I'd love to see what you build with it.*
