# QA — "Can Machines Think?" EN (PLAYBOOK s7) · started 2026-10-26 23:20 CST

**State: PRE-RENDER QA only. The full film is rendering (film/run_film.sh); CMT_EN_FINAL_v1.mp4 does not exist yet. Do not deliver or upload until the sections below marked OPEN are closed.**

## Audio (final, untouched)
- dub/voice_en/mix_en_v3.wav 841.1 s, -14.0 LUFS, TP -2.3 dBTP (dub/voice_en/mix_v3_info.json, QA_EN.md). Owner approved 2026-10-26 21:45 CST. Picture timing = timings_v3.json via plan/shots_v3.json -> film/cuts.json (25,232 frames @30 = 841.07 s; the WAV is 841.1 s, mux uses -shortest... CHECK the last 0.03 s on assembly).

## Picture — still review (s7.4), 2026-10-26
- One still per cut (85) rendered from the real pipeline: film/stills/; contact sheet film/contact_v3_build.jpg (viewed in 3 parts at 384 px tiles + full-size checks of every world).
- Golden Rule check: each section has its own world chosen for its idea (CONCEPT v3); no graphs/tables/charts; numbers appear as physical things (marbles 73/36/59, card stacks 79/33, 10,000 grains, 4-1 stones) with short labels; no blue/neon grounds, no robots/brains/holograms; people only as credited photos or faceless figures.
- Facts on screen: Move 37 placed from the real record (P10, fifth line; Fan Hui commentary SGF confirms 'Black 37'); 'experts: 3rd-4th line' is the general professional habit on the side (no invented specific expert moves); Othello positions and the changed prediction are computed with real Othello rules; Chinese slips are correct Mandarin (你喜欢下雨吗？ / 喜欢，雨声让我平静。); quotes: Turing 1950 opening line and closing sentence verbatim; study tags: 'Jones & Bergen · PNAS 2026' + 'preprint 2025', 'GPT-4 · tested 2023', '2023 · 19 researchers', '1 in 10,000', '4-1' (FACTCHECK.md / script v3).
- Credits: 7 photos with on-screen credit tags while shown (author · licence · Wikimedia Commons); sources.md holds the Commons pages and licences (verified via API 2026-10-26).
- Fixed after review: see NEXT_STEPS status. Soft spots kept (listed there).

## OPEN until the render is assembled
- [ ] film/qa/blackscan.txt: only designed dark moments (C2-01a dip, C8-05a dip, CLOSE-hold -> quote fade, END last 0.5 s)
- [ ] every segment yuv420p / tv / bt709 and exact frame count (render.js verifies per cut; assemble.sh re-checks)
- [ ] duration video = audio (841.07 vs 841.1 s)
- [ ] full watch-through for sync, label timing and motion pacing; spot checks 4:26.9, 5:38, 7:52, 13:42
- [ ] watermark present, never over labels (engine apply_watermark.py, qa/watermark.log)
- [ ] engine/qa.py run on the master; contrast spot checks (labels sit on dark panels by design)
- [ ] Gofile upload + md5 match, link to the owner; publish only after his OK
