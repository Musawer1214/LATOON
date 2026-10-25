# NEXT_STEPS — "Can Machines Think?" (Big Questions)

**Status: SCRIPT v1 DRAFT, awaiting owner review** (written 2026-10-18 CST; owner reviews and discusses this evening before any voice-over).
Owner said 2026-10-18 06:41 CST: no rush, quality over speed, he reviews this evening before any voice-over.

## Files in this folder
| File | What |
|---|---|
| lines.py | single source: every line (id, chapter, EN, visual note, claim ids, UR, PS). Edit here, then `python3 build_script.py` |
| build_script.py | regenerates script.json, script_en.md, dub/script_ur.json, dub/script_ps.json (timing at 155 wpm + pauses) |
| script_en.md | readable English script: chapters, numbered lines, ~timings, claim tags |
| script_en_v1.pdf | the same, as a clean PDF for the owner to read |
| script.json | lines with ids, timing, scene/visual note (language-neutral), layer, claim ids |
| dub/script_ur.json, dub/script_ps.json | line-by-line Urdu and Pashto (everyday spoken Pakistani style, technical terms in English, numbers as digits) |
| FACTCHECK.md | claim -> primary source, quote, confidence; what we deliberately don't say; re-check list |

## Numbers (v1)
- 61 lines, 9 chapters, ~1,900 spoken words, est. ~13:00 of speech + ~18 s end card (~13:20). Above the 10-12 min target (allowed "up to ~15 only if the story needs it"). Trim options for the owner below.
- Viewer prompts: viva (C1-07), who understands? (C4-07), where would you draw the line? (C5-08), what would change your mind? (C8-05).
- Thought: Ghalib, «کہتے ہیں کہ غالبؔ کا ہے اندازِ بیاں اور» (C6-07), verified on Rekhta + Pritchett.
- Local examples: Lahore chat (C0-01), viva in Peshawar/Lahore + "ratta" (C1-07, callback C4-04), Lahore monsoon (C4-09).

