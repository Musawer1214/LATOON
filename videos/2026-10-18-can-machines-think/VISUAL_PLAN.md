# VISUAL PLAN — "Can Machines Think?" (Big Questions) · v1 2026-10-24

World, palette, symbols and tools: CONCEPT.md ("The Section Model": architect's daylight studio, plaster/card/oak/brass models cut in
section; OUTSIDE vs INSIDE). This file = how the film is staged, timed and rendered.

> **STATUS OF THIS PLAN (owner workflow change, 2026-10-24 22:04 CST):** the owner will read the Urdu v2 aloud and send a voice
> recording with revisions, new dialogue and updates; the final Urdu, then English and Pashto, are written from that. So the script
> WILL change. **Firm:** concept, world, palette, models, symbols, tools, chapter-level plan (s2), ending (s3), render pipeline (s5).
> **Provisional:** the per-line shotlist and every time in plan/shotlist.md (v2 line ids). After the new lines.py: re-map shots in
> plan/shots.py, run `python3 plan/make_shotlist.py`, then re-time everything to the real English voice (picture follows voice).
> No TTS is spent before the owner confirms the final script.

## 1. Pace and length (measured, not guessed)
- Narrator pace for planning: **140 wpm** (Iapetus narrator median 140.8 wpm, range 127-156, from The Archive's 11 locked EN narrator
  lines, dub/voice/en/timings_LOCKED_2026-10-23.json). build_script.py's 155 wpm was optimistic.
- Script v2 at 140 wpm + its own pauses + 3 s title + 8 x 2.5 s chapter cards: **speech ends ~19:34; with the closing hold, silent quote
  and 12 s end frame, total ~19:55.** At 155 wpm it was ~17:43. Either is above the 10-12 min target ("up to ~15 only if the story
  needs it", PLAYBOOK 2.3). This is the owner's call in his read-through (decision 2 in NEXT_STEPS.md); the cut list there still applies.
- Never speed the voice to fit (s4.6/CONTENT_STANDARD 6b): cut whole beats instead.

## 2. Chapter plan (firm)
| Ch | Models on the table | Camera journey | Key visual beats | Real images | Prompt |
|---|---|---|---|---|---|
| C0 Cold open (~1:35) | ROOM PAIR, TABLE OF PAIRS, STUDY DESK, LONG TABLE | moving in frame 1; push -> log pull-back -> match cut -> crane over the long table | two slots giving alike replies; token heaps (73%); Mind 1950 page; the whole table of chapters; TITLE | Turing (aged 16, PD) | |
| C1 The question he refused (~2:55) | BALLOT BOX, IMITATION GAME section, VIVA | outside the game room -> rise over the section cut -> eye level at the viva | struck ballot box; person lifted out of A, brass machine in; 7 of 10 judges; spotlight onto the people; parrot on the shoulder | Manchester computer replica (CC BY-SA) | viva (C1-07): empty chair |
| C2 Lovelace (~2:05) | ENGINE, STUDY DESK, NOTEBOOK | follow a punched card through the engine; top-down on the notebook | cards in = cards out (red thread); a model that surprises; notebook filling itself | Lovelace (PD), Engine trial piece (CC BY-SA 2.0) | |
| C3 Move 37 (~2:00) | CHESS, GO BOARD | orbit the chess fan; push to the one stone | ghost futures fan (brute force); ghost games stream in; Move 37 lands, figures turn | Deep Blue (CC BY 2.0), Lee Sedol (CC BY 2.0) | |
| C4 The Room (~3:15) | CHINESE ROOM, RAIN, FIRE | outside first -> section cut -> top-down for the Systems Reply | notes under the door; rulebook; syntax ✓ meaning ✗; chalk ring; pages fly into the man; rain/fire simulation | Searle (CC BY-SA 3.0) | who understands? (C4-07): three spotlights |
| C5 A board inside (~3:45) | DIALS, SEALED BOX, TURNSTILE, BALANCE | through the dissolving book -> outside the sealed box -> probes go in -> macro on tweezers | brass-dial wall; inner board of light; ONE disc flipped changes the move; one-way turnstile 79/33; parrot vs map on a balance | none | where would you draw the line? (C5-08): blank chalk line |
| C6 The test is passed (~3:25) | TABLE OF PAIRS (return), COIN, SLIPS, QUOTE CARD, PARCELS | back to the opening table, now labelled | half-mask = persona; five token heaps; 15-min timer; spinning coin; chit-chat pile vs 12%; Ghalib card; wrapped parcel | none (studies re-staged with source tags) | |
| C7 Thinking is not feeling (~3:30) | MODEL TOWN (dusk), CHECK-WALL, SUBSTRATE | the light turns to dusk; street level; along the plate wall; orbit | lit windows "polite convention"; unlit indicator plates; one pattern in clay/silicon/brass; Turing desk vs Searle room face to face | none | |
| C8 What would change your mind? (~1:45) + close | THREE DOORS, LONG TABLE | back to daylight; dolly past the doors; rise over the fading streets | door 1 open, 2 ajar, 3 shut; streets fading into haze | none | what would change your mind? (C8-05): the shut door |
Chapter cards: 2.5 s each, a printed card lying on the table (still s9 style), silent (bed + one soft UI pop). Title card 3 s after C0-05.

Re-hooks grow from the story at each chapter end (script lines C1-08, C2-06, C3-05, C4-09, C5-08, C6-08, C7-07), every ~2-3 min.
Beats: 54 B-beats in the provisional list, median gap ~22 s; the five spans over 40 s (C1-03->C1-05, C1-06->C1-08, C2-01->C2-04,
C7-03->C7-06, C8-01->C8-04) and lines over 25 s (C5-07, C5-08, C6-03, C6-06, C7-02) get a mid-line sub-beat (a second model action or a
camera reveal) in the build so nothing holds longer than ~30 s.

## 3. Closing beat and end frame (owner endings rule 2026-10-24; firm)
No spoken channel line, nothing spoken after the story. Last spoken words: C8-05 (the viewer question) in v2.
1. CLOSE-hold ~2 s: the shut third door, bed only.
2. CLOSE-quote ~7 s, SILENT: card with Turing's exact last sentence "We can only see a short distance ahead, but we can see plenty there
   that needs to be done." — A. M. Turing, 1950 (FACTCHECK T12), Cormorant on paper, red rule. (C8-04 speaks a paraphrase of it; if the
   owner moves C8-04 to the end in his read-through, the card follows his line directly.)
