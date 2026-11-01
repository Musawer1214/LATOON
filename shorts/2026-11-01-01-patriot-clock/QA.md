# QA (PLAYBOOK s11)

<!-- AUTO-QA START -->
### Automated checks (qa.py, Patriot_Clock_LATOON_short_wm.mp4): 0 FAIL, 2 WARN

| | Check | Result |
|---|---|---|
| PASS | resolution | 1080x1920 at 30.00 fps (expected 1080x1920) |
| PASS | streams | 1 video, 1 audio (h264, aac) |
| PASS | duration | 54.85 s (Shorts must be under 60 s; 38-55 s works best) |
| PASS | size | 46.6 MB master; upload the ~6 MB re-encode (s15: libx264 preset slow CRF 23, AAC 160k) |
| PASS | loudness[mp4] | -14.1 LUFS, -3.5 dBTP (target -14 / -1) |
| PASS | silence[mp4] | no gaps |
| WARN | srt[en] | 16 cues; no vo_en.wav stem to compare against |
| WARN | srt | 1 SRT file(s); Shorts ship EN/UR/PS SRTs |
| PASS | text overflow | none |
| PASS | safe zones | ok |
| PASS | watermark corners | clear |
| PASS | text overlap | none |
| PASS | no narration captions | on-screen text is labels only |
| PASS | label length | all labels 1-3 words |
| PASS | hook motion | mean frame change 4.99 over the first 0.1 s (frame 1 must already move) |
| PASS | hook keyword | big number/keyword by 2 s: '0.1' |
| PASS | palette | no neon or blue-purple |
| PASS | credits | 0 image/clip files used, all in sources.md |
| PASS | contact sheet | 3 full-res page(s) + overview in qa/ - review them before export |
<!-- AUTO-QA END -->
