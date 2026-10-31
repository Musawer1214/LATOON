# QA (PLAYBOOK s11)
<!-- qa.py writes its automated section between the AUTO markers; the manual checks stay yours. -->
<!-- AUTO-QA START -->
<!-- AUTO-QA END -->
## Manual
1. Facts: every spoken and on-screen claim checked against the dossier.
2. Frames: full-res contact sheet reviewed; watermark positions checked.
3. Audio per language: Iapetus natural, names right, bed under the voice.
4. Captions: SRT timing per language (auto check above) + spot check in Studio.
5. Metadata.
QA 2026-10-31: LUFS -14.0, TP -3.3 dBTP, 58.7 s, 1080x1920, no black/freeze runs (ffmpeg), 13 shots + end card, cream/navy contrast 14.2, orange/navy 6.1. contrast_check.py not run (needs engine layout json; custom renderer). Voice: ASR all words match, 146.8 wpm span (below 150 target, above 140 floor), F0 +41% vs reference, highs -12.5 LU. WARN: voice slightly under target pace; hatch photo is the escape-hatch cutout not a cabin window (stated in description).
