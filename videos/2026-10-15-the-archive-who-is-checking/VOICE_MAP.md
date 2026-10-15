# VOICE MAP: The Archive (5 characters, EN / UR / PS)

Status: **FINAL — owner approved 2026-10-15 17:24 ("go ahead with video completion").** Audition run 2026-10-15 (7 requests); cast kept. See "2026-10-15 run" below for what changed.

## Voices (names verified 2026-10-15 against the official Gemini TTS page)
Source: https://ai.google.dev/gemini-api/docs/speech-generation, "Prebuilt voices" table (30 voices, page last updated 2026-10-12). Every name below appears there with the descriptor shown. The docs table gives no gender; the gender noted is the voice's presentation in AI Studio previews (**confirm by ear in the audition**). The docs also offer an Extended Voice Library (`GET /v1beta/voices`, filterable by gender) and Voice design. Both are options if a prebuilt does not sound right, but s25 asks for prebuilt.

| Character | Voice | Docs descriptor | Why | Base style prompt (speech_metadata.style) |
|---|---|---|---|---|
| NARRATOR | **Iapetus** | Clear | Owner-fixed channel voice | `calm documentary narrator, unhurried, warm` |
| ELIZA | **Erinome** (female) | Clear | Owner: female ELIZA; a clear voice reads flat and teletype-like | `flat, mechanical, even; no emotion, like a teletype` |
| PARRY | **Algenib** | Gravelly | Grit for a tense, guarded voice; very far from Iapetus | `tense, clipped, guarded, dry` |
| CHATGPT | **Puck** | Upbeat | Eager, quick, a little too agreeable | `warm, quick, eager to please` |
| CLAUDE | **Gacrux** (female) | Mature | Measured and precise, and clearly distinct from Iapetus (narrator) and Erinome (ELIZA) | `precise, measured, quiet` |

Fallbacks (if the audition rejects one; all are on the same docs table): ELIZA → Kore (Firm) or Schedar (Even); PARRY → Fenrir (Excitable) or Orus (Firm); CHATGPT → Achird (Friendly) or Laomedeia (Upbeat); CLAUDE → Vindemiatrix (Gentle) or Sadaltager (Knowledgeable).

**Same voice in every language:** each character keeps its voice in EN, UR and PS. No pitch shifting or other transforms (s25). **ELIZA speaks English in all three tracks.** Her 1966 script answered other languages with "I AM SORRY, I SPEAK ONLY ENGLISH" (R01), so her EN take is reused in the UR and PS mixes. This is authentic and saves 2 requests.

## Per-line delivery
Each line in script_en.json carries `delivery` = base style + a short per-line tweak (for example PARRY S2-11 "Do you?": `cold, then silence`). make_cast_jobs.py sends each line as its own text item with its own `speech_metadata.style`. Per the docs, Gemini 3.8 TTS treats `text` strictly as a verbatim transcript, so **style is never read aloud**. That keeps the PLAYBOOK rule against style instructions inside spoken text. Pauses between lines use the inline `<long pause>` tag so the cutter splits on real silences (s16.2). The docs warn that long persona blocks cause voice drift, so base styles are kept to one short line.

## Model per language (DUBBING.md, plus this video's need for non-spoken per-line style)
| Language | Model | Reason |
|---|---|---|
| EN | **gemini-3.8-flash-tts** | Character acting with per-line styles needs speech_metadata (3.8 family). DUBBING's EN default (2.5) has no non-spoken style channel. The docs call 3.8 Flash best for "nuanced acting … complex multi-speaker dialogue". **Deviation from DUBBING's EN→2.5 default: owner approval needed.** |
| UR | **gemini-3.8-flash-lite-tts** | Supports speech_metadata; DUBBING verdict 2026-10-11: Urdu "equal and clean" on Lite. Note: the docs' supported-language table did not list Urdu when read 2026-10-15, but LATOON has shipped Urdu on 3.x/Lite since 2026-10-10. Keep it on the audition. |
| PS | **gemini-3.8-flash-tts** | DUBBING: Pashto → 3.8 Flash first; **2.5 fails Pashto**. "Southern Pashto" is listed on the docs table. Known shared weakness: Pashto pronunciation (ړ, ځ), rated 4/10 for Iapetus. Audition PARRY in PS. |

One model per language for the whole video, so voices never shift mid-video (s16).

## Request plan (free tier: 10 requests/day per model; reset 12:00 PKT, 13:00 PKT after 2026-11-01)
Units come from script_en.json `tts_units`: one character per request, ≤80 s, balanced.

| Batch | Model | Requests | Content |
|---|---|---|---|
| Audition (owner listens before anything else) | 3.8 Flash | 6 | 5 characters × 1 EN line + PARRY PS line |
| Audition | 3.8 Flash-Lite | 1 | CLAUDE UR line |
| EN | 3.8 Flash | 10 | narrator 1, chatgpt 1, claude 4, parry 3, eliza 1 |
| PS | 3.8 Flash | 9 | same minus ELIZA (reused) |
| UR | 3.8 Flash-Lite | 9 | same minus ELIZA (reused) |
| Redo buffer (~20%) | 3.8 Flash ≤4, Lite ≤2 | ≤6 | joins or reads that fail s16 checks |
| **Total** | | **≤41** (3.8 Flash ≤29, Lite ≤12; 3.1 and 2.5 untouched) | |

Schedule (after the owner approves the script, casting and frames; each "day" is one quota window):
- **Day 1:** audition (3.8 ×6, Lite ×1). Owner picks or approves voices.
- **Day 2:** EN on 3.8 (10/10). UR on Lite (9/10).
- **Day 3:** PS on 3.8 (9/10) + 1 redo. Lite: up to 1 redo.
- **Day 4 (buffer):** remaining redos on 3.8 (≤3) and Lite (≤1).