3. END ~12 s, SILENT: LATOON end frame (Neuron star, L A T O O N, red rule + dot, "Voyaging the Unseen"), brand block above y 360, lower
   two-thirds clear for the Studio end screen (Subscribe + next video), bed fades out, last 0.5 s fade.

## 4. Look stills (real pipeline) — look/
Rendered with look/scene.html (Three.js r170) in headless Chromium SwiftShader at 1920x1080 via look/cap.js (two renders per shot, first
discarded = capture warm-up, PLAYBOOK 7.4b). Contact sheet: **look/contact_sheet.jpg** (s1-s8); chapter card s9 in look/stills/s9.png;
first pass kept as look/contact_v1.jpg + contact_v1b.jpg, scene_v1.html.
| Still | Shot | Proves |
|---|---|---|
| s1 | C0-03 table of room pairs, token heaps, 73% | the cold-open picture works without words |
| s2 | C1-03 imitation game in section | the section-cut grammar (outside walls, poché caps, inside visible) |
| s3 | C2-02 cards in = cards out + credited prints | how real archival photos sit in the world (mounted prints) |
| s4 | C3-03 Move 37 | the one-stone moment, scale figures as the audience |
| s5 | C4-02 Chinese Room | the hero model: notes under the door, rulebook, outside reader |
| s6 | C5-05 sealed box, inner board, tweezers | "a map inside" without a chart |
| s7 | C7-02 dusk town, lit windows | the deliberate turn to dusk for the inner-life chapter |
| s8 | C8-03 three doors | the honest ending as an image |
| s9 | chapter card | type system on the table |
Fixed after looking at v1: table was saturated orange (toy-like) -> pale ash/birch, calmer and on the Map Warm family; brass read as flat
brown -> lower metalness, warmer brass; engine base was a dark brown block -> plaster with a brass rail; 73% label sat on the models -> its
own paper panel + "AI / person" tags; imitation-game rooms were split the wrong way (A and B in one room) -> rebuilt with A behind B, the
judge separate, labels "C judge / A machine / B person"; Chinese-room labels covered the wall -> moved under the title; rulebook was a flat
slip -> a thick book with a red spine; Othello inner board read as wooden planks -> sage board on a lamp-lit base; the lifted disc was
TEAL (teal = human in this film) -> red; source tags got a soft paper panel; chapter-card stray figure removed.
Still weak (fix in the build, not blocking the look decision): s2 the brass machine in room A is small and half hidden (raise camera or
lower walls of A); s7 the brass machine and its sonnet sheet are too small to read (needs its own close shot); s8 the frosted window over
door 3 reads as a plaque and the figures are stiff; s6 tweezers look like chopsticks (thinner, angled); scale figures are simple capsules
(fine as architect's figures; add a slight taper/shoulders). The Go position is illustrative: the build re-stages the real Game 2
record (Commons SVG, CC BY-SA 4.0) so Move 37 sits on its real point.

## 5. Render pipeline (firm; NO Kaggle)
- One Three.js page per chapter set (look/scene.html is the seed: shared studio, materials, figure, section wall, overlay type), every
  value a pure function of t (as sample3d/scene_film.html), driven by a film.json exported from the FINAL voice timings.
- Stills and checks on the sandbox (SwiftShader). Final film on **Colab T4** with The Archive's kit (sample3d/colab_setup.sh, t2.sh,
  colab_render.sh, colab_ship.sh; GL flags in Drive gl.env: --use-angle=vulkan ...; chunks resumable in Drive; ship via litterbox;
  sandbox fetch_colab_chunks.sh). Measured there ~0.2 s/frame -> ~36,000 frames (~20 min) ≈ 2 h GPU.
- Chunked-render lessons (PLAYBOOK 7.4b), all mandatory:
  1. capture warm-up: discard screenshots until a real frame appears (cap_film.js warm-up block: two consecutive >80 KB JPEGs); never
     record the first frame of a page load;
  2. every chunk encoded with the SAME pix_fmt and colour range: yuv420p, limited (tv), BT.709 tagged (`-pix_fmt yuv420p -color_range tv
     -colorspace bt709 -color_primaries bt709 -color_trc bt709`); check each chunk with ffprobe before the stream-copy concat;
  3. after concat, scan every frame's YAVG (signalstats) and flag any flat-black run between non-black frames; only designed fades stay;
  4. encode/faststart in /tmp, then copy to /workspace (JuiceFS trailer error).
- Overlays (labels, source tags, quote/chapter cards) drawn on the page's overlay canvas so they ride in the same frames (no separate
  composite pass), watermark via engine/apply_watermark.py, sound: bed + UI/motion SFX timed to on-screen events + voice (PLAYBOOK 4.8).
- Language-neutral picture: no burned narration captions; UR/PS are audio tracks + SRTs only (one render serves all three channels).
