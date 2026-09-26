# 06 · Automation — every tool from 12 serials — v2.0 Advanced Perfect Edition

**This is the full tool inventory from 12+ repos — 2940 files measured — every script that enforces a law. Copy, adapt, never invent from scratch.**

---

## The tool inventory — all tools from all projects

### Grey Wolf — Perfect Rebuild — run_all.py 4 steps

**Path:** `soul-land-2-the-grey-wolf/tools/`

- `run_all.py` — [1/4] manuscript synced: 6 reader editions + FULL edition (manuscript/ gains FULL edition) [2/4] style gate passed — style_gate.py: band 2400-3400, avg 14-18, over60 0, the-way 0, bare 0, dialogue density, etc. [3/4] site built — build_site.py: 6 chapters + index -> docs/ [4/4] panel ledger in sync — check_panels.py: ledger rows 80 IN SYNC, frozen meter fails build. Exit 0 only if all pass.
- `style_gate.py` — style laws self-enforcing band 2400-3400 avg 14-18 over60 0 the-way 0 bare 0 dialogue density etc.
- `build_site.py` — reading site 6 chapters + index -> docs/ 6 reader editions + FULL edition.
- `check_panels.py` — drift guard frozen meter fails build ledger rows 80 IN SYNC Exact-figures section single cultivation authority.

### Golden Lion — Agent-Driven Near-Daily

**Path:** `soul-land-2-the-golden-lion/`

- `checks/verify.py` — gate sl2-goldenv PASS 8 chapters, structural gates.
- `checks/measure_prose.py` — prose measurement.
- `tools/ship_chapter.py` (inherited from kit) — one-command chapter ship mechanical 80% + authored 20% checklist, see Ship Law in glossary.
- `foundation/STATUS_PANEL.md` — single-state truth Snapshot v20 G09 sect-join executed ch8 shipped assessment-eve armed chapters live 8, THE single source of truth, if number isn't here doesn't exist yet.

### Devouring Dragon — Beast-POV Plain Language + Canon-Voice

**Path:** `soul_land_devouring_dragon/` (via soul-land-universal-kit) + `soul-library/`

- `tools/measure_prose.py` — floor/ceiling/60-cap + retired-word hits + the-way tic cap 2 + one-line beat paragraphs allowed house style, s40 plain language law ~350 substitutions, s34 avg ≤25 no >60.
- `tools/build_oc_status.py` — OC status sheet generated from authority files glance table full sheet §1-8 verbatim life ledger live edge next chapter regenerates on every ship Sentinel fails build if stale, foundation/OC_STATUS.md + library's dd-status.html.
- `tools/ship_chapter.py` — one-command chapter ship WHAT IT AUTOMATES mechanical 80%: gates first measure_prose floor/ceiling/60-cap + verify single-file + full project sweep ship STOPS if any fails kit root README chapter count bumped LIVE BUILD line + tree-table row serial README LIVE EDGE/NEXT BEAT block swapped machine block <!-- LIVE-EDGE-START ... LIVE-EDGE-END --> wholesale block replace nothing stale survives site chapter copied serials.json appended search_data.json rebuilt analytics rebuilt news.html + feed.xml entries calendar edge profile README chapter counts bumped pushed needs SHIP_TOKEN env sentinel re-run at end expects green WHAT IT DELIBERATELY DOES NOT AUTOMATE authored 20%: STATUS_PANEL entry + LIVE EDGE line HIS_STATUS_PANEL live line ADAPTATION_LOG delta SERIAL_LOG row CONTINUITY row PLACES/TIMELINE rows checklist printed refuses "shipped" until --mirrors-done Exit 0 only when every automated step verified.
- `tools/analytics.py` — measure every chapter house way sentence avg dialogue density length write analytics_data.json measured never typed.
- `tools/build_recaps.py` — build recaps_data.json The Story So Far from kit devouring-dragon foundation/CONTINUITY.md two table formats LAST occurrence per chapter wins recap table overrides anchor table.
- `tools/lint_continuity.py` — cross-chapter consistency checks TIMELINE monotonicity no chapter may travel back in time each row's real-age span must start at-or-after previous row's close TIMELINE coverage every chapter on disk must have written row no row may reference chapter that does not exist PLACES references every "(chN)" citation must point at existing chapter CONTINUITY coverage chapters ch1..chN all present in anchor/recap tables exit 0 clean.
- `tools/sentinel.py` (soul-library) — independent workspace health scan scans kit + library RUNS real gates checks every live-edge claim it can find writes sentinel.html + sentinel_data.json into site root every value measured never typed re-run any time python3 tools/sentinel.py --kit /path/to/kit checks per serial panel/README live-edge vs chapter files on disk library snapshot vs disk gate result actually executed where gate exists workspace checks kit README serial-row counts vs disk Control Centre registered edge vs disk if checkout given public profile README live-edge vs disk fetched live lesson counting *.md in chapters/ dir over-counts when dir carries notes/README files Tide false-positive count only chapter-numbered files checker must measure thing it claims to measure 25 checks 25 PASS.