## Trim options if the owner wants ~11:30 (saves ~90 s)
1. C2-04 (Turing's "machines take me by surprise") ~11 s
2. C1-05 (the bet is about us) ~13 s
3. C6-04 (15-minute replication) ~9 s
4. C7-06 + C7-07 merged into one line (computation vs substrate) ~15 s
5. C5-03 (0.01% legal-move error) ~8 s
6. C3-01 to one sentence (Deep Blue) ~6 s
7. C6-07 Ghalib (only if he feels it is forced) ~15 s
8. C4-09 Lahore monsoon line ~4 s

## Questions for the owner's review (this evening)
1. Title pick (3 options in the report / below).
2. Length: keep ~13 min, or trim to ~11:30 with the list above?
3. Ghalib line: keep? Local examples (ratta, viva, Lahore monsoon): right tone?
4. Urdu/Pashto wording: he edits freely while recording; send changed lines typed so subtitles match.
5. ELIZA appears once only, as the study's baseline (C6-03). OK, or remove the name entirely?

Title options: (1) "Can Machines Think? What Turing Refused to Answer" · (2) "AI Passed the Turing Test. Does It Think?" · (3) "Can Machines Think? 75 Years of the Hardest Question in AI".

## Plan after approval (do not start before the owner approves)
1. Apply the owner's edits in lines.py -> rebuild -> mark FINAL (script.json meta.status) and log the approval here and in STATUS.md.
2. Recording PDF for the owner (Urdu first, then Pashto; numbered cards with ~seconds and mood note; tips box), like voice_own/theseus/script.html, saved in voice_own/2026-10-xx-can-machines-think/. Long-video version: split into ~6-8 short sessions by chapter so he can record over several evenings. NOT created yet (owner instruction 2026-10-18).
3. The owner records Urdu and Pashto narration himself; Hark processes per PLAYBOOK s6.2 (owner-approved mix) and sends the finished UR/PS audio to him for review before any Studio upload.
4. English narration on Gemini (Iapetus, single narrator) later, from the FINAL script only, using spare gemini-3.1-flash-tts-preview / gemini-2.5-flash-preview-tts quota (PLAYBOOK s4.5.2a), <= ~3 paragraphs per request, one model for all English; log each file in VOICE_STATUS.md.
5. Build per PLAYBOOK s5.1/s5.7 (stock first, one canvas + guided camera, Manim 3D for rooms/boards, real credited photos); image licences per FACTCHECK re-check list.
6. Teaser Shorts already queued for this video: "Could You Tell a Human From an AI in 5 Minutes?" and "The Room That Answers Chinese" (CONTENT_PLAN s3); keep their facts consistent with FACTCHECK.md (F1-F6, S1-S5).

Nothing has been voiced, rendered or uploaded. No recording PDF exists yet.

## v2 (2026-10-18 evening)
- Owner rewrote Urdu + 4 sticky notes; v2 applied in lines.py (v1 in lines_v1.py). EN/PS follow his Urdu flow. Place names trimmed; C4-09 = Searle's fire example.
- Delivered Can_Machines_Think_script_v2_UR_PS_EN.pdf (make_trilingual_pdf.py). English est ~17:43 total at 155 wpm.
- Next: owner checks v2 and records UR/PS from this PDF. Do not voice EN until he marks FINAL.

## Workflow change (owner, 2026-10-24 22:04 CST)
- Owner reads the Urdu v2 aloud (Can_Machines_Think_UR_readthrough_v2.pdf) and sends a voice recording with his updates, new dialogue and changes.
- Hark transcribes it, writes the final Urdu, then finalizes English and Pashto to follow it; owner confirms; Hark voices English (Gemini); owner records final UR/PS.
- Script is NOT final until then: no TTS, shot timings provisional.

## PRE-PRODUCTION started 2026-10-24 21:52 CST (owner: "start work on long video next in queue ... I will do Urdu and Pashto voiceovers and you do the English version")
**Script still NOT final (owner workflow change 22:04 CST: his Urdu voice read-through comes first). No TTS spent. lines.py text unchanged.**
- CONCEPT.md: per-chapter "what the viewer must SEE"; world = "The Section Model" (architect's daylight studio, plaster/card/oak/brass scale models cut in section; OUTSIDE vs INSIDE; wall-with-a-slot device; parrot/map/sand-timer/token/lit-window symbols; dusk only in C7). Distinct from The Archive's night library. Archival image list with licences (Commons, read 2026-10-24).
- VISUAL_PLAN.md: chapter plan (firm), ending (firm), render pipeline (Colab T4, NO Kaggle, 7.4b lessons), look-still notes. plan/shots.py + plan/make_shotlist.py -> plan/shotlist.md/.csv = **PROVISIONAL per-line shotlist and timings (v2 ids)**; regenerate after the final lines.py, then re-time to the real EN voice.
- Length at measured pace (Iapetus narrator 140.8 wpm, Archive): v2 speech ~19:34, total ~19:55 incl. closing hold + silent quote + 12 s end frame (the 17:43 figure assumed 155 wpm). Owner to decide length in his read-through.
- Look stills (Three.js headless, real pipeline): look/scene.html, look/cap.js, look/stills/s1-s9.png, **look/contact_sheet.jpg** (v1 sheets + scene_v1.html kept). Weak points still listed in VISUAL_PLAN s4.
- VOICE_PLAN.md: EN = Iapetus on gemini-3.8-flash-tts only, after The Archive PS is done (never 3.1/2.5); ~14-16 requests + redos, 3-4 windows. UR/PS = owner's own voice from the final recording PDF (to make after the final script), processing per PLAYBOOK 6.2, always sent to him before any upload.
- Ending (owner rule 2026-10-24): no spoken channel line; C8-05 -> ~2 s hold -> silent Turing quote card (T12) ~7 s -> silent LATOON end frame 12 s.
- WARNING: the two teaser Shorts listed above ("Could You Tell a Human From an AI in 5 Minutes?", "The Room That Answers Chinese") were DISCOUNTED by the owner on 2026-10-20 (REJECTED_IDEAS.md). Do not make them; any teaser needs a fresh owner pick.

### Next (in order)
1. Receive the owner's Urdu read-through recording -> transcribe -> final Urdu in lines.py -> EN + PS follow -> rebuild (build_script.py; set WPM=140) -> owner confirms FINAL.
2. Re-map plan/shots.py to the final ids, `python3 plan/make_shotlist.py`; make the owner's final UR/PS recording PDF (voice_own/).
3. EN voice on gemini-3.8-flash-tts once The Archive PS no longer needs it; lock timings.
4. Build chapter sets from look/scene.html; stills per chapter; then Colab render.
Owner decisions open: (a) length: keep all of v2 (~19-20 min at real pace) or cut whole beats (list above); (b) title from the 3 options; (c) optional: end on C8-04 (Turing's line) by swapping C8-04/C8-05 (order only).
