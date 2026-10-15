# VISUAL RESEARCH: The Archive — how to make it look and feel like the script

Status: RESEARCH FOR OWNER DECISION (2026-10-15). Nothing here changes the script, VOICE_STATUS or the existing viz3d code. No TTS spent, nothing uploaded, no paid generation used.
Concept frames: `concept/<direction>/` (12 stills + one parallax motion test). Overview: `concept/CONTACT_SHEET.jpg`.
Fixed for every direction: **ChatGPT is BLUE** (cobalt `#2456D6`–`#2F6BFF`). Because blue is taken, every direction moves **Claude to warm terracotta `#D97757`** (the original master gave Claude silver-blue, which would now clash with ChatGPT). Owner to confirm.

---

## 0. Short answer

- **What the story is about:** not "AI is dangerous" but *the illusion of understanding and the diffusion of responsibility*. A machine can return words that feel like care or certainty; only a person with time, authority and the power to say no can decide whether to trust them. The archive is a mirror. The film ends by handing the question to the viewer.
- **Why the tests felt wrong:** the cute chibi mascots, candy-coloured book spines and golden-hour library say "children's adventure / brand mascot". That tone works for S1–S3 jokes but cannot carry Scene 4's melancholy or Scene 5's Gaza / surveillance / Minab passage, and the real company logos on the characters' chests sit right next to war claims (both a tone problem and an editorial risk).
- **Five directions** (A–E below). **Recommended: D, "The Paper Archive" (handmade miniature / clay-and-paper figurines, after Rithy Panh's *The Missing Picture*)**, built as free open-model or Hark-generated stills, animated in code with depth parallax, light and particles. **Runner-up: E, the upgraded current 3D pipeline** (it already exists, runs fully in the sandbox, and with sound, music, darker lighting and restrained acting it gets meaningfully closer; honest ceiling below).
- **The single biggest upgrade in every direction is sound** (room tone, rain, typewriter, the match, silence at Minab, a sparse score). Plan in §6.

---

## 1. Emotional read

### 1.1 Core theme
The owner's own final position (Idea.pdf §9): *"A machine may give an answer. It takes a person — with enough information, authority and time — to decide whether to trust it."* Three ideas run under every scene:
1. **Feeling understood ≠ being understood** (ELIZA, S4). The machine is a mirror, not a witness (S5-21).
2. **Certainty ≠ correctness** (PARRY's arc: "I can be certain long before I am right", S5-34; ChatGPT's "You are absolutely right" sycophancy beat).
3. **Many hands ≠ no one accountable** (S5-29/30). "Human in the loop" can mean someone was merely *present*.

So the film is about **trust, illusion and accountability**, told by machines who are each implicated: ChatGPT too agreeable, Claude precise but *named in the record*, PARRY suspicious, ELIZA purely mechanical. Nobody is the hero; the viewer is the one left holding the question. The visuals must therefore feel **human, quiet and grave underneath a curious, sometimes funny surface**, and must be able to go completely still.

### 1.2 Scene-by-scene arc (tension 0–10)

| Scene | What the viewer should feel | Tension | Turning point | Visual temperature |
|---|---|---|---|---|
| **S1 The Archive** (0:00–0:55) | Hush, wonder, small in a vast place. Curiosity, not triumph. | 2 | "I thought we were the beginning." / "Just the latest chapter." Humility enters. | Near-dark; one match; dust. |
| **S2 The Corridor** (0:55–2:35) | Unease, being watched; dry humour (the $399.29 bill, the coin toss). | 4 → 5 | "Do you?" (1 s hold): the accusation turns on the visitors. | Red-amber behind glass; cold reflections. |
| **S3 The Long Way Here** (2:35–4:15) | Orientation, lineage, slight awe; then a warning ("confidently wrong"). | 3 → 4 | "Sounding like a person is not the same as deserving trust." | Brass rail, soft ticks; rules turning into a lattice. |
| **S4 ELIZA's Room** (4:15–5:40) | Tenderness and melancholy; the comfort is real, the understanding may not be. Weizenbaum's unease ("a certain danger lurks there", 1966). | 4 → 5 | "The comfort may be real. The understanding may not be." | Warm lamp vs cold rain: the most intimate scene. |
| **S5-A The promise** (5:40–6:44) | Warmth, hope, real gains (AlphaFold), then a dent (METR). | 3 | "Sounding helpful does not prove the help worked." | Warm, faster rhythm. |
| **S5-B The pipeline** (6:44–8:18) | Creeping chill; bureaucratic vertigo; the machines realise they are part of systems. Claude's own name appears. | 6 → 7 | "You assume that." / "You were inside that system." | Light cools; the archive becomes an office. |
| **S5-C The agreeable mirror** (8:18–9:02) | Uncomfortable laughter: ChatGPT agrees without checking. | 5 | "A model that agrees with everyone is a mirror, not a witness." | ChatGPT's blue borrows PARRY's amber, then returns. |
| **S5-D Minab** (9:02–10:56) | Grief and gravity. Silence. No music, no effects, no cuts to harm. The audience must *sit* with it. | **9 (peak)** | Casualty line → real pause. "Many hands were involved. That does not mean no one is accountable." | One candle. Locked frame. Characters dimmed. |
| **S5-E After** (10:56–11:05) | The question hangs; light returns only halfway. | 7 | "Oversight is not a checkbox." / PARRY's admission. | Half light. |
| **S6 What We Know** (11:05–12:00) | Sober clarity: known / disputed / unknown. Not comfort, not despair. | 5 | ELIZA's "What does that suggest to you?" lands as the viewer's question, not her insight. | Three hanging sheets; reverse dolly. |
| **Epilogue: The Open Drawer** | Quiet implication: it's been the same label for 60 years; the machines just got more convincing. A call to check. | 4 | A human hand opens the drawer. | The only human presence in the film. |

**Shape:** a slow curiosity ramp (S1–S3), an intimate dip (S4), a long climb through S5 to a silent peak at Minab, then release into clarity, not resolution. The visuals need *dynamic range of tone*: playful enough for the bill joke, still enough for Minab. That range is exactly what the chibi tests lacked.

### 1.3 Where the current tests failed the feeling (candid)
Looking at `viz3d/frames/` (char_*.png, style_*.png, motion tests):
1. **Tone of the characters.** Bouncy chibi bodies with emoticon faces (^ ^, pixel smiles) read as kids' content or an app mascot. They can do S1–S3 comedy, but at Minab a smiling cloud with a toe-bounce idle is wrong even when it stands still; the design itself says "don't take this seriously". **Yes: the cute chibi approach is tonally wrong for the Gaza / Lavender / Minab passage** as currently designed. It can be rescued only by changing proportions, faces and acting (Direction E).
2. **Logos on chests.** The real OpenAI blossom and Claude spark on the bodies turn the characters into corporate spokes-mascots, which the master explicitly rejects ("fictional representations … not company spokespeople"). Worse, during S5-11 to S5-26 they place brand marks beside allegations about war. Recommend: identify by colour, name in subtitles/first-appearance caption, logo only on a one-time ID card if at all.
3. **Palette.** Saturated pink/teal/saffron spines plus golden-hour god rays everywhere = cosy fantasy library (Harry-Potter feel), no darkness to retreat into. The script's own picture plan asks for near-dark openings, a single candle and light "returning only halfway". The owner's channel colour refs were applied as a rule; for this video they should be an accent at most.
4. **Lighting and camera.** Even, bright, many practicals; every shot lit for clarity rather than mood. Few silhouettes, little negative space, no single-source scenes.
5. **Fact vs fiction plate idea was right** (monochrome engraved Record plates breaking into the scene). Keep it in every direction.
6. **Not wrong:** the rig work (walks, blinks, lip-sync) is solid engineering; Direction E reuses it.

---

## 2. Reference works and what to take from each (watch-notes from articles and interviews)

| Reference | What it teaches for The Archive | Source |
|---|---|---|
| **Orson Welles, *The Trial* (1962)** | Shot in the abandoned Gare d'Orsay; Welles: "the story is all about people waiting, waiting, waiting for their papers"; vast spaces emphasise helplessness; 850 typists in one hall ("I want it to run to the end of the world"). → S1 scale, S5-B "many hands" hall. | https://www.wellesnet.com/trial%20bbc%20interview.htm ; https://en.wikipedia.org/wiki/The_Trial_(1962_film) ; https://www.perisphere.org/2023/04/14/you-must-have-done-something-orson-welles-the-trial/ |
| **Terry Gilliam, *Brazil* (1985)** | Bureaucracy so big "the right hand never knows what the left is doing"; pneumatic tubes raining paperwork; Norman Garwood's retro-futurist design. → the pipeline as paper flowing between desks. | https://www.bfi.org.uk/lists/brazil-terry-gilliam-influences ; https://www.wideanglecloseup.com/Brazil_ScriptAnalysis.pdf |
| **Alain Resnais, *Night and Fog* (1956)** | Resnais feared a flood of horror images would numb; he counterpointed calm moving camera through *empty present-day places* with archive. Restraint and absence carry the weight. → Minab: empty table, one candle, a record, no reenactment. | https://www.criterion.com/current/posts/4154-night-and-fog-the-never-ending-cries ; https://holocaustmusic.ort.org/memory/holocaust-film/night-and-fog/ |
| **Rithy Panh, *The Missing Picture* (2013)** | Static carved clay figurines in dioramas replace images that don't exist; Panh: "My figurines don't move … We're the ones moving, creating the atmosphere." Handmade humility makes atrocity speakable without spectacle; archive footage interrupts as the "official" record. → the core of Direction D. | https://www.newwavefilms.co.uk/assets/905/the_missing_picture_pressbook_no_footer.pdf ; https://www.bfi.org.uk/sight-and-sound/reviews/film-week-missing-picture ; https://www.fastcompany.com/3027819/the-power-of-constraints-how-missing-picture-used-clay-figures-to-reenact-cambodias-nightmar |
| **Ari Folman, *Waltz with Bashir* / *Flee*** | Animation substitutes for missing footage and protects people; a cut to real archival material lands as "this is not fiction". → if real archival photos are used, cut to them sparingly and abruptly, never animate them. | https://www.documentary.org/column/waltz-bashir-fallibility-yet-persistence-memory ; https://theconversation.com/flee-animation-is-a-powerful-medium-for-documentaries-about-conflict-and-refugees-177004 |
| **Forensic Architecture** | Models as "operative devices": cones of vision show what is *in and out of frame*, i.e. how much is known; timelines as the master frame. → Direction C, and the KNOWN / DISPUTED / UNKNOWN beat. | https://www.forensicarchitecture.org/methodology/3d-modelling ; https://mubi.com/en/notebook/posts/remains-to-be-seen-the-video-work-of-forensic-architecture ; https://www.cjr.org/the_media_today/qa_omar_ferwati_forensic_architecture_israel_gaza.php |
| **Hito Steyerl, *How Not to Be Seen* (2013)** | Visibility as a function of resolution and filters; "war is invisible"; satirical calm robot voice against serious content. → the surveillance beat (S5-12/13). | https://www.moma.org/collection/works/181784 ; https://www.tandfonline.com/doi/full/10.1080/14680777.2017.1326564 |
| **Refik Anadol, *Archive Dreaming* (2017)** | 1.7 M documents of the SALT / Ottoman Bank archive sorted by ML into a navigable point cloud; the archive "dreams" correlations. → S3 lattice, and an archive that becomes data. | https://refikanadol.com/works/archive-dreaming ; https://www.creativeapplications.net/project/archive-dreaming/ |
| **DreamWorks, *The Wild Robot* (2024)** | Sanders: a normal CG look "would play too young"; they painted every surface so a robot story could be a "sophisticated tone poem". → the precise diagnosis of the chibi tests, and Direction B. | https://www.latimes.com/entertainment-arts/awards/story/2025-02-12/wild-robot-chris-sanders-a-visual-tour ; https://www.polygon.com/animation-cartoons/446701/the-wild-robot-chris-sanders-interview-animation/ ; https://beforesandafters.com/2025/01/10/if-you-want-a-painterly-bush-paint-the-bush/ |
| **Fortiche, *Arcane*** and **Sony, *Spider-Verse*** | Painted textures projected on 3D; FX animated on twos; NPR compositing as a post-process ("showing the hand of the artist without painting every pixel"). → a code-side painterly pass is possible. | https://80.lv/articles/arcane-artists-show-how-they-combine-traditional-art-3d-for-backgrounds ; https://dl.acm.org/doi/fullHtml/10.1145/3587421.3595463 |
| **Cartoon Saloon, *Wolfwalkers*** | Two line languages: the town in rigid 1650s woodcut (a "cage", no sky), the forest in loose watercolour. → S5-B institutions in woodcut, S4 warmth loose. | https://www.cgw.com/Publications/CGW/2021/Jan-Feb-March-2021/Between-Two-Worlds.aspx ; https://variety.com/2020/film/spotlight/wolfwalkers-tomm-moore-1234768028/ |
| **Love, Death + Robots, "Zima Blue"** | A machine's story told in flat, graphic, meditative 2D with one signature colour; slow pace earns pathos. → one hero colour per character, patience. | https://za.ign.com/love-death-and-robots/130997/how-netflixs-love-death-robots-created-that-eye-popping-animation |
| **Spike Jonze, *Her* (2013)** | Removed blue, warmed everything: technology as comfort, the dilemma as human. → S4 and S5-A warmth; and note that blue (now ChatGPT's) should stay the *only* blue in frame. | https://www.thewrap.com/oscarwrap-production-design ; https://www.latimes.com/entertainment/movies/moviesnow/la-et-mn-her-spike-jonze-future-costumes-20131223-story.html |
| **Alex Garland, *Ex Machina* (2015)** | Designer Mark Digby: "shiny surfaces are for bad guys"; avoided sci-fi cliché; Ava's mesh makes her both machine and human by light. → avoid neon/holograms; let light reveal character. | https://www.dezeen.com/2015/05/22/ex-machina-set-designer-mark-digby-interview-alex-garland-juvet-landscape-hotel-norway-jensen-skodvin-architects ; https://www.motionpictures.org/2015/04/alex-garland-on-building-ex-machinas-perfect-woman/ |
| **Johnny Harris / Vox** | Physical paper documents in hand, maps as one continuous board, "visual anchors". → Record plates as real paper, handled. | https://storytelling.voxmedia.com/2017/4/18/15325756/vox-syria-video-behind-the-scenes ; https://www.storybench.org/behind-the-scenes-of-the-vox-web-series-borders/ |
| **LEMMiNO** (top cinematic YouTube essays) | Calm narration, restrained motion, abstract visuals and archival images, never literal B-roll; renders at 1080p and upscales. → pacing and 1080p-then-upscale workflow. | https://becomeviral.com/blog/lemmino-case-study ; https://pickscribe.com/v/nx4V9Uh_FW0 |
| ***Coded Bias* / *The Social Dilemma* / *AlphaGo*** | Coded Bias was Cinema Eye-nominated for animation (its AI is a voice plus graphics, never a robot); The Social Dilemma's dramatised family was criticised as heavy-handed. → keep the AI abstract or handmade, avoid literal dramatisation of harm. | https://www.documentary.org/screening/coded-bias ; https://topdocumentaryfilms.com/best-ai-documentaries/ |

Not separately researched (general knowledge only, no claims relied on): Kurzgesagt, Pixar shorts, Ghibli.

---

## 3. Five visual directions

Common rules for all five:
- **Facts vs fiction:** fictional dialogue lives in the stylised world; every real-world fact arrives as a **Record**: a physical cream paper sheet/plate (engraved border, source line), or a licensed real archival photo of *people and places of computing history* (Weizenbaum, MIT, Stanford SAIL, ARPANET map, RFC 439 page). **Never** imagery of Gaza, Minab or any strike, no victims, weapons, flags, damage, identifiable faces of the affected.
- **Minab (S5-22 → S5-30):** one locked frame, one candle, characters dimmed, no score, no effects, real pause after the casualty line (script rule).
- **Narrator:** no avatar until the epilogue, where the narrator is **a human hand** opening the drawer: the only human in the film, the one who must check.
- **ELIZA (female):** a slender, poised figure built around a teletype and a long paper strip; flat and literal, never wise. **PARRY:** red-amber, fractured, guarded, never a mental-illness joke. **ChatGPT:** blue, warm and quick, a little too eager. **Claude:** terracotta, measured, implicated (its own name in the record).
- **Typography:** ELIZA = uppercase monospaced teletype (e.g. IBM Plex Mono, OFL); Records = a classic serif (EB Garamond / Libre Caslon, OFL) with small caps source lines; the six years and KNOWN / DISPUTED / UNKNOWN in the same serif, letter-spaced. No wall-sized jargon.

### Direction A — "Engraved Candle Noir" (the owner's original master, done properly)
- **Concept:** the 19th-century steel-engraved archive from Idea.pdf, finally lit like noir: Welles' vastness, Rembrandt chiaroscuro. The machines are **light, not bodies**: luminous abstract presences that brighten when they speak and dim at Minab.
- **Palette:** ink `#0E0B09`, umber `#2A1D14`, cream `#E9DFC8`, candle amber `#F2B35E`; ChatGPT `#2F6BFF`, Claude `#D97757`, PARRY `#C0603A`, ELIZA ivory `#EDE6D3` with faint phosphor `#9BC48A`.
- **Lighting:** single motivated practicals (match, lamp, candle, moon shaft); 80% of the frame in shadow; the presences are real light sources on the engraving.
- **Camera:** slow dolly and crane (2.5D), long holds (6–20 s), Dutch angle only for PARRY, locked frame at Minab, reverse dolly in S6.
- **Characters:** ChatGPT = interlaced blue light-rings; Claude = terracotta light-lattice; PARRY = cracked red-amber glass shards behind glass; ELIZA = a column of looping paper tape over a typebar ring, ivory light. They "act" through brightness, pulse, contraction (PARRY), colour bleed (ChatGPT borrowing amber in S5-C).
- **Real incidents:** Record plates in engraving style; licensed archival photos converted to engraving in code for history (not for conflict).
- **Sound:** room tone, the match, distant clock, paper; a low cello/organ drone; nothing at Minab.
- **Epilogue:** the hand (lit by the candle) opens a drawer; the card reads Weizenbaum's 1966 line.
- **Frames:** `concept/A_engraved_candle_noir/A1_hall_match.png` (best), `A2_minab_candle.png`, `A3_parry_glass.png`.
- **Self-review:** strongest at S1/S2/Minab; risk is that 12 minutes of abstract lights becomes visually monotonous in the long S5 debate and loses the owner's wish for characters with bodies. In A2 the generator added faint ghost silhouettes in the shelves; a production plate must remove them.

### Direction B — "Painted Documentary" (Wild Robot / Arcane painterly + Wolfwalkers woodcut)
- **Concept:** an illustrated, hand-painted animated documentary. The archive and S4 are loose gouache with warm light; the institutions of S5-B switch to rigid woodcut (Cartoon Saloon's "cage" language) to show how decisions get split across many hands.
- **Palette:** gouache warm (ochre `#C99A4B`, deep green `#2F4A3A`, lamp amber `#F2B35E`, rain blue-grey `#5B7A93`) + woodcut (cream `#E9DFC8`, ink `#1A1410`, single cobalt accent `#2F6BFF`).
- **Lighting:** painterly, soft edges, warm vs cool split; S5-B flat print light, no sky.
- **Camera:** painted planes in depth (multiplane), gentle pushes; animated characters.
- **Characters:** mature, non-chibi painted machine-figures (B1: ELIZA as an elegant teletype woman wrapped in paper tape; ChatGPT a rounded blue glass figure; Claude a faceted terracotta ceramic figure; PARRY red-amber shards).
- **Real incidents:** woodcut silhouettes of featureless clerks and desks for "many hands"; Records as printed pamphlets.
- **Sound:** rain, keys, paper; a small chamber ensemble.
- **Epilogue:** painted hand, warm lamp.
- **Frames:** `concept/B_painted_documentary/B1_eliza_room.png` (best), `B2_woodcut_pipeline.png`.
- **Self-review:** beautiful and emotional, but it **needs real character animation** in a painted style, which is the hardest thing to produce for free from code (see §4: a video model per shot, with poor identity consistency). B2 woodcut is excellent for S5-B and can be borrowed by any direction.

### Direction C — "Forensic Void" (Forensic Architecture / Steyerl / Anadol)
- **Concept:** the archive as an investigation. Black void, white wireframe architecture, documents as point clouds, timelines as the master frame. The pipeline (data → recommendations → human review) is drawn as a spatial model; cones of vision show what is known and unknown.
- **Palette:** black `#07090C`, bone `#E8E4DA`, signal blue `#2F6BFF` (also ChatGPT), terracotta `#D97757` (Claude), red-amber `#C0603A` (PARRY), one amber point `#F2B35E` for human presence.
- **Lighting:** emissive lines and points only; the single warm light is always the human (a desk lamp, a candle).
- **Camera:** smooth orbital moves around models, precise, measured; locked at Minab.
- **Characters:** data-presences: ChatGPT a blue particle swarm, Claude a terracotta lattice, PARRY a cluster of red shards that contract, ELIZA a moving paper-tape line with typed characters.
- **Real incidents:** annotated diagrams of *reported claims* (who reported what, who disputes it) as timeline cards, never reconstructions of the strike. C2 Minab: an empty wire table, one candle, a faint plan outline, a timestamp tick.
- **Sound:** sub-bass hum, soft data clicks, then total silence.
- **Epilogue:** wireframe drawer, a real warm hand enters (the only photographic element).
- **Frames:** `concept/C_forensic_void/C1_pipeline_model.png` (best), `C2_minab_void.png`.
- **Self-review:** the clearest way to explain S5-B and S6, fully code-native (cheapest to render). But cold: it starves S4 (comfort) and S1 (wonder), and risks implying a forensic investigation of Minab that LATOON has not done. Best as an *insert language* inside another direction, for S5-B and S6.

### Direction D — "The Paper Archive" (handmade miniature, after *The Missing Picture*) — RECOMMENDED
- **Concept:** the whole archive is a handmade miniature built of paper, card, balsa and clay, lit by real-looking practical light: the archive of *human-made records*. The four machines are small **carved and glazed figurines**: they have bodies and quiet carved faces (the owner gets characters), but they are still and dignified, like Panh's figures. The camera and the light move, not the figures. A human hand appears only at the end.
- **Why it fits the theme:** it makes the machines *objects people made*, which is the film's point; handmade material reads as care and gravity, so Minab can be held in silence without spectacle; static figurines are honest about what they are (no fake "understanding" on their faces); and there is direct precedent for depicting atrocity this way (Panh, Cannes Un Certain Regard, Oscar-nominated).
- **Palette:** card and paper `#CDBB9C` / `#E9DFC8`, walnut `#3A2618`, shadow `#140E0A`, candle `#F2B35E`, lamp green `#3F8F4F`, rain blue `#2C4A78`; figurines: ChatGPT glazed cobalt `#2456D6`, Claude terracotta clay `#D97757`, ELIZA folded ivory paper `#EDE6D3`, PARRY cracked red-amber glass `#8E2A12`→`#C0603A`.
- **Lighting:** macro-photography practicals: one candle, one desk lamp, rain light from a window, dust in the beam. Speaker = light pool shifts or rack focus.
- **Camera:** macro slider moves, 2.5D dolly and push, rack focus, shallow depth of field, slight handheld micro-drift; locked at Minab; S6 pull-back through the miniature, reversing the opening.
- **Characters / acting:** carved poses swapped per beat (lean in, look away, hunch), figurine close-ups, subtle "breath" (tiny scale or light pulse) only while speaking; PARRY's glass glints when tense; ChatGPT's glaze catches amber in S5-C; ELIZA's paper strip types out in code at 14–18 characters per second (her mouth is the paper).
- **Real incidents:** Records are *real paper on the miniature table*: typed index cards, an RFC 439 page, an engraved plate; licensed historical photos printed and laid on the table (Weizenbaum, ARPANET map). Gaza / Microsoft / Claude / Minab reporting: only typed source cards (outlet, date, quote), never images. Minab: the empty table, one candle, one face-down card.
- **Typography:** typed index cards (Plex Mono), hand-lettered drawer labels, serif Records.
- **Sound:** foley-rich: paper, wood creak, candle crackle, rain, typewriter, carriage bell, clock; a solo piano or cello motif; silence at Minab.
- **Epilogue:** a real adult hand pulls a card-catalogue drawer; the figurines look up at it (D3). This is the strongest image in the set for the theme.
- **Frames:** `concept/D_paper_miniature/D3_epilogue_drawer.png` (best), `D1_table_figurines.png`, `D2_eliza_miniature.png`, plus **motion proof** `D1_parallax_test_3s_1080p.mp4` (3 s, depth-parallax push with candle flicker and grain, made in this sandbox).
- **Self-review:** emotionally the best fit; very feasible (stills + code). Risks: (1) **identity consistency** of four figurines across 70–90 stills (needs reference-image generation or a small LoRA, §4); (2) a slower, quieter film than the channel's other videos; (3) in D3 the drawer labels came out as readable "ARCHIVE A-M / CARDS 120-149" text; production plates need controlled or blank labels.

### Direction E — "Upgraded current pipeline" (arc3d ModernGL + rigged characters, ChatGPT blue) — RUNNER-UP
- **Concept:** keep the code-only 3D world and the rigged characters, but direct them like a mature short: darker, slower, single-source lighting, fewer characters per frame, restrained acting, full sound design and score.
- **Changes from the tests:** (1) ChatGPT body blue `#2456D6` (cloud head kept), Claude stays terracotta-orange `#D9773F`; (2) **night archive**: kill the golden hour, one candle or lamp as key, deep blue-black fill, haze, real shadows; spines desaturated to walnut/oxblood/olive, colour only in the characters' glow; (3) **faces calmed**: remove ^ ^ grins and bouncing idles; eyes only (small pixel eyes, slow blinks, look-downs); mouths optional; screen glow dims with mood; (4) **acting by stillness**: walks only where the script moves; at the table they sit; PARRY's jitter only in S2; (5) **camera**: table-height 50 mm, slow pushes, over-shoulder two-shots, long holds, locked at Minab with all faces dimmed to a faint glow; (6) **logos off the bodies**; (7) grade: lower saturation, lifted blacks, film grain, halation on practicals; (8) Records as monochrome paper inserts (already built).
- **How far it gets (honest):** with sound and music it goes from "kids' mascot video" to "earnest indie low-poly short". The E1/E2 frames show the *target*; arc3d's real output will sit below them: no global illumination or soft area shadows, simpler materials, visible low-poly edges, llvmpipe-limited resolution. It can carry S1–S4 and S5-A/C well; **S5-D (Minab) remains the weak point**: robots with screen faces at a table during a casualty passage will still read lighter than the words, even dimmed. Mitigation: at Minab cut the characters out of frame entirely (empty chairs + candle).
- **Frames (AI mood targets, not arc3d renders):** `concept/E_upgraded_3d/E1_upgraded_table.png` (best), `E2_upgraded_hall.png`.

---

## 4. Tools and libraries: honest assessment

### 4.1 Hardware reality
- **Hark sandbox:** 2× ARM Neoverse-V2 cores, ~7 GB RAM, **no GPU** (checked: `nproc`=2, `aarch64`). Good for: compositing, parallax, grading, particles, typography, audio, ffmpeg encoding. Bad for: path tracing, diffusion models, video models.
- **Owner's PC** (Ryzen 7 8845H, Radeon 780M iGPU, 32 GB, Windows): would run ModernGL much faster and small diffusion models via DirectML/ROCm-on-Windows slowly, but the owner has ruled out workflows that need his PC in the loop. **Every plan below avoids the PC.**
- **Free cloud GPU** is the missing piece (§4.3).

### 4.2 Measured here
| Test | Result | Notes |
|---|---|---|
| **Depth Anything V2 Small, ONNX, CPU (onnxruntime 1.31, 2 threads)** | fp32: **2.53 s** at 924×518, 9.5 s at 1414×798. int8-quantised: **1.77 s** at 924×518, 7.8 s at 1414×798 | One depth map per still, not per frame, so this cost is negligible. Model: `onnx-community/depth-anything-v2-small` (Apache-2.0 for Small). Script: `concept/tools/bench_depth.py` (model files in /workspace/work/archviz/). |
| **2.5D parallax + grade at 1080p** (numpy/OpenCV remap, flicker, grain, x264 encode) | **0.19 s/frame** (90 frames in 16.8 s) | `concept/tools/parallax.py` → `D1_parallax_test_3s_1080p.mp4`. 12 min ≈ 21,600 frames ≈ **~70 min** at 1080p; 4K ≈ 4× (~4–5 h). Layered occlusion-aware parallax (separating foreground figures) adds ~2×. |
| arc3d ModernGL (from VISUAL_PLAN, earlier benchmark) | 3.6–3.7 s/frame animated 1080p | ~20 h full film; ~8–10 h with plate reuse. |
| Mitsuba 3 | `llvm_ad_rgb` crashes (SIGILL) on this ARM CPU; scalar 101 s/frame | Not viable. |

### 4.3 Free GPU paths (no budget, no owner PC)
| Path | Can Hark drive it by code? | Free allowance | Verdict |
|---|---|---|---|
| **Kaggle Notebooks** | **Yes, officially.** `kaggle kernels push -p <dir>` uploads a script/notebook and runs it; `kaggle kernels status` polls; `kaggle kernels output -p out/` downloads results straight into the sandbox; `kaggle quota` shows remaining GPU hours. GPU via `kernel-metadata.json` (`"enable_gpu": true`, `"machine_shape": "NvidiaTeslaT4"`; a user report says the `--accelerator` flag alone did not switch from P100). | ~**30 GPU h/week**, ≤9 h per session, 2 concurrent GPU sessions; T4×2 (16 GB each) or P100. Internet in kernels needs a phone-verified account (to download weights). | **Best free path.** Needs the owner's Kaggle account + API token in the Hark vault (one-time). Sources: https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels.md ; https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels_metadata.md ; https://github.com/Kaggle/kaggle-cli/issues/821 ; https://github.com/ShaneZhong/autokaggle/blob/main/KAGGLE_API.md (limits, third-party summary) |
| **Google Colab (free)** | Partly. Google now ships a `google-colab-cli` (`colab run --gpu T4 script.py`), but its own skill notes "accelerator availability is tier-gated; most accounts can only get CPU"; the free-tier FAQ disallows remote control / bypassing the notebook UI; limits are unpublished and fluctuate. The REST Colab API is allowlist-only. | Unreliable free T4, ≤12 h | **Not dependable** for scheduled production. https://github.com/googlecolab/google-colab-cli ; https://research.google.com/colaboratory/faq.html ; https://developers.google.com/colab/api/reference/rest |
| **Hugging Face ZeroGPU Spaces** via `gradio_client` | Yes (`Client("owner/space", token=HF_TOKEN).predict(...)`). | Free account **5 GPU-min/day** (a forum answer also reports a ~3 runs/day cap); PRO 40 min. | Fine for a test, **far too small** for production. https://huggingface.co/docs/hub/spaces-zerogpu ; https://huggingface.co/docs/hub/spaces-api-endpoints ; https://discuss.huggingface.co/t/what-is-the-free-zerogpu-quota-for-1-space/178610/1 |
| **Hark's built-in image generator** (made every concept frame here) | Yes, it is a Hark tool; accepts up to 4 reference images (helps keep the four figurines consistent). | No API bill to the owner; subject to Hark plan usage. | **Strong option for stills.** Commercial-use terms of its outputs should be confirmed in Hark's terms before relying on it (not verified here). |
| Hosted video tools' free daily credits (Kling, Hailuo, Runway etc.) | Browser only; not verified this session. | Typically watermarked and/or non-commercial on free tiers (unverified). | Not recommended. |
| Paid Veo / Gemini image | API. Veo 3.1 Fast $0.10–0.12/s, Lite $0.05–0.08/s; Nano Banana 2 ~$0.045–0.15/image; **no free tier for image or video generation**. Imagen 4 is shut down. | — | Out of budget (owner). https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/imagen |

### 4.4 Open models: what runs on a free Kaggle T4, and licences for a monetised YouTube channel
| Model | Use | T4 feasibility (estimate unless sourced) | Licence for commercial YouTube |
|---|---|---|---|
| **FLUX.1-schnell** | stills (plates, figurines) | ~35–50 s per 1024² image on Kaggle T4 (Q5 GGUF, ~13 GB VRAM), per a practitioner report: https://sigco.tistory.com/114 | **Apache-2.0** ✔ |
| **SDXL (+ IP-Adapter / ControlNet / LoRA)** | stills, style LoRA, consistency via reference | 5–8 s per image on T4 (same report) | CreativeML **OpenRAIL++-M** ✔ (use-based restrictions) |
| FLUX.1-dev | stills | fits with quantisation | **Non-commercial** ✘ |
| **Wan 2.1 T2V-1.3B / VACE-1.3B** | short motion shots (candle, rain, dust, slow push) | 8.19 GB VRAM; ~4 min per 5 s 480p on an RTX 4090 → estimate **~15–25 min on a T4**; distilled "turbo"/DMD variants are ~5× faster. Community Kaggle notebooks exist: https://gist.github.com/DigitalKreasi25/0b7b64589dd3d174481f05d880bc7aef | **Apache-2.0** ✔ https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B |
| **Wan 2.2 TI2V-5B** | image-to-video at 720p | official path wants 24 GB; ComfyUI offload reportedly fits 8 GB; ~515 s per 5 s 720p clip on a 16 GB RTX 5060 Ti (https://vramready.com/benchmarks/) → **~20–40 min per clip on T4 (estimate)** | **Apache-2.0** ✔ https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B |
| LTX-Video (incl. LTX-2) | fast I2V | runs on 24 GB; smaller distilled versions lower | Free commercial use **under $10 M annual revenue** ✔ for LATOON https://ltx.io/model/license |
| HunyuanVideo / 1.5 | T2V | heavy (60–80 GB class) | Tencent licence, **excludes EU, UK, South Korea**; not for T4 https://huggingface.co/tencent/HunyuanVideo/raw/main/LICENSE |
| CogVideoX-5B | T2V/I2V | fits with offload | Commercial use requires **registration** for a basic licence (≤1 M visits/month) https://huggingface.co/zai-org/CogVideoX-5b/raw/main/LICENSE |
| AnimateDiff | SD1.5 motion | light | Apache-2.0 code; weights follow the base model (not verified per checkpoint) |
| Depth Anything V2 Small | depth for parallax | CPU OK (measured) | Apache-2.0 (Small only; Base/Large are CC-BY-NC) |
| Real-ESRGAN | 4× upscale stills to 4K | seconds per image on T4 | BSD-3 |

**Video-model reality check:** 12 minutes of finished picture is ~144 five-second shots. At ~20–40 T4-minutes per clip plus retries, a fully video-model film would eat **50–100+ GPU hours (2–4 weeks of Kaggle quota)** and still drift in character identity between shots. Use video models only for a handful of atmospheric inserts (rain on glass, candle flame, dust), not for dialogue.

### 4.5 Code-side libraries (all run in the sandbox)
- **NumPy + OpenCV:** parallax remap, rack-focus blur from depth, grade (lift/gamma/gain, split-tone), film grain, halation (bloom of highlights, red-shifted), chromatic aberration, vignette, candle flicker, light-pool masks that move to the speaker. Measured 0.19 s/frame at 1080p for the basic stack.
- **ModernGL (llvmpipe):** volumetric dust, light shafts, particle presences (Direction A/C), the existing arc3d world (E). Works here; slow but fine for 2D/particle passes.
- **Numba / Taichi:** CPU particle systems (dust, embers, paper fragments). Taichi's CPU backend on ARM should work but is untested here; Numba is the safer choice.
- **Manim:** S3 timeline and the rules→lattice transformation, KNOWN/DISPUTED/UNKNOWN typography (or plain pycairo/Pillow, already in use for Record plates).
- **pycairo / Pillow:** Records, typed paper strips, labels, subtitles burn-ins (none planned; soft SRTs).
- **ffmpeg:** encode only, driven from Python.
- **Not recommended here:** Mitsuba (crashes on this CPU), 3D Gaussian splatting (needs a capture/scene and a GPU rasteriser; CPU paths are ~100× slower, e.g. OpenSplat CPU mode https://github.com/WebODM/OpenSplat), diffusers on CPU (SD-Turbo 512² ≈ 5–8 s per image with OpenVINO on a fast x86 desktop CPU, per https://github.com/rupeshs/fastsdcpu; this 2-core ARM box would be several times slower, and quality at 512² is not 4K-plate quality).

### 4.6 Recommended stack per direction (all PC-free)
| Dir | Stills / assets | Motion | Render (sandbox) | Quality ceiling |
|---|---|---|---|---|
| **A** | ~60–80 engraved plates: SDXL/Flux on Kaggle (or Hark generator) + a code engraving filter for consistency | parallax + procedural light presences (Numba/ModernGL particles) | ~0.4–0.6 s/frame 1080p → **~2.5–3.5 h**; 4K ~10–12 h | High for mood; monotony risk |
| **B** | painted stills (Kaggle SDXL + painterly LoRA) | **Wan 2.1/2.2 I2V on Kaggle** for every character shot | GPU 50–100 h (weeks of quota) + compositing ~2 h | High per shot, low consistency; least feasible |
| **C** | almost none: geometry, point clouds, type all in code | code | ~1–2 s/frame → **~6–10 h** | Clean, explanatory; emotionally cold |
| **D** | ~70–90 miniature stills (Hark generator with 4 figurine references, or Kaggle Flux/SDXL + IP-Adapter / a small figurine LoRA trained on Kaggle, ~1–2 GPU h) + Real-ESRGAN to 4K on Kaggle | layered depth parallax, rack focus, candle/lamp light pools, dust, ELIZA's typed strip, optional 5–10 Wan clips for rain/flame | **measured 0.19 s/frame** basic → ~1.2 h at 1080p; with layers and 4K **~6–9 h** | High; reads as a real handmade film |
| **E** | existing arc3d scene + re-graded materials | rigged characters (existing), lip-sync from final WAVs | 3.6 s/frame → **~8–10 h** with plate reuse (20 h full) | Medium: indie low-poly; Minab weak |

GPU budget for D on Kaggle: stills ~90 × 3 variants × ~45 s ≈ 3.5 h + LoRA 1–2 h + upscale <1 h + optional Wan inserts 3–5 h ≈ **8–12 GPU h, i.e. under half of one week's free quota.**

---

## 5. Recommendation

**Go with D, "The Paper Archive."** Reasons:
1. **It matches the script's emotion end to end.** Curiosity in a tiny world (S1), suspicion in cracked glass (S2), tenderness at a paper-strip typewriter (S4), and a Minab passage that can be held in silence with one candle without any image of harm. Handmade material carries gravity in a way neither mascots nor neon can.
2. **It *is* the theme.** Machines as objects people made, records as paper people typed, and a human hand that has to open the drawer and check.
3. **It keeps what the owner wanted** (characters with bodies and faces, cinematic camera moves, real archival material as Records) while dropping what broke the tone (bouncy chibis, logos, candy palette).
4. **It is the most feasible quality path under the new constraints:** stills from free sources (Kaggle open models driven by the Kaggle CLI, or Hark's own generator), then everything else in code in this sandbox at a measured 0.19 s/frame. No paid video, no owner PC, ~8–12 free Kaggle GPU hours.
5. **Precedent:** Panh's static figurines carried a genocide film to Cannes and the Oscars; restraint is a respected grammar for exactly this material.

**Borrow from the others:** C's spatial pipeline diagram for S5-B (drawn on paper cards on the miniature table), B2's woodcut "many hands" hall as a printed sheet the camera pushes into, A's engraved Record plates.

**Runner-up: E (upgraded current pipeline).** Choose it if the owner wants animated, lip-synced characters above all, or wants to reuse the existing rig investment. With darker lighting, calmer faces, no logos and a full sound plan it is a real improvement; at Minab, cut to empty chairs and a candle.

---

## 6. Sound and music plan (for every direction; the biggest single upgrade)

### 6.1 Sources and licences
- **YouTube Audio Library** (in YouTube Studio): YouTube states tracks and SFX downloaded there are copyright-safe and won't receive Content ID claims; monetisable; some tracks need attribution. https://support.google.com/youtube/answer/3376882 . Downloading needs the owner's Studio session (Hark has a saved Studio login; downloads land in the browser session, not the sandbox, so this is a browser step).
- **Pixabay Music / SFX:** free under the Pixabay Content License, no attribution, but **some tracks are registered with Content ID**; Pixabay provides a licence certificate to dispute claims. Prefer its SFX; check music before use. https://pixabay.com/service/faq ; https://pixabay.com/blog/posts/how-to-clear-a-youtube-content-id-claim-with-a-pix-190
- **Freesound, CC0 filter only** (CC-BY needs credit; avoid CC-BY-NC): room tones, paper, typewriter, rain, candle. Freesound API downloads of originals need an OAuth2 user token; previews are lossy (owner account needed for clean originals; not verified this session).
- **Code-generated audio (numpy/scipy, in sandbox):** room tone (filtered brown noise), low drones, soft marker ticks for S3, rain beds from filtered noise grains, candle crackle (sparse impulses). Fully owned, zero licence risk.
- **AI music, open and commercial-safe:** **ACE-Step** (code Apache-2.0; v1.5 weights listed MIT, "commercial-ready", <4 GB VRAM, runs on a Kaggle T4): https://github.com/ace-step/ACE-Step ; https://huggingface.co/ACE-Step/Ace-Step1.5 . **Stable Audio Open / 3.0** for SFX textures: free commercial use under $1 M revenue with registration: https://stability.ai/news-updates/stable-audio-open-research-paper . **Avoid MusicGen** (weights CC-BY-NC): https://github.com/facebookresearch/audiocraft/blob/main/model_cards/MUSICGEN_MODEL_CARD.md

### 6.2 Cue sheet
| Scene | Music | Sound design |
|---|---|---|
| S1 (0:00–0:22 image only) | none | room hum, far clock, the match strike, paper settling |
| S1 dialogue | a single low sustained note entering at "Look at that door" | footsteps on boards (soft), dust |
| S2 | low cello / bowed drone, tense, very quiet | glass creak, a lock, PARRY's shard tinkle; **1 s true silence after "Do you?"**; typewriter ding under the $399.29 bill (dry comedy) |
| S3 | gentle piano motif: rigid repeating figure (rules) that loosens into a flowing line at 2017 | one soft tick per year; brass rail resonance |
| S4 | **no score** (script rule) | rain on glass, lamp hum, typewriter keys at 14–18 cps, carriage bell |
| S5-A | warm, sparse piano + strings, quicker | table creaks, page turns |
| S5-B | score cools to a thin pad; pulse slows | paper shuffles, distant typing pool, pneumatic tube thunks (Brazil nod), room gets larger |
| S5-C | a dry pizzicato "agreeing" figure that stops dead when ELIZA interrupts | — |
| **S5-D Minab** | **nothing** | **nothing: not even room tone**; a real pause after the casualty line |
| S5-E | almost inaudible room bed returns | — |
| S6 | three-note cello/piano phrase, unresolved | paper lifting, sheets swaying |
| Epilogue / end card | phrase resolves only halfway | a drawer sliding, a card lifted |

Mix: dialogue first; score −24 to −30 LUFS-relative bed under voice; all music ducked under lines; follow PLAYBOOK loudness targets.

---

## 7. Decisions for the owner
1. **Direction:** D (recommended), E (runner-up) or another.
2. **Characters:** carved figurines (D) vs calmed low-poly mascots (E) vs abstract light (A).
3. **Claude's colour:** terracotta `#D97757` now that ChatGPT is blue?
4. **Logos:** remove the real OpenAI/Claude marks from the bodies (recommended; name by colour and caption)?
5. **Free GPU:** create/verify a Kaggle account (phone-verified for internet), generate an API token, and let Hark store it in the vault so generation runs in the cloud without his PC.
6. **Stills source:** Hark's built-in generator (with reference images) and/or open models on Kaggle (Flux-schnell Apache-2.0, SDXL OpenRAIL++). Confirm Hark's output terms for commercial use first.
7. **Music:** YouTube Audio Library tracks, ACE-Step original score on Kaggle, or a mix.
8. **Archival photos:** which historical images (Weizenbaum, MIT, SAIL, ARPANET map, RFC 439) to license or use from public-domain/CC sources, logged in SOURCES_MEDIA.md.
9. **Resolution:** the master says 4K/30. D and A reach 4K via Real-ESRGAN plates + sandbox compositing; E realistically stays 1080p and upscales.

## 8. What this research did not establish
- No production-quality consistency test of the four figurines across many stills (the concept frames differ in figure design between D1, D2, D3).
- No arc3d re-render with the Direction E changes; E frames are AI mood targets, not proof of arc3d output.
- No live Kaggle run (no token available); T4 timings for Wan are extrapolated from 4090 / 5060 Ti figures.
- Hosted video tools' free tiers and Freesound API download terms were not verified.
- Kurzgesagt, Pixar shorts and Ghibli were not researched with sources.
- Depth-parallax at 4K and occlusion-aware layer separation were not benchmarked (estimates only).
