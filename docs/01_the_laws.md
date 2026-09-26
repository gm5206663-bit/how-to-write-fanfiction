# 01 · The Laws of Record — v2.0 Advanced Perfect Edition

**25 laws. Every one paid for with a real failure, a real author strike, or a real rebuild. Each has a rule (what you do) and a check (how it's enforced). A law without a check is a wish.**

> Compressed form — pin above desk:
> ```
> canon first, ask never · canon shown, OC beside · traits dated, power floor · nothing pre-decided, bends logged
> one truth, zero copies · read everything, update everything · plain words · compress routine, expand butterfly
> author outranks files · no gate, no ship · scope law: write once · panel law: panels only when needed, default none
> clean and clear: avg 14-18, band 2400-3400, over60 0, the-way 0 · panel prose rule: full only on update/gain
> every meter its own clock · everything that grows feeds every open meter · 100% is gate never resting
> world defines roads, System never invents · effective talent measured, not typed · Spirit Sea + body separate
> MCU: camera goes where canon goes, receipts first, film order, plural panels · never replace canon cause, deny ACCESS not competence
> StoryOS: every file sha256, independent drift scan, stdlib only · Control Centre: state in data, site generated from state
> ```

---

## Law 1 — The Canon-First Creation Law

> **Check canon before inventing. Butterfly-check everything. Personality-first. Style-match canon. Self-audit every chapter. Follow canon by default, ask never.**

- **Rule:** Before writing any scene, find out what canon actually says from **primary text** (novel, film, manga). If canon covers the beat, follow canon by default — never ask permission to be canon-faithful. If you invent, trace ripple: what else changes downstream?
- **Why:** First long serial drifted so quietly timeline unrecoverable by mid-book. Rebuild cost > writing.
- **Check:** canon spine + canon ledger — every chapter lists canon chapters consumed + butterflies. Gate scans contradictions.
- **Advanced:** Three adaptation lenses (from Devouring Dragon s53/s54/s56): novel explanation, manhua panels, donghua structure — receipts in CANON_STUDY.md, laws indexed at top of RAILS.md.

## Law 2 — The Multi-Panel Law

> **Canon always shown, never skipped. The OC is added, never centered. Canon shown, never skipped; the OC added, never centered.**

- **Rule:** Canon events happen on page. You may not skip canon scene because inconvenient; OC may not replace canon character's moment. OC stands beside canon, not on top.
- **Why:** Readers come for world they love. Fastest way to lose them is bending world around OC.
- **Check:** per-chapter panel audit: which canon beats appear, whose arc owns emotional center?
- **Advanced — Panel Law Re-Bound s45:** Panels only when needed, default NONE. Story is beast's (or OC's) — e.g., Devouring Dragon Ch15-18 rebuilt 0% panels, men's thread closed for good. Laws bind forward; pre-law chapters stand as written (No Backward Work ruling).

## Law 3 — The Unfixed Law

> **For AT holders nothing is fixed — traits are dated states; power is a baseline, never a ceiling.**

- **Rule:** Every character sheet entry is **dated state**, not permanent fact. "Rank 39 (as of ch 52)". Power in foundation is floor story starts from, not cage.
- **Why:** Bibles written as eternal truths go stale by ch30, then writers either ignore bible (state rot) or obey it (dead characters).
- **Check:** status panel carries dates; gate banned-value scan catches prose stating numbers panel superseded. Caught real bug: stale copies presented Dawnflame 1,120 / Dawn-Iron 2,040 as current while live panel banned exact values.

## Law 4 — The Natural-Ripple Principle

> **Nothing pre-decided — romance included. Canon spine; bends only when earned and logged.**

- **Rule:** No fixed ending, no planned pairing, no reserved twist. Canon spine is river; fic is boat. When bend canon, bend must be earned by story so far and logged in ledger.
- **Why:** Pre-decided arcs force characters off logic. Readers smell rails.
- **Check:** butterfly registry — every bend entry: cause, first divergence chapter, downstream effects. T-registry for MCU (e.g., T-14 armor family named Mark because OC named Mark).