### Lan Shen — Dual-Track Canon-Parallel 9 Layers

**Path:** `lan_shen/checks/`

- `checks/run_all.sh` — 9 layers ALL GREEN.
- `checks/verify.py` — 9 structural gates 7 inherited from kit +2 local RESULT PASS.
- `checks/style_gate.py` — voice law measured from author's corpus RESULT PASS warnings.
- `checks/canon_copy_check.py` — narration 12-grams quoted runs >=7 words density <=120 words RESULT PASS, V1 15ch retired 2026-09-23 for canon-parallel doctrine violation transcribed translation dialogue 297 verbatim words re-voiced Ch1-4 to 0-63.
- `checks/marker-leak grep` — no codex glyph may reach finished prose 8 glyphs widened 2026-09-20 PASS.
- `checks/privacy grep` — no personal email / token / sandbox id / arena.local host PASS building each pattern from pieces so script does not match itself.
- `checks/build hygiene` — no __pycache__ / .pyc / .bak / .DS_Store PASS.
- `checks/selftest.py` — 20 checks proves every gate can fail PASS every injected defect caught and named.
- `checks/kit selftest.py` — inherited-gate regression against vendored kit PASS.
- `checks/banned_token_check.py` — regression tokens values known-dead PASS.
- `check (d) date arithmetic` — every "N days ago / N days later" recomputed by hand against day map highest-yield check caught 9 month-count errors in ch9 alone and 4 stale year counts in ch13.
- `tools/status_gen.py` — STATUS.md auto-generated never hand-edit regenerated automatically at end of every checks/run_all.sh battery run or by hand python3 tools/status_gen.py if file appears with ⚠️ marker it is real but unregistered add line to generator 116 files 8779w.

### MCU Stark Heir + Eternal Varun — 8 Gates + 2 Manifest Zero-Digit Zero-CJK

**Path:** `mcu_fanfic_stark_heir/tools/` + `mcu_eternal_fanfic/tools/`

- `tools/mcu_verify.py` — 8 gates +2 manifest:
  - G1 unreadable-script — CJK regex per line scanned 22 files 0 hits
  - G2 backslash-n — literal \n surviving into VALUE rejected
  - G3 digits-in-prose — 4 chapters prose outside fences 0 digits zero-digit law
  - G4 dialogue-floor — Chapter_01 96 lines Chapter_02 83 Chapter_03 67 Chapter_04 72 floor enforced
  - G5 anchor-order — Chapter_01 anchor 2008 OK same-era sequence allowed single-anchor order only span-contiguity needs start-end panels
  - G6 placeholders — 0 placeholders foundation TBDs out of scope
  - G7 marker-discipline — markers fenced only cards ≤1 and last
  - M1 manifest-edge — edge ch4 matches 4 files edge ch3 matches 3 files
  - M2 forbidden-future — denylist ['Chitauri','Ultron','Extremis','Vibranium','Sokovia','Blip','Thanos','Avengers','Infinity'] absent ['Uni-Mind','Tiamut','Emergence','Blip','Thanos','Kro'] absent
  - TOTAL PASS 0 failures
- `tools/mcu_verify.py --selftest` — pass_definition exit 0 with FAIL=0 across all gates + manifest edge matches chapters on disk.
- Stark Heir STATUS_PANEL.md Snapshot v20? Actually Stark Heir STATUS_PANEL §0 LIVE through IM1 beats 1-15 post-Chapter Four age 12 shipped gated Ch1 v5 Before News Ch2 v2 Albatross 6231w Ch3 v3 Return 4909w Ch4 Workshop Rebirth 5467w gates PASS zero-digit zero-CJK canon receipts on file canon_coverage/.

### Blue Silver — Seven-Gate Maturity

**Path:** `blue_silver/`

