# Enigma long video, v2 plan (state at end of the 2026-10-10 17:00 run)

Why v2: during the run the owner set new rules (PLAYBOOK "Cadence, length and consistency", 20:57 CST; OWNER_NOTE.md): long videos at least 15 minutes, Iapetus voice only, premium polish, no deadline, roaming watermark, Urdu+Pashto versions at publish. The 7:40 v1 (Iapetus, script.json, 23 paragraphs) was NOT delivered.

Done:
- script_v2.json (36 paragraphs, 2,026 words, 15 sections: hook, origins, machine, mirror, poland, escape, crib, bombe, habits, shark, lever, secret, turing, lesson, close). Facts checked (sources in mk_script_v2.py header + description.txt). Paragraphs that are unchanged from v1 keep their v1 scenes.
- Gemini notebook for v2 narration: /workspace/latoon/dub/enigma2_en.ipynb (7 chunks, gemini-3.8-flash-tts, groups in gem2/groups.json). 3.8 quota for 2026-10-10 is used up; it resets 12:00 PKT.
- Engine, images (img/, credits.json), v1 scenes (src/scenes_a-d.py), thumbnails thumb_A/B/C.png, description/metadata (v1 chapters), audio.py, docs.py, watermark_deliver.py (top-right/bottom-right because the chapter tag sits top-left).

To do (2026-10-11 run):
1. Run enigma2_en.ipynb in Colab (session google-aistudio). If any chunk 429s on 3.8, rerun only that chunk on gemini-3.1-flash-tts-preview. Download each mp3 via the real link on the tmpfiles page (grep "https://tmpfiles.org/dl/<token>/..."), browser User-Agent.
2. cp script_v2.json script.json; adapt gem/split.py and gem/words.py to gem2 (7 chunks) -> vo/pNN.wav, durs.json, words.json.
3. timeline.py: new SCENE_PARAS for the 15 sections (paragraph indices from script_v2.json); scenes keep B(i, frac) indexing per section, so update index use where paragraphs were inserted (poland now 5 paras; machine P3 longer; bombe P3 longer).
4. New scenes: origins (radio mast/wireless photo + frequency-analysis bar chart + Scherbius patent/1923 commercial Enigma), poland doubled-key chains (6-letter indicators, 1-4/2-5/3-6 links, cycle loops), escape (map-free: route card Warsaw -> Romania -> France, Różycki portrait with 1942, Lamoricière note), habits (keyboard with neighbouring-key cillies, Herivel square grid), shark (U-boat PD photo, M4 four-rotor photo "Bletchley_Park_Naval_Enigma_IMG_3604.JPG" check licence, U-110/U-559 dates, dark-months calendar), secret (1974 stamp, sealed file), turing (1936 tape machine drawing, ACE, 1950 question, £50 note only if a licensed image exists; otherwise portrait + dates). Find licensed Commons images via /workspace/work/enig/cs.py; add to credits.
5. Total must be >= 15:00. If short, add a researched paragraph (never padding).
6. Preview contact sheets, fix, render (2 workers), audio.py, master to -14 LUFS, concat, mux, python3 src/watermark_deliver.py master.mp4 /workspace/work/upload/enigma_1080.mp4 (CRF 20, maxrate 4.5M; must be < 200 MB).
7. docs.py (titles for new sections), update description chapters, metadata end-screen time, thumbs ok. topics_log row DELIVERED, AWAITING UPLOAD; send owner the MP4.
