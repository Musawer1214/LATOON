# CONCEPT v3 — "Can Machines Think?" (Big Questions) · 2026-10-26 CST

Script: **v3 FINAL** (v3_en.json, 10 sections C0-C9, 52 cards). Picture is timed to the real English voice: dub/voice_en/timings_v3.json
(narration 821.2 s, speech ends 820.06 s; film 841.1 s with the closing hold + silent quote + end frame). Shot list: plan/shots_v3.json
(built by plan/shots_v3.py from these timings).

**Binding rule: PLAYBOOK 5.0b THE GOLDEN RULE** ("Design the theme, the visual, around the content, not content fixed into the theme")
+ 5.0a SHOW, DON'T CHART. Process used for every card below: (1) what an ordinary viewer must SEE to get the idea with the sound off;
(2) only then the world, palette and staging that fit THAT idea; (3) the tool from the existing stack.

**What changed from v1/v2 (2026-10-24 "Section Model"):** v2 put every chapter into one architect's daylight studio of plaster models.
Re-checked against the Golden Rule, that is a house theme forced onto every idea (the owner's own examples ask for a real 1950 room, the
actual Go board, a believable room with slips under the door, a real Othello board with a probe into the network). v3 therefore gives
each section its OWN believable world built for its idea, as separate cinematic shots with calm pacing (reference: Rubin v5). The old
look/ stills and scene.html stay as a material/lighting library only.

## What carries across sections (meaning, not a theme)
- **SIGNAL RED #E03C26 = the machine's output** (its chat replies, its move, its reply slip, its chosen square). **TEAL #0F7A86 = the
  human side** (human replies, human tokens). Same meaning in every world.
- **The paper slip / message** is the film's thread: chat bubble (C0) -> teleprinter tape (C1) -> punched card (C2) -> game record (C3)
  -> slip under the door (C4) -> move tape (C5) -> index card (C6) -> chat transcript (C7) -> poem sheet (C8) -> the viewer's own blank
  card (C9). A section change is a match cut on that object.
- **Outside vs inside:** each section first shows the thing from outside (what we can observe), then tries to look in. The film's last
  image is the one inside we cannot open.
- On-screen text: short language-neutral labels only (names, years, numbers, English terms), small credit/source tags; no captions,
  no tables, no bar charts, no graphs. Numbers appear as physical things (marbles in a jar, a stone among grains) for a moment only.
- Never: blue/navy grounds, neon/cyan glow, glowing brains, humanoid robots, holograms, particle-swarm "AI" clichés, faces on machines.
  People: only real credited photos, or faceless/back-lit figures, hands kept out of close-up.
- Camera: slow dollies, push-ins and crane moves, spring settles; cuts land in the narration's pauses (shot starts sit in the card gaps).
  Nothing faster than ~2 s per move; a held image is allowed to breathe. Visual change every ~6-12 s inside a card (sub-beats).

## Tools (existing stack only)
| Tool | Used for |
|---|---|
| Three.js r170, headless Chromium (stills on sandbox SwiftShader; film on Colab T4 kit, never Kaggle) | the believable 3D worlds: 1950 room, Victorian study, Go/chess/Othello boards, the Chinese Room, card catalogue, rain room, doors |
| GLSL / ModernGL (viz3d-style shader passes) | inside-the-network interior (C5), rain on glass (C8), the search fan of ghost futures (C3-01) |
| Skia (2D) | chat screens and bubbles (C0, C7), labels, credit tags, quote card, chapter/section tags, end frame |
| our 2D engine (camera.py Parallax, guided camera) | real archival photos as full-frame cut-ins with gentle push/parallax (Turing, SSEM replica, Lovelace, Engine, Deep Blue, Lee Sedol, Searle) |
| Manim CE | one beat only: the Go board's possibility count as a calm zoom across the board's 361 points (C3-02) if the Three.js version reads too busy; otherwise not used |
| Remotion | not needed for this film (kept available) |

---

