# 01 · The Laws — 42 entries of record (F0–F26 · P12 · N1–N5 · X1–X6 · 7 structural)

**Guide v3.2 · Law revision v5.6 · updated 2026-10-25.** Where this file and any other disagree about what a law says, this file wins. The measured inventory and the two version axes live in [`../VERSION_OF_RECORD.md`](../VERSION_OF_RECORD.md).

---

## How to read a law

Every law here was paid for — by a rejected chapter, a lost file, or a complaint in the author's own words. Nothing in this list is theoretical. Each of the three groups below follows the same shape:

- **What it says** — the rule itself.
- **The check** — the mechanism that enforces it (a script, a generated file, or a review step). *A law without a check is a wish.*
- **Paid for by** — the serial and the incident that earned it.

Two house rules govern the list itself:

1. **Numbers are receipts.** The gaps — F1, F21, F24, F25, F27+ — are reserved forever. A renumbered law loses the mistake that paid for it. New laws take the next free number above F26.
2. **Author words are quoted, never paraphrased into something better.** Where a law came from an author ruling, the ruling appears in the author's own words, marked as a quote.

---

# Group 1 — The F-series: the constitution of a gated beast-serial

The F-series was written for *Soul Land 2 — The Grey Wolf* (OC Ye Cang, beside Huo Yuhao), and it generalizes to any serial with a power system: **a character's strength is a ledger, not a mood.**

### F0 — The OC is grown, full-meta, an Earth mind in the world; innate 1, beside the canon lead
The original character is an adult mind reborn — full meta-knowledge of the setting — with a deliberately weak start (innate soul power rank 1 in the source incident) and a position *beside* the canon protagonist, never in front of him. Reborn-mind discipline is the OC's real edge: patience, method, and the refusal to show off.
- **Check:** the status panel's identity card; the OC's decisions must read as an adult's.
- **Paid for by:** the Grey Wolf build (F0 is its base lock).

### F2 — Bloodline while awakening (see F15 for the full model)
A bloodline is inherited, not granted: the Grey Wolf bloodline seats on awakening night — 7% on night one — and grows only when later events (a first kill, a thousand-year ring) deepen the line. Bloodline is never awarded for ordinary training.
- **Check:** inheritance events are logged in the ledger with the scene that showed them.
- **Paid for by:** the Grey Wolf rebuild — "bloodline at awakening" was the fix for a fiat grant.

### F3 — Research everything; check canon perfectly
Before a chapter is drafted, the canon this chapter will consume is fetched and read — primary text first. This is the standing instruction *"check canon perfectly"*, and it is the root of the whole canon-first family (see F4, and the receipts law in Group 3).
- **Check:** the canon ledger and the receipt files — nothing enters a chapter unverified.
- **Paid for by:** canon drift everywhere; formalized as a standing author instruction.

### F4 — All files: the full docset exists before chapter one
A gated serial needs roughly **twenty foundation files** — panel, ledger, systems, timeline, cast, receipts — before the first chapter is drafted. The docset is the serial's source of truth; chapters are written *out of it*.
- **Check:** the docset inventory in the serial's handoff file; the gate reads these files.
- **Paid for by:** every serial that started clean vs. every attempt that stalled mid-arc.

### F5 — Workshop refresh
Working practices are refreshed and re-verified: archives are built with `tar`, not `rsync`; git identity is re-exported in every fresh shell; `gh` is absent — the REST API with a token is the path; tokens never enter the tree.
- **Check:** the privacy grep in the gate battery — no credential may reach the repository.
- **Paid for by:** a real personal email once reaching public history; the lesson became a gate layer.

### F6 — Do yourself: stop writing chapters until the foundations are approved
When the author says *"perfect rebuild"* or *"clean and clear"* or *"no nonsense repetition"*, writing stops. The agent audits, asks questions, checks canon, rebuilds the foundation — and only then does prose resume. Ask first; the foundation stage is a stage, not a failure to start.
- **Check:** the rulings file — any unanswered ruling locks drafting.
- **Paid for by:** the Grey Wolf perfect rebuild; the rule that a rebuild begins with questions, not pages.

