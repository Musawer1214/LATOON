# NEXT STEPS: The Archive (state as of 2026-10-15 ~20:00 CST)

**Status: script v3 FINAL (owner approved 2026-10-15 17:24). Voicing IN PROGRESS. Nothing uploaded.**

## VOICE — state 2026-10-15 ~20:00 CST (details: VOICE_STATUS.md, VOICE_MAP.md "2026-10-15 run")
Spent in the quota window that opened 2026-10-15 15:00 CST (12:00 PKT): **gemini-3.8-flash-tts 10/10, gemini-3.8-flash-lite-tts 10/10** (no 429 was returned; the observed 10/day cap is reached by count, so no more calls on either model until the next reset). 3.1 and 2.5: 0 (not used for this video).
- Done: audition (7), EN narrator_u0/u1, chatgpt_u0, eliza_u0, UR narrator_u0/u1, chatgpt_u0, claude_u0–u3, parry_u0/u1. All ingested to dub/takes/, split, measured (dub/voice_state.json).
- Accepted so far: EN 24 lines, UR 89 lines (dub/voice/{en,ur}/lines/<id>.wav + words/<id>.json + timings.json). Everything else is rejected by PACING/s16 or not voiced yet.
- Superseded (do NOT run): cast_jobs_en.json claude_u0–u3, parry_u0–u2; cast_jobs_ps.json (all 10); cast_jobs_ur.json parry_u2. Their lines are in dub/redo_jobs.json as small requests.

### Voice jobs remaining (exact names from dub/redo_jobs.json; each window opens 15:00 CST = 12:00 PKT; 16:00 CST from 2026-11-01)
| Window opens | gemini-3.8-flash-tts (10/day) | gemini-3.8-flash-lite-tts (10/day) |
|---|---|---|
| **Fri 2026-10-16 15:00 CST** | EN: archive_en_narrator_s0, archive_en_eliza_s0, archive_en_eliza_s1, archive_en_chatgpt_s0, _s1, _s2, _s3, archive_en_parry_s0, _s1, _s2 (10) | UR: archive_ur_parry_s0, _s1, _s2, _s3, archive_ur_claude_s0, _s1 (6) — **notebook prebuilt: dub/nb_w1_2026-10-16.ipynb (all 16)** |
| Sat 2026-10-17 15:00 CST | EN: archive_en_parry_s3, _s4, _s5, archive_en_claude_s0 … _s6 (10) | UR re-voice of any UR ChatGPT/narrator line that falls outside +-15% of its new EN line (<=4) |
| Sun 2026-10-18 15:00 CST | EN: archive_en_claude_s7, _s8, _s9 (3); PS: archive_ps_narrator_s0, _s1, _s2, archive_ps_parry_s0, _s1, _s2, _s3 (7) | spare |
| Mon 2026-10-19 15:00 CST | PS: archive_ps_parry_s4, _s5, archive_ps_chatgpt_s0 … _s3, archive_ps_claude_s0 … _s3 (10) | spare |
| Tue 2026-10-20 15:00 CST | PS: archive_ps_claude_s4 … _s9 (6) + up to 4 redos | redos |
| Wed 2026-10-21 15:00 CST | buffer: redos only | redos |

How to run a window (resumable): `cd dub && python3 voice_runner.py nb nb_<date>.ipynb <job names>` (skips jobs already done) → browser session "google-aistudio": Colab > Upload notebook > GEMINI_KEY notebook access ON > Run all > copy the whole output → save as dub/logs/<nb>_output.txt → `python3 voice_runner.py ingest dub/logs/<nb>_output.txt` (download within 60 min: tmpfiles links expire) → `python3 voice_runner.py asr-take <job>` (one per command, ~30-60 s each) → `python3 voice_runner.py analyze <job>` → `python3 voice_runner.py timings en|ur|ps`. A rejected line goes back into redo_lines.json → `ARCHIVE_SMALL=1 python3 make_cast_jobs.py` rebuilds redo_jobs.json. Sandbox resets lose pip installs: `pip install numpy scipy faster-whisper` first (whisper models cached in /workspace/work/whisper_models). If a model returns PerDay 429 the notebook skips it: stop, wait for the reset. Stop and report after 2 failed loops on the same line or voice.