## Law 5 — The Two-Copies Law

> **A fact maintained in two places will be wrong in one of them, and the check reads the other.**

- **Rule:** Every fact lives in exactly ONE authoritative place. Mirrors either banned, or dated and archived. When copy needed for convenience, copy must be marked generated and check must fail if two drift.
- **Why:** One project existed in five copies at once. Two frozen at Ch31 while live edge Ch52 — someone almost read stale as truth. Cleanup took full day and dated receipt file with git mv R100 receipts.
- **Check:** staleness layer — check fails if second copy reappears; independent drift scanner never trust only project's own checker. Sentinel checks kit README serial-row counts vs disk, library snapshot vs disk, Control Centre registered edge vs disk, profile README live-edge vs disk.

## Law 6 — The Use Everything Protocol

> **Read all files → research canon from primary text → run every law and test → update every file after. Same-turn. Never "later".**

- **Rule:** Before drafting: read whole docset. After drafting: update everything — codex, status panel, continuation prompt, chapter footer, ledger, serial log, index, site, search_data, analytics, news, feed, calendar, profile. Same-turn.
- **Why:** Docset 95% synced is docset that lies 5% of time.
- **Check:** gate sync check — every chapter carries ledger footer; panel chapter counter must equal highest chapter on disk; ship_chapter.py automates mechanical 80% (gates first, kit root README bump, serial README LIVE EDGE/NEXT BEAT swap, site chapter copied serials.json appended search_data rebuilt analytics rebuilt news+feed+calendar, profile bumped, sentinel re-run) — authored 20% (STATUS_PANEL entry, ADAPTATION_LOG delta, SERIAL_LOG row, CONTINUITY row, PLACES/TIMELINE rows) checklist printed and refuses "shipped" until --mirrors-done.

## Law 7 — The Plain Language Law (s40)

> **Plain words. Say the thing. Ornament is a tax you pay twice.**

- **Rule:** Prose favors plain, direct language. Ornament must earn place. Dialogue carries scenes; description serves beat. Early Devouring Dragon buried simple events under heavy prose and readers bounced — re-carve to plain made every later chapter faster to write and gate.
- **Check:** prose-method doc per serial — registers, dialogue floor (e.g., ≥3 dialogue exchanges per scene), word floor per chapter, banned purple constructions, retired-words table.
- **Advanced — Clean and Clear Law (Grey Wolf perfect rebuild):** avg 14-18 words/sentence, no repetitive skill list in body, show mastery via daily life action (e.g., hem roads villages Grey Ridge Hunt using all basics MASTERED High daily life no fights yet), lore dumps in footer only, band 2400-3400w, over60 0, the-way 0, bare 0. User rejected Ch6 style avg 6.8 med 5 repeating "100% MASTERED High" per sentence repeating golden lock/toughest skull/tofu waist/Light of Netherworld 10x — required natural prose avg 14-18 no repetitive skill list.

## Law 8 — The Pacing / Compression Law (s44)

> **Do not map one canon chapter to one fic chapter by default. Compress routine beats; expand only what the butterfly changes. Sameness gets one line; the 1,000-year road is told by time-skip summary.**

- **Rule:** Canon routine chapters (travel, class, minor training) compress into brief passages. Expand only where OC presence genuinely changes outcome — butterfly, character, system, tactics, relationships.
- **Why:** Born on Fire Phoenix: 1:1 pacing made fic slow-motion replay of canon. Fix structural.
- **Check:** each chapter footer lists canon chapters consumed; 1:1 ratio across consecutive chapters triggers review. Fire Phoenix pacing rule: compress routine source beats; expand only meaningful butterfly, character, system, tactical, relationship changes.

## Law 9 — The Author-Rulings Law