### F7 — FULL panels: the status panel is the single source of truth
Every list, every number, current. The panel opens whenever the character looks for it, prints at every key beat, and is updated the same turn any number moves. **If a number isn't in the panel, the number doesn't exist yet** — and the drift guard fails the build on a stale line.
- **Check:** the panel drift guard (`check_panels.py` pattern) + generated status files.
- **Paid for by:** the panel-drift incidents across the workshop.

### F8 — Honest pace: every meter keeps its own pace
Every growth meter advances on its own fuel — reading advances by pages, understanding by comprehension events, spearmanship by thrusts, cooking by meals, combat style by sparring. Meters are infusion-fed: they advance because life actually happened, never because the plot needs a number.
- **Check:** the meters file; the drift guard freezes any meter whose behavior stops matching its pace law.
- **Paid for by:** the rejection of fiat leaps (R14 in the one-in-a-thousand register: exact numbers, live ledgers, no fiat leaps).

### F9 — Grade ladder: grades are honest current readings
The ladder runs **Low · Waste · Ordinary · High · Excellent · Top · Top-tier · Ultimate · Divine · Extreme** (with *attribute roads* beyond), and a grade is a *reading of what actually is*, not a permanent label. Grades rise as the thing grows, and 100% within a grade triggers evolution to the next grade's technique — instantly (see F14).
- **Check:** grade claims must match the exact-figures section of the status panel.
- **Paid for by:** the Grey Wolf rebuild — "everything Mid or above at the Ch6 gate" per the author's view.

### F10 — Ring seats beast bloodline
Every soul ring seats the bloodline of the beast it came from. The line deepens on living releases, hunts, and years — and on the ring's own age (F16). It feeds blood, body, soul, vitality, recovery, the predator's frame, and the senses, and it shows in the appearance before it shows in any number.
- **Check:** each ring's seat entry in the ledger, with its beast and years.
- **Paid for by:** the Grey Wolf's two thousand-year rings.

### F11 — Full grant: seven parts, level per ring
A ring grants everything at once — **skill · rank · gift · soul's upgrade · body flood · blood · years** — and the ring-color table is law: **white 10 · yellow 100 · purple 1,000 · black 10,000 · red 100,000** years. A first ring has an absorption limit (~420 years) but *ages beyond it once seated*.
- **Check:** the full-grant block in the skills canon; the gate measures the numbers.
- **Paid for by:** the Grey Wolf grant audits.

### F12 — Walls alone are ring-gated
Rank bottlenecks are walls, and a wall yields only to a ring — earned through the trials the canon defines, alone. Nothing else moves the wall: not money, not time, not wishing.
- **Check:** the cultivation authority section of the panel is the single source for wall state.
- **Paid for by:** canon's own bottleneck law, enforced against convenience.

### F13 — Honest yield: 24/7
Training yields honestly, around the clock — passive gains are real, quiet, and logged; nothing arrives for free and nothing is wasted. Growth by living: nothing purchasable, no ceiling.
- **Check:** the exact-figures section vs chapter evidence.
- **Paid for by:** the anti-resource-buy rules (see the bans list in the glossary).

### F14 — Evolution Chain Law: there is no such thing as 100% MASTERED
**The core technique law.** Every technique has a grade — Low, Mid, High, Top — and advances 1–100% *within* its grade. **At 100%, that same second, it evolves into the next technique of its lineage** — instantly, with no resting state and no terminal. There is no such thing as "100% MASTERED".

> *"What the hell : 100% · MASTERED, there is no such thing, when it's work like that basic walking and running low it go 1 to 100% the just as it reach 100% that' second it evolve into next like imagine silent wind step, mid level , then it's go same 1 to 100% then as it's reach 100% , it's become next, ghost Frost Strom step, High then it's same, Yes suitable techniques can fuse like three fuse and become a High and others many, how logically thing's work There is no such thing : 100% · MASTERED So why you add what i ever tell you to make this nonsense"*
> — the author, on the old mastery model (recorded verbatim)

**The line, in example:** Basic Walking (Low) 1–100% → evolves the second it hits 100% → **Silent Wind Step (Mid)** 1–100% → **Ghost Frost Storm Step (High)** 1–100% → **Storm Frost Ghost Veil (Top)**. Running (Low) → Wind Stride (Mid) → Storm Step (High). Every grade carries a **different name** — Mid is not "Low, improved"; it is its own technique with its own identity and its own next.

