# 11 · Register and Camera — the two prose laws nobody separates

**Guide v3.1 · law revision v5.5 · added 2026-10-25.** This chapter exists because of a failure that
no other chapter of this guide would have caught, on a serial this guide's own laws had already
declared green.

---

## §1 — What happened

A *Black Clover* serial was handed the instruction, in the author's own words:

> **"Hey write like canon how it written and show actually."**

It had a prose law. It had a gate. It had a chapter that passed every check in it. **And the chapter
was written in the wrong voice.**

Then it was fixed, and the author came back:

> **"I'm not talking story but I'm talking about style."**

**Two corrections to get one thing right.** Here is the whole of it, because the repair is the most
useful thing in this document.

| | Draft 1 | Draft 2 | **Draft 3** |
|---|---|---|---|
| What was fixed | — | **volume** (dialogue, refrains, spell names) | **sentences** |
| Sentence average | 17.12 | 13.21 | **8.92** |
| Longest sentence | 55 | 51 | **34** |
| Dialogue share | 27% | 54% | **60%** |
| "the way" | 1 | 0 | **0** |
| Similes in narration | many | **many** | **0** |
| Interiority in narration | many | **several** | **0** |
| Exclamation marks | ~10 | 44 | **56** |

**Read the longest-sentence row: 55 → 51 → 34.** Draft 2 was *loud* and still not canon, because loud
is a volume and canon's actual signature is **short**. A panel has to be read at a glance. A forty-word
sentence cannot be a panel.

---

## §2 — The distinction that cost two rounds

**Register** and **style** are not the same axis, and a serial can be perfect on one while failing the
other.

| | Register | Style |
|---|---|---|
| **What it is** | *What the voice does* — how loud, how much dialogue, whether people announce their dreams and their spells | *What a sentence is allowed to contain* — the camera's field of view |
| **Measured by** | dialogue share, exclamation density, refrain repetition, spell-call format | sentence length, what kind of thing gets narrated |
| **Got wrong how** | calibrated against the **wrong corpus** | **not calibrated at all** |

**Draft 1 failed register** — it was a quiet literary voice on a shouting shonen source.

**Draft 2 passed register and still failed style** — the shouting was now correct and it was still
sitting in narration that read like a novel: *"March came in warm off the ridge. The firefly dandelions
opened all at once, as they did every year…"* Twenty-five words to establish that it was March, in a
book whose source writes a caption box and moves.

**You can hit every register target and still be writing the wrong book, because the register lives in
the dialogue and the *style* lives in everything between it.**

---

## §3 — The camera law, for prose

P12 is the camera law for film and television: canon is consumed and retold in order, the camera goes
where canon goes, and it never lingers inside your OC's head while canon events happen off-screen.

**This is the same law applied to the sentence:**

> ### The narration is a camera. It says what happened and what is in the room.
> ### Everything else comes out of a character's mouth, or it does not go in the book.

Five checkable consequences. All of them are in `tools/camera_gate.py`, and **every one of them was
proven on a fixture that commits the defect.**

### N1 — No simile in narration
`like` · `as if` · `as though`, outside quotation marks. **Speech may be as lyrical as the character
is. The camera may not be lyrical at all.**

- ✗ *They came off the shelves like leaves off a tree in one gust.*
- ✓ *They came in one gust. Hundreds of them. Single file. Down through the grey.*
- **Check:** `camera_gate.py` N1 · **Paid for by:** *Black Clover*, 2026-10-25.

### N2 — No interiority in narration
`felt` · `realized` · `wondered` · `seemed` · `thought about` · `knew that`. **A feeling is shouted by
the person having it, or shown by a body doing something. It is never reported by the narrator.**

- ✗ *Yuno thought about that one for a while, and then stopped thinking about it, because he was fifteen and there was flour to carry.*
- ✓ *Yuno looked at the yard. He looked at the wood in his hands. "…You don't talk much."*
- ✗ *Nash thought about that and did not like it.* → ✓ *Nash made a face.*
- ✗ *Yuno said, without heat.* → ✓ *Yuno put the flour down.*
- **Check:** `camera_gate.py` N2 · **Paid for by:** *Black Clover*, 2026-10-25.

**This is the single highest-yield rule in the chapter.** Almost every "the prose feels like a novel,
not the source" complaint is N2, and N2 is decidable by a regex.

### N3 — Dialogue is the engine
For a source whose own pages are mostly speech, the chapter's dialogue share is a **target band**, not
a vibe. Default **45–70% of paragraphs**. Below it, you have written narration with dialogue in it. Above
it, nobody is standing anywhere.

- **Check:** `camera_gate.py` N3 · **Paid for by:** *Black Clover* (27% shipped, and it read quiet).

### N4 — Short sentences, and a hard cap
Average **8–14** for a shonen source; **60-word hard cap regardless of source.** Fragments are legal and
frequent. **The cap matters more than the average** — a mean can be dragged down by a hundred good short
lines while the forty-word ones still kill the page.

