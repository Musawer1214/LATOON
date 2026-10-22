# QA (PLAYBOOK s11)

<!-- AUTO-QA START -->
### Automated checks (qa.py, Why_Is_The_Night_Sky_Dark_v1_master.mp4): 0 FAIL, 3 WARN

| | Check | Result |
|---|---|---|
| PASS | resolution | 1080x1920 at 30.00 fps (expected 1080x1920) |
| PASS | streams | 1 video, 1 audio (h264, aac) |
| PASS | duration | 51.90 s (Shorts must be under 60 s; 38-55 s works best) |
| PASS | size | 25.8 MB master; upload the ~6 MB re-encode (s15: libx264 preset slow CRF 23, AAC 160k) |
| PASS | loudness[mp4] | -14.2 LUFS, -2.2 dBTP (target -14 / -1) |
| PASS | silence[mp4] | no gaps |
| WARN | srt | 0 SRT file(s); Shorts ship EN/UR/PS SRTs |
| WARN | layout | no layout log (render.py qa) - safe zones checked from frames only |
| PASS | no narration captions | on-screen text is labels only |
| PASS | label length | all labels 1-3 words |
| PASS | hook motion | mean frame change 3.80 over the first 0.1 s (frame 1 must already move) |
| WARN | hook keyword | no big number or keyword logged in the first 2 s |
| PASS | loop seam | last vs first frame difference 1.1 (lower = smoother loop) |
| PASS | palette | no neon or blue-purple |
| PASS | credits | 0 image/clip files used, all in sources.md |
| PASS | contact sheet | 3 full-res page(s) + overview in qa/ - review them before export |
<!-- AUTO-QA END -->

## Manual QA (s7), 2026-10-22 PKT — v1
- Concept: CONCEPT.md written first (golden rule 5.0b): forest -> stars morph with a gaze ring, blaze, real dark sky, dust that would glow (Herschel 1848), Poe (credited), top-down light-travel map (ring = distance light has had time to travel; hollow ghost = light not yet arrived), ghost stars in the gaps, person under the sky. No graphs/tables. Tech: ModernGL GLSL (CPU) + Skia, no new tools.
- 7.2 Colour: warm near-black / cream / ember (dust only); no navy/neon; blaze is capped cream #F6EBD0-ish (never pure white). Labels cream on near-black (>12:1): 1848, Edgar Allan Poe, credit line, 13.8 billion years, a beginning, the past. contrast_check.py not run (needs qa_layout.json; labels by eye). Dark end card matches the video (cream on near-black).
- 7.3 Facts vs dossier/Harrison review: Herschel 1848 (absorbing medium would heat up and radiate), Poe 1848 Eureka (voids explained by a background so distant no ray has reached us), 'mostly' (finite age), 13.8 billion years. Expansion not claimed. Stylised: real stars are tiny; the blaze uses shells of smaller, more numerous stars; map ring not to scale, no expansion drawn.
- 7.4 Frames: contact sheets reviewed; end card 49.2-51.9; loop seam 1.1. Weak spots: 12-13.5 s transitional star noise (tweed look) before the blaze; map streaks of light are a little busy.
- 7.5 Audio: Gemini 2.5 Iapetus read fast (~190 wpm in speech); one request only, so lines slowed 0.90-1.0 (atempo) with gaps reset (voice/assemble.py). Mix -14.0 LUFS / -2.8 dBTP master; encoded -14.2 / -2.2. Not listened by ear (no playback in sandbox).
- 7.6 Captions: subs_en.srt 16 cues. UR/PS subs after the owner's recordings.