- **Check:** the ban sweep (`banned_token_check.py` pattern) — a valid "MASTERED terminal" may not appear in any doc or chapter; only the explanatory quote of the fix is allowed.
- **Paid for by:** the author's strike against the old model — *"There is no such thing: 100% MASTERED"*. The old F14/F18 "mastery no stages → MASTERED" text was nonsense and was purged.

### F15 — Interconnection: everything feeds everything (2.96× cascade)
Effective talent is not a fixed number. It is **innate 1 + the bloodlines + every basic evolving through its chain + fusions** — talent *grows as bloodlines grow and techniques evolve*. One meter rising visibly moves others (the recorded cascade: a Grey-Wolf Mid appearance at 2.96× effect). The whole is faster than its parts can account for.
- **Check:** the exact-figures section lists the current stacking honestly; the cascade is logged when it fires.
- **Paid for by:** the Grey Wolf interconnection audits.

### F16 — Thousand-year: aging is by what pours through
Rings age **in their seats — not by the calendar, but by what pours through them**. The Grey Wolf's Ghost ring went 120 → 1,350 years (purple) by the Ch5 gate; the second seat reached 1,850. Thousand-year rank puts everything at Mid or above and fuses the hunt into **Grey Ridge Hunt** (see F26 for fusion discipline).
- **Check:** the ring's age is a ledger entry; the gate fails a stale age.
- **Paid for by:** the thousand-year ring audits.

### F17 — Evolution on breakthrough: martial soul, skills, concealment
When bloodline change and a ring-grade breakthrough land (yellow → purple at 1,000 years; purple → black at 10,000), the martial soul evolves (**Grey Wolf → Ice Wolf → Storm Frost Ghost Wolf**, as one lineage with different names per grade), skills upgrade *keeping identity while power grows and the new effect appears* — and concealment is its own law: **Ring Veil** shows a true purple ring as yellow to the world. The true color lives in the ledger. Canon shows true ring colors to the reader; the veil is the character's, never the narrator's lie.
- **Check:** skill-upgrade entries on the breakthrough gate; the veil's state in the panel.
- **Paid for by:** the Grey Wolf Ch5–Ch7 gates.

### F18 — Life-skills evolve on the same chain
Everything a person learns is a technique: soul-power control, body control, five senses, observation, running, walking, stillness, hunter's sense, mountain stride, spear, tally, plain speech, reading, understanding, spearmanship, cooking, combat style. Each has its grade and its 1–100%, each evolves with a new name, and suitable ones fuse. *Reading* is paced by pages; *Cooking* by meals; *Combat Style* fuses all the basics that feed it.
- **Check:** the meters file carries each skill's own pace law; the engine freezes a meter that stops moving honestly.
- **Paid for by:** the life-skill audits — the old "100% MASTERED High" model was nonsense.

### F19 — Canon skill format: describe skills the way the canon does
Skills are written in the canon's own descriptive format — the light, the physical transformation, the tell, the effect — e.g. Dai Mubai's White Tiger possession (pale white light, muscles expanding, hair shifting, hands enlarging, claws like 20 cm daggers), Feng Xiaotian's Wind Blade Burst (ten half-crescents, sealing, evasion, 10× quantity), Double Wolf Possession (+50% attack/defense/agility), Swift Wind Dual Wings (cyan wings, 50 m flight, best condition, shatter to preserve life), Tornado Wind Blade (countless sharp wind blades), Thirty-Six Continuous Slashes (strength and speed rising per chop, evolving 54/72).
- **Check:** skills canon file — the description format is the canon's, not the system's.
- **Paid for by:** the skills-canon rebuilds.

