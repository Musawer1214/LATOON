# The Archive, URDU edition: final-look QA (2026-10-24 ~21:40-22:40 CST)

Published: LATOON Urdu **8bm_fe-Vj2I** https://www.youtube.com/watch?v=8bm_fe-Vj2I (Public, oEmbed 200).
Uploaded file: vo/review/Archive_UR_FINAL_1080p.mp4 (754,891,786 B) = sample3d/Archive_EN_FINAL_v2.mp4 video stream copied (packet data identical, checked by md5 of the copied stream) + the fixed UR mix, AAC 192k, single audio stream.
Old (pre-fix) files: vo/review/pre_final_2026-10-24/ (track wav/m4a, SRT); old placement dub/voice/ur/placement_pre_final_2026-10-24.json.

## Fixed (dub/fix_ur_final.py, then dub/mix_dub.py ur, dub/make_srt_dub.py ur)
1. **Doubled word S3-10 -> S4-01**: S3-10's take ended with a leaked "ELIZA" (start of S4-01 from the same take), so viewers heard "...ہونا نہیں۔ ELIZA ... ELIZA۔ مہمان۔". Cut at 3.30 s. ASR now: "...لائق ہونا نہیں" | "ELIZA" | "مہمان".
2. **Minab dead air**: S5-22's take had 1.94 s of silence at its end, so after the casualty line the silence was 4.4 s, not the designed ~2.5 s. Tail trimmed; sentence pauses lengthened with the take's own room tone (+0.6 after "Iran", +0.35 "ہوا،", +0.45 "تھے۔", +0.25 "ہے،"); speech now ends 695.30 (EN 695.42), silence to S5-23 at 698.08 = 2.9 s (EN's own silence there: 2.93 s).
3. **Dead-air gaps**: lead silence trimmed on S3-06 and E-06 (~1 s each); S1-00x1 starts 22.35 (EN 22.0); balancing pass delayed 17 lines (each <= 1.6 s total, never earlier than EN, a line handing to another speaker still ends >= 0.3 s before that speaker's EN start) to split long silences. Max lateness now 1.63 s (S5-22), same as before.
4. **S1-03 ChatGPT "کس کا؟"** (median F0 94 Hz, lowest of all 26 ChatGPT UR lines, others 115-223): pitch +3 semitones, formants preserved (rubberband, tempo 1.0, same length) -> ~105 Hz (p75 118), low end of the voice's range. +4 st made Whisper hear "چیسکا"; +3 st is heard "کسکا" as the original. No TTS.
5. **Minab bed cut**: bed was hard-cut at the hold start (possible click); now an 80 ms fade (mix_dub.py).
6. **Short subtitle cues**: PARRY "PARRY، 1971۔" 0.54 -> 0.80 s, "PARRY: PARRY۔" 0.42 -> 0.80 s (next cue delayed <= 0.5 s). 205 cues, no overlaps, no tagline/CTA cue, last cue 15:05.10-15:08.65.
7. **AAC true peak**: plain 192k AAC of the -1.76 dBTP wav overshot to -0.7 dBTP; encoded through a 4x-oversampled limiter (0.75, latency-compensated, lag 0 samples checked) -> -1.5 dBTP.

## Final measurements
- Duration 921.500 s (video and audio), 1 video + 1 audio stream (AAC), colour tv/bt709.
- Loudness -14.3 LUFS integrated, true peak -1.5 dBTP (MP4). yt64k m4a (for the main-channel track): -15.6 LUFS / -1.8 dBTP.
- Black/blank frames: YAVG scan of all 27,645 frames: dark runs only at 0.00-0.50 (opening fade), 897.30-897.70, 904.40-904.57, 909.40-909.63 (designed card fades), 921.43-921.47 (last frame). No isolated dark frames; minimum YAVG elsewhere 21.7.
- Music dropouts: no 0.5 s window below -42 dBFS anywhere except the designed Minab hold (695.5-698.08, digital silence).
- Clicks: HF-transient scan in voice-free stretches: 34 candidates, all quiet (-42 to -60 dB HF) bed/SFX transients, EN final has 21 of the same kind; none at a line edit (one 15 ms after S4-09x3's start is the take's onset). Line wavs: no line starts or ends above -40 dB (no cut-off words).
- Overlaps: none (no line starts before the previous ends).
- ASR (Whisper small) of the final mix around every changed line, the opening, Minab and the ending: no doubled or missing words. Ending: S6-06 stops at "...چیک کون کر رہا ہے؟" (896.67), no "LATOON / Voyaging the unseen", silent quote card, ELIZA E-05 "What else would you like to discuss?" at 904.8-907.8, silent end card + music fade.
- Contact sheet (/workspace/work/ur_contact.png, 18 frames incl. 895-920 s): picture correct, quote card and end card present.

## Voice silences over 2.0 s (final, 22-896 s)
| time (s) | length | between | EN at that spot | verdict |
|---|---|---|---|---|
| 202.11-204.29 | 2.18 | S2-11x3 -> S2-11x4 | 1.67 s silence | OK: turn change to Claude, 0.5 s over EN |
| 251.03-253.33 | 2.30 | S2-14 -> S3-01 | 2.01 s | OK: scene change S2->S3 |
| 293.34-295.39 | 2.05 | S3-05 -> S3-06 | 0.99 s | OK at the limit: S3-06 already 1.5 s late |
| 305.19-307.25 | 2.06 | S3-06 -> S3-07 | 1.18 s | OK at the limit (S3-06 capped at 1.6 s late) |
| 340.39-342.41 | 2.02 | S3-09 -> S3-10 | 1.27 s | OK at the limit |
| 345.40-348.27 | 2.87 | S3-10 -> S4-01 | 1.99 s | Scene change S3->S4; UR line is 2.5 s shorter than EN and already 1.6 s late (cap). Music carries it. |
| 395.44-397.44 | 2.00 | S4-09x1 -> S4-09x2 (ELIZA) | 1.01 s | OK at the limit: ELIZA's EN take starts at its EN time |
| 398.83-401.08 | 2.25 | S4-09x2 (ELIZA) -> S4-09x3 | 1.45 s | OK: ELIZA EN take fixed; Claude centred in its EN slot |
| 412.34-414.60 | 2.26 | S4-09x3 -> S4-09x4 | 1.52 s | OK: turn change |
| 441.12-443.24 | 2.12 | S4-13 -> S5-01 | 2.43 s | Scene change, shorter than EN |
| 457.71-459.80 | 2.09 | S5-01 -> S5-02 | 1.18 s | OK at the limit |
| 562.88-565.11 | 2.23 | S5-13 -> S5-14 | 2.24 s | Same as EN |
| 669.94-672.00 | 2.06 | S5-21 -> S5-22 | ~1.0 s | Minab record plate lands here (stamp SFX) |
| 680.52-682.64 | 2.12 | inside S5-22 | 1.06 s | The take's own pause after "سو سے زیادہ بچے مارے گئے۔"; kept as the emphasis beat |
| 695.30-698.20 | 2.90 | S5-22 -> S5-23 | 2.93 s | Designed Minab hold |
| 817.87-819.90 | 2.03 | S5-34 -> S6-01 | 2.02 s | Scene change, same as EN |
| 896.54-905.13 | 8.59 | S6-06 -> E-05 | same | Designed quote card + ELIZA E-05 |
| 0-22.47 | | open | 0-22.12 | Designed image-only open (EN final's own audio) |
Before the fixes there were 17 such gaps (besides open/end), incl. 4.55 s (Minab), 3.05 s, 2.88 s, 2.74 s, 2.73 s, 2.63 s, and 2.27 s + 1.76 s around the stray 'ELIZA' at S3-10 -> S4-01.

## Open / doubts
- Per-line pitch spread across older accepted UR takes (49 longer lines > 8% off their speaker median) not changed; the owner's ear decides.
- S1-03 is still the lowest ChatGPT line after the +3 st correction (Hark could not listen; measured only).
- End screen: Studio saved the Video element at 15:12:10 (Subscribe at 15:10:00 correct); the browser could not set 15:10:00 after two tries.
- Studio's /video/<id>/details URL showed "Oops, something went wrong"; /video/<id>/edit worked.