- Seven-gate structure canon panel ledger firewall prose continuity selftest matured here all seven gates passing 15ch 34,711w Book One complete ends with A Yin naming him kill count zero permanent small and gated coexist rebuild protocol.

### Adaptive Prodigy — Ten-Layer Verification

**Path:** `Soul_Land_3_Project/`

- `checks/run_all.sh` — must exit 0 ten-layer ALL GREEN state footer locks sync zero-tolerance presence workspace divergence compl etc.
- `THE_CODEX.md` v3.06 single source of truth, `CODEX/05_PROJECT_SOUL_LAND_3.md` archived 2026-09-18 to `_attic/CODEX_05_PROJECT_SOUL_LAND_3_stale_v2_25.md` staleness layer enforces TWO-COPIES LAW fails if second copy reappears.
- 116ch / 354,685 story words suite-counted full-spectrum repair pass green.

### Fire Phoenix — Private Ch52 Validation Per Chapter + Support Sync

**Path:** `/tmp/audit_private/soul_land_4_fire_phoenix/` + symlinked workspace

- `audits/POST_RANKING_REBUILD_VALIDATION_2026-09-17.md`
- `audits/CHAPTER_52_VALIDATION_2026-09-19.md`
- `audits/CHAPTER_52_SUPPORT_SYNC_2026-09-19.md`
- `canon_coverage/Canon_Coverage_Chapter_52.md`
- Five-copies disaster fix took full day dated archive with git mv receipts 345 renames all R100 zero deletions zero content changes and README_STALE_ARCHIVED.md markers.

### StoryOS — State + Drift + Server

**Path:** `storyos-site/`

- `scripts/build.py` — scans StoryOS workspace one or more project folders emits self-contained static payload into data/ — data/index.json portal gates growth integrity small load first data/state/<proj>.json full state locks firewalls characters decisions rules data/chapters/<proj>/<n>.json one chapter prose footer separated + coverage data/vault/<proj>.json every file path bytes sha256 kind data/issues.json independent drift/stale-edge findings + scanner-gap proof design notes no third-party dependencies Python 3.9+ stdlib only published state DERIVED FROM PROJECT'S OWN FILES never hard-coded here authority order foundation/CURRENT_STATE_MANIFEST.json -> foundation/STATUS_PANEL.md -> HANDOFF.md if they disagree disagreement reported not silently resolved chapter prose split from ## Footer production block so reader page can show prose only while agents still get footer every vault file carries sha256 so consumer can detect alteration.
- `scripts/drift.py` — independent stale-edge scanner does not trust project's checker.
- `scripts/server.py` — static app + JSON API + proposal inbox + key-gated writes + audit log.
- `app/index.html` — whole UI one self-contained file no external assets.
- `bin/serve-tunnel.sh` — build + serve + cloudflared http2 + end-to-end edge verification.
- `data/` — generated index.json state/ chapters/ vault/ issues.json.
- Run it published snapshot live on GitHub Pages served from gh-pages branch cut from published-site/ regenerate when publish.

### Control Centre — Selftest + Extract State + Bootstrap + Build

**Path:** `the-universal-storyline-creation/`