This fits the free tier with no model ever above 10 in a day. The daily topic Shorts are paused (s26), so 3.8 and Lite are free on those days. If the owner prefers EN on 2.5 (the DUBBING default), EN loses per-line style and moves to 2.5 ×10; the rest is unchanged.

## Tooling
- dub/make_cast_jobs.py → dub/cast_jobs_{en,ur,ps}.json + dub/cast_audition.json (built, **not run**). These are request bodies for the Interactions API (`POST /v1beta/interactions`, single-speaker, `generation_config.speech_config: [{voice}]`), one per unit.
- dub/make_nb.py hard-codes Iapetus and the generateContent path, so it can't voice this cast. A small runner (or a make_nb variant) that posts these bodies is needed. Verify on the audition that a multi-item single-speaker `content` list is accepted. The docs show multi-item only for multi-speaker; the fallback is one text item with lines joined by `<long pause>` and the base style only.
- Output is unary WAV (24 kHz mono, RIFF header) per the docs. Cut on `<long pause>` silences, place each line at its script_en.json `start`, and run the s16 checks (pace, pitch, every join).


## Pacing (owner rule 2026-10-15)
See PACING.md: normal steady dialogue speed (~140-155 wpm), proper breaks between lines (0.6-1.5 s), reject fast or accelerating takes, never speed-up audio to fit picture.


## 2026-10-15 run: docs re-check, audition, changes (owner asked 18:00 to re-check the docs before relying on old assumptions)
**Docs re-read 2026-10-15 ~18:50 CST:** speech-generation (last updated 2026-10-12), models/gemini-3.8-flash-tts (2026-10-09), rate-limits (2026-10-13), changelog (2026-10-14).
- Model names unchanged: `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts` (both GA since 2026-09-22). Prebuilt voice table unchanged (Iapetus, Erinome, Algenib, Puck, Gacrux all listed).
- Request format unchanged: `POST /v1beta/interactions`, `input[].content[]` text items with `speech_metadata.style`, `response_format {type: audio}`, `generation_config.speech_config [{voice}]`; unary output is WAV (RIFF, 24 kHz mono); audio sits in `steps[].content[]` (`type: audio`). Inline tags `<short pause>` / `<long pause>` still documented. 3.8 Flash TTS input limit 8,192 tokens.
- Rate limits: the docs no longer print per-model free-tier numbers ("can be viewed in Google AI Studio"); RPD resets at midnight Pacific (= 15:00 CST / 12:00 PKT now; 16:00 CST / 13:00 PKT after 2026-11-01). The 10 requests/day/model figure is LATOON's observed free-tier limit (DUBBING.md), not a docs number; the runner stops a model on the first `PerDay` 429.
- Changelog items that touch us: none breaking. 2.5 models are now limited to projects that used them before (2026-09-18); this video does not use 2.5.
- AI Studio web UI was unreachable from Hark's browser today (ERR_TUNNEL_CONNECTION_FAILED, twice incl. a fresh session); the API via Colab worked normally, and the listening check ran in the Gemini app (free Auto mode).

**Audition result (7 requests, 2026-10-15 17:40 CST; listening check by Gemini app "Auto", plus measurements):** all five voices kept.
- NARRATOR Iapetus: male, fits, F0 ~120 Hz. ELIZA Erinome: female, flat/mechanical, F0 ~200 Hz. PARRY Algenib: male, tense/clipped, heavy vocal fry in EN. CHATGPT Puck: fits "bright, eager" (judge heard it as female-presenting; F0 ~150 Hz). CLAUDE Gacrux: female-presenting, quiet/precise, clearly distinct from the narrator per the judge (F0 overlaps the narrator's but timbre differs). Claude UR on Lite: same speaker as EN, Urdu 9/10. PARRY PS on 3.8: "sounds authentically Pashto" 8.5/10, **but judged a different-sounding speaker from PARRY EN** (see concerns).
- Multi-item single-speaker requests (one text item per line, each with its own style) are accepted (no fallback needed).

**Changes made (judgment calls, all in dub/make_cast_jobs.py):**
1. Every style now ends with "natural conversational pace" (PACING.md); CHATGPT base style "warm, quick, eager to please" → "warm, bright, eager to please" ("quick" fought PACING).
2. Small requests: the first big units ran fast (ChatGPT's 26-line request: median 167 wpm, lines up to 300 wpm; narrator's last item sped to 230 wpm; one `<long pause>` tag was read aloud as "long pause"). All remaining and rejected lines now go in requests of <=7 lines (8 if a single line would be left over) and <=35 s estimated speech, without the `<long pause>` tag (each line is already its own text item), and with a per-speaker pace word (CHATGPT "relaxed, steady pace, never rushed"; ELIZA "slow and deliberate, every word the same weight"; others "unhurried"/"measured"). Job list: dub/redo_jobs.json.
3. Request count therefore rises: 3.8 Flash 23 EN + 23 PS (was 10 + 10), Lite 6 more UR. One model per language is unchanged (EN 3.8 Flash, UR Lite, PS 3.8 Flash).
4. Runner: dub/voice_runner.py (Colab notebook via Secret GEMINI_KEY; the sandbox host has no Gemini key), splits takes by aligning the ASR transcript to the script and cutting in the middle of the real silence between lines (s16.1), measures wpm/syllable rate/F0 per line, applies PACING, writes accepted lines only.