## C0 · Opening: The Five-Minute Test (1.1-66.6 s)
**The idea:** a machine can pass for a person in a chat, and its *style* (a persona) does much of the work; but passing for human is not
the same as thinking.
**World chosen for it:** a real contemporary evening: a laptop on a wooden desk, warm lamp, the room dim around it (it is a chat, so the
viewer must recognise a chat). Then a tabletop with two glass jars (the "votes") — a physical count, not a chart. Palette: lamp amber,
walnut, off-white screen, teal and red bubbles. Tools: Skia chat UI rendered as a texture onto the Three.js laptop screen; Three.js desk/jars.
| Card | What the viewer must SEE (sound off) | Staging |
|---|---|---|
| C0-01 | Two chat windows side by side, A and B, replies arriving in both, equally normal (short bubbles, an emoji, a question). A timer at 5:00 running down. A cursor hovers between A and B: "which one is the person?" | frame 1 already moving: slow push into the laptop screen; bubbles abstract (no readable sentences), labels A / B, timer |
| C0-02 | A theatre half-mask slides over window B (the persona). Marbles drop into a jar marked "human?": the AI's jar fills to 73 of 100. The mask is lifted away and the jar drains to 36. | cut to the jar table; label "GPT-4.5 · 73%" then "36%"; marbles teal/red |
| C0-03 | Window B's style (bubble shapes, slang emoji) glows: the *way of talking* is what people answered to. Then the screen pulls back to show the laptop is just a surface: behind it a closed, unlit box. Mistaking ≠ thinking. | pull back from the screen to the desk; behind the laptop a dark sealed box on the desk |
| C0-04 | Three short glimpses of the journey: a typed 1950 page, one black Go stone landing, a locked door with a slip under it. Three questions as three objects: a mask (imitating), a folded map (understanding), a lit window (experience). | three 3-4 s cuts, each a teaser of a later world; the three objects line up on the desk |

## C1 · First Question: How Do You Test Thinking? (67.9-140.9 s)
**The idea:** "thinking" can't be defined, so Turing swaps it for a test you can observe: a written conversation through a wall.
It judges from the outside; that is its strength and its limit. Viva: a right answer can still be memorised.
**World chosen for it:** a real 1950 British office/lab: green-grey painted walls, linoleum, a teleprinter clacking out paper tape,
tungsten desk lamp, wooden partitions, a Manchester-style machine cabinet glimpsed through a doorway. Warm sepia film grade, soft grain.
Viva: a plain modern exam room in daylight (neutral, placeless). Tools: Three.js rooms; real photos via 2D engine (Turing aged 16, PD;
SSEM replica, CC BY-SA 3.0); Skia for labels.
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C1-01 | A 1950 journal page typed line by line: "Can machines think?" Then a dictionary page for "think" whose definition keeps branching into crossed-out alternatives: no agreed meaning. | credited Turing photo as a framed print on the desk; push onto the page; label "1950 · A. M. Turing" |
| C1-02 | The imitation game: a judge at a teleprinter in one room; a wall; behind it two closed doors A and B. Paper tape goes through a slot in the wall to both. Inside (shown to us, not the judge): a person behind one door, a 1950 machine cabinet behind the other. The judge must guess. | wide of the three-room layout from above, then the judge's side at eye level; red tape = machine, teal = person |
| C1-03 | The judge only ever sees tape coming out of the slot. The wall stays shut: the test is from the OUTSIDE. | camera on the judge's side, the wall fills the frame; label "Turing test" |
| C1-04 | Advantage: two people arguing over a word (two crossed speech marks) give way to a simple observable act (the judge circles A or B). Limit: a perfect human-sounding tape still tells nothing about what's behind the door: the camera tries to pass through the wall and stops. | slow push into the wall that stops at the plaster |
| C1-05 | A viva: examiner and student (faceless, backs/silhouettes) across a table. The first answer card is correct (tick). The next question card: the student's answer turns out to be a page copied from a textbook (the page lifts out of the book and matches the answer word-shape for word-shape). Memorised vs understood. | eye level, daylight exam room; then match cut on the answer card to the judge's tape (same difference) |