> **Author rulings outrank every file. Including the laws. User's latest explicit correction outranks all.**

- **Rule:** When human author decides, decision recorded verbatim in rulings file and takes precedence over every document, including these laws. Agents do not override; they log it. Authority order: User's latest explicit correction > Adaptation-Talent Definitive Master Foundation v2.0 > project's bible/foundation locks > latest STATUS_PANEL > earlier chapters/panels > assistant inference (lowest).
- **Why:** Tools exist to serve story, not trap it. Rules system with no override valve becomes thing it was built to prevent.
- **Check:** rulings file with numbered dated entries; serial log records every ruling same turn.

## Law 10 — The Gate Law

> **No chapter ships without the gate passing. No gate is trusted until its selftest passes. A check that executes nothing verifies nothing.**

- **Rule:** Every serial ships with checker (verify.py-style). Gate must exit 0 before chapter committed. And gate itself must be tested: feed known defects and prove catches them (mine 10/10 defect classes, minigate 5/5). A check that has never caught anything is decoration.
- **Check:** selftest — examples/minigate.py (~100 lines stdlib only with selftest). Three rules of gates: 1) gate must selftest, 2) never weaken gate to pass it (if fails, chapter wrong or panel stale — fix work not test), 3) never trust only project's own checker (scanner hard-coded 11 SL4-specific firewall filenames so project declaring firewalls in differently-named file read as zero firewalls and reported PASS — happened, made generic after) — fix: independent drift scanner built on different assumptions side-by-side, two checkers disagree is most honest alarm.

## Law 11 — The Scope Law (s39)

> **Write it once; no explanation paragraphs; budget 2,400–3,000; scope law.**

- **Rule:** Write event once, not narrated explained then re-summarized. Ch13/14 shipped at 4,008 and 4,673 words — every event narrated explained re-summarized — cut -32% -30% nothing added. Budget per chapter 2,400-3,400 (Grey Wolf) or 2,000-3,400 (Devouring Dragon) or 2,800 floor from ch3 (Golden Lion). Bloat is nonsense.
- **Check:** measure_prose.py floor/ceiling/60-cap + retired-word hits + the-way tic count cap 2.

## Law 12 — The Style Law + House Grammar (s34/s35)

> **Average sentence ≤25 (Grey Wolf perfect rebuild 14-18), no sentence >60 (cap later s43), ≥3 registers, dialogue mandatory in panels, ≥3 dialogue lines per 1000 words (house norm 0.8 was 20× less — disgusted).**

- **Rule:** Average sentence 62-64 words with single sentences 328 and 430 words, one register, 0.8 dialogue lines per 1000 words — author: "what bad chapter's… i can't read few lines before i disgusted by how bad is this." Fixed to avg ≤25, no >60, ≥3 registers, dialogue mandatory.
- **Check:** style_gate.py voice law measured from author's corpus (blue_silver/chapters_rebuilt/ corpus, thresholds measured not chosen by taste), plus six-vertex style bans + SCOPE/ART/PLAIN/CNDR/FP readability ceilings (Fire Phoenix). Grey Wolf clean-and-clear: avg 11.3-18.5, over60 0, the-way 0, bare 0.

## Law 13 — The Panel Prose Rule (F22)

> **Not every time, in chapter you only write when there is update or just gain, then you write full, normally i can check in status file everything when i needed — panel prose rule: no full panel in chapter unless level/ring/bloodline update; beat 0 lines allowed; full details in STATUS.md SKILLS_CANON.md.**

- **Rule:** From Grey Wolf F22: chapter prose should not contain full status panel every time — only when there is update or just gain, then write full, normally reader can check status file. Beat 0 lines allowed (e.g., Ch6 The Hem Road 0 panel lines, daily life no fights yet).
- **Why:** Repetitive full panel every chapter is noise, not emphasis. Show mastery via daily life action.
- **Check:** PANELS.md ledger of every line ever printed — 80 rows IN SYNC for Grey Wolf, check_panels.py drift guard — frozen meter fails build.

