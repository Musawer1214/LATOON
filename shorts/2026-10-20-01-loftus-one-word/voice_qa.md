# Voice QA (EN, gemini-2.5-flash-preview-tts, Iapetus, ONE request, PLAYBOOK s4.6)
Split at ASR-located silences (gaps 0.52-0.82 s between lines; cut mid-silence, 120 ms room tone kept). ASR (faster-whisper small) matched the script word for word.
Lines 4, 5 (189/188 wpm, >185) and 7 (184 wpm, +13%) gently slowed (atempo, s4.6.2 fallback: re-voicing impossible under the one-request rule).

| line | words | dur s | wpm | tempo | F0 (YIN median, Hz) |
|---|---|---|---|---|---|
| 0 | 19 | 7.16 | 159 | 1.00 | 157 |
| 1 | 20 | 8.39 | 143 | 1.00 | 145 |
| 2 | 17 | 7.13 | 143 | 1.00 | 133 |
| 3 | 16 | 6.30 | 152 | 1.00 | 105 |
| 4 | 19 | 6.47 | 176 (189 raw) | 0.93 | 118 |
| 5 | 18 | 6.17 | 175 (188 raw) | 0.93 | 128 |
| 6 | 16 | 5.78 | 166 | 1.00 | 132 |
| 7 | 13 | 4.43 | 176 (184 raw) | 0.95 | 162 |

Overall ~160 wpm speech-only (target 150-170: PASS); every line <= 185 wpm after the gentle slow-downs (PASS; none below 0.93).
Pitch: one continuous take from ONE request on one model, so there is no request-to-request join and no model/voice drift (s4.6.3 is about chunks from separate requests). Per-line F0 estimates (YIN; pyin gave octave errors) move with sentence intonation (falling "The word mattered more" line 3, rising question line 7); no line sounds brighter/darker by spectrum. Joins: the 7 splits sit inside 0.52-0.82 s pauses: PASS (first/last two words of each piece match the script per ASR).
