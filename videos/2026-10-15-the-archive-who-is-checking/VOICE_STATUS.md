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

Exact remaining jobs and their windows: NEXT_STEPS.md "Voice jobs remaining".

## Spend log
- Window opened 2026-10-15 15:00 CST: gemini-3.8-flash-tts **10/10** (audition 6 + en narrator_u0, narrator_u1, chatgpt_u0, eliza_u0), gemini-3.8-flash-lite-tts **10/10** (audition 1 + ur narrator_u0/u1, chatgpt_u0, claude_u0–u3, parry_u0/u1). No 429 returned; cap reached by count. 3.1 / 2.5: 0.
