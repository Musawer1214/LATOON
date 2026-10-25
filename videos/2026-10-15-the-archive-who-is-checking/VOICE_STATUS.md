# VOICE_STATUS: The Archive: Who Is Still Checking?

**SCRIPT STATUS: FINAL** — owner approved 2026-10-15 17:24 "go ahead with video completion" (approves the VOICE_MAP.md cast and request plan as proposed, plus one script addition: the who's-who intro, script v3).

**OWNER APPROVED 2026-10-15** (PLAYBOOK s25b gate cleared).

- Script: script_en.json **v3** (v2 + [ADDED] who's-who intro S1-00x2..S1-00x6 after the cold-open hook; owner lines verbatim + 3 approved fixes; gen_script.py verbatim guard passes). dub/dub_script_ur.json, dub/dub_script_ps.json (v3). Diff: SCRIPT_RECONCILE.md §7.
- Voices (FINAL unless the audition fails one): NARRATOR Iapetus, ELIZA Erinome, PARRY Algenib, CHATGPT Puck, CLAUDE Gacrux. ELIZA's EN take is reused in the UR and PS mixes.
- Models: EN gemini-3.8-flash-tts, UR gemini-3.8-flash-lite-tts, PS gemini-3.8-flash-tts (one model per language for the whole video).
- Runner: dub/voice_runner.py (resumable; state in dub/voice_state.json). Requests run in Colab (Secret GEMINI_KEY), browser session "google-aistudio".
- Jobs: dub/cast_audition.json (7), dub/cast_jobs_en.json (11), dub/cast_jobs_ur.json (10), dub/cast_jobs_ps.json (10), dub/redo_jobs.json (made by the s16/PACING checks).

**Scheduled sweeps:** the voicing of this video is run by the chat's voice runner. A sweep may spend leftover quota on it ONLY by running the exact remaining jobs listed in NEXT_STEPS.md "Voice jobs remaining" through voice_runner.py (never ad-hoc requests, never a different model or voice), then updating this table.

| Unit | EN (3.8 Flash) | UR (3.8 Flash-Lite) | PS (3.8 Flash) |
|---|---|---|---|
| audition | DONE 10-15 (5 EN) | DONE 10-15 (Claude) | DONE 10-15 (PARRY) |
| narrator | u0/u1 DONE 10-15; 9 of 11 lines accepted (S1-00x2, S1-00x5, S6-06, E-07 rejected) → narrator_s0 | u0/u1 DONE 10-15 | small jobs s0–s2 pending |
| chatgpt | u0 DONE 10-15 but too fast (median 167 wpm, "long pause" read aloud once) → whole speaker re-voiced: chatgpt_s0–s3 | u0 DONE 10-15 (re-check vs new EN) | s0–s3 pending |
| claude | not voiced (big units superseded) → claude_s0–s9 | u0–u3 DONE 10-15 (u2 pitch outlier → claude_s0/s1 re-voice) | s0–s9 pending |
| parry | not voiced → parry_s0–s5 | u0/u1 DONE 10-15 (u1 pitch outlier) + u2 lines → parry_s0–s3 | s0–s5 pending |
| eliza | u0 DONE 10-15; 5 lines too fast → whole speaker re-voiced: eliza_s0/s1 | reuse EN | reuse EN |

**UR VOICE COMPLETE 2026-10-24 20:40 CST (pending the owner's listen): 120/120 UR lines pass PACING (E-07 cut by the 10-24 re-cut; S6-06 tagline trimmed), 0 flagged. Full UR track built on the re-cut timeline: vo/review/Archive_UR_track.wav (921.5 s, -14.16 LUFS, -1.76 dBTP) + Archive_UR.srt; Gofile https://gofile.io/d/nf5mQUge. Not on YouTube yet.**
**PS (2026-10-24 20:40 CST): 85 of 120 placed, 41 accepted, 44 flagged, 35 not voiced. Next: 10-25 window = archive_ps_claude_s1..s9 + archive_ps_parry_s6 (10 on 3.8 Flash); then redos. Estimate 4 more windows (3-5).**

**EN VOICE COMPLETE AND LOCKED 2026-10-23 16:45 CST: EN 121/121 pass, 0 flagged, ~15:22 total. Locked timeline: dub/voice/en/timings_LOCKED_2026-10-23.json. Per-line fixes are in the NEXT_STEPS.md banner of that time (time-stretched: S3-01 0.94, E-07 0.92; numeral false positives accepted: S2-11x3, S2-12x3, S4-09x5; pauses shortened inside silences: S5-15x3, S5-20, S6-06, S4-09x5 lead; new take: S6-03 r110).**

(older) **Current (2026-10-21 06:15 CST): EN 94 accepted / 27 flagged of 121 (est 15:11); UR 104 / 17; PS 28 placed / far from done (waits for 3.8 Flash after EN).** Next: 10-21 15:00 CST window = EN r60-r62 (8 req) + UR r50 (4 req), see NEXT_STEPS banner.

Exact remaining jobs and their windows: NEXT_STEPS.md "Voice jobs remaining".

## Spend log
- Window opened 2026-10-15 15:00 CST: gemini-3.8-flash-tts **10/10** (audition 6 + en narrator_u0, narrator_u1, chatgpt_u0, eliza_u0), gemini-3.8-flash-lite-tts **10/10** (audition 1 + ur narrator_u0/u1, chatgpt_u0, claude_u0–u3, parry_u0/u1). No 429 returned; cap reached by count. 3.1 / 2.5: 0.

- Window opened 2026-10-16 15:00 CST: ran nb_w1_2026-10-16 (16 requests: 10 on gemini-3.8-flash-tts EN, 6 on gemini-3.8-flash-lite-tts UR), no 429. 3.8 Flash 10/10, Flash-Lite 6/10 (4 spare, none left in the plan; UR redo of out-of-range lines is Sat). Ingested, ASR'd, analysed; timings: EN 64 lines placed / 80 missing-or-flagged; UR 114 placed / 26 flagged.

- Window opened 2026-10-17 15:00 CST: 3.8 Flash **10/10** (EN parry_s3-s5, claude_s0-s6), 3.8 Flash-Lite **8/10** (UR redo r10-r12 set, 8 requests). No 429. EN 105 placed / 67 flagged; UR 117 placed / 24 flagged; PS not started. 16 EN redo requests queued (redo_jobs.json, tag r1). See NEXT_STEPS.md.

- Window opened 2026-10-18 15:00 CST: 3.8 Flash **10/10** (EN narrator_r10, claude_r10-r18), 3.8 Flash-Lite **10/10 by server count** (UR parry_r20-r22, chatgpt_r20/r21, narrator_r20/r21, claude_r20 + parry_r30; chatgpt_r30 returned 429, not retried). EN 114 placed / 57 flagged; UR 121 placed / 13 flagged; PS not started.

- Window of 2026-10-20 (10-20 window, spent 10-21 early, 06:04-06:07 CST): nb_w5_2026-10-20win, 3.8 Flash **10/10** (EN chatgpt_r50/r51, parry_r50/r51, claude_r50-r54, narrator_r50; 45 of the 46 flagged lines, ELIZA S4-12 held back for lack of a request), Lite **10/10** (UR parry_r40/r41, chatgpt_r40-r42, claude_r40-r43, narrator_r40). No 429. EN 94 accepted / 27 flagged (19 lines fixed); UR 104 / 17. 3.1/2.5: 0.

- Window of 2026-10-21 15:00 CST (run 15:30-16:05): 3.8 Flash **10/10** (EN narrator_r60, eliza_r60, chatgpt_r60, parry_r60/r61, claude_r60-r62, chatgpt_r70, parry_r71), Lite **10/10** (UR narrator_r50, chatgpt_r50, claude_r50, parry_r50, narrator_r60, chatgpt_r61/r62, claude_r63/r64, parry_r65). No 429. EN 121 placed / 17 flagged (est 15:17); UR 121 / 14 (est 15:10).
- Window 2026-10-22 15:00 CST: nb_w7: 3.8 Flash 6 EN requests, Lite 4 UR requests (10 total; 4 Flash + 6 Lite possibly still spare). No 429. EN 121/12 flagged, UR 121/12.
- 2026-10-22 second batch nb_w7b: Flash +4 (10/10), Lite +4 (8/10). EN 11 flagged, UR 9.
- Window 2026-10-23 15:00 CST: nb_w8 3.8 Flash +6 (EN r100/r101), no 429. EN 9 flagged.
- 2026-10-23 16:35 CST nb_w8b: 3.8 Flash +2 (EN chatgpt_r110/r111), 8/10 used, no 429. Plus derived fixes zfix_r12 (no request). EN 121/121 pass, LOCKED 16:45 CST.
- Window opened 2026-10-24 15:00 CST (spent 20:00-20:05 CST, nb_w9_2026-10-24): 3.8 Flash-Lite **10/10** (UR archive_ur_chatgpt_r100-r103, claude_r100-r103, parry_r100/r101), 3.8 Flash **10/10** (PS archive_ps_parry_s1-s5, chatgpt_s0-s3, claude_s0; parry_s5 turned out to duplicate parry_s4's lines). No 429; 3.1/2.5 untouched. Plus derived UR fixes archive_ur_zfix_r13 (no request). UR 120/120 pass (0 flagged); PS 85 placed / 41 accepted / 44 flagged / 35 not voiced.

2026-10-25 15:50 CST: **PS window of 10-25 spent (nb_w10_2026-10-25, Colab session google-aistudio, 3.6 min): gemini-3.8-flash-tts 10/10** = archive_ps_claude_s1..s9 + archive_ps_parry_s6 (all PS lines are now voiced once). No 429, 3.1/2.5 untouched, Lite not used (UR is done; PS is Flash-only). Ingested, ASR'd (pip install faster-whisper pyloudnorm first after a sandbox reset), analysed. **PS timings: 120 placed, 67 missing/flagged (est 15:55).** Next windows: redos for the flagged PS lines (3-4 lines per request), check the weak-alignment splits by ear; then place_dub/mix for PS; UR track still waits on owner (UR edition already public on the LATOON Urdu channel 8bm_fe-Vj2I; main-video UR audio track not added yet).