## C2 · Second Question: Can a Machine Create Something New? (142.3-216.2 s)
**The idea:** Lovelace: a machine only does what we tell it. Turing: build one that learns from mistakes, and it may do what its
builders did not expect.
**World chosen for it:** an 1840s study: gaslight, brass, mahogany, Jacquard punched cards, Babbage's Engine as a credited photo and as
a working brass mechanism. Then Turing's child-machine as a physical learner: a marble-run of small brass flaps that adjusts after every
failed run. Tools: Three.js (study, mechanism, marble run); 2D engine for Lovelace portrait (PD) and the Engine trial piece (CC BY-SA 2.0).
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C2-01 | Lovelace's portrait (credited); the real Analytical Engine trial piece (credited); the design unfinished: drawings with blank, unbuilt parts. | photo cut-ins with gentle push; label "1843 · Ada Lovelace · Charles Babbage"; drawings on a desk |
| C2-02 | Punched cards go INTO the brass mechanism and the output is exactly the pattern the cards ordered, nothing more (cards in = result out, joined by a red thread). | close on the card reader; the output strip matches the punched holes |
| C2-03 | The child-machine: a marble rolls down a board of little brass flaps, misses the cup, the flaps nudge; again, nearer; again, it lands. Learning from mistakes, no one setting the flaps. | top-down then low angle; 3 tries in one calm move; label "learns" |
| C2-04 | The builder's blueprint on the table shows one intended route; the marble now takes a different, better route the blueprint never drew. | blueprint in the foreground (route in pencil), the marble's path glows red where it differs |
| C2-05 | The marble drops into a cup that becomes a game piece; down the table two very different machines wait: a tall cabinet (counting) and a board (learning). | match cut marble -> stone; dolly to the two boards |