### F20 — Beast-study: know the beast from the canon, whole
A soul beast is not a normal animal. Study the source's beast on its own terms — e.g. the Ghost Wolf's canon facts (golden hair-lock on the forehead, iron-gray coat, green glowing eyes; *the paradox*: toughest skull, fragile body — "copper-headed, iron-boned, tofu-waist"; the elite, calculation-driven phantom hunter — psychological warfare, avoids head-on fights, attrition that tracks until the quarry tires or exposes a flank; the 1,000-year Light of Netherworld; Advanced Ghost Doppelganger's three phantom clones hiding the real body; its canon stage — the Shrek Beast Dueling Area climax against Huo Yuhao and He Caitou). Even the commonest thing is a soul beast — a dog is a spirit hound; a serpent is a Black-Ravine Serpent (rule SB-11).
- **Check:** the beast-study file exists and is cited by the chapter's coverage doc.
- **Paid for by:** the beast-type study.

### F22 — Panel prose rule: full panels only on change
> *"Not every time in chapter you only write when there is update or just gain then you write full normally i can check in status file everything when i needed"*
> — the author (recorded verbatim)

A full status panel appears in a chapter **only when something updates or is gained** — a level, a ring, a bloodline beat. Ordinary chapters may print **zero panel lines**; the status file carries everything when it is needed. (The Grey Wolf's *Ch6 — The Hem Road* holds the standard: daily life, no fights yet, **0 panel lines** — mastery shown by use, not by printout.)
- **Check:** the chapter's panel-line count is measured; the panel ledger must stay IN SYNC regardless of what printed.
- **Paid for by:** the author's complaint against panels repeated every chapter.

### F23 — The Evolution Chain Fix, pinned
F23 is the completion of F14: the chain was recorded in the docs before it was pinned in the law list — this entry is the pin. **No terminal; 100% is the trigger; every grade has its own name and its own logical next; fusion is a native part of the model.** All earlier "100% MASTERED High" references are superseded.
- **Check:** the ban sweep + the law-presence grep (both described in `03`).
- **Paid for by:** the same strike that produced F14; F23 pins it so no later edit can quietly lose it.

### F26 — Footwork Fusion: *which fool masters so many step techniques separately? They fuse!*

> *"Basic Walking → Silent Wind Step → Ghost Frost Storm Step, Basic Running → Wind Stride → Storm Step → Ghost Wind Burst, Mountain Stride → Ridge Stride → Wind Ridge Step — What you think what am i saying, what you understood why fusion, there is so many footwork technique what they don't fuse, In Frist please which fool master so many step techniques"*
> — the author (recorded verbatim)

**The fix, mandatory:** Basic Walking (Low) + Basic Running (Low) + Mountain Stride (Low) are *all footwork*. At 100% each, they **fuse into ONE movement technique** — **Silent Wind Step (Mid)** at 1% — not three separate High lines. From there the single line runs Silent Wind Step (Mid) → Ghost Frost Storm Step (High) → **Storm Frost Ghost Veil (Top)**. One line, not three. Footwork + footwork + footwork = footwork, with a new name.

**And the discipline that pairs with it — correct evolution per technique, not everything into Silent Wind Step.** The full per-technique map is in **Appendix B** (body, senses, spear, reading, cooking, combat style, cultivation, concealment and more — each with its own lineage and its own next).

- **Check:** the skills canon must show one footwork line, not three; a reviewer reads the technique table against Appendix B.
- **Paid for by:** the author's footwork complaint, 2026-10 (law revision v5.4).

---

# Group 2 — Franchise laws: film and television

### P12 — The camera law (and the P12 amendment)
For film/TV fandoms: **canon is consumed and retold in order — the camera goes where canon goes.** The camera never lingers inside your OC's head while canon events happen off-screen; the canon scene is shown, complete, from the canon's own angles, and your OC's line runs *parallel*, touching at the points the story chooses.

- **Film order** — beats are consumed in the work's own release order, staged scene-by-scene, receipts first.
- **Plural panels** — a chapter may carry several canon-side panels: what each canon perspective sees.
- **Absolute canon ownership** — canon owns its events; the OC may participate only where the story has earned the right, and every touch is registered (the T-registry).
- **Check:** `mcu_verify.py` (8 gates, zero-digit and zero-CJK rules for MCU), coverage docs per chapter, T-registry entries.
- **Paid for by:** *Stark Heir* (Iron Man eras, film order, plural panels) — and the amendment that followed its first arc.

---

# Group 3 — Structural laws: the workshop itself

### StoryOS — the state site signs everything
The publishing layer that turns a workspace into a reader + agent console. Every file carries its **sha256**; an **independent drift scanner** re-checks the project against itself and *does not trust the project's own checker*; standard library only — no frameworks, no CDN. **Receipts, not trust** — the machine version of F3.

### Control Centre — state in data, site generated
The account's navigation console. You do not edit the site; you change the `state/` data, and the site and the plain-text transfer bootstrap regenerate. **Generated, never hand-edited** — so a fresh agent reads one page and reaches correct state.

### Soul Library — one index.html, no frameworks
The public reading shelf. One static page, no frameworks, no tracking; a sentinel runs **26 independent checks** (2026-10-13: 26 of 26 ran, 26 pass) — including the coverage line that states how many checks *ran*, because a check that silently skips is a check that lies.

### Dual-Track — canon-parallel construction
The OC runs **parallel to canon on the same clock**: canon happens on the page, complete and unskipped, in the canon lead's own close-third where possible; the OC lives in the same city, the same streets, the same days — and a butterfly is only logged when the two tracks make contact *on the page*. **Canon shown, never skipped; the OC added, never centered.** The knowledge firewall file says what the OC knows and when. *Paid for by:* *Lan Shen V2* — the rebuild that retired a 15-chapter epoch for violating exactly this.

### Foundation-Stage — rulings first, prose second
Some serials begin life ruled but unwritten: stage zero is a *stage*, not a failure to start. Zero chapters until the rulings are answered, and that is a success state. *Paid for by:* the foundation serials that exist as rulings and scaffolds by design.

### Ship Law — mechanical 80%, authored 20%
Shipping a chapter is a **checklist, not a mood**: the mechanical steps (measure → gate → sync generated files → commit → push → stamp the live edge) must exit 0; the authored steps (the chapter's own final read) are declared, not skipped. **Nothing refuses to ship louder than a checklist that prints and verifies each step.** *Paid for by:* every ship script in the workshop (`ship_chapter.py` and its siblings).

### Clean-and-Clear — the prose law
Natural prose, average sentence length **14–18**, chapter band **2,400–3,400 words**, **0** sentences over 60 words, **0** "the-way" constructions, **0** bare fragments — no repetitive skill lists in the body; mastery is shown by daily-life **action**; lore dumps live in the footer or the status file, not the scene. *Paid for by:* the author's rejection of the chapter whose average sentence was 6.8, median 5, repeating "100% evolving High" per sentence and the same four canon phrases ten times. The rebuild that followed is the standard every serial now aims at.

> **Amendment (v5.5, 2026-10-25) — Clean-and-Clear is a HOUSE register, and its bands are fandom-conditional.**
> 14–18 was measured over this workshop's own shelf, and a band measured over your own fan fiction can
> only reproduce your own fan fiction. **Before chapter one, measure the SOURCE** — dialogue share,
> sentence average, longest line, whether it prints technique names in a fixed format, whether it uses
> narration for interiority at all — and set the band from that. **The one number that never moves is
> the 60-word cap.** See [`11_register_and_camera.md`](11_register_and_camera.md).
> *Paid for by:* a chapter that passed five structural gates while reading like the wrong book.


---

# Group 4 — The N-series: what a sentence is allowed to contain

**The F-series governs a character's ledger. The N-series governs the camera.** Written for *Black
Clover* on 2026-10-25, after a chapter cleared every structural gate and was still in the wrong voice —
twice. **N4 is the only law in this guide that overrides a number measured from our own shelf.**

### N1 — No simile in narration
`like` / `as if` / `as though`, outside quotation marks. **Speech may be as lyrical as the character is;
the camera may not be lyrical at all.** Canon compares by event, never by image: *"in one gust"*, never
*"like leaves off a tree in one gust"*.
- **Check:** `tools/camera_gate.py` N1 (selftested, fires on a planted simile outside speech).
- **Paid for by:** *Black Clover*, 2026-10-25.

### N2 — No interiority in narration
`felt` · `realized` · `wondered` · `seemed` · `thought about` · `knew that`, outside quotation marks.
**A feeling is shouted by the person having it, or shown by a body doing something. It is never
reported.** *"Yuno thought about it and then stopped thinking about it"* becomes *"Yuno looked at the
yard. He looked at the wood in his hands."*
- **Check:** `tools/camera_gate.py` N2.
- **Paid for by:** *Black Clover*, 2026-10-25 — **the highest-yield rule in the guide**: nearly every
  "this reads like a novel, not the source" complaint is N2, and N2 is decidable by a regex.

### N3 — Dialogue is the engine: the share is a band, not a vibe
Default **45–70% of paragraphs in speech** for a source whose own pages are mostly speech. Below the
band you have written narration with dialogue in it; above it, nobody is standing anywhere.
- **Check:** `tools/camera_gate.py` N3.
- **Paid for by:** *Black Clover* (27% shipped, and it read quiet).

### N4 — Short lines, and a 60-word cap that never moves
Average **8–14** for a shouting source; **60-word hard cap regardless of source.** Fragments are legal.
**The cap matters more than the average** — a mean can be dragged down by a hundred good short lines
while the forty-word ones still kill the page.
- **Check:** `tools/camera_gate.py` N4. **Overrides the Clean-and-Clear amendment's band, never its cap.**
- **Paid for by:** *Black Clover* (longest sentence 55 → 51 → **34**; the 51 draft was still wrong).

### N5 — Announced, never narrated
If the source prints its moves in a fixed format, print them in that format. *[Attribute] Magic: [Spell
Name]!* — *"WATER CREATION MAGIC: HOLY FIST OF LOVE!"* — never *"she cast Water Magic."*
- **Check:** `tools/camera_gate.py` N5.
- **Paid for by:** *Black Clover*.
- **Generalises to any fandom with a visible technique grammar**: a summary in narration is a *format*
  error, not merely a voice error.

**The law under all five:** *the narration is a camera — it says what happened and what is in the room.
Everything else comes out of a character's mouth, or it does not go in the book.*


---

# Group 5 — The X-series: writing from a moving source

**The N-series governs what a sentence may contain. The X-series governs which machine you are writing
from.** Written the same day, after the same serial was corrected a third time — *"you take manga okay
but i also show, i mean by it anime style is."* **A manga is a series of chosen instants. An anime is a
series of imposed durations.** Everything below follows from that one line.

### X1 — Sound leads the cut
Every scene arrives as a **sound** before it arrives as a picture. An anime cannot cut silently; a prose
chapter with a heading that labels a place, and no sound in the paragraph after it, has been written from
a manga.
- **Check:** does the scene's first paragraph carry a noise? · **Paid for by:** *Black Clover* (five caption boxes in one chapter).

### X2 — The hold
The anime can hold a face and do nothing with it. **A manga panel cannot — an empty panel is a wasted
panel.** Silence is material only animation owns.
- **Check:** count the still paragraphs — no dialogue, no movement, no new fact. **A scene with zero holds was written from a manga.** · **Paid for by:** *Black Clover* (0 → 6).

### X3 — The narrowing, not the cut
A manga goes wide panel → close-up panel. **The anime moves there** — one continuous push from the wide to
the hand to the knuckles. Reach the detail through movement, not through a jump.
- **Check:** movement or jump? · **Paid for by:** *Black Clover*.

### X4 — Breath in the line
**Manga dialogue is typeset. Anime dialogue is performed.** `…` is a held shot, not punctuation. A scream
cracks mid-word. `"Ah—"` is an interruption. If every line is a complete sentence, it was transcribed, not
performed.
- **Check:** is any line broken where a **body** breaks it? · **Paid for by:** *Black Clover*.

### X5 — Episode architecture
**Cold open → A-part → eyecatch → B-part → next time.** The cold open is why canon's legend lands: in the
manga it is a caption; in the anime it is a voice over a battlefield before the title.
- **Check:** the three markers are **all present or all absent** — never two of three. · **Paid for by:** *Black Clover*.

### X6 — The moving source expands; it does not compress
An anime episode adapts its manga chapters **and goes past them**; it never cuts canon to fit, it makes
room. **So an anime-styled chapter is usually LONGER than a manga-styled one.**
- **Check:** the canon consumed against the episode's own running order. **A card claiming `EP. N` that stops where the chapter stopped is a false card.** · **Paid for by:** *Black Clover* — card said `ep. 1`, chapter stopped at the four-leaf, ep. 1 runs to the five-leaf.

**The law under all six:** *the card says what you drew on, and the medium in the card sets the grammar.
`ANIME BASE: ep. N` is not a citation — it is a promise about how the chapter moves.*

---

# Appendix A — The compressed pin (receipt)

The pin below is the workshop's own compressed storage of the F-series and the structural laws — kept verbatim as a receipt of how the law list was carried between projects. It is *compressed*, not canonical prose: for what each law *means*, read the groups above.

```
F0 OC grown Earth full meta silent wolf innate1 beside Yuhao
F2 bloodline at awakening
F3 research everything
F4 all files
F5 workshop refresh
F6 Do yourself
F7 FULL panels
F8 honest pace
F9 grade ladder
F10 ring seats beast bloodline
F11 full grant 7 parts level per ring white10/yellow100/purple1k/black10k/red100k
F12 walls alone ring-gated
F13 honest yield 24/7
F14 Evolution Chain Law v5.1: There is no such thing as 100% MASTERED. Basic walking and running Low go 1 to 100% — just as it reaches 100% that second it evolves into next like Silent Wind Step Mid level — then same 1 to 100% then as it reaches 100% it becomes next Ghost Frost Storm Step High then same. Suitable techniques can fuse like three fuse and become a High and others many, how logically things work. Low 1-100% → Mid 1-100% → High 1-100% → Top — no terminal — 100% is evolution/fusion trigger
F15 interconnection 2.96× Grey Mid appearance cascade — talent grows as bloodlines grow and techniques evolve Low→Mid→High
F16 thousand-year 1350/1850 purple level29-30 everything Mid+ fusion Grey Ridge Hunt — evolution chain, not terminal — three Low fuse → Mid, three Mid → High
F17 evolution Storm Frost Ghost Wolf at High+purple skill upgrade on breakthrough Ghost Veil/Storm Step at 1000y check SL3 concealment Ring Veil hides purple as yellow fool shows two thousand-year full basics fuse Reading/Understanding/Spearmanship/Cooking/Combat Style etc but evolution chain Low→Mid→High — Basic Walking Low different name 1-100% → Silent Wind Step Mid different name → Ghost Frost Storm Step High different name → Storm Frost Ghost Veil Top different name — every grade different name, suitable fuse
F18 life-skills evolution chain v5.1: no terminal — Walking Low→Silent Wind Step Mid, Running Low→Wind Stride Mid, Body Control Low→Flowing Body Mid, Soul Power Control Low→Flowing Control Mid, Five Senses Low→Keen Senses Mid, Reading Low→Fluent Reading Mid, Understanding Low→Deep Understanding Mid, Spearmanship Low→Spear Flow Mid, Cooking Low→Camp Cooking Mid, Combat Style Low→Grey Ridge Hunt High, Hunter's Sense Low→Beast Sense Mid, Stillness Low→Patience as Limb Mid, etc — suitable techniques can fuse like three fuse and become a High
F19 canon skill format Dai Mubai White Tiger possession pale white light muscles expand golden hair white/black king pattern forehead hands double size white fur claws 20cm daggers Feng Xiaotian Wind Blade Burst 10 half crescent sealing evasion 10× quantity Double Wolf Possession +50% attack defense agility Swift Wind Dual Wings cyan wings flight 50m best condition shatter preserve life Tornado Wind Blade countless sharp wind blades tornado Thirty-Six Continuous Slashes strength speed increasing each chop evolves 54/72
F20 Ghost Wolf 1000-year canon facts golden hair lock forehead iron-gray coat green glowing eyes identifier toughest skull fragile body tofu waist paradox copper-headed iron-boned tofu-waist waist/neck vulnerable elite calculation-driven phantom hunter psychological warfare suspicious avoids head-on high-speed attrition tracking till tire/exposed flank 1000-Year Light of Netherworld speed-boost physical mitigation aura flash past sensory tracking Advanced Ghost Doppelganger 3 phantom clones hiding real body Soul Land 2 Shrek Academy Beast Dueling Area Huo Yuhao+He Caitou vs Thousand-Year Spectre Wolf climax Dark Gold Terror Claw Bear right palm bone dark golden blades shattering skull
F22 panel prose rule Not every time in chapter you only write when there is update or just gain then you write full normally i can check in status file everything when i needed beat 0 lines allowed full details in STATUS.md SKILLS_CANON.md
F23 Evolution Chain Fix v5.1 — There is no such thing as 100% MASTERED terminal — Low 1-100% → Mid → High instant evolution second it hits 100% — every grade different name — same law family as F14/F18
F26 footwork fusion complaint — which fool masters so many step techniques separately? They fuse! — Basic Walking Low + Basic Running Low + Mountain Stride Low all footwork fuse into ONE movement technique not three separate High
P12 camera law camera goes where canon goes receipts first film order plural panels + P12-AMENDMENT
StoryOS sha256 independent drift stdlib only data/index.json state/ chapters/ vault/ issues.json
Control Centre state in data site generated index.html GENERATED TRANSFER_BOOTSTRAP.txt GENERATED state/workspace.json measured never typed
Soul Library one index.html no frameworks sentinel 26 PASS
Dual-Track canon-parallel canon on page complete unskipped close-third OC parallel same clock same streets butterfly only when tracks contact
Foundation-Stage rulings first prose second always zero chapters until ruled
Ship Law mechanical 80% + authored 20% checklist Exit 0 only when every automated step verified
Clean-and-clear avg 14-18 band 2400-3400 over60 0 the-way 0 bare 0 road craft hem roads villages — evolution chain Low→Mid→High, no terminal
```

*The pin's Soul Library line carried the shelf count of its day; the live count is on the shelf itself (26 of 26 sentinel checks, 2026-10-13).*

---

# Appendix B — The technique map (F26, applied)

Correct evolution **per technique** — every lineage distinct, every grade a different name, and **not everything into Silent Wind Step**:

| Technique | Low | Mid | High | Top |
|---|---|---|---|---|
| Footwork (Walking + Running + Mountain Stride **fused**) | the three fuse | Silent Wind Step | Ghost Frost Storm Step | Storm Frost Ghost Veil |
| Body control | Basic Body Control | Flowing Body | Storm Body | Ghost Body |
| Soul-power control | Basic Soul Power Control | Flowing Control | Spirit Control | Spirit Sea Control |
| Five senses | Basic Five Senses | Keen Senses | Spirit Eye | Divine Perception |
| Observation | Basic Observation | Hunter's Eye | Spirit Perception | Void Eye |
| Hunter's sense | Basic Hunter's Sense | Beast Sense | Predator Sense | Phantom Sense |
| Stillness | Basic Stillness | Patience as Limb | Void Stillness | Eternal Stillness |
| Spear | Basic Spear | Spear Flow | Storm Spear | Ghost Spear Dominion |
| Tally | Basic Tally | Clear Mind | Profound Tally | Ledger Mind |
| Plain speech | Plain Speech | Clear Speech | Silver Tongue | Soul Speech |
| Reading | Basic Reading | Fluent Reading | Deep Reading | Spirit Reading |
| Understanding | Basic Understanding | Clear Understanding | Profound Understanding | Enlightened Understanding |
| Spearmanship | Basic Spearmanship | Spear Flow | Storm Spear | Ghost Spear |
| Cooking | Basic Cooking | Camp Cooking | Feast Cooking | Spirit Feast |
| Combat style | Basic Combat Style | Grey Ridge Hunt | Storm Frost Ghost Hunt | Ghost Storm Dominion |
| Soul-power cultivation | Basic Soul Power Cultivation | Flowing Soul Cultivation | Dark Pool Cultivation | Spirit Sea Cultivation |
| Hunter's craft | Basic Hunter's Craft | Forest Craft | Grey Ridge Craft | Ghost Ridge Craft |
| Concealment (ring veil) | Ring Veil | Ring Veil (deepened) | Veil of Ghost | Phantom Veil |
| Netherlight | Light of Netherworld | Netherlight | Ghost Veil | Ghost Storm Veil |
| Storm charge (2nd ring skill) | Wind Blade Burst | Windstride | Storm Step | Storm Frost Ghost Wings |

**Fusion discipline:** 2–3 suitable Lows at 100% fuse → one Mid at 1%; 2–3 Mids → one High; 2–3 Highs → one Top. Fusion follows logic, never convenience: *movement + movement + body = movement; mental + mental + mental = mental; perception + perception + patience = perception.* No random fusion. No terminal. 100% is the evolution trigger — with a new name.

---

*Law revision v5.4 · 31 entries of record · rebuilt 2026-10-13 from the compressed originals; every law, receipt and author quote preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