## Law 14 — Every Meter Its Own Clock (F14)

> **Mastery no stages→MASTERED, 120→168 pour-based, Mid-caliber 1% Mid. Every meter with own pace law. Everything that grows feeds every open meter. 100% is gate never resting state.**

- **Rule:** From Grey Wolf: Reading 0-100% paced by pages read, Understanding paced by comprehension events, Spearmanship paced by thrusts, Cooking paced by meals, Combat Style paced by sparring, Hunter's Sense paced by tracking, Mountain Stride paced by distance, Tally paced by counting, Plain Speech paced by conversations, etc. Each meter has own pace law in METERS.md v4.0 perfect rebuild. When one grows, it feeds every open meter (interconnection). 100% is gate never resting — not final, just threshold for next.
- **Check:** METERS.md v4.0 + check_panels.py — frozen meter fails build if not updated same-turn.

## Law 15 — Interconnection & Appearance Cascade (F15)

> **Interconnection 2.96× Grey Mid appearance cascade. Traits are dated states, but appearance cascades from soul + body + bloodline.**

- **Rule:** Grey Wolf appearance: iron-gray coat, green glowing eyes, golden hair lock forehead, robust body ~500kg, 2.96× Grey Mid interconnection — every growth changes appearance slightly, logged in CHARACTERS.md v5.0.
- **Check:** CHARACTERS.md v5.0 + STATUS.md v5.0 + BANNED_TOKENS.json drift guard.

## Law 16 — Thousand-Year & Evolution (F16/F17)

> **Thousand-year 1,350/1,850 purple level29-30 everything Mid+ fusion Grey Ridge Hunt. Evolution Storm Frost Ghost Wolf at High+purple, skill upgrade on breakthrough Ghost Veil/Storm Step at 1000y check SL3, concealment Ring Veil hides purple as yellow fool shows two thousand-year, full basics fuse.**

- **Rule:** From Grey Wolf F16/F17: first ring 1350y purple concealed as yellow via Ring Veil, second ring 1850y purple concealed as yellow, both thousand-year, level 29-30, everything Mid+ fusion, Grey Ridge Hunt. Evolution at High+purple to Storm Frost Ghost Wolf ice+wind High (wind even), skill upgrade on breakthrough: Ghost Veil 3 clones golden lock toughest skull tofu waist Light of Netherworld + Storm Step Wind Blade Burst Wings 50m flight + Stormwind Wind Blade Burst.
- **Check:** SKILLS_CANON.md v5.0 perfect rebuild with Ghost Wolf canon facts: golden hair lock forehead iron-gray coat green glowing eyes identifier, toughest skull fragile body tofu waist paradox copper-headed iron-boned tofu-waist waist/neck vulnerable, elite calculation-driven phantom hunter psychological warfare suspicious avoids head-on high-speed attrition tracking till tire/exposed flank, 1000-Year Light of Netherworld speed-boost physical mitigation aura flash past sensory tracking, Advanced Ghost Doppelganger 3 phantom clones hiding real body, Shrek Academy Beast Dueling Area Huo Yuhao+He Caitou vs Thousand-Year Spectre Wolf climax Dark Gold Terror Claw Bear right palm bone dark golden blades shattering skull.
- **Canon receipt:** Dai Mubai White Tiger possession pale white light muscles expand golden hair white/black king pattern forehead hands double size white fur claws 20cm daggers; Feng Xiaotian Wind Blade Burst 10 half crescent sealing evasion 10× quantity, Double Wolf Possession +50% attack defense agility, Swift Wind Dual Wings cyan wings flight 50m best condition shatter preserve life, Tornado Wind Blade countless sharp wind blades tornado, Thirty-Six Continuous Slashes strength speed increasing each chop evolves 54/72.

