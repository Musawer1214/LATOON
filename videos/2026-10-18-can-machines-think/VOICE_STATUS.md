**2026-10-26 21:45 CST OWNER: "The voice is good, so you can proceed with the full video. Rendering with this voice."** The current English narration/mix (mix_en_v3.wav, 14:01) is FINAL. NO Lite redos (the C2-01/C3-05/C4-02/C5-02 redo list is CANCELLED). Go straight to the scene build and render on this audio.

# VOICE_STATUS — CMT English v3 (Lite, Iapetus)
**2026-10-26 ~22:30 CST: ALL 52 CARDS SPLIT, ASR-QA'd, ASSEMBLED AND MIXED (no TTS spent this run).** Raw takes = 814.8 s (13:35) / 2,290 words = 168.6 wpm gross (owner accepted); speech-only per-card median 175 wpm. Every Lite take has a start click + ~130 ms loud end burst: trimmed in assemble_v3.py.
- Per-card WAVs: dub/voice_en/cards/<id>.wav (+ .asr.json); QA: dub/voice_en/QA_EN.md, qa_data.json, split_report.json (all joins in >= 250 ms silence).
- Narration: dub/voice_en/narration_en_v3.wav (821.2 s, -16.0 LUFS, -2 dBTP stem; raw = narration_en_v3_raw.wav); timings: dub/voice_en/timings_v3.json (card start/end + word times).
- Mix: dub/voice_en/mix_en_v3.wav (841.1 s incl. closing 21 s; -14.0 LUFS, TP -2.3 dBTP; bed stem bed_en_v3.wav; settings mix_v3_info.json); preview mix_en_v3_preview_60s.mp3.
- **REDO next Lite window (one request, 4 paragraphs, ~170-175 wpm):** C2-01 (Lovelace slurred), C3-05, C4-02, C5-02 (>15% faster than median). Optional: C0-04, C3-07, C6-01, C5-05. After redo: assemble_v3.py -> mix_v3.py -> plan/shots_v3.py -> build_script_v3.py.

**2026-10-26 04:54 CST OWNER REVERSAL: "for this video 168 is good".** KEEP the first Lite pass (50/52 cards, ~168 wpm) as the final English narration. Do NOT re-voice at 145 (the 04:51 note below is cancelled for this video). Only voice the last 2 closing cards on Lite Iapetus in the 15:00 CST window, matching the existing pace (~160-175 wpm), then assemble the full narration and QA.

**2026-10-26 04:51 CST OWNER: '145 WPM on all video'.** The 168-wpm Lite pass (50/52 cards) is rejected; re-voice ALL 52 cards on 3.8 Flash-Lite Iapetus at 145 wpm (accept 138-152) from the 15:00 CST window. See VOICE_PLAN.md banner.

# VOICE_STATUS (CMT English, Lite, Iapetus) — 2026-10-26 04:40-05:00 CST
Window used: Lite 10/10 (aud + cmt_en_00..07 ok; cmt_en_08 = C9-02,C9-03 hit 429 -> re-queue after 15:00 CST reset).
Files: dub/voice_en/*.mp3 (raw, unQA'd); jobs: dub/jobs_main.json (ids per chunk). Chunks hold cards C0-04.. onward; aud = C0-01..C0-03.
PACE: ~168 wpm overall (aud 136w/49.9s=163; chunks ~170) — faster than the 140 target. Not ASR-checked yet. Owner to decide: accept or re-voice slower.

**2026-10-26 15:35 CST:** cmt_en_08 (C9-02, C9-03) voiced on Lite Iapetus, 31.8 s, no errors. All 52 cards now voiced; raw takes total 722.7 s (12:03). Next: split takes into cards at silences, ASR QA, v3 timings/script.json, Cylinder Five mix, v3 shotlist.
