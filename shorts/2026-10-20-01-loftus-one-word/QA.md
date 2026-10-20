# QA (PLAYBOOK s11)
<!-- qa.py writes its automated section between the AUTO markers; the manual checks stay yours. -->
<!-- AUTO-QA START -->
### Automated checks (qa.py, Loftus_One_Word_Memory_LATOON_short.mp4): 0 FAIL, 3 WARN

| | Check | Result |
|---|---|---|
| PASS | resolution | 1080x1920 at 30.00 fps (expected 1080x1920) |
| PASS | streams | 1 video, 1 audio (h264, aac) |
| PASS | duration | 57.03 s (Shorts must be under 60 s; 38-55 s works best) |
| WARN | size | 124.1 MB master; upload the ~6 MB re-encode (s15: libx264 preset slow CRF 23, AAC 160k) |
| PASS | loudness[mp4] | -14.1 LUFS, -1.8 dBTP (target -14 / -1) |
| PASS | silence[mp4] | no gaps |
| PASS | loudness[en] | -14.1 LUFS, -1.9 dBTP (target -14 / -1) |
| PASS | silence[en] | no gaps |
| PASS | srt[en] | 15 cues, 100% of speech covered |
| WARN | srt | 1 SRT file(s); Shorts ship EN/UR/PS SRTs |
| PASS | text overflow | none |
| PASS | safe zones | ok |
| PASS | watermark corners | clear |
| PASS | text overlap | none |
| PASS | no narration captions | on-screen text is labels only |
| PASS | label length | all labels 1-3 words |
| PASS | hook motion | mean frame change 2.69 over the first 0.1 s (frame 1 must already move) |
| PASS | hook keyword | big number/keyword by 2 s: 'SAME CRASH' |
| PASS | loop seam | last vs first frame difference 2.6 (lower = smoother loop) |
| WARN | palette | 35.6s 0.3% |
| PASS | credits | 3 image/clip files used, all in sources.md |
| PASS | contact sheet | 3 full-res page(s) + overview in qa/ - review them before export |
<!-- AUTO-QA END -->
## Manual
1. Facts: every spoken and on-screen claim checked against the dossier.
2. Frames: full-res contact sheet reviewed; watermark positions checked.
3. Audio per language: Iapetus natural, names right, bed under the voice.
4. Captions: SRT timing per language (auto check above) + spot check in Studio.
5. Metadata.

