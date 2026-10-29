# 13 · Working from a checked source — the six errors

**The situation.** A serial adapts a manga chapter into a two-chapter opening. The author fetches the source
pages. The chapters are written. Every prose gate passes. The author reads them and says:

> *"I think you should check everything, I can't tell you every mistakes one by one."*

They were right. Six canon errors were in the two chapters, and **every one of them was a detail I remembered
instead of a detail I had fetched** — in a session where the source had been fetched, quoted and filed.

⭐ **That is the whole lesson: checking is an event, and writing is a different day.** Y1–Y7 exist because
"we already looked it up" is not a state. It is a memory, and memory is the thing that fails.

---

## The six errors

| # | What was written | What the source says | Found by |
|---|---|---|---|
| 1 | the grimoire came **"up the road"** | manga: **out of a hole in the tower wall** · anime: **out of the sky** | the author |
| 2 | a boy **complaining about a book he cannot read** at the tower steps | **the ceremony awards him nothing.** His book arrives hours later, mid-fight | the author |
| 3 | the thief served **"eight years in the Magic Knights"** | **thirty-two years old; a former first-class junior of a named squad**, discharged after being set up to fail | the gate |
| 4 | the thief with **no scar and no book** | **a burn down the left side of his face; a three-leaf grimoire in a pouch on his thigh** — his chains come out of the book | the gate |
| 5 | a minor noble casting **a spell that does not exist** | **no such spell in any book** | the gate |
| 6 | a canon lead casting **a spell canon never gives him at that moment** | **he is on the floor before he finishes casting** | the gate |

**Two by the author, four by a machine that did not exist an hour earlier.** That ratio is the argument for
the Y-series: the human catches the ones that *feel* wrong, the gate catches the ones that *read fine*.

⭐ **Error 1 is the dangerous class.** Manga and anime disagree. The fix is never to split the difference —
**an averaged detail exists in neither source and cannot be checked against anything.** An existing register
ruling decides which source governs, and the losing detail is logged as a deliberate divergence.

---

## The method that replaces "I checked it"

### 1. Two registries, written before the chapter

```
canon/facts.json    {"facts":  [{"id":"C001","topic":"…","statement":"…","source":"…"}]}
canon/spells.json   {"spells": [{"name":"…","attribute":"…","owner":"…","source":"…"}]}
```

⭐ **A canon detail enters the registry before it enters the prose.** The registry is the only place a fact is
allowed to live in a form the writer can quote, and *source* is a required field — a page, an episode, or the
words `OC — not canon`.

### 2. Every canon beat in a chapter cites its id

```
- **CLAIM (C043):** "not one of them came down" — the ceremony awarded him nothing
```

The quote must be **the line actually in the chapter**. This is the part that stops the registry becoming
decoration: a claim that cites an id the registry does not contain, or quotes a line the chapter does not
contain, is a hard fail.

### 3. The gate runs on the chapter, not on the intent

```
python3 tools/claim_gate.py chapters/*.md
```

| Check | It refuses |
|---|---|
| **C1** spell registry | a shouted spell that does not exist, **and a real spell in the wrong mouth** |
| **C2** claim trace | a claim citing a missing fact, or quoting a line that is not in the chapter |
| **C3** number trace | (note only) a number hung on a canon character inside no claimed sentence |

**Selftest 5/5** — including a case proving a *correct* chapter passes, because a gate that fails everything
is as useless as one that fails nothing.

⭐ **C1 earned its keep on its first run against a real serial — and the error was in the registry, not the
prose.** A spell was filed under the wrong owner; the chapter had it right. **Registries rot too, and a gate
that reads the registry is also a gate on the registry.**

---

## The distinction that made the whole thing visible

While pinning C1 down, the serial hit a question worth writing down: **what is a spell, and what is a
technique?**

| | **Spell** | **Technique** |
|---|---|---|
| What it is | a formula **inscribed in a grimoire** | what a body and its mana can do |
| Where it comes from | the book gives it when the person changes | you train it; nobody hands it to you |
| How it is invoked | the name is said and **the book answers** | nothing answers |
| Example | `CHAIN MAGIC: MAGIC BINDING IRON CHAIN FORMATION!` | swordsmanship, footwork, mana control |

**Why it matters to a gate:** the two are written differently, so a chapter can contradict its own world by
punctuation. A character with no book shouting `ICE MAGIC: WHITE GARDEN!` is claiming a page he does not have.

⭐ **And it produces a scene for free.** The OC with an empty book and an enormous technique is told, by the
man beating him: *"That is not a spell. There is no book in your hand."* The distinction became dialogue
instead of a footnote.

---

## The two failures that no gate can catch — only a rule can

### Nobody narrates what the scene can see

> *"…That was a spell," he says, upside down, to nobody.*

The reader watched the wall go up. **He is talking to the reader.** Cut, and give the reaction to the man who
would actually have it:

> **"A wall," he says. "You made a wall."**

⭐ **Placement beats silence.** The fix for a narrator is not deleting the line — it is giving it to the
character who is surprised, angry or afraid of what just happened.

### The OC stands in the scene and changes nothing

A chapter had the original character arrive half-way through a canon fight, take a beating, and alter the
outcome not at all. He was **furniture**. ⭐ **Being hurt is not participation.**

The test is one sentence long: **what is different about this scene because he was in it?** If the answer is
"nothing", he is not in the scene — he is standing next to it, and the reader can tell.

---

## What "checked" looks like as a workflow

```
1  FETCH        the page or the episode. Not the memory of either.
2  REGISTER     every fact and spell as a row, with a source. No row, no prose.
3  RULE         if two sources differ, the existing ruling decides. Never average.
4  WRITE        the chapter, spending only registered details.
5  CITE         one CLAIM row per canon beat, quoting the line it paid for.
6  GATE         claim_gate (canon) + camera_gate (voice) + the prose checks.
7  LOG          every deliberate divergence, with what it changed.
```

**Step 3 is the one everybody skips**, and it is the one that produced a location which does not exist in any
version of the story.