### After all takes pass
- [ ] Listen to every join (2 s windows) and log PASS per join in QA.md (s16.5); compare per-take F0/centroid (s16.3) — flagged so far: UR claude_u2 (F0 130 vs ~146 Hz) and UR parry_u1 (106 vs 121 Hz), both already queued for re-voice.
- [ ] `voice_runner.py timings en|ur|ps` → dub/voice/<lang>/timings.json (PACING gaps: 0.75 s between speakers, 0.4 s same speaker, 1.2 s after questions/records/prompts, 1.75 s scene changes, owner holds incl. 2.5 s Minab). ELIZA's EN takes are reused in UR/PS.
- [ ] Hand to the visuals side: `director.attach_voices(shotlist, "dub/voice/en/words", "dub/voice/en/lines")` and re-time blocking from timings.json. **shotlist.json has no beats for the new intro lines S1-00x2..x6 yet** (needs a roll-call beat per character).
- [ ] Projected runtime with measured pace and PACING breaks: **about 13:30–14:00** (script-model estimate 11:47; measured speech runs ~10–15% longer than the model, and the PACING gaps are longer than the model's 0.35 s breaths). Owner lines stay; flag the length to the owner.

## FIX PASS on the weak shots — state 2026-10-15 ~17:15 CST (details: VISUAL_PLAN §0c)
Owner approved fixing the weak shots now. Done, no TTS, nothing uploaded, script files untouched, logos off:
- [x] S2-03 re-framed (high reverse, both visitors full figure, PARRY silhouette foreground); S3-05 re-blocked (three separate silhouettes); E-01 re-framed (readable card close-up, then a clean wide with everyone in full figure) and the card shows the 1966 quotation verbatim from script v2; E-03 lifted (mean luma 11.8 → 19.9/255, still night); S5-08 re-rendered with the fitted plate.
- [x] PARRY deep muted brick red everywhere (not pink); corridor rebuilt so he writes behind his desk three-quarter to camera; visitors flank the desk; ChatGPT no longer cut in the hero; same fix in S2-01..S2-07.
- [x] Minab: the 2.5 s hold was already inside script v2's timing (runtime unchanged, 11:01.9); it is now an explicit `pause` event in the shot list (silence, no subtitle, no plate, static frame) and the Record plate comes after it.
- [x] Whole animatic re-rendered on the Kaggle T4 (kernel `archive-render-fixv2`, 19.5 min kernel wall): `viz3d/frames/animatic_540p_placeholder_v2.mp4` + `animatic_contact_sheet_v2.jpg`; corridor hero re-rendered at 1080p (`E_hero_corridor_1080p.png`); before/after board `viz3d/frames/fix_pass_before_after.jpg`. Kaggle GPU used in total today: about 38 min of kernel wall.
- [ ] Owner: watch `animatic_540p_placeholder_v2.mp4`; note anything still off per shot id. Known weak (VISUAL_PLAN §0c): candle bloom beside PARRY's face in the front corridor shots, Claude's back still pale terracotta there, S2 front shots look alike, hero hides PARRY's pen hand.

## Direction E PRODUCTION PASS — state 2026-10-15 ~15:30 CST (details: VISUAL_PLAN §0b)
Owner approved the visuals ("you are good to go on visuals", quality over schedule). Done, no TTS, nothing uploaded to YouTube:
- [x] Every set built as its own stage with a practical-first light rig and its §3 camera language: hall, door, PARRY's corridor, gallery rail, ELIZA's room, the table, the three sheets, the drawer (`viz3d/sets.py`).
- [x] S1-S6 + epilogue blocked as data: `viz3d/shotlist.json` (35 shots, 116 beats, emotion key per character per beat, big gestures, looks, Record/prompt events, per-word mouth hook) from `viz3d/blocking.py`; `viz3d/director.py` renders it.
- [x] Renderer polish: RSM one-bounce GI (6 VPLs from the key practical), soft facets + wrap, PARRY hunched writing pose with pen, taller/dimmer ELIZA; logos stay a switch (`--logo on|off`), everything previewed with no logo.
- [x] GPU-portable: `glctx.py` (REQUIRE_GPU=1 aborts on llvmpipe), `render_shot.py`, `viz3d_bundle.tar.gz`, `requirements_viz3d.txt`, `GPU_RENDER.md`.
- [x] Kaggle GPU tested end to end (`kaggle_render.py`): private dataset `musawerhussain/archive-viz3d-bundle`, private kernels `archive-render-bench` and `archive-render-hero`; Tesla T4 renders 1080p at **0.33-0.34 s/frame** (CPU sandbox about 6-12 s), so the whole film is about 1.8 h of T4 time. Benchmark + hero kernels: about 3 min of kernel wall time.
- [x] 540p animatic (11:02, placeholder timing, no voice; S1-S2 on sandbox CPU, S3-end on Kaggle T4 after a sandbox reset killed the CPU job) + contact sheet + three 1080p hero stills + polish before/after in `viz3d/frames/`. Kaggle GPU used in total: about 18 min of kernel wall time.

Next for E:
- [ ] Owner: pick logos on or off (v1 animatic superseded by v2, see the fix pass above).
- [ ] After voices are FINAL: ASR word timings per line -> `director.attach_voices(shotlist, words_dir, wav_dir)`, re-time blocking from the measured durations (keep the 2.5 s Minab hold after S5-22: blocking.py turns `hold_after` into the `pause` event), then render finals on Kaggle in shot batches (`kaggle_render.py run --jobs ...`, about 1.8 h of T4 for 1080p30; the weekly quota is 30 h).
- [ ] Remaining visual gaps (VISUAL_PLAN §0b/§0c): unshadowed/subtle GI, no finger rig, ELIZA sit pose, small gallery plaques, TEMP sound bed, the fix-pass leftovers listed in §0c.

## Direction E (owner chose it, final) — state 2026-10-15 ~09:15 CST
Look work done in code (VISUAL_PLAN §0): our renderer now reaches E1's night/candle mood. For the owner's review:
- `viz3d/frames/E_table_hero_logo.png` vs `E_table_hero_nologo.png` — **owner picks logos on or off.**
- `viz3d/frames/E_compare_vs_E1_E2.jpg` (ours beside E1/E2), `viz3d/frames/E_hall_walk.png` (E2 composition), `viz3d/frames/E_motion_test_10s.mp4` (+ `E_motion_test_10s_contact.jpg`) (1080p30; walk → hop onto chair → lip-synced line calm→concerned → ChatGPT saddens; temp code-made sound bed + borrowed narration line, both TEMP in SOURCES_MEDIA #5–6).
- Remaining gaps listed honestly in VISUAL_PLAN §0 (no GI, crisp CG facets, PARRY standing not writing, hall darker than E2, small gestures).

Next for E (after the owner's notes):
- [ ] Apply notes; block S1–S6 shots in eshots.py style (one stage per set: hall, PARRY's corridor, gallery rail, ELIZA's room, the table, the three sheets, the drawer), each with its own practical-first light rig and camera move from §3.
- [ ] Drive mouths from the final voice files (per-word gate via `envelope2(words=...)` once ASR timings exist), emotion keys per script beat.
- [ ] Real mix per VISUAL_RESEARCH §6 (licensed rain/room tone/candle or keep code-made beds; silence at Minab).
- [ ] Renderer polish if time allows: a cheap one-bounce GI approximation (light probes / reflective shadow map from the candle), softer facet shading option, PARRY writing pose.

### Option: render the final film on a free cloud GPU — DONE on Kaggle 2026-10-15 (see the production-pass section above; notes below kept for history)
- **Why:** the sandbox renders E frames on 2 ARM CPU cores with Mesa llvmpipe: ~6 s per 1080p frame (measured: 5.9 s/frame mean over the 300-frame 10 s test, ≈30 min), so an ~11 min film (~19,800 frames) is ~32 h of CPU, plus re-renders after notes. The same arc3d code is plain OpenGL 3.3 through moderngl, so it runs unchanged on an NVIDIA GPU; for a rasteriser like this the GPU should be one to two orders of magnitude faster (estimate, not measured here).
- **Known catch (Colab, documented):** inside Colab's container `moderngl.create_context(standalone=True, backend="egl")` silently picks **Mesa (CPU)** even on a GPU runtime; installing the NVIDIA GL userspace that matches the driver (`apt install libnvidia-gl-535` or the version `nvidia-smi` shows) made the EGL context report `NVIDIA Corporation`; an Xvfb + `__GLX_VENDOR_LIBRARY_NAME=nvidia` workaround also worked. Source: moderngl issue #665, https://github.com/moderngl/moderngl/issues/665 . Kaggle uses a similar Docker setup; untested there.
- **Plan if the owner wants it:** a notebook that pip-installs `moderngl numpy pillow scipy cairosvg scikit-image shapely mapbox_earcut`, installs the matching `libnvidia-gl-*`, asserts `ctx.info["GL_RENDERER"]` is the GPU (fail loudly if it says llvmpipe), pulls viz3d/ from a private copy, renders frame ranges, and returns PNGs/MP4. Needs the owner's Kaggle API token in the vault (Kaggle internet requires a phone-verified account). Verify one frame is pixel-identical-ish to the sandbox render before a full run.

## Waiting on the owner (HISTORY: items 1, 3, 4, 5 resolved 2026-10-15 17:24 — owner approved script, casting, ELIZA English-only and FINAL; logos on/off still open)
1. Script review: script_en.md **v2** (owner lines verbatim + 3 approved fixes; additions tagged [ADDED]; 1,537 words, ~11:01). Diff and decisions: SCRIPT_RECONCILE.md. Facts: FACTCHECK.md (additions: WaPo/NBC Claude record, Pentagon dropped Claude, Palantir CTO dispute, Bloomberg "not clear why").
2. Look: **superseded by Direction E** (owner chose E; see the section above). Old style frames viz3d/frames/style_*.png kept for history.
2b. CHARACTERS v2 (2026-10-15, VISUAL_PLAN §2b): char_turnaround.png, char_{claude,chatgpt,eliza,parry}_closeup.png, style_table_v2.png, motion_test_characters_6s.mp4 (walk + lip-synced talking beat; temp borrowed narration audio), rig_test_walk_lineup_540p.mp4. Owner to approve the four designs (esp. PARRY's angular head and ELIZA's typed-text face) and the motion personalities.
3. Casting: VOICE_MAP.md voices (Iapetus / Erinome / Algenib / Puck / Gacrux), and EN on 3.8 Flash (deviates from the DUBBING EN→2.5 default).
4. ELIZA English-only in UR/PS tracks (authentic to her 1966 script): OK?
5. Then the owner sets VOICE_STATUS.md to FINAL. Until then automated sweeps must not voice it.

## After approval
- [ ] **PACING.md is binding** (owner 2026-10-15): steady 140-155 wpm, reject >165 wpm or speed-ups, proper breaks, never time-compress voice.
- [ ] Audition, 7 requests (dub/cast_audition.json): write a small Interactions-API runner (make_nb.py is Iapetus/generateContent only). Verify that a multi-item single-speaker content list is accepted.
- [ ] Voice EN 10 / UR 9 / PS 9 over ~3 quota days (VOICE_MAP request plan); s16 checks on every join.
- [ ] Character production pass: re-block background characters in two-shots (PARRY/ELIZA hidden in the motion test), bigger readable gestures, a phoneme or per-word timing track from the final voice files to drive mouths (rig takes any 0..1 curve), more emotions per beat (ChatGPT overconfident grin, PARRY scared, ELIZA flat) as the script needs; S5 table blocking with all four.
- [ ] Production render: rerun viz3d/setup_gl.sh (the sandbox loses apt/pip installs), then build all shots in shots.py from scene_design.json + script timings. Fix the self-review notes in VISUAL_PLAN §4. Render in background chunks (~8–10 h with plate reuse).
- [ ] Record plates for every real fact (record_insert.py); SOURCES_MEDIA.md for any licensed image.
- [ ] Mix: no music or effects S5-22→S5-30; 2.5 s pause after the casualty line (shot list `pause` event in S5-08: total silence, not even room tone).
- [ ] Re-check before upload: FACTCHECK.md checklist (Pentagon report, Bloomberg/Palantir, OHCHR page, NBC page, Microsoft review).
- [ ] Title: owner picks at publish.
