# QA (PLAYBOOK s11)

<!-- AUTO-QA START -->
### Automated checks (qa.py, AI_I_Dont_Know_sample.mp4): 0 FAIL, 1 WARN

| | Check | Result |
|---|---|---|
| PASS | resolution | 1080x1920 at 30.00 fps (expected 1080x1920) |
| PASS | streams | 1 video, 1 audio (h264, aac) |
| PASS | duration | 59.53 s (Shorts must be under 60 s; 38-55 s works best) |
| PASS | size | 30.0 MB master; upload the ~6 MB re-encode (s15: libx264 preset slow CRF 23, AAC 160k) |
| PASS | loudness[mp4] | -14.2 LUFS, -3.7 dBTP (target -14 / -1) |
| PASS | silence[mp4] | no gaps |
| PASS | loudness[en] | -14.1 LUFS, -3.4 dBTP (target -14 / -1) |
| PASS | silence[en] | no gaps |
| PASS | srt[en] | 14 cues, 100% of speech covered |
| WARN | srt | 1 SRT file(s); Shorts ship EN/UR/PS SRTs |
| PASS | text overflow | none |
| PASS | safe zones | ok |
| PASS | watermark corners | clear |
| PASS | text overlap | none |
| PASS | no narration captions | on-screen text is labels only |
| PASS | label length | all labels 1-3 words |
| PASS | hook motion | mean frame change 2.88 over the first 0.1 s (frame 1 must already move) |
| PASS | hook keyword | big number/keyword by 2 s: 'CONFIDENT' |
| PASS | loop seam | last vs first frame difference 1.2 (lower = smoother loop) |
| PASS | palette | no neon or blue-purple |
| PASS | credits | 0 image/clip files used, all in sources.md |
| PASS | contact sheet | 3 full-res page(s) + overview in qa/ - review them before export |
<!-- AUTO-QA END -->

## Manual QA — SAMPLE build, 2026-10-20 (not uploaded)
- Facts (s7.3) vs sources.md (OpenAI blog 2025-09-05 + arXiv 2509.04664): every spoken line and on-screen number checked. Scoreboard exactly gpt-5-thinking-mini 52/22/26 and OpenAI o4-mini 1/24/75 (DON'T KNOW / RIGHT / WRONG), SimpleQA, GPT-5 system card; 1 in 365; fix wording paraphrases "penalize confident errors more than uncertainty, give partial credit for appropriate uncertainty". Hedge kept: "a big reason", not the only reason. Takeaway is LATOON advice, not attributed to OpenAI.
- Frames: contact.jpg (31 frames) + qa/contact_0*.jpg reviewed by eye. Fixed before final: exam framing (tick/zero were clipped right), GUESS/BLANK chips leaving frame during the orbit, calendar too wide for 9:16, "BIRTHDAY?" under flying tiles, chip clipping at frame edges, "CHECK IT" below 1600, "I DON'T KNOW" chips (qa narration rule) -> "DON'T KNOW", the 75 % tower firing 0.6 s before "seventy-five" (ASR drift) -> now on the word after a real 0.6 s pause.
- Layout log (three/layout.js -> qa_layout.json, 1,050 text samples every 0.25 s): no margin, safe-zone, watermark-corner or overlap issues.
- Contrast (engine/contrast_check.py, contrast.md): first pass 3 FAIL (model names straddling the plinth edge 2.7:1; "+1" brass text 3.6:1) -> names moved onto the floor in INK, "+1" darker brass; re-checked after the final render (see contrast.md).
- Audio: -14 LUFS integrated, true peak <= -1 dBTP (qa.py); short-term loudness 3-s windows -12.3..-16.4 LUFS through the voiced part, LRA 2.8 LU; voice ~16 LUFS stem over music ~-27 ducked 7 dB, SFX ~-27.5 ducked 3 dB; music near-silence before 26 %, 75 %, 1-in-365, penalty, check. Listening was checked by measurement (loudness windows, ducking, voice ASR) — Hark cannot hear audio; the owner should give it one listen.
- Voice pace: voice/pace.md (articulation 154 wpm, overall ~122 wpm, no time-stretch).
- Watermark: 22 % cream mark TL/TR (2 switches), via wm_local.py (local copy of engine/apply_watermark.py with a trailing-comma ffprobe parse fix).
- Open: UR/PS tracks + SRTs not made (sample). WARN srt (1 SRT) expected.
