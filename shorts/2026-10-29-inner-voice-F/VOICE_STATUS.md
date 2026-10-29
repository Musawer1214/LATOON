# VOICE_STATUS — Hidden Mind "Does Everyone Have a Voice in Their Head?" (English, theme F build)

- Script: research/2026-10-28-inner-voice/script_en_v2_OWNER.md (owner FINAL, 1,625 spoken words; wording unchanged).
- Model: **gemini-3.8-flash-tts** (latest free Gemini speech model), voice **Iapetus**, Interactions API with `speech_metadata.style` (not read aloud). One model for all English.
- Route: Colab (browser session google-aistudio), notebooks built by voice/make_jobs.py (NB_CODE from The Archive's voice_runner).

## Requests spent (quota window opened 2026-10-28 15:00 CST, resets 2026-10-29 15:00 CST)
| Time CST | Notebook | Jobs | Count | Notes |
|---|---|---|---|---|
| 10-29 ~02:45 | nb_cal.ipynb | hm_en_r00 (hook, style A "about 150 wpm") | 1 | 66.1 s, 161 wpm gross, opening quarter 184 wpm -> too fast; replaced by r00b. Kept in takes/ as fallback. |
| 10-29 ~03:00 | nb_main.ipynb | hm_en_r00b..r08b (style B "about 140 wpm", relaxed but engaged) | 9 (+1 transient 503 on r05b, retried OK) | 649.9 s raw for 1,625 words = 150 wpm gross in-take |

3.8 Flash used this window: 10 of 10 (the 503 may or may not count). No requests left until 15:00 CST 2026-10-29.
3.8 Flash-Lite / 3.1 / 2.5: not used.

## Assembly and QA (2026-10-29 ~03:30 CST)
- ASR (faster-whisper small.en) on all 9 takes: wording matches the script (only ASR spellings differ: "M .X." for MX, "Hurlbert", "65"). No missing or added lines.
- voice/assemble.py cuts the takes into sentences only inside real silences (>=120 ms below -45 dBFS; where two sentences had no silence between them they stay joined, 105 units for 148 sentences) and re-spaces them with designed pauses: 0.42 s between sentences, 0.65 s after questions, 0.7 s between paragraphs, 1.0–2.1 s after each self-test prompt, 2.0 s between chapters, 4.4 s for the title card, and a 4.0 s pause in the beeper section for the one soft beep. All 105 unit edges verified silent (< -45 dBFS).
- Pace: 11 units ran >15 % faster than the median (hook opening lines, "Think about your last birthday", "Think back to the beginning", "Have you ever asked them…" etc.). Re-voicing was impossible (quota spent), so they were gently slowed with Rubber Band (formant-preserving), tempo 0.90–0.95, never below 0.90.
- Result: narration 697.4 s, 1,625 words = **139.8 WPM gross** (sections 134–153 WPM). Voice chain: HPF 80 Hz, de-esser, gentle 2.5:1 compression, +1.5 dB at 220 Hz, +1 dB at 3.2 kHz.
- Optional later: if the owner wants the hook opening re-voiced at a calmer native pace instead of the 0.93 stretch, that is 1 request in the next window (15:00 CST).
| 10-29 15:01 | nb_redo1.ipynb | hm_en_redo1 (11 stretched lines re-voiced + 6 second takes, style B) | 1 | 115.1 s, wording exact; spliced with no stretch (voice_proc_v2.wav, sent_times_v2.json). 3.8 Flash 1/10 this window. |
