**2026-10-26 04:54 CST OWNER REVERSAL: "for this video 168 is good".** KEEP the first Lite pass (50/52 cards, ~168 wpm) as the final English narration. Do NOT re-voice at 145 (the 04:51 note below is cancelled for this video). Only voice the last 2 closing cards on Lite Iapetus in the 15:00 CST window, matching the existing pace (~160-175 wpm), then assemble the full narration and QA.

**PACE DECISION 2026-10-26 04:51 CST (owner: "145 WPM on all video"):** the first Lite pass (50/52 cards, ~168 wpm, run of 04:40 CST) is TOO FAST and is REJECTED as final. Re-voice ALL 52 cards on gemini-3.8-flash-lite-tts, Iapetus, at a target of 145 wpm per card (accept 138-152 wpm), steady across the whole video. Ask for slower delivery in the style prompt (calm documentary narrator, unhurried, clear pauses between sentences) rather than time-stretching; never speed up, and do not stretch 168->145 (too much). Keep the 168-wpm takes only as a fallback reference. Measure wpm per card with ASR word timings (speech only, excluding leading/trailing silence) and re-queue any card outside 138-152.

**MODEL DECISION 2026-10-26 04:35 CST (owner, overrides below):** English narration of v3 is voiced on **gemini-3.8-flash-lite-tts, Iapetus, for the WHOLE video** (one model throughout, never mixed). Lite's quota is free since The Archive UR finished 2026-10-24, so it starts in the next window (15:00 CST) without waiting for the Archive Pashto lines on 3.8 Flash. Do NOT pre-voice this video on 3.1/2.5 or 3.8 Flash. First request = a short audition (2-3 cards) to confirm pace (~140 wpm) before the rest.

# VOICE PLAN — "Can Machines Think?" · v1 2026-10-24

Owner 2026-10-24 21:52 CST: "I will do Urdu and Pashto voiceovers and you do the English version."
Owner 2026-10-24 22:04 CST (workflow change): he reads the Urdu v2 aloud and sends a voice recording with revisions, new dialogue and
updates -> Hark transcribes it and writes the final Urdu -> English and Pashto are finalised to follow it -> owner confirms -> Hark voices
English on Gemini -> owner records the final Urdu and Pashto. **Nothing is voiced before his confirmation. No TTS spent so far.**

## A. English (Hark, Gemini TTS)
- Voice: Gemini prebuilt **Iapetus**, single narrator, natural conversational delivery, no style words inside the spoken text.
- Model: **gemini-3.8-flash-tts** for ALL English of this video (one model per language per video), used only AFTER The Archive's Pashto
  voicing is finished on 3.8 Flash (its NEXT_STEPS estimate: PS windows through ~2026-10-26..10-28, mix ~10-28/29). **Never
  gemini-3.1-flash-tts-preview or gemini-2.5-flash-preview-tts for this video** (those are the Shorts' models).
  Note: PLAYBOOK s4.5 2a still says spare 3.1/2.5 quota could pre-voice this video; the owner's long-video instruction for this video
  (3.8 Flash only) overrides it; PLAYBOOK line to be aligned when he confirms.
- Route: Colab notebook (dub/make_nb.py pattern or The Archive's dub/voice_runner.py), session "google-aistudio", Secret GEMINI_KEY;
  results back via tmpfiles links (download at once). Quota ~10 requests/day/model, window opens 15:00 CST (16:00 CST from 2026-11-01);
  stop at a 429, never force, pay or use another account.
- Requests: <= ~3 paragraphs (~60-90 s) each, split on chapter/line boundaries. v2 = 61 lines / 2,583 words ≈ 18.5 min of speech at
  140 wpm -> **~14-16 requests first pass** (2 windows), plus redos for flagged lines (Archive history ~30-40% first-pass flags) ->
  **plan 3-4 daily windows** of 3.8 Flash, once The Archive PS is done. Recompute from the final script.
- Prompt text per request: the lines verbatim, joined with their script pauses as plain paragraph breaks; one short director note in the
  system/style field only (calm documentary narrator, ~140 wpm, clear pauses before numbers), never in the spoken text.
- Checks per line (voice_runner-style): ASR first/last two words match; 135-155 wpm target (hard max 165, re-voice > 15% over median);
  pitch within ~8% of the median; cut only inside real silences >= 250 ms with >= 120 ms room tone; never speed up (max 1.05),
  slow-down no lower than 0.90 only if re-voicing is impossible. Numbers/years read right (73 percent, 1843, 2026, "one in ten thousand",
  "Mary Lee Pfeiffer", "LLaMA 3.1", "GPT-4.5", "PNAS"); names: Lovelace, Babbage, Kasparov, Lee Sedol, Searle, Bengio, Ghalib.
- Mastering: high-pass 80 Hz, gentle de-ess, light compression, warmth EQ, loudnorm -14 LUFS / -1 dBTP. Log every request and file in
  VOICE_STATUS.md (create at first voicing) and the DUBBING.md spend log.
- Lock: when all lines pass -> timings_LOCKED json + joined track -> export film.json -> render (VISUAL_PLAN s5).

## B. Urdu and Pashto (the owner's own voice)
- Source text: **Can_Machines_Think_script_v2_UR_PS_EN.pdf** (trilingual v2, in this folder) and the Urdu read-through PDF
  **Can_Machines_Think_UR_readthrough_v2.pdf** (make_ur_reading_pdf.py, built 2026-10-24 for his draft read). He records the FINAL
  Urdu/Pashto only after the final script is written from his read-through; a final recording PDF will then be made (Urdu first, then
  Pashto; numbered cards with ~seconds and a mood note; tips box), saved in voice_own/2026-10-xx-can-machines-think/, split into ~6-8
  sessions by chapter so he can record over several evenings.
- Recording tips (on the PDF): quiet room, fan off, phone 15-20 cm slightly to the side, 2 s between lines, repeat the whole line after a
  mistake, say the card number before each line (e.g. "C4-02"), send any changed lines typed so subtitles match.
- Processing (PLAYBOOK 6.2, owner-approved Theseus v3 mix): faster-whisper transcription, cut retakes/false starts, keep his wording;
  double high-pass 110 Hz, -5 dB @180, -3 dB @350, +3 dB @3k, +1.5 dB @6k, afftdn, de-ess 0.35, comp -22 dB 2.5:1, LP 11 kHz,
  ~-17 dB RMS/line; same bed + SFX as EN; full mix -14 LUFS / -1 dBTP.
- Timing: the picture is timed to English; each UR/PS line is placed at its EN line start and may wait if the previous line still runs
  (The Archive's place_dub.py method); a UR/PS line that runs far past its shot gets a held visual in the EN edit if needed (decided once
  all three exist). Speech must end before the closing quote card.
- **Always send the finished UR and PS audio to the owner for review before any Studio upload** (main-channel tracks or LATOON Urdu /
  LATOON Pashto uploads). Subtitles come from the final script plus his spoken changes, not ASR.
