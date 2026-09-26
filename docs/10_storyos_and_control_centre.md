# 10 · StoryOS and Control Centre and Soul Library — publishing patterns — v2.0 Advanced Perfect Edition

**Three publishing patterns from 12 repos — how to make your serials readable by humans and agents without re-explaining.**

---

## StoryOS — everything about projects and agents on one host

**Purpose:** Built so new agent can arrive knowing nothing and still get live edge locks firewalls learned rules and thing not allowed to do without human re-explaining.

**Stack:** Standard library only no node_modules no CDN no framework no build step at runtime Python 3.9+.

**Structure:**
- `scripts/build.py` — scans StoryOS workspace one or more project folders emits self-contained static payload into data/ — data/index.json portal gates growth integrity small load first data/state/<proj>.json full state locks firewalls characters decisions rules data/chapters/<proj>/<n>.json one chapter prose footer separated + coverage data/vault/<proj>.json every file path bytes sha256 kind data/issues.json independent drift/stale-edge findings + scanner-gap proof design notes no third-party dependencies Python 3.9+ stdlib only published state DERIVED FROM PROJECT'S OWN FILES never hard-coded here authority order foundation/CURRENT_STATE_MANIFEST.json -> foundation/STATUS_PANEL.md -> HANDOFF.md if they disagree disagreement reported not silently resolved chapter prose split from ## Footer production block so reader page can show prose only while agents still get footer every vault file carries sha256 so consumer can detect alteration.
- `scripts/drift.py` — independent stale-edge scanner does not trust project's checker.
- `scripts/server.py` — static app + JSON API + proposal inbox + key-gated writes + audit log.
- `app/index.html` — whole UI one self-contained file no external assets.
- `bin/serve-tunnel.sh` — build + serve + cloudflared http2 + end-to-end edge verification.
- `data/` — generated index.json state/ chapters/ vault/ issues.json.
- Run it published snapshot live on GitHub Pages served from gh-pages branch cut from published-site/ regenerate when publish.

**How to use:** Drop your projects under StoryOS workspace, run `python3 scripts/build.py --root /path/to/workspace`, open `app/index.html` or serve via `scripts/server.py`, check `data/issues.json` for drift.

---

## Control Centre — navigation and state reference for every serial

**Purpose:** Navigation and state reference for every Soul Land serial plus portable authoring law that governs them built so fresh agent or human collaborator can reach correct state in one read without being told anything twice and without inventing anything missing. This is system not document site and transfer bootstrap generated from state/ you do not edit them you change state.

**Thirty seconds:**
- `make selftest` -> measure -> bootstrap -> build
- `make serve` above then serve site on :8080 open index.html
- Whole Control Centre live on GitHub Pages published 2026-09-23 https://gm5206663-bit.github.io/the-universal-storyline-creation/
- Hand to another agent give them TRANSFER_BOOTSTRAP.txt same state as plain text needs no access.

**Layout:**
- `index.html` GENERATED never hand-edit
- `TRANSFER_BOOTSTRAP.txt` GENERATED never hand-edit
- `README.md` this file
- `PROTOCOL.md` contribution contract
- `Makefile` commands
- `state/` data what actually persists:
  - `workspace.json` measured from disk by extract_state.py
  - `canon.json` canon spine rank ladder ring ages user rulings
  - `laws.json` twelve locks seven gates pipeline firewall states
  - `firewalls.json` knowledge firewall registry
  - `log.json` every growth event append-only
  - `contributions.json` contributed records
  - `projects_registry.json` navigation ref every serial (now 13 projects)