- `tools/selftest.py` — CONTROL CENTRE SELFTEST negative tests for validate.py every rule gets bad case and good case baseline minimal valid firewall passes valid firewall without provenance passes array of two valid contributions passes parse level malformed JSON rejected empty array rejected non-object contribution rejected Gate 1 unreadable script CJK in string rejected kana rejected hangul rejected em dash and en dash allowed not blanket non-ASCII ban box-drawing characters allowed bullet marker allowed Gate 2 literal backslash-n real newline inside JSON string allowed multi-line belief with several newlines allowed literal backslash-n surviving into VALUE rejected nested deep rejected.
- `tools/extract_state.py` — Extract real project state from workspace into state/*.json run from repo root's control_centre/ directory every number written here measured from disk never typed by hand re-run any time workspace changes if fiction workspace not present alongside control_centre/ normal case for agent handed Control Centre on its own script leaves committed state/workspace.json untouched and exits 0 measurements already stored in state/ so bootstrap and site still build nothing downstream depends on re-deriving them REQUIRED_DIRS blue_silver SOUL_LAND_UNIVERSAL_KIT guard cold-start walk_files is_binary check PK ZIP PNG JPEG GIF PDF gzip measure files words mislabeled_binaries PROJECTS blue_silver Book One complete 15 rebuilt chapters gate-pass sl4_fire_phoenix After Chapter 31 Ticket Owed to Fire live SOUL_LAND_UNIVERSAL_KIT 11 laws +13 templates portable SOUL_LAND_NEW Tian Yu 6 chapters pre-Chapter-11 active reference/sl3_lin_hao Reference archive craft only never canon reference soul_land_starter Blank-project bootstrap skeleton template blue_silver_chapters file title n words kit_laws file n words title templates sl4_chapters Chapter_\\d+.md.
- `tools/bootstrap.py` — transfer bootstrap generated from state/.
- `tools/build.py` — site generated from state/.
- `state/` — data what actually persists workspace.json measured from disk by extract_state.py canon.json canon spine rank ladder ring ages user rulings laws.json twelve locks seven gates pipeline firewall states firewalls.json knowledge firewall registry log.json every growth event append-only contributions.json contributed records projects_registry.json navigation ref every serial (now 13 projects).
- `index.html` GENERATED never hand-edit TRANSFER_BOOTSTRAP.txt GENERATED never hand-edit README.md this file PROTOCOL.md contribution contract Makefile commands.
- `Makefile` commands: `make selftest` -> measure -> bootstrap -> build `make serve` above then serve site on :8080 open index.html whole Control Centre live on GitHub Pages published 2026-09-23 https://gm5206663-bit.github.io/the-universal-storyline-creation/ hand to another agent give them TRANSFER_BOOTSTRAP.txt same state as plain text needs no access.

### Soul Library — Analytics + Recaps + Lint + Sentinel

**Path:** `soul-library/`

- `tools/analytics.py` — measure every chapter house way sentence avg dialogue density length write analytics_data.json measured never typed.
- `tools/build_recaps.py` — build recaps_data.json The Story So Far from kit devouring-dragon foundation/CONTINUITY.md two table formats LAST occurrence per chapter wins recap table overrides anchor table.
- `tools/lint_continuity.py` — cross-chapter consistency checks TIMELINE monotonicity no chapter may travel back in time each row's real-age span must start at-or-after previous row's close TIMELINE coverage every chapter on disk must have written row no row may reference chapter that does not exist PLACES references every "(chN)" citation must point at existing chapter CONTINUITY coverage chapters ch1..chN all present in anchor/recap tables exit 0 clean.
- `tools/sentinel.py` — independent workspace health scan scans kit + library RUNS real gates checks every live-edge claim it can find writes sentinel.html + sentinel_data.json into site root every value measured never typed re-run any time python3 tools/sentinel.py --kit /path/to/kit checks per serial panel/README live-edge vs chapter files on disk library snapshot vs disk gate result actually executed where gate exists workspace checks kit README serial-row counts vs disk Control Centre registered edge vs disk if checkout given public profile README live-edge vs disk fetched live lesson counting *.md in chapters/ dir over-counts when dir carries notes/README files Tide false-positive count only chapter-numbered files checker must measure thing it claims to measure 25 checks 25 PASS.
- `tools/build_oc_status.py` — OC status sheet generated from authority files (Devouring Dragon).
- Reader one self-contained index.html no frameworks no CDN no tracking reading progress localStorage only method how-to-write-fanfiction.

### Universal Kit — Ship Chapter

**Path:** `soul-land-universal-kit/`

- `tools/ship_chapter.py` — one-command chapter ship mechanical 80% + authored 20% checklist, see Ship Law, exit 0 only when every automated step verified.

### How-to-Write-Fanfiction — Minigate Example

**Path:** `how-to-write-fanfiction/examples/`

- `minigate.py` — ~100 lines stdlib only with selftest minimal example CONFIG = your serial's contract banned values firewall terms floors file layout CHECKS = pure functions take repo root return pass/fail per rule GATE = run all checks print PASS/FAIL lines exit 0 only if all pass SELFTEST = build tiny throwaway serials each with exactly one defect assert gate fails on every one and passes on clean one design notes checks read files never memory one defect class per check exit codes contract 0=ship non-zero=loop not finished wire into commit habit no green no push keep stdlib-only Python 3.9+.
- `miniserial/` — tiny throwaway serial for selftest.

---

## How to adapt minigate.py to your serial — advanced

1. Fork `examples/minigate.py` into `tools/verify.py` (or `checks/verify.py` or `tools/mcu_verify.py` depending on serial pattern).
2. Fill `CONFIG`:
   - `banned_values` — numbers panel superseded e.g., Dawnflame 1,120 Dawn-Iron 2,040 etc.
   - `firewall_terms` — knowledge firewall terms.
   - `floors` — wordcount floors band floor ceiling e.g., Grey Wolf 2400-3400 Golden Lion 2800 from ch3 Devouring Dragon 2400-3000.
   - `file_layout` — chapter file pattern e.g., `Chapter_\\d+.md` vs `chapter_\\d+.md` vs `Chapter_\\d+_.*\\.md`, foundation files, etc.
   - `forbidden_future` — MCU denylist e.g., ['Chitauri','Ultron',...] etc.
   - `retired_words` — plain language law retired-words table ~350 substitutions.
   - `style` — avg target 14-18 clean and clear vs ≤25 vs 21.1 etc, over60 cap 0, the-way tic cap 2, bare 0, dialogue floor 96/83/67/72 etc.
3. Add checks from this doc's What a gate checks table — start with 3 most relevant, add one per chapter shipped.
4. Write selftest — 5 defect serials + 1 clean, assert gate fails on every defect and passes on clean, 10/10 classes caught on real ones 5/5 on minigate example 20 checks lan_shen selftest.py every injected defect caught and named.
5. Wire into ship — no green no push — `tools/ship_chapter.py` gates first ship STOPS if any fails.

### Advanced: Grey Wolf run_all.py 4 steps pattern

```python
# [1/4] manuscript synced: reader editions + FULL edition
# [2/4] style gate passed — band 2400-3400 avg 14-18 over60 0 the-way 0 bare 0
# [3/4] site built — 6 chapters + index -> docs/
# [4/4] panel ledger in sync — 80 rows IN SYNC frozen meter fails build
```

### Advanced: Lan Shen 9 layers pattern

```python
# 1 verify.py 9 structural gates 7 inherited +2 local PASS
# 2 style_gate.py voice law measured from corpus PASS warnings
# 3 canon_copy_check.py narration 12-grams quoted >=7 words density <=120 PASS
# 4 marker-leak grep no codex glyph may reach finished prose 8 glyphs PASS
# 5 privacy grep no personal email / token / sandbox id / arena.local host PASS
# 6 build hygiene no __pycache__ / .pyc / .bak / .DS_Store PASS
# 7 selftest.py 20 checks proves every gate can fail PASS
# 8 kit selftest.py inherited-gate regression PASS
# 9 banned_token_check.py regression tokens values known-dead PASS
# + check (d) date arithmetic every "N days ago / N days later" recomputed by hand against day map highest-yield
```

### Advanced: MCU 8 gates pattern

```python
# G1 unreadable-script CJK regex per line scanned 22 files 0 hits
# G2 backslash-n literal \n surviving into VALUE rejected
# G3 digits-in-prose 4ch prose outside fences 0 digits zero-digit law
# G4 dialogue-floor Chapter_01 96 lines Chapter_02 83 Chapter_03 67 Chapter_04 72 floor enforced
# G5 anchor-order Chapter_01 anchor 2008 OK same-era sequence allowed single-anchor order only span-contiguity needs start-end panels
# G6 placeholders 0 placeholders foundation TBDs out of scope
# G7 marker-discipline markers fenced only cards ≤1 and last
# M1 manifest-edge edge ch4 matches 4 files
# M2 forbidden-future denylist absent
# TOTAL PASS 0 failures
```

### Advanced: Soul Library sentinel pattern

```python
# python3 tools/sentinel.py --kit /path/to/kit
# scans kit + library RUNS real gates checks every live-edge claim writes sentinel.html + sentinel_data.json
# every value measured never typed
# 25 checks 25 PASS
```

---

*Every tool from 12 repos 2940 files measured — copy, adapt, never invent from scratch. Working examples ready: examples/minigate.py (100 lines stdlib only with selftest) + soul-land-2-the-grey-wolf/tools/run_all.py (4 steps) + lan_shen/checks/run_all.sh (9 layers) + stark_heir/tools/mcu_verify.py (8 gates) + soul-library/tools/sentinel.py (25 checks) + storyos-site/scripts/build.py (data/index.json + state/ + chapters/ + vault/ + issues.json sha256) + the-universal-storyline-creation/tools/selftest.py + extract_state.py + bootstrap.py + build.py + soul-land-universal-kit/tools/ship_chapter.py (mechanical 80% + authored 20%).*
