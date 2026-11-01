# QA (PLAYBOOK s11)

<!-- AUTO-QA START -->
### Automated checks (qa.py, Tickle_Yourself_LATOON_short_wm.mp4): 0 FAIL, 4 WARN

| | Check | Result |
|---|---|---|
| PASS | resolution | 1080x1920 at 30.00 fps (expected 1080x1920) |
| PASS | streams | 1 video, 1 audio (h264, aac) |
| PASS | duration | 52.00 s (Shorts must be under 60 s; 38-55 s works best) |
| PASS | size | 46.8 MB master; upload the ~6 MB re-encode (s15: libx264 preset slow CRF 23, AAC 160k) |
| PASS | loudness[mp4] | -14.1 LUFS, -3.1 dBTP (target -14 / -1) |
| PASS | silence[mp4] | no gaps |
| WARN | srt[en] | 17 cues; no vo_en.wav stem to compare against |
| WARN | srt | 1 SRT file(s); Shorts ship EN/UR/PS SRTs |
| PASS | text overflow | none |
| PASS | safe zones | ok |
| PASS | watermark corners | clear |
| PASS | text overlap | none |
| PASS | no narration captions | on-screen text is labels only |
| PASS | label length | all labels 1-3 words |
| PASS | hook motion | mean frame change 12.54 over the first 0.1 s (frame 1 must already move) |
| PASS | hook keyword | big number/keyword by 2 s: 'TICKLE?' |
| WARN | loop seam | last vs first frame difference 115.7 (lower = smoother loop) |
| WARN | palette | 49.8s 0.5% |
| PASS | credits | 0 image/clip files used, all in sources.md |
| PASS | contact sheet | 3 full-res page(s) + overview in qa/ - review them before export |
<!-- AUTO-QA END -->

## System v2.0 s8 checklist (final: final/Tickle_Yourself_LATOON_short_wm.mp4; upload copy final/Tickle_Yourself_LATOON_short_upload.mp4)
| # | Check | Result |
|---|---|---|
| 1 | Auto bundle (engine_next/qa.py) | PASS: 0 FAIL, 4 WARN (above) |
| 2 | Black frames | PASS: none (PIL frames, no black runs; end card on paper) |
| 3 | Loudness | PASS: -14.1 LUFS, TP -3.1 dBTP (≤ -1.0) |
| 4 | Motion (motion_check.py, qa/motion.json) | PASS: 10/12 footage shots ≥ 2.5x grain floor (0.52); mri (1.16) and robot (0.69) are slow source clips: video diff ≥ 0.25x source (0.34 / 0.33) and first-to-last span 34.6 / 8.8 ≥ 3x floor and ≥ 0.3x source span (11.9 / 3.8) → PASS by the span rule |
| 5 | Static frames | PASS: every shot has a push/pull or animated diagram; no hold > 3 s |
| 6 | Empty paper | PASS: no bare paper stretch (diagrams fill every paper shot) |
| 7 | Cut rate | PASS: 21 shots in 52 s, a change every ~2.5 s (longest shot 3.4 s, moving footage with a punch-in) |
| 8 | Contrast (contrast_check.py) | PASS: 0 below target (lowest 3.4:1 large coral '0.2 s' vs 3:1). Note: qa_layout.py label default fixed to y=1480 (render default); the first run logged labels 80 px low and gave 4 false FAILs |
| 9 | B flaws | PASS: full-res contact sheets reviewed; no subject cropped after punch-ins; no empty pills; credit pill on shot 7 moved off the wave panel |
| 10 | Chunks | PASS: 6 PIL chunks, one encoder setting (libx264 yuv420p), concat-copy; no black chunk starts |
| 11 | Voice | WARN (written off): ASR 132/132 words exact; span 160.1 wpm (target 150-165); -14.0 LUFS, TP -1.44; highs -11.96 LU (in -9..-13); F0 median 187.1 Hz. Per-line in-take pace: lines 4, 7, 8 at 191-199 wpm (> 180) and line 5's first unit 192. s4 says re-voice, but the Shorts rule allows ONE request per Short and it is spent, so no re-voice; no time-stretch. Overall pace inside band; flagged for the owner |
| 12 | Music/SFX | PASS: music -19.9 dB under speech (18-21), -20.7 in gaps; 6 soft SFX each on a visible event (≥ 5.8 s apart); near-silence before the payoff line (43.0-43.9 s) |
| 13 | Facts | PASS: every spoken/on-screen claim matches the dossier + PubMed abstracts (1998 Nat Neurosci 1:635; 1999 J Cogn Neurosci 11:551); 0.2 s = 200 ms; "twist" = 0-90° rotation |
| 14 | Captions/metadata | PASS: subs_en.srt 17 cues timed to words.json; no burned narration captions; labels 1-3 words; safe zones PASS |
| 15 | Full watch | PASS (frame review): contact sheets + stills at every shot, audio levels measured; phone-size overview checked |

WARN write-offs: srt[en] (no separate VO stem; SRT built from the voice word times), srt count (English only by owner order 2026-10-31 22:19 CST), loop seam (end card → hook frame by design), palette 0.5% at 49.8 s (bluish goggles in Pexels 8942709 footage, photo not graphics).
