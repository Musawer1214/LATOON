# Loftus one-word memory Short - status (updated 2026-10-20 09:10 CST)
v3 BUILT (VISUAL SYSTEM v3, Thread mode), QA 0 FAIL, NOT UPLOADED. Owner (via main run, 08:18 CST): publish v3 without his review once it passes QA; the main run does the upload.
- Final: v3/Loftus_One_Word_v3.mp4 (1080x1920, 57.03 s, 27.6 MB, H.264 CRF 21 + AAC 192k, watermarked, -14.1 LUFS / -3.1 dBTP)
- Upload-size copy (browser bridge < 8 MB): v3/Loftus_One_Word_v3_upload.mp4 (7.7 MB, 2-pass 0.9 Mbps, light denoise; checked by eye, numbers/text crisp)
- Title/description/tags: v3/metadata.txt (no image credits: v3 has no photos). Soft EN captions: v3/subs_en.srt (21 cues rebuilt from the voice word timings). Contact sheet: v3/contact.jpg. QA: v3/QA.md (+ v3 section in QA.md).
- Old private Studio draft GQXhT7dgE5s (pre-upgrade render): do NOT touch now. At publish: upload v3 as a new video; the stale draft is a separate decision (delete only with the owner's/main run's OK).
- v2 files in this folder (Loftus_One_Word_Memory_LATOON_short*.mp4, final_wm.mp4) are SUPERSEDED; never upload them.
- UR/PS: still the owner's own voice (PDF voice_own/2026-10-20-loftus-one-word/). Same 57.0 s timing; mix the dubs over v3/bed_v3.wav (v3 music+SFX, no voice, -20 LUFS master; re-level when mixing), not the old bed.wav. Send audio to the owner before Studio (s6.2).
- Rebuild/resume: v3/v3.py (picture, Skia), v3/v3_audio.py (score+SFX+mix), v3/render_chunks.sh <start frames> (resumable 140-frame chunks into v3/segs/), v3/finish.sh (concat, mux, watermark, encode), v3/upenc.sh (small upload encode), v3/make_srt.py. PYTHONPATH=/workspace/latoon/research/premium_feel/pylib; after a sandbox reset run research/premium_feel/lib/setup.sh.

---- earlier status (v2, superseded) ----
# Loftus one-word memory Short (2026-10-20 daily topic Short) - status
HELD, NOT UPLOADED (owner 2026-10-20 ~05:46 CST said the visuals don't look premium; tonight's publish is delayed for an upgraded-look pilot). Do NOT upload or schedule until the owner/main run says so.
(The earlier line "uploaded and scheduled 18:00 PKT" was wrong: nothing was scheduled.)

Studio state (read 2026-10-20 ~05:30 CST, read-only): an OLD Draft of this Short exists, ID GQXhT7dgE5s ("Can One Word Change What You Remember? #shorts", Draft/private, no schedule). It holds the PRE-upgrade render. Studio can't replace a video file: when publishing, upload the new encode and delete that stale draft (or ask first).

Built (2026-10-20 recovery run): v2 visual upgrade re-render, QA 0 FAIL (QA.md "Visual upgrade re-render").
- Master: Loftus_One_Word_Memory_LATOON_short.mp4; watermarked: final_wm.mp4
- Upload file (6.1 MB): /workspace/work/upload/loftus_one_word_short.mp4 (copy: Loftus_One_Word_Memory_LATOON_short_upload.mp4)
- Soft EN captions: subs_en.srt. Metadata: metadata.txt (its SCHEDULE line is stale; pick a new slot).
- Render on this sandbox: python3 seg.py <a> <b> in ~400-frame chunks to /tmp/lsegs, concat, mux mix_en.wav (build.sh in one go exceeds the 120 s command limit). Quick frame review: python3 sheet.py out.jpg t1 t2 ...
- Thumbnail/cover in the locked template (PLAYBOOK s1.7) NOT yet made.

If the upgraded pilot changes the look, re-do scenes.py on the new look; voice (vo_t*.wav), timing, SFX list and SRT can be reused (NO new TTS).

UR/PS: owner's own voice later. Recording PDF: /workspace/latoon/voice_own/2026-10-20-loftus-one-word/Loftus_One_Word_Memory_Urdu_Pashto_Script.pdf. Processing steps when recordings arrive: transcribe (faster-whisper small, numpy array input), prep_own.py + finalize_own.py, dub/dub_short.py to the 57.0 s timing, SRTs, send audio to owner for approval before Studio (s6.2).