## Manual QA (2026-10-20 daily Short run)
- Facts (s7.3): every spoken and on-screen number checked against Loftus & Palmer 1974 (original scan): 1974; 45 students, 7 films; 40.8 / 34.0 mph (Table 1; the course copy's OCR "40.5" is wrong); staged crashes 20/30/40/40 vs 37.7/36.2/39.7/36.1; test 2: 150 students, one week, 16/50, 7/50, 6/50 (Table 2); "one memory" (p. 588). km/h conversions 65.7 / 54.7 -> "≈ 66 / ≈ 55". No overclaim (spoken: "16 of 50", not "everyone").
- Voice (s4.6): voice_qa.md. ONE request (gemini-2.5-flash-preview-tts, Iapetus). ASR matches script word for word; 7 splits inside 0.52-0.82 s pauses: PASS; lines 4/5/7 gently slowed 0.93/0.93/0.95 (raw 189/188/184 wpm); overall ~160 wpm. Closing line not spoken; end card on screen ~1.7 s then loop dissolve.
- Sound (s4.8 update 2026-10-20): three layers (Short bed, 45 UI/motion SFX cues each on an on-screen event, voice). SFX measured 29-46 dB under the voice (rms per cue), ducked under speech; bigger swooshes (swoosh_fast, sweep_air, swoosh_short) only at scene changes in voice gaps; no risers/impacts. Mix -14.1 LUFS, -1.8 dBTP.
- Frames (s7.4, LOOK.md): Map Warm paper ground throughout; foreground SIGNAL RED/OXBLOOD (smashed), TEAL/DEEP TEAL (hit), INK2 (no question), OCHRE/WALNUT (guesses), BRASS2 cars; no blue ground, no glow, no AI look. Guided camera in scene 2 (verb canvas), gentle pushes in scenes 5-6; Manim 3D beat (m3d/crashtrack.py, House3D warm shading, INK2 silhouette + contact shadow) in scene 3; engraved locator map inset (Natural Earth) in scene 1; 4 credited real sources (Prelinger staged-crash film, Loftus photo, crash-test car, broken windscreen). Spot frames checked by eye: no typos, labels correct, car pictograms clean.
- qa.py: 0 FAIL, 5 WARN, all reviewed: size (upload uses the encode); 1 SRT (EN first; UR/PS later per s11.9); watermark corner '40.8' in scene 2 -> watermark run with --avoid bl:16.1-23.6; text overlap = headline cross-fades at scene changes; palette 0.3% at 35.6 s = broken-windscreen photo.
- contrast_check.py: 5 items flagged, all sampled mid-transition (23.5, 49.5 = scene boundaries; 16.23 counter fade-in; 7.0 scene fade-out). Steady-state re-measured on the frames: NEVER THERE stamp on SNOW slip 6.5:1, '≈ 55 km/h' 7.2:1, ONE MEMORY 17.7:1; all PASS.
- No burned narration captions (owner reminder 2026-10-20): labels only (qa.py PASS). Soft EN SRT: subs_en.srt (15 cues, 100% speech).
- Hook: frame 1 moving (staged crash film), "SAME CRASH" readable < 2 s, loop seam 2.6.

## Visual upgrade re-render (2026-10-20 ~05:50 CST, recovery run after the previous worker crashed)
- Changes: (1) scene 0->1 cut: template "rise" left ~0.5 s of blank paper + faded/white "1 WORD" chip (fout used D without HOOK_PRE); TRANS[1] now "page", hook content holds to the cut, 1 WORD chip larger (size 50). (2) scene 1 opens on a big engraved Natural Earth map of the US, Seattle pin pulse, zoom into Seattle (US map crossfades into a Puget Sound close-up), card shrinks to an inset beside the names (fixes ~2.5 s of near-empty frame). (3) TWO SOURCES scene rebuilt: SAW card (the staged-crash film frame, eye + SEEN) and TOLD card (speech card "SMASHED?" + TOLD) from the first frame; guided camera pushes to each on "saw"/"told"; on "blend" both fly into one memory print that gains broken-glass cracks; red/teal braid + ONE MEMORY; ends on identity framing = scene 7's opening print (match cut, payoff opens already cracked). (4) No "rise" cuts left (5 -> page, 6 -> mask). (5) Headlines start at t0 0.22 so two scenes' headlines never overlap inside a transition. (6) Camera/labels nudged so 40.8, 16/50, KNOWN SPEED stay clear of the bottom-left watermark corner. SFX cues re-timed/added for the map pulses, zoom, shrink, card landings, merge and cracks (three layers kept).
- qa.py: 0 FAIL, 3 WARN (master size -> upload encode; 1 SRT = EN first; palette 0.3% at 35.6 s = broken-windscreen photo). Text overlap and watermark-corner warnings are gone.
- contrast_check.py: 6 items flagged, all sampled exactly at scene boundaries mid-transition (7.5, 16.23, 23.5, 37.0, 49.5); every steady-state sample of the same labels PASSes (e.g. ONE MEMORY 17+:1 class, SEATTLE 17.7:1, SMASHED? 16.8:1).
- Frames viewed by eye (preview sheets for 0-57 s + watermarked frames at 9.0 / 48.9 s): no typos, no clipped text, watermark present, end card intact.
- Files: master Loftus_One_Word_Memory_LATOON_short.mp4 (124 MB), final_wm.mp4, upload encode Loftus_One_Word_Memory_LATOON_short_upload.mp4 = /workspace/work/upload/loftus_one_word_short.mp4 (6.1 MB, CRF 26 medium, 57.03 s). v1 code kept as scenes_v1_backup.py. Audio/voice unchanged (no new TTS).
- HELD (owner 2026-10-20 ~05:46 CST: visuals "don't look premium"; publish delayed for an upgraded pilot). Not uploaded, not scheduled.

## v3 rebuild - VISUAL SYSTEM v3, Thread mode (2026-10-20 ~09:10 CST)
File: v3/Loftus_One_Word_v3.mp4 (1080x1920 30 fps, 57.03 s, 27.6 MB, H.264 High CRF 21 maxrate 3.8M + AAC 192k 48 kHz, faststart). Upload-size copy v3/Loftus_One_Word_v3_upload.mp4 (7.7 MB, -14.1 LUFS / -3.2 dBTP). Contact sheet v3/contact.jpg; qa.py full-res pages v3/qa/.
- qa.py (`engine/qa.py v3/Loftus_One_Word_v3.mp4 --build v3 --fmt short --langs en`, full table in v3/QA.md): **0 FAIL, 3 WARN**, all expected: (1) only the EN SRT (UR/PS wait for the owner's voice, s6.2); (2) no layout log because v3 is not an engine render.py build, so safe zones/overlaps were checked by eye on every contact frame; (3) "hook keyword not logged" for the same reason: "SAME CRASH." is fully on screen by ~0.4 s (frame checked). PASS: resolution, streams, duration, loudness -14.1 LUFS / -3.1 dBTP (mp4) and -14.1 / -3.4 (mix_en.wav), no silence gaps, SRT 21 cues 99% speech, labels only (no narration captions), labels 1-3 words, hook motion in frame 1, loop seam 1.4, palette (no neon/blue-purple), credits (0 third-party images).
- Facts (s7.3) vs ../sources.md (Loftus & Palmer 1974, original scan + course copy): 1974; names; 45 STUDENTS, 7 FILMS (Exp. 1); verb SMASHED 40.8 / HIT 34.0 mph (Table 1; spoken "about 41"); staged crashes 20/30/40/40 mph with mean estimates 37.7/36.2/39.7/36.1 (pins), dashed "REAL SPEED" diagonal = where estimates would sit if they tracked speed (illustrative reference line, not data); TEST 2, 150 STUDENTS, ONE WEEK LATER; broken glass yes 16/50 smashed, 7/50 hit (Table 2; the 6/50 control is not shown or spoken); "one memory" paraphrase of p. 588; paper card shows the real title "Reconstruction of Automobile Destruction", "LOFTUS & PALMER · 1974", "p. 588" (body lines are abstract bars, not text). On-screen credit "Data: Loftus & Palmer (1974)" while paper numbers are shown. No claim beyond the script.
- Voice: the EXISTING Gemini English take (../vo_en.wav, same placement as v2), no new TTS request. Picture timed to its word cues (cues.json + timing.json).
- Sound (s4.8 + RESEARCH s2): original 90 BPM D-minor score synthesised in code (kalimba "thread" ostinato, warm pad, e-piano, upright, light drums; section changes at each story beat; stitches play a rising scale; SEEN (low mallet) and TOLD (high kalimba) motifs land on one bell chord at "blend"; suspended figure on the question; D-major resolve on the end card); ~70 frame-synced SFX (synth whooshes/thuds/ticks/glass/pencil/paper + Mixkit UI pops from engine/sound/sfx); near-silence 0.16 s before the crash, NEVER THERE stamp, SMASHED stamp and the 16-crack hit; music ducked 7 dB and SFX 3 dB under the voice (smoothed voice envelope); stamps high-passed and lowered so they don't mask "never"/"smashed". Mix -14.0 LUFS, true peak -3.3 dBTP.
- Watermark (s1.6): engine/apply_watermark.py, 22% cream mark, top-left then top-right (1 switch, around 30-33 s). Headlines start at y >= 280 and nothing key sits in any watermark corner (TL/TR y 110-176, lower-left x 64-274 y 1340-1406), checked on the contact frames.
- End card (s1.5/s5.4): thread gathers into the red core at the engine end-card position, official Neuron star (engine/brand.py neuron_star, 128 px) grows out of it, "L A T O O N" Playfair + red rule with dot + "Voyaging the Unseen" Cormorant; fully built ~55.6 s, on screen ~54.8-56.6 s, then dissolves into the hook's first frame (loop). Nothing spoken over it.
- Colour/contrast (s5.2, WCAG on PAPER #F2E8D2): INK 14.8:1, INK2 8.4:1 (small labels/credit), OXBLOOD 6.8:1, DTEAL 5.9:1, NUMRED 4.0:1 (only large numbers >= 120 px, floor 3:1), INK on YEL chip 11.6:1. Red #E03C26 only on the thread/rules/core, never small text. No blue/navy ground, no glow, no gradients beyond matte ball shading.
- Anti-slop checklist (RESEARCH s5): 1 every object drawn for this story (thread, cars, film frame, audience, gauge, pinned chart, windshield, stitch grids, paper, yarn ball); 2 asymmetric left-set headlines, one focal point per beat; 3 no glow/neon/glass; 4 transitions are thread morphs + camera travel (log-space zoom out, travel down, pan along the week, travel down), no slide cuts; 5 every move tied to a spoken word; 6 paper fibre, cycling grain, wobbling ink lines, yarn twist; 7 springs/anticipation/follow-through on heroes, staggered letters; 8 short editorial labels, real numbers + source; 9 score written for the piece, SFX on events; 10 verified data + credit.
- Known flaws (honest): the 0.7 s collapse into the mark (54.0-54.75) reads as a small loop + shrinking ball rather than a clean drawstring; the audience is simple head-and-shoulder silhouettes; in 9.3-12.1 s the lower half is mostly the projector light until the students appear; the S7 re-told drawing's sprocket rows are wider than the drawing; frame 0 starts with the cars only partly in frame (they are already moving).
- Status: QA-clean, NOT uploaded. Old Studio draft GQXhT7dgE5s untouched.
