# SAMPLE Short — "Why Can't AI Just Say 'I Don't Know'?" (2026-10-20)

**For the owner's review only. Not uploaded, Studio untouched.**
Final: `AI_I_Dont_Know_sample.mp4` · contact sheet: `contact.jpg` (28 frames) · soft captions: `subs_en.srt`
Script: `script.md` (as voiced) · sources: `sources.md` · QA: `QA.md` · voice pace: `voice/pace.md`

## Concept (Visual System v3, Clay World mode)
One continuous clay world on a warm paper floor. One hero slab transforms through the whole story; the camera travels, never cuts.
| Time | Beat | What happens |
|---|---|---|
| 0-5.5 s | Question | A clay answer card stands up (already moving on frame 1). A brass tick pops: "CONFIDENT". On "wrong" the card winds up and flips to an oxblood X: "…WRONG?" |
| 5.5-11.2 | Evidence | The card tips onto the floor and spreads into an exam sheet; answer bubbles pop in row by row. Chips "OpenAI · 2025", "Kalai et al."; "GRADING" with a red rule. |
| 11.2-17.9 | Exam | Two rows sink away, two stay. A graphite ball drops into a bubble ("GUESS") and a brass tick springs up "+1"; the blank row ("BLANK") gets a clay "0". |
| 17.9-21 | Thesis | Camera orbits; the guess's tick rises on a brass podium: "GUESSING WINS". |
| 21-36 | Scoreboard | The sheet folds into a plinth; two clay towers grow segment by segment as the numbers are spoken: gpt-5-thinking-mini 52 / 22 / 26, OpenAI o4-mini 1 / 24 / 75 (DON'T KNOW / RIGHT / WRONG legend). Near-silence, then the 75 % slab rises on "seventy-five". Source line "SimpleQA · GPT-5 system card". |
| 36-43.4 | Birthday | The towers burst into 365 clay day-tiles that click onto a board; one tile turns brass and lifts: "1 IN 365". A clay "?" appears: "DON'T KNOW" "= 0". |
| 43.4-52.3 | Fix | Tiles sink; a clay balance rises. The X sits on the left pan, a dark PENALTY weight drops and the beam falls ("CONFIDENT ERROR"); the "?" rides to the right pan and gets a brass tick ("CREDIT"). |
| 52.3-57.2 | Takeaway | The plinth becomes the card again, now a source document: lines draw, a brass seal pops ("SOURCE?"), a brass tick stamps on ("CHECK IT"). Mirrors the opening: the tick is now earned. |
| 57.05-59.5 | End card | Dissolve to the engine end card (Neuron star, L A T O O N, red rule, "Voyaging the Unseen"); last 0.6 s dissolves into frame 1 (loop). Nothing spoken. |
"Data: OpenAI, Kalai et al. (2025)" sits bottom-right from 7 s to 52 s.

## Tools
- Picture: Three.js r170 in headless Chromium (SwiftShader, CPU), frame-by-frame capture (`three/scene.html`, `three/cap.js`, `three/render.sh`), MeshStandard clay with bump noise, brass metal, VSM soft shadows, RoomEnvironment reflections, Neutral tone mapping, 2D canvas overlay for type/UI chips, cycling grain + vignette. Springs (closed-form), anticipation on the flip, staggered pops, eased camera keyframes. 1740 frames in 12 chunks, ~1.5-3 s/frame.
- End card: engine `end_card()` + `loop_blend()` (`endcard.py`). Watermark: engine apply_watermark logic (local copy `wm_local.py`, see flaws), corners TL/TR, 22 %.
- Voice: Gemini prebuilt "Iapetus", gemini-3.1-flash-tts-preview, via Colab (session "google-aistudio"), 2 requests total. Edited with `voice/edit_vo.py` (cuts only inside real silences, no time-stretch).
- Music + SFX: original score synthesised in code (`audio.py` on `pfaudio.py`): 96 BPM, F major / D minor, soft marimba + plucks + warm pad + upright, changes at every beat, woodblock "clock" under the calendar, near-silence before 26 %, 75 %, 1-in-365, the penalty and the check; ~110 SFX on events (synth whooshes/thuds/ticks/ratchets/pencil + engine/sound/sfx UI pops, ticks, chime, stamp). Music ducked 7 dB under voice, SFX 3 dB. Mix -14 LUFS.
- QA: engine/qa.py (`QA.md`), overlay layout log (`qa_layout.json` from `three/layout.js`) for safe zones/overlaps, WCAG contrast table, contact sheet.

## Voice status (owner pace rule 2026-10-20)
- Take 1 (139-word script, plain request): 54.8 s but 178 wpm while speaking, several sentences 200-240 wpm. **Rejected** (too fast).
- Take 2 (132-word script; calm documentary-narrator direction given before the script, not spoken — confirmed by ASR): calm, ~154 wpm articulation, matching the long-video narrator feel. But it ran 67.5 s, so two whole sentences were removed at real silences to stay under 60 s: "Most AI tests score the same way." and "Rare facts, like a birthday, can't be learned from patterns." Pauses tightened to 0.4-0.9 s; the existing pause before "75 percent" lengthened to ~0.6 s with room tone.
- Final voice: 115 words, 0.25-57.06 s. Articulation 154 wpm (hard max 160 ✓), ~135 wpm across sentence spans, ~122 wpm overall incl. pauses (below the 140-150 target overall because of the natural pauses). No speed-up anywhere.

## Known flaws (honest)
1. The birthday line now starts "A guess has a one in 365 chance" without the spoken setup (the "rare facts" sentence was cut for length); the "BIRTHDAY?" headline carries the context visually. A shorter re-voice in the next quota window would fix it properly.
2. "So guessing beats I don't know" follows the exam directly (the "Most AI tests score the same way" bridge was cut); "GRADING" + "OpenAI" chips carry the link.
3. Overall pace incl. pauses is ~122 wpm (target 140-150) — calm rather than brisk; articulation 154 wpm.
4. Runtime 59.5 s (owner's 55-60 OK; above the 45-55 house target). The end card is fully built only ~0.3 s before it starts dissolving into the loop (visible ~1.9 s in total).
5. Empty-ish moments: ~21.1-22.4 s (plinth, legend chips appearing, before the first tower) and ~52.6-53.4 s (scale gone, card still flat).
6. The tower-to-tiles burst (36.0-37.2 s) is busy for ~1 s and briefly reads like confetti.
7. Some cue times come from ASR word timings that drift after long pauses; key ones (75 %, sentence starts) were checked against the waveform and corrected; minor visual-to-word offsets of ~0.2-0.4 s remain (e.g. the 26 % segment rises on "wrong", just before "twenty-six").
8. engine/apply_watermark.py fails with this ffprobe (it prints a trailing comma after width,height). I used a local copy with a one-line parse fix (`wm_local.py`) and did not edit the engine; the engine file needs that fix.
9. English only: no UR/PS tracks or SRTs (sample).

## FINAL / PUBLISHED (2026-10-20 20:45 CST)
- YouTube: https://youtube.com/shorts/bQ5CmhfKfX0 (ID bQ5CmhfKfX0), SCHEDULED Public 2026-10-20 20:00 PKT. Playlist Shorts; related J4bsx3OhGso; EN SRT uploaded; metadata in metadata.txt.
- Final fix: model-name labels (gpt-5-thinking-mini / OpenAI o4-mini) drawn as cream chips below the plinth (contrast 14.3/14.4:1). Segments f0580-f1015 re-rendered (old in three/segs/old_label/), qa_layout.json 21.5-36.5 s regenerated.
- Final QA: 0 FAIL / 1 WARN (EN-only SRT); contrast 0 below target; -14.2 LUFS, -3.7 dBTP; 59.53 s. Upload copy AI_I_Dont_Know_upload.mp4 (8.0 MB). Flaws 1-7 above still stand (end-card hold unchanged); flaw 8 fixed in the engine.