## C3 · Third Question: A Move Nobody Expected (217.6-322.5 s)
**The idea:** Deep Blue won by counting moves fast; AlphaGo learned from games and self-play, and played a move no human expected.
New and winning is still not proof of understanding.
**World chosen for it:** the real games. A tournament chessboard under hard light for 1997; for 2016 a real kaya-wood Go board with slate
and shell stones in a quiet match room, the actual Game 2 position (re-staged from the game record, Commons SVG CC BY-SA 4.0).
Tools: Three.js boards; GLSL for the fan of ghost futures; real photos Deep Blue (CC BY 2.0) and Lee Sedol (CC BY 2.0).
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C3-01 | Deep Blue's cabinet (credited photo). On the chessboard, from one position a vast fan of faint ghost futures branches out, each scored: brute counting. | photo cut-in, then the board with the GLSL fan; label "1997 · Deep Blue · Kasparov" |
| C3-02 | Lee Sedol (credited photo) at the Go board. Over the 19x19 board ghost stones flicker on every point at once, more and more: far too many to count. | match room wide; then top-down board with flickering ghosts; label "2016 · AlphaGo · Lee Sedol" |
| C3-03 | Thousands of faint expert games stream across the board and settle; then the board plays itself, games flashing past faster, ghost stones fading into a sense of good shape. | top-down, time-lapse of translucent stones; label "self-play" |
| C3-04 | The real Game 2 position. One black stone is placed on the fifth line where nobody expects it (Move 37). A pause; the frame holds on that single stone. | slow push to the stone; label "Move 37"; red rim light on the stone (machine's move) |
| C3-05 | The stone among 10,000 grey grains: one in ten thousand. Later in the game, a soft light spreads from the stone to the black group it ends up supporting: its value appears. Scoreline as stones: 4-1. | macro cut to grains; back to board, the glow spreads; label "1 in 10,000 · 4-1" |
| C3-06 | Two ghost stones where human experts would play (teal) vs the machine's stone (red) somewhere else. | top-down hold; teal ghosts vs red stone |
| C3-07 | Lovelace's portrait print laid beside the Go board: her objection weakened, not closed. The stone is new and winning, but the board gives no sign of WHY. | print slides in beside the board; label "new ≠ understood" |

## C4 · Fourth Question: The Chinese Room (323.8-418.9 s) — MUSIC SILENT from "Imagine..." to "That was Searle's question"
**The idea:** following rules for symbols perfectly is not understanding them. Systems Reply; Searle's answer; the gap between a right
answer and inner understanding. Then: are today's AIs just a huge rulebook, or does something else form inside?
**World chosen for it:** a believable small locked room: whitewashed walls, one bare bulb, a desk, a huge rulebook, baskets of paper
slips, a door with a letter slot; outside, a corridor where Chinese speakers post slips and read replies. The man is seen from behind,
faceless. Chinese characters are REAL and correct on the slips (he can't read them; the viewer sees them as he does: shapes).
Tools: Three.js (room, bulb, slips, book); Skia for slip textures (real Chinese text, checked); John Searle credited photo (CC BY-SA 3.0).
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C4-01 | Searle (credited photo). Then: a locked door; inside, a man at a desk under a bulb; the Chinese on a slip shown as he sees it: strange marks. | photo cut-in -> exterior of the door -> inside, over his shoulder; label "1980 · John Searle" |
| C4-02 | A slip slides in under the door. He opens a thick rulebook, matches the marks' shapes to a page, copies the marks shown there onto a new slip. | close on the slip under the door; over-shoulder on the book; red ink for his reply |
| C4-03 | He pushes the reply out. Outside, the reader nods (a second slip comes in): to them, someone in there knows Chinese. | split by the wall: outside satisfied / inside the same blank routine |
| C4-04 | Back inside: nothing about him has changed; his own reply still looks like marks to him. The question as an image: the reply slip (correct) next to his blank face-down notebook (no meaning). | hold on him from behind, bulb swinging slightly; music returns on "That was Searle's question" |
| C4-05 | Systems Reply: camera rises top-down; a chalk circle is drawn around man + book + baskets: "the whole system". Searle's answer: the book's pages fly into the man (memorised), the walls fold away, he stands in an open field answering alone — and the marks still look like marks to him. | top-down crane; labels "Systems Reply", then "memorised" |
| C4-06 | The gap: a correct reply slip on one side, an empty space on the other, a thin line between them. | slow push into the gap between the two |
| C4-07 | The rulebook's pages rise, multiply and blur into a vast lattice of connections (the bridge to the next section): rules, or something else taking shape? | match dissolve book -> lattice (hand off to C5's network interior look) |

## C5 · Fifth Question: A Map Inside the Machine (420.2-519.0 s)
**The idea:** a small model trained only on move lists of Othello builds an internal map of the board, and uses it: flip a square in
that map and its next move changes. Small world, limited, but more than repeating.
**World chosen for it:** a real Othello board (green felt, black/white discs) on a games table; the model as a sealed dark-glass box fed by
a paper tape of move codes; inside it, a warm-lit field of nodes (the network) where an 8x8 board pattern emerges. Palette: felt green,
ink, amber node light (no neon, no cyan). Tools: Three.js (board, box, tape); GLSL/ModernGL for the network interior; composited.
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C5-01 | A real Othello game: a disc placed, a row of discs flips colour; again. The board keeps changing. | close, low angle; label "Othello" |
| C5-02 | The board is covered over; only a paper tape of move codes (F5 · D6 · C3 ...) feeds into a sealed box. Out comes the next legal move. No picture of the board, no rule book enters. | tape into box; label "moves only" |
| C5-03 | The box keeps predicting right. Question as an image: inside the box, either a stack of memorised tape strips, or a board? A light probe hovers at the glass. | push to the glass; two faint possibilities flicker inside |
| C5-04 | A probe goes in: the camera passes through the glass into the network; in the activity an 8x8 grid of glowing cells emerges, matching the real board's discs. | GLSL interior, slow forward dolly; the real board ghosted above to compare |
| C5-05 | Tweezers of light flip ONE cell in that inner map. Out of the box, the next predicted move changes, and it fits the altered board. | macro on the inner cell (red flip); cut to the output slip changing |
| C5-06 | Wide: the inner map lights up as the model chooses: it is USED, not a side effect. Label "learned, not taught". | pull back through the glass to the whole box on the table |
| C5-07 | The Othello board, tiny on the table, in front of a big window onto the real busy world: a small world is not the world. The box still beats the "parrot" picture (a coiled tape of ready-made sentences unspools and falls away). | pull back to the window; label "small world" |

## C6 · Sixth Question: When the Answer Comes, but the Connection Doesn't (520.4-595.4 s)
**The idea:** the Reversal Curse: a model knows "A's mother is B" but often can't answer "B's son is A". A specific 2023 test, not a
permanent limit. So both quick verdicts overreach.
**World chosen for it:** a library card catalogue: a wooden cabinet of index drawers. Knowledge filed ONE way. Warm reading-room light,
oak, brass label holders, typed index cards. Tools: Three.js (cabinet, drawers, cards); Skia for typed card faces.
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C6-01 | A drawer labelled with name A opens: a card inside reads "mother: B". The drawer for B opens: no card pointing back. Same relationship, one direction only. | dolly along the cabinet; label "2023" |
| C6-02 | Labels "Tom Cruise" -> card "mother: Mary Lee Pfeiffer"; drawer "Mary Lee Pfeiffer" -> empty. A person's notebook beside it with a forgotten entry crossed out (people forget too); the machine's gap is systematic: dozens of drawers empty the same way. | close on cards, then wide of many empty drawers |
| C6-03 | Two stacks of found cards: forward drawers yield 79 of 100, reverse 33 of 100 (counted as cards, briefly). A small date tag "GPT-4 · tested 2023". | short hold; labels "Reversal Curse · 79% · 33%"; red/teal cards |
| C6-04 | Both sides: on the left the Othello inner map glowing (C5); on the right the empty reverse drawer. A balance between them stays level. | split staging on one table; slow push to the level balance |

## C7 · Seventh Question: What Does 73 Percent Really Tell Us? (596.7-686.4 s)
**The idea:** the real study behind the opening number: three-way chats, persona instructions (73% vs 36%), 15-minute chats (GPT-5 ~59%),
people judged style not knowledge. It shows convincing imitation, not inner understanding.
**World chosen for it:** back to the opening desk, now as the real experiment: the judge's screen with two chat panes at once, a printed
persona card clipped to the AI side; the jars from C0 return. Daylight now (the study, not the mystery). Tools: Skia chat UI; Three.js desk.
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C7-01 | The judge's screen: two chats at once (human, AI), then the judge's choice button. Source tag "Jones & Bergen · PNAS 2026 (preprint 2025)". | screen-level, calm; label "PNAS 2026" |
| C7-02 | The persona card clipped to the AI side ("shy · young · internet slang"); jar fills to 73; card unclipped, jar 36. The design of the test shown as the card itself. | jar table again; labels "73%" / "36%" |
| C7-03 | A wall clock: 5 minutes becomes 15. The jar for GPT-5 still fills to ~59. | clock hands sweep; label "15 min · GPT-5 · 59%" |
| C7-04 | What the judges looked at: highlights fall on bubble style, flow, a typo, an emoji; a thick encyclopedia on the desk stays closed. A small typo makes a bubble look MORE human. | close on the screen, warm highlights; encyclopedia untouched |
| C7-05 | The AI chat pane, convincing, in front; behind the laptop the dark sealed box from C0 is still closed. Imitation shown, inside unknown. | pull back to the C0 framing (callback) |

## C8 · Eighth Question: Thinking and Feeling (687.7-768.6 s) — MUSIC SILENT through C8-05
**The idea:** solving, using information about the world, and feeling are three different things. A poem about rain isn't feeling rain.
2023 indicator study: no convincing evidence then; not impossible in principle; indicators wouldn't prove it. We can't see anyone's
inner experience directly.
**World chosen for it:** a quiet room at dusk with a big window and real rain on the glass; amber lamp inside, umber shadows (the only
dark section: the one thing we cannot look into). Tools: Three.js room; GLSL rain on glass; Skia for the poem sheet (English lines,
short, not read aloud).
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C8-01 | Three objects on the sill: a solved puzzle (solving), a folded map (information about the world), and a person's silhouette at the window feeling the cool air (experience). Three separate pools of light. | dolly along the sill, one pool at a time |
| C8-02 | A printer/teleprinter types a poem about rain onto a sheet; outside, real rain streams down the glass; the machine sits dry. | close on the sheet; rack focus to the rain |
| C8-03 | A brass panel of small indicator lamps, each lamp tagged by a theory name (short). The nineteen researchers as a row of nineteen chairs/desk lamps around a table. | slow push along the panel; label "2023 · 19 researchers" |
| C8-04 | The lamps stay mostly dark: "no convincing evidence". One lamp flickers on — and the window behind stays shut: lights on a panel are not proof. | hold; one lamp lights; label "indicators ≠ proof" |
| C8-05 | Two people across a table, seen only as lit windows from outside: we never see in. Then the machine: a closed door with light under it. No music. | exterior: two lit windows; then the door; long held frames |

## C9 · Ending: What Evidence Do We Need? (769.9-820.1 s) + close
**The idea:** ask the question more clearly: humanlike conversation (yes, in some tests), an inner map (in limited tasks, evidence),
understanding like us or feeling (no agreement). Don't play down, don't over-claim. Then the viewer's question.
**World chosen for it:** the three objects from C0-04 return as three doors on one calm daylight table: door 1 (conversation) open,
door 2 (inner map) ajar, door 3 (experience) shut. Tools: Three.js; Skia labels, quote card and LATOON end frame.
| Card | What the viewer must SEE | Staging |
|---|---|---|
| C9-01 | Door 1 open (chat bubbles beyond), door 2 ajar (the Othello inner-map glow beyond). | dolly past the doors; labels "conversation · yes (some tests)", "inner map · limited" |
| C9-02 | Door 3 shut, frosted glass neither lit nor dark. A balance on the table settles level: don't play down, don't over-claim. | hold on door 3; the balance settles |
| C9-03 | A blank card and a pencil on the table: the pencil writes, makes a mistake, erases it, writes again (talks, learns, corrects). The camera stops on the shut door: the question is handed to the viewer. | slow push to door 3, then hold |
| CLOSE | ~2 s hold on door 3 (bed only) -> silent quote card ~7 s: "We can only see a short distance ahead, but we can see plenty there that needs to be done." — A. M. Turing, 1950 -> silent LATOON end frame 12 s (Neuron star, L A T O O N, red rule, "Voyaging the Unseen"; lower two-thirds clear for the end screen). | music's natural ending lands on the end frame |

## Real archival images (licences as read on Commons 2026-10-24; re-verify and log in sources.md before the build)
| Use | File | Licence | Credit |
|---|---|---|---|
| C1 Turing (aged 16, captioned so) | Alan_Turing_Aged_16.jpg (look/img/turing16.jpg) | Public domain | possibly Arthur Reginald Chaffin, 1928-29 |
| C1 machine he programmed (replica) | SSEM_Manchester_museum.jpg | CC BY-SA 3.0 | Parrot of Doom |
| C2 Ada Lovelace | Ada_Lovelace_portrait.jpg (look/img/lovelace.jpg) | Public domain | Alfred Edward Chalon, c.1840 |
| C2 Analytical Engine trial piece | Babbages_Analytical_Engine,_1834-1871._(9660574685).jpg (look/img/engine.jpg) | CC BY-SA 2.0 | Science Museum London / SSPL |
| C3 Deep Blue | Deep_Blue.jpg | CC BY 2.0 | James the photographer |
| C3 Lee Sedol | Lee_Se-Dol_-_2016_(cropped).jpg | CC BY 2.0 | LG Electronics |
| C3 Game 2 record (reference for the re-staged board) | Lee_Sedol_(W)_vs_AlphaGo_(B)_-_Game_2.svg | CC BY-SA 4.0 | Wesalius |
| C4 John Searle | John_searle2.jpg (look/img/searle.jpg) | CC BY-SA 3.0 | Matthew Breindel, 2005 |
Music credit (EN/UR/PS descriptions): music/LICENSE.md (Cylinder Five, Chris Zabriskie, CC BY 4.0).

## Test stills (2026-10-26) — look/v3_stills/
Rendered with look/v3/scene_v3.html (Three.js, headless Chromium SwiftShader, 1920x1080, warm-up frame discarded): see VISUAL_PLAN /
NEXT_STEPS for what each proves and what to fix.
| Still | Shot | Proves | Fix in the build |
|---|---|---|---|
| imit.png | C1-02a | the 1950 cut-away rooms read at a glance: judge, wall with slots, A = valve cabinet, B = person; red/teal tapes | figures are crude capsules; turn the cabinet's dials toward camera; add teleprinter detail |
| move37.png | C3-04a | a real-feeling kaya board + stones carries Move 37 without graphics | position illustrative (use the real Game 2 record); label must sit by the red stone; board over-lit, lower the key and add depth of field |
| slip.png | C4-02a | the Chinese Room as a believable room: slip of real Chinese under a lit door gap | add the man's desk/chair edge for scale; keep the low warm spill |
| map.png | C5-05a | "a map inside" + one flipped square, without a chart | cells read like a starry sky: make them network activity (GLSL), shorter probe, label off the white disc |