- `tools/selftest.py` — CONTROL CENTRE SELFTEST negative tests for validate.py every rule gets bad case and good case baseline minimal valid firewall passes valid firewall without provenance passes array of two valid contributions passes parse level malformed JSON rejected empty array rejected non-object contribution rejected Gate 1 unreadable script CJK in string rejected kana rejected hangul rejected em dash and en dash allowed not blanket non-ASCII ban box-drawing characters allowed bullet marker allowed Gate 2 literal backslash-n real newline inside JSON string allowed multi-line belief with several newlines allowed literal backslash-n surviving into VALUE rejected nested deep rejected.
- `tools/extract_state.py` — Extract real project state from workspace into state/*.json run from repo root's control_centre/ directory every number written here measured from disk never typed by hand re-run any time workspace changes if fiction workspace not present alongside control_centre/ normal case for agent handed Control Centre on its own script leaves committed state/workspace.json untouched and exits 0 measurements already stored in state/ so bootstrap and site still build nothing downstream depends on re-deriving them REQUIRED_DIRS blue_silver SOUL_LAND_UNIVERSAL_KIT guard cold-start walk_files is_binary check PK ZIP PNG JPEG GIF PDF gzip measure files words mislabeled_binaries PROJECTS blue_silver Book One complete 15 rebuilt chapters gate-pass sl4_fire_phoenix After Chapter 31 Ticket Owed to Fire live SOUL_LAND_UNIVERSAL_KIT 11 laws +13 templates portable SOUL_LAND_NEW Tian Yu 6 chapters pre-Chapter-11 active reference/sl3_lin_hao Reference archive craft only never canon reference soul_land_starter Blank-project bootstrap skeleton template blue_silver_chapters file title n words kit_laws file n words title templates sl4_chapters Chapter_\\d+.md.
- `tools/bootstrap.py` — transfer bootstrap generated from state/.
- `tools/build.py` — site generated from state/.
- `bin/serve-tunnel.sh` — build + serve + cloudflared http2 + end-to-end edge verification.
- `data/` generated index.json state/ chapters/ vault/ issues.json.

**Method:** One read and stranger reaches correct state. State in data site generated. Every number measured never typed.

---

## Soul Library — read the serials every gated serial published as one clean reading site

**Purpose:** Every gated Soul Land fanfiction serial published as one clean reading site 193ch 796K+ words every shipped chapter machine-checked.

**Live:** https://gm5206663-bit.github.io/soul-library/

**What's on shelf:**
- Golden Lion SL2 LIVE 8ch near-daily
- Grey Wolf SL2 LIVE PERFECT REBUILD 6ch
- Devouring Dragon SL+1000y LIVE 24ch gate-PASS canon-voice rollout Ch1-10
- Blue Silver pre-canon Book One complete 15ch
- Adaptive Prodigy SL3 116ch ten-layer green
- Unraveled Tide SL2 24ch paused
- Combined 193ch 796K+ words every shipped chapter gate-checked.

**How built:**
- Chapter text copied unchanged from source of truth soul-land-universal-kit and soul-land-2-the-grey-wolf when library and workspace disagree workspace wins word counts measured from files never typed.
- Reader one self-contained index.html no frameworks no CDN no tracking reading progress localStorage only method how-to-write-fanfiction.
- Rebuild chapter sources under chapters/<serial>/ metadata in data/serials.json to refresh copy live chapter files from workspace re-measure update data/serials.json counts measured from disk never typed.

**Tools:**
- `tools/analytics.py` — measure every chapter house way sentence avg dialogue density length write analytics_data.json measured never typed.
- `tools/build_recaps.py` — build recaps_data.json The Story So Far from kit devouring-dragon foundation/CONTINUITY.md two table formats LAST occurrence per chapter wins recap table overrides anchor table.
- `tools/lint_continuity.py` — cross-chapter consistency checks TIMELINE monotonicity no chapter may travel back in time each row's real-age span must start at-or-after previous row's close TIMELINE coverage every chapter on disk must have written row no row may reference chapter that does not exist PLACES references every "(chN)" citation must point at existing chapter CONTINUITY coverage chapters ch1..chN all present in anchor/recap tables exit 0 clean.
- `tools/sentinel.py` — independent workspace health scan scans kit + library RUNS real gates checks every live-edge claim it can find writes sentinel.html + sentinel_data.json into site root every value measured never typed re-run any time python3 tools/sentinel.py --kit /path/to/kit checks per serial panel/README live-edge vs chapter files on disk library snapshot vs disk gate result actually executed where gate exists workspace checks kit README serial-row counts vs disk Control Centre registered edge vs disk if checkout given public profile README live-edge vs disk fetched live lesson counting *.md in chapters/ dir over-counts when dir carries notes/README files Tide false-positive count only chapter-numbered files checker must measure thing it claims to measure 25 checks 25 PASS.
- `tools/build_oc_status.py` — OC status sheet generated from authority files (Devouring Dragon) foundation/OC_STATUS.md + library's dd-status.html regenerates on every ship Sentinel fails build if stale.
- `tools/ship_chapter.py` (kit) — one-command chapter ship mechanical 80% + authored 20%.

**Method:** One index.html no frameworks no CDN no tracking reading progress localStorage only. Every value measured never typed. Sentinel 25 PASS.

---

## How to adapt publishing patterns to your serials

### StoryOS pattern — when you have many serials + agents

1. Fork `storyos-site/` structure: `scripts/build.py` + `scripts/drift.py` + `scripts/server.py` + `app/index.html` + `bin/serve-tunnel.sh`.
2. Drop your projects under workspace root.
3. Run `python3 scripts/build.py --root /path/to/workspace` → emits `data/index.json` + `data/state/<proj>.json` + `data/chapters/<proj>/<n>.json` + `data/vault/<proj>.json` + `data/issues.json` with sha256 for every file.
4. Serve via `scripts/server.py` or open `app/index.html`.
5. Check `data/issues.json` for drift — independent stale-edge scanner does not trust project's checker.

### Control Centre pattern — when you need one-read state for strangers

1. Fork `the-universal-storyline-creation/` structure: `state/` + `tools/extract_state.py` + `tools/selftest.py` + `tools/bootstrap.py` + `tools/build.py` + `index.html` GENERATED + `TRANSFER_BOOTSTRAP.txt` GENERATED + `PROTOCOL.md` + `Makefile`.
2. Run `python3 tools/extract_state.py` → measures workspace.json from disk every number measured never typed.
3. Run `make selftest` → negative tests for validate.py every rule gets bad case and good case.
4. Run `python3 tools/bootstrap.py` → generates TRANSFER_BOOTSTRAP.txt same state as plain text needs no access.
5. Run `python3 tools/build.py` → generates index.html site.
6. `make serve` → serve site on :8080.
7. Hand to another agent give them TRANSFER_BOOTSTRAP.txt same state as plain text needs no access.

### Soul Library pattern — when you need clean reading site for many serials

1. Fork `soul-library/` structure: `chapters/<serial>/` + `data/serials.json` + `index.html` one self-contained file no frameworks no CDN no tracking reading progress localStorage only + `tools/analytics.py` + `tools/build_recaps.py` + `tools/lint_continuity.py` + `tools/sentinel.py` + `tools/build_oc_status.py`.
2. Copy live chapter files from workspace into `chapters/<serial>/` — chapter text copied unchanged from source of truth when library and workspace disagree workspace wins word counts measured from files never typed.
3. Run `python3 tools/analytics.py` → measure every chapter house way sentence avg dialogue density length write analytics_data.json measured never typed.
4. Run `python3 tools/build_recaps.py` → build recaps_data.json The Story So Far.
5. Run `python3 tools/lint_continuity.py` → cross-chapter consistency checks TIMELINE monotonicity coverage PLACES references CONTINUITY coverage exit 0 clean.
6. Run `python3 tools/sentinel.py --kit /path/to/kit` → independent workspace health scan scans kit + library RUNS real gates checks every live-edge claim writes sentinel.html + sentinel_data.json measured never typed 25 checks 25 PASS.
7. Update `data/serials.json` counts measured from disk never typed.
8. Publish `index.html` + `data/` + `chapters/` to GitHub Pages.

---

*Three publishing patterns proven — StoryOS sha256 independent drift stdlib only, Control Centre state in data site generated one-read state for strangers TRANSFER_BOOTSTRAP.txt same state as plain text needs no access, Soul Library one index.html no frameworks no CDN no tracking reading progress localStorage only sentinel 25 PASS 193ch 796K+ words every shipped chapter machine-checked.*