- **Check:** `camera_gate.py` N4 · **Paid for by:** *Black Clover* (longest 55 → 34).

### N5 — Spells are announced, never narrated
*[Attribute] Magic: [Spell Name]!* — the source's own format, in the source's own shape.

- ✗ *She cast Water Magic and he fell down.*
- ✓ *"WATER CREATION MAGIC: HOLY FIST OF LOVE!"*
- **Check:** `camera_gate.py` N5 · **Paid for by:** *Black Clover*.

> **N5 generalises to every fandom with a visible technique grammar.** If the source prints its moves
> in a fixed shape, a summary in your narration is a *format* error, not just a voice error.

---

## §4 — The method that repairs this: the proof sheet

The repair was not a rewrite from a feeling. It was **a paired sheet, and the pairs are the same beat
twice** — left, how it was written; right, how the source writes it; and a note saying **what changed in
the sentence, not in the story.**

```
BEAT: the boys walk up to the tower.

✗  March came in warm off the ridge. The firefly dandelions opened all at once,
   as they did every year, and the seed-fluff came up off the fields and hung in
   the road so thick that the walk to the tower went through it.

✓  > MARCH. THE GRIMOIRE TOWER. THE GRIMOIRE ACCEPTANCE CEREMONY.
   They walked up in the morning with the seed-fluff in the road.

WHY: canon does not write a season. It labels a panel and moves. My version spends
     twenty-five words making the reader feel March so the story can start.
     Canon spends eleven starting.
```

**Two properties make the sheet work.**

1. **The story is held constant.** If the beats differ between columns, you are comparing plots and
   learning nothing. **Change the sentences, freeze the story.**
2. **Every pair carries a stated cause.** "It's better" teaches nothing; *"canon does not write a
   season"* is a rule you can reuse on the next chapter.

**And the proof must be on the page, not in the notes.** An agent that *says* it has matched the
register has told you nothing. **The pairs are the evidence.**

---

## §5 — The rule that outranks your own measurements

The original prose law in this workshop — **Clean-and-Clear** — specifies an average sentence of
**14–18**. It was measured, honestly, over the workshop's own shelf: hundreds of chapters, well over a
million words.

**And it was the wrong number for this job**, because a law measured over *your own fan fiction* can
only ever reproduce **your own fan fiction.** Point that measurement at a source that shouts, and the
gate will happily pass a book that sounds nothing like it.

> ### Measure the source, not the shelf.
> ### A house style is what you have written. The register is what the source *is*.

**Clean-and-Clear is not wrong — it is unlabelled.** It is a *house* register, earned by a shelf, and it
is a perfectly good target when the source is quiet or when the serial is not an adaptation of anything.
It stops being a target the moment a source exists with its own measurable voice, because then the
question is not "what does our shelf sound like" but **"what does this story sound like."**

**The order of operations, cheaply:**

1. **Read the source's own text** — dialogue, caption boxes, how it opens, how its crowd talks.
2. **Write down its features as numbers** — dialogue share, line length, whether it repeats a refrain,
   whether it prints spells in a fixed format.
3. **Set the band from that**, not from your backlog.
4. **Only then** touch a chapter.

**Skipping step 1 is what produced two rejected drafts in one day.**

---

## §6 — The amendment to Clean-and-Clear

**Add-only, per house rules.** The Clean-and-Clear text stands as written and as measured. This is the
amendment that rides with it:

> **Clean-and-Clear is a house register, and every band in it is fandom-conditional.**
> Before the first chapter, measure the **source**: dialogue share, sentence average, longest line,
> whether the source prints spell/technique names in a fixed format, and whether it uses narration for
> interiority at all. **The source's numbers set the band. The shelf's numbers do not.**
> **The one number that never moves is the 60-word cap.**

---

## §7 — What this changes in the gate battery

| Layer | Before | Now |
|---|---|---|
| `examples/minigate.py` | the ledger — numbers, canon claims, banned values | **unchanged** |
| `tools/camera_gate.py` | — | **the voice — N1, N2, N3, N4, N5, selftested 9/9** |

**Both run. Neither replaces the other.** A chapter can pass the ledger and fail the camera, and that
is exactly what happened on 2026-10-25: a chapter passed five structural gates while reading like the
wrong book.

---

## §8 — The three sentences worth keeping

1. **Narration is a camera: what happened, and what is in the room.**
2. **Register is what the voice does; style is what a sentence is allowed to contain.** Hit the first
   and skip the second, and you have written the wrong book in the right key.
3. **Measure the source, not the shelf.** A law calibrated to your own backlog can only ever give you
   your own backlog back.

---

*Paid for by: a Black Clover serial, three drafts, one day, and an author who had to say "not the story,
the style" before it landed. Receipts: sentence average 17.12 → 8.92, longest 55 → 34, similes in
narration → 0, interiority in narration → 0.*
