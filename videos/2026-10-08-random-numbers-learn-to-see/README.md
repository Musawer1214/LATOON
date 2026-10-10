# Build notes
- Final: random-numbers-learn-to-see_final.mp4 (1920x1080, 30 fps, libx264 veryfast CRF 18, AAC 192k, -14.2 LUFS, TP -1.4 dBTP, 9:45.5). Silent picture: video_noaudio.mp4.
- Stems (48 kHz, 16-bit stereo, same gain as the mix): audio/vo_en.wav (English voice only), audio/bed.wav (music + SFX only, NOT ducked, so a dub can be ducked to its own timing), audio/mix.wav (final ducked mix).
- Upload copy (CRF 23): /workspace/work/upload/random-numbers-learn-to-see.mp4
- Re-render: export PYTHONPATH=/workspace/work/pylib; ./run_render.sh 0 2 & ./run_render.sh 1 2 (900-frame chunks to chunks/), then concat chunks/list.txt. Audio: python3 src/audio.py, then volume +3.75 dB and alimiter 0.82. Docs: python3 src/docs.py. Timing lives in src/timeline.py (slot = read x 1.10 + 0.7 s).
- For a dub: keep picture, replace vo_en.wav with the dubbed VO placed at the paragraph starts in script_en.md / timing.json, and duck bed.wav under it.