## Law 17 — Effective Talent & Spirit Sea (Grey Wolf)

> **Effective talent 3.5× Spirit Sea 850 body ~500kg. Spirit Sea 10-100m, road craft preference: hem roads villages Grey Ridge Hunt in use all basics MASTERED High daily life no fights yet.**

- **Rule:** Effective talent measured, not typed — 3.5× = (all basics MASTERED High + interconnection 2.96× + bloodline + Spirit Sea). Spirit Sea 850 (10-100m), body ~500kg robust. Road craft: Ch6 focus hem roads villages Grey Ridge Hunt in use all basics MASTERED High daily life no fights yet effective talent 3.5x Spirit Sea 10-100m.
- **Check:** STATUS.md v5.0 + METERS.md v4.0 + SYSTEM_SPEC.md v4.0 perfect rebuild.

## Law 18 — MCU Camera Law (P12 + P12-AMENDMENT, P13, P14)

> **Canon runs on page, complete and unskipped, in film order, from plural canon-side panels. Camera goes where canon goes. Receipts first. Film order. Plural canon-side panels.**

- **Rule:** From Stark Heir: canon runs on page complete unskipped in film order from plural canon-side panels (P12 + P12-AMENDMENT camera law, P13, P14). OC lives braided around it with absolute canon ownership. Butterfly only logged when two tracks touch on page (T-registry in MCU_TIMELINE.md incl T-14 armor family canon-designated Mark because that is his name — origin-stage queued for Ch.4). Canon consumed: Iron Man 1 beats 1-15 staged scene-by-scene film order (ambush → cave → find → return → chest-swap → workshop rebirth complete → gala Everhart photographs). Next: Chapter Five Gulmira sortie jets tank-punch board lockout.
- **Check:** foundation/MCU_TIMELINE.md complete MCU chronology + butterfly registry, foundation/CROSS_PROJECT_LAW.md P1-P15 + P12-AMENDMENT camera law, foundation/STATUS_PANEL.md, TIMELINE_MARK.md, chapters/, tools/mcu_verify.py 8 gates zero-digit zero-CJK.

## Law 19 — MCU Never Replace / Never Nerf Law

> **Never replace a canon cause (participate, protect, preserve — Gaurav rule). Never nerf to preserve canon: deny ACCESS (parallel separate scene), never competence. Talent never named/voiced in-story; embodied only.**

- **Rule:** From MCU Eternal Varun: Never replace canon cause, never nerf to preserve canon deny ACCESS never competence, Talent never named/voiced embodied only, true mission reaches Varun ONLY via Arc 5 canon chain, Sersi stays Uni-Mind center unless user approves, Gilgamesh canon death via separation (no access) flippable to branch-save ONLY before that chapter written, romance FIRST is AJAK earned Arc 2+ lock file governs later loves natural unforced no planned list zero romance before maturity, no digits in prose no chapter footers no CJK anywhere ASCII filenames.
- **Check:** KNOWLEDGE_FIREWALLS_VARUN.md who may/must-not know what, ADAPTATION_TALENT_LOCAL_MCU_ETERNAL.md, POWER_LAW_GRAVITY_KINETIC.md, CANON_LEDGER_MCU_ETERNALS.md canon beats + confidence tags, NO_MISTAKE_LIVE_RULES.md hard bans.

## Law 20 — StoryOS Law

> **Everything about your projects and your agents, on one host. Standard library only. No node_modules, no CDN, no framework, no build step at runtime. Python 3.9+. Every file with its sha256, live gate, character locks, knowledge firewalls, independent stale-edge drift scan.**

- **Rule:** From storyos-site: scripts/build.py scan projects -> data/*.json with sha256 for every file, scripts/drift.py independent stale-edge scanner does not trust project's checker, scripts/server.py static app + JSON API + proposal inbox + key-gated writes + audit log, app/index.html whole UI one self-contained file no external assets, bin/serve-tunnel.sh build + serve + cloudflared http2 + end-to-end edge verification, data/ generated index.json state/ chapters/ vault/ issues.json.
- **Check:** data/index.json portal gates growth integrity, data/state/<proj>.json full state locks firewalls characters decisions rules, data/chapters/<proj>/<n>.json one chapter prose footer separated + coverage, data/vault/<proj>.json every file path bytes sha256 kind, data/issues.json independent drift/stale-edge findings + scanner-gap proof.

## Law 21 — Control Centre Law

> **Navigation and state reference for every Soul Land serial, plus portable authoring law that governs them. This is a system, not a document. The site and the transfer bootstrap are generated from state/. You do not edit them; you change the state. One read and fresh agent reaches correct state.**

- **Rule:** From the-universal-storyline-creation: state/ is data what actually persists — workspace.json measured from disk by tools/extract_state.py, canon.json canon spine rank ladder ring ages user rulings, laws.json twelve locks seven gates pipeline firewall states, firewalls.json knowledge firewall registry, log.json every growth event append-only, contributions.json contributed records, projects_registry.json navigation ref every serial. Site and transfer bootstrap generated from state/ via tools/bootstrap.py + build.py, you do not edit them you change state. make selftest -> measure -> bootstrap -> build, make serve :8080, open index.html whole Control Centre live on GitHub Pages, hand to another agent via TRANSFER_BOOTSTRAP.txt same state as plain text.
- **Check:** tools/selftest.py negative tests for validate.py every rule gets bad case and good case, tools/extract_state.py measures from disk never typed, workspace.json totals projects files words blue_silver_chapters sl4_chapters kit_laws kit_templates, tools/validate.py, tools/ingest.py.

## Law 22 — Soul Library Law

> **Read the serials. Every gated Soul Land fanfiction serial published as one clean reading site — 193 chapters, 796K+ words, every shipped chapter machine-checked against canon before it lands here. One self-contained index.html — no frameworks, no CDN, no tracking; reading progress lives in browser's localStorage only.**

- **Rule:** From soul-library: chapter text copied unchanged from source of truth soul-land-universal-kit and soul-land-2-the-grey-wolf, when library and workspace disagree workspace wins, word counts measured from files never typed, reader one self-contained index.html no frameworks no CDN no tracking, method that keeps serials canon-true how-to-write-fanfiction. Rebuild: chapter sources under chapters/<serial>/ metadata in data/serials.json, to refresh copy live chapter files from workspace re-measure update data/serials.json counts measured from disk never typed. Tools: analytics.py measure every chapter house way sentence avg dialogue density length write analytics_data.json, build_recaps.py build recaps_data.json The Story So Far, lint_continuity.py cross-chapter consistency checks TIMELINE monotonicity coverage PLACES references CONTINUITY coverage, sentinel.py independent workspace health scan scans kit + library RUNS real gates checks every live-edge claim writes sentinel.html + sentinel_data.json measured never typed, per-serial checks panel/README live-edge vs chapter files on disk library snapshot vs disk gate result workspace checks kit README serial-row counts vs disk Control Centre registered edge vs disk public profile README live-edge vs disk fetched live.
- **Check:** data/serials.json 6 serials 193ch 796K+ (golden_lion 8 24K LIVE CH8 NEW CHAPTERS DAILY, grey_wolf 6 15.8K LIVE PERFECT REBUILD CH6, devouring_dragon 24 65K LIVE GATE-PASS CH24, blue_silver 15 34.7K BOOK ONE COMPLETE, adaptive_prodigy 116 572K, unraveled_tide 24 84K), search_data.json 193 entries full-text search, analytics_data.json avg words avg sentence avg dialogue, recaps_data.json, sentinel 25 PASS.

## Law 23 — Dual-Track Doctrine (Lan Shen V2)

> **Canon runs on page, complete and unskipped, in Wulin's own close-third. The original character lives in parallel — same clock, same streets — and a butterfly effect is only logged when the two tracks make contact on the page. Canon shown, never skipped; the OC added, never centered.**

- **Rule:** From lan_shen V2 epoch canon-parallel rebuild: canon runs on page complete unskipped in Wulin's own close-third, OC lives parallel same clock same streets, butterfly only logged when two tracks make contact on page. V1 15ch retired 2026-09-23 for canon-parallel doctrine violation (transcribed translation dialogue 297 verbatim words) — re-voiced Ch1-4 to 0-63 verbatim words each. 9 layers ALL GREEN, 2ch live 8779w, next ch3 foundling girl canon 005.
- **Check:** tools/verify.py 9 structural gates 7 inherited from kit +2 local, style_gate.py voice law measured from author's corpus, canon_copy_check.py narration 12-grams quoted runs >=7 words density <=120 words, marker-leak grep no codex glyph may reach finished prose 8 glyphs widened 2026-09-20, privacy grep no personal email token noreply id sandbox domain, build hygiene no __pycache__ .pyc .bak .DS_Store, selftest.py 20 checks proves every gate can fail, kit selftest.py inherited-gate regression, banned_token_check.py regression tokens values known-dead, plus check (d) date arithmetic every "N days ago / N days later" recomputed by hand against day map — highest-yield check caught nine month-count errors in ch9 alone and four stale year counts in ch13.

## Law 24 — Foundation-Stage Doctrine

> **Foundation-stage is a stage, not a failure to start. Rulings first, prose second — always. Zero chapters until ruled.**

- **Rule:** From Seed of Creation, Second Heartbeat, Holy Spirit foundation-stage serials: scaffolded, four rulings pending, zero chapters until ruled. Second Heartbeat Tang San's twin brother foundation with butterfly registry and ripple rules before word of prose. Holy Spirit 4ch governed by NO-MISTAKE KIT. Foundation-stage serials have OPEN_RULINGS.md numbered decisions only author can make, drafting locked until answered.
- **Check:** foundation/OPEN_RULINGS.md + RULINGS_LOG.md + SERIAL_LOG.md + STATUS_PANEL.md — no prose until rulings resolved.

## Law 25 — The Ship Law (Mechanical 80% + Authored 20%)

> **Ship script automates mechanical 80%: gates first, kit root README bump, serial README LIVE EDGE/NEXT BEAT swap, site chapter copied serials.json appended search_data rebuilt analytics rebuilt news+feed+calendar, profile bumped, sentinel re-run. Authored 20% deliberately not automated: STATUS_PANEL entry + LIVE EDGE line, HIS_STATUS_PANEL live line, ADAPTATION_LOG delta, SERIAL_LOG row, CONTINUITY row, PLACES/TIMELINE rows — checklist printed and refuses "shipped" until --mirrors-done.**

- **Rule:** From soul-land-universal-kit/tools/ship_chapter.py born 2026-09-23 from mistakes ledger's most-recurring failure mode SYNC GAP — three times Sentinel caught surface left stale after ship (panel LIVE EDGE line, profile count, news/feed). Tool exists so class of mistake cannot happen again: every mechanical step done here verified after execution refused past any failing gate.
- **Check:** ship_chapter.py exit 0 only when every automated step verified, step that cannot verify itself is bug in tool — report it not hand-wave past it. Usage: python3 tools/ship_chapter.py chapters/Chapter_24_X.md --serial devouring_dragon --title "The Stone Country" --live-edge "LIVE EDGE: Chapter 24 — ..." --next-beat "NEXT BEAT: ..." --news-text "..." [--site /path/to/site] [--kit /path/to/kit] [--dry] [--mirrors-done] [--run-sentinel]

---

*All 25 laws are enforced by checks. A law without a check is a wish. A check that has never caught anything is decoration. A gate that has never failed selftest is rubber stamp. Two checkers that disagree is most honest alarm.*
