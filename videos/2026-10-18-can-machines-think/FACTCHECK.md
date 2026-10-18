# FACTCHECK — "Can Machines Think?" script v1 (2026-10-18)

Every spoken claim in script.json maps to an ID below (the `claims` field of each line; tags like [T3] in script_en.md).
All sources were opened on 2026-10-18 unless marked otherwise. Confidence: H = stated in the primary source in these words or numbers; M = fair paraphrase or needs one more check at build.
Dossier re-check items closed: PNAS full page opened (F1-F6); Butlin full abstract + footnote read (B1-B3); move 37 now sourced (G2); Othello-GPT venue confirmed (M2).

## Turing 1950 (Mind) and Lovelace 1843

| ID | Claim in script | Primary source | What the source says | Conf. |
|---|---|---|---|---|
| T1 | 1950, Turing publishes in the journal Mind; first line "I propose to consider the question, 'Can machines think?'" | A. M. Turing, "Computing Machinery and Intelligence", Mind LIX (236), 433-460 (1950), doi:10.1093/mind/LIX.236.433. Full text opened: https://courses.cs.umbc.edu/471/papers/turing.pdf | Section 1 opens with exactly this sentence. | H |
| T2 | He refuses to define the words; by common usage the answer would come from "a Gallup poll"; "But this is absurd." | same, §1 | "...is to be sought in a statistical survey such as a Gallup poll. But this is absurd." (Script paraphrases "machine" and "think" as "think"; quoted words exact.) | H |
| T3 | "Too meaningless to deserve discussion"; bet: in about fifty years an average interrogator would have no more than a 70% chance of right identification after five minutes; by the end of the century people would speak of machines thinking "without expecting to be contradicted". | same, §6 | "I believe that in about fifty years' time ... an average interrogator will not have more than 70 per cent chance of making the right identification after five minutes of questioning. The original question, 'Can machines think?' I believe to be too meaningless to deserve discussion. Nevertheless ... at the end of the century ... one will be able to speak of machines thinking without expecting to be contradicted." | H |
| T4 | The game starts with a man, a woman and an interrogator in another room, answers typed; then "what if a machine takes one seat?" | same, §1 | Man (A), woman (B), interrogator (C) in a room apart; answers "typewritten" / teleprinter; "What will happen when a machine takes the part of A in this game?" | H |
| T5 | Viva voce comparison; used to discover whether someone "really understands something or has 'learnt it parrot fashion'". | same, §6 (4) Argument from Consciousness | "The game (with the player B omitted) is frequently used in practice under the name of viva voce to discover whether some one really understands something or has 'learnt it parrot fashion.'" | H |
| T6 | Lovelace's objection; Turing: "Machines take me by surprise with great frequency", largely because he does not calculate enough. | same, §6 (6) Lady Lovelace's Objection | Exact quote; "This is largely because I do not do sufficient calculation to decide what to expect them to do". Note: Turing dates her memoir 1842 and quotes it without "whatever". | H |
| T7 | London, 1843: Lovelace's notes on Babbage's Analytical Engine; quote "The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform." Notes famous for showing how it could be programmed. | Original text (Note G): Menabrea, "Sketch of the Analytical Engine", with notes by A.A.L., Taylor's Scientific Memoirs vol. III, London 1843; transcription opened https://www.fourmilab.ch/babbage/sketch.html . Date and publication: Science Museum https://www.sciencemuseum.org.uk/objects-and-stories/women-computing ("published in August 1843 in Taylor's Scientific Memoirs"; notes "outlined the potential ... for general programming"); Bodleian https://blogs.bodleian.ox.ac.uk/adalovelace/2018/07/26/ada-lovelace-and-the-analytical-engine/ | Quote exact from Note G (with "whatever"). Menabrea's French original was Oct 1842; her translation + notes 1843. | H |
| T8 | "107 years earlier" (1950 − 1843). | arithmetic on T1/T7 | — | H |
| T9 | Turing "by then programming the Manchester computer". | Turing 1950 §5/§6 | "I have set up on the Manchester computer a small programme..." | H |
| T10 | The child machine: "a notebook as one buys it from the stationer's", little mechanism, lots of blank sheets; then educate it; learning machines as the answer to Lovelace. | Turing 1950 §7 Learning Machines | "Presumably the child brain is something like a notebook as one buys it from the stationer's. Rather little mechanism, and lots of blank sheets." §7 returns to Lovelace's objection. | H |
| T11 | Jefferson 1949: no machine equals brain until it writes a sonnet "because of thoughts and emotions felt"; Turing: extreme view = only way to be sure is to be the machine (solipsism), applies to people too; "the polite convention that everyone thinks". | Turing 1950 §6 (4) | Quotes Jefferson's Lister Oration 1949; "the only way by which one could be sure that machine thinks is to be the machine ... the only way to know that a man thinks is to be that particular man ... it is usual to have the polite convention that everyone thinks." Script says "Professor Jefferson" as Turing does (Geoffrey Jefferson). | H |
| T12 | Closing line: "We can only see a short distance ahead, but we can see plenty there that needs to be done." | Turing 1950, last line | Exact. | H |

## Games (Deep Blue, AlphaGo)

| ID | Claim | Source | Says | Conf. |
|---|---|---|---|---|
| G1 | New York, May 1997: Deep Blue beats reigning world champion Kasparov in a six-game match; brute force, 200 million positions per second; evaluation function built by the team (grandmasters advised). | IBM Heritage, https://www.ibm.com/history/deep-blue | "first computer system to defeat a reigning world chess champion ... six-game", Equitable Center New York, 3.5-2.5; "brute force computing power"; "200 million chess positions per second"; team "created a more powerful evaluation function ... hired additional chess grandmasters". Kasparov quote ("something similar to an artificial intellect") is on this page but was cut in v1. | H |
| G2 | Seoul, March 2016, Lee Sedol (18 world titles); AlphaGo learned from thousands of expert games then self-play; game two, move 37, "1 in 10,000 chance of being used" (DeepMind's figure); won 4-1; Lee Sedol quote. | Google DeepMind, https://deepmind.google/research/breakthroughs/alphago/ ; method also in Silver et al., Nature 529, 484 (2016) https://www.nature.com/articles/nature16961 | Page states all of these; quote: "I thought AlphaGo was based on probability calculation and that it was merely a machine. But when I saw this move, I changed my mind. Surely, AlphaGo is creative." Script says "one of the greatest Go players of his era" (page: "widely considered the greatest player of that decade"). | H |

## Searle 1980

| ID | Claim | Source | Says | Conf. |
|---|---|---|---|---|
| S1 | John Searle, Berkeley, 1980; Chinese is "just so many meaningless squiggles" to him; argued over 40+ years (1980→2026). | J. R. Searle, "Minds, Brains, and Programs", Behavioral and Brain Sciences 3 (3), 417-457 (1980). Opened: https://home.csulb.edu/~cwallis/382/readings/482/searle.minds.brains.programs.bbs.1980.pdf | Affiliation "University of California, Berkeley"; "To me, Chinese writing is just so many meaningless squiggles." | H |
| S2 | Rulebook in English; answers "absolutely indistinguishable from those of native Chinese speakers"; program alone not sufficient for understanding; "only a syntax but no semantics". | same | All in text. | H |
| S3 | Systems reply (man + ledger + paper + data banks understand); Searle: let him internalize/memorize the rules, do it in his head, even outdoors; still understands nothing. | same, "I. The systems reply (Berkeley)" | Exact structure. | H |
| S4 | Searle never said machines can't think: "We are precisely such machines"; it is the brain's biological causal powers, not a program by itself. | same, conclusion | "'Could a machine think?' The answer is, obviously, yes. We are precisely such machines." ; "...because I am a certain sort of organism with a certain biological (i.e. chemical and physical) structure"; abstract: "no program by itself is sufficient for thinking". | H |
| S5 | A simulation of a rainstorm leaves nobody drenched. | same | "No one supposes that ... a computer simulation of a rainstorm will leave us all drenched." | H |

## Inside the models

| ID | Claim | Source | Says | Conf. |
|---|---|---|---|---|
| M1 | Today's models: no hand-written rulebook, billions of learned numbers, trained to predict the next piece of text. | Brown et al., GPT-3, arXiv 2005.14165 (175B parameters, already logged in longform/2026-10-14-inside-chatgpt-press-enter/sources.md) | 175 billion parameters; autoregressive next-token training. v1 says only "billions" to avoid repeating the Inside ChatGPT number line. | H |
| M2 | 2022, Harvard/MIT/Northeastern; GPT variant trained on Othello move sequences, 20 million (synthetic) games; no board, no rules given; top-1 illegal ~0.01% (about 1 in 10,000); probes read the board state from activations; interventions on that representation change predictions. Published ICLR 2023. | K. Li, A. K. Hopkins, D. Bau, F. Viégas, H. Pfister, M. Wattenberg, "Emergent World Representations", arXiv 2210.13382 (ICLR 2023 oral). Abstract + PDF opened: https://arxiv.org/abs/2210.13382 | Affiliations Harvard (4), MIT (Hopkins), Northeastern (Bau); "no a priori knowledge of the game or its rules"; synthetic set 20 million games; "error rate is 0.01% for Othello-GPT trained on the synthetic dataset"; non-linear probes predict board state with high accuracy; "Interventional experiments indicate this representation can be used to control the output." | H |
| M3 | (cut from v1; available) A follow-up found a linear "mine vs theirs" board representation. | Nanda, Lee & Wattenberg, arXiv 2309.00941 https://arxiv.org/abs/2309.00941 | Abstract states this. | H |
| M4 | 2023 reversal curse: GPT-4 answers questions like "Who is Tom Cruise's mother?" 79% vs 33% for the reverse ("Who is Mary Lee Pfeiffer's son?"). | Berglund et al., "The Reversal Curse", arXiv 2309.12288 (ICLR 2024 version v4). Abstract opened: https://arxiv.org/abs/2309.12288 | "GPT-4 correctly answers questions like the former 79% of the time, compared to 33% for the latter." Script says "questions like", not one question. Result is for GPT-4 in 2023; newer models may differ (script dates it). | H |

## The 2025-2026 Turing test

| ID | Claim | Source | Says | Conf. |
|---|---|---|---|---|
| F1 | 2025, researchers in San Diego; hundreds of people; pre-registered; Turing's three-party setup; 5-min simultaneous chats; two independent groups (UCSD undergraduates; paid Prolific participants); Jones & Bergen, peer-reviewed, PNAS 2026. | C. R. Jones & B. K. Bergen, "Large language models pass a standard three-party Turing test", PNAS 123 (21) e2524472123, published online 19 May 2026, https://www.pnas.org/doi/10.1073/pnas.2524472123 (full page opened). Preprint arXiv 2503.23674 (31 Mar 2025). | 126 UCSD + 158 Prolific participants (+205 in the 15-min study); "randomized, controlled, and preregistered"; IRB at UC San Diego; GPT-4.5 (released 2025) puts the 5-min studies in 2025. | H |
| F2 | Persona GPT-4.5 picked as human 73%, more often than the real humans (so interrogator accuracy ~27%, worse than chance); persona = "young person who is introverted, knowledgeable about internet culture, and uses slang" (script: "shy young person who uses slang"). | PNAS, Abstract, AI Models, Results, Table 1 | 73% overall (69% UCSD, 76% Prolific), "significantly more often than interrogators selected the real human participant". | H |
| F3 | LLaMa-3.1 persona 56%; without persona GPT-4.5 36%, LLaMa 38%; ELIZA 23% (manipulation check), GPT-4o 21%. | PNAS Results + Table 1 | "GPT-4.5-NO-PERSONA and LLAMA-NO-PERSONA had overall win rates of 36% and 38% respectively". NB the PNAS abstract lists "(38% and 36%)" in the other order; Table 1 totals confirm GPT-4.5 = 50/141 = 35.5%, LLaMa = 47/123 = 38.2%. Script order (GPT-4.5 36, LLaMa 38) matches Results/Table. | H |
| F4 | 15-minute replication: GPT-5 persona 59% (LLaMa 56%, ELIZA 17%). | PNAS Table 2 | GPT-5-PERSONA 59.3%. | H |
| F5 | Most common strategy small talk (61% of games); only 12% probed knowledge and reasoning; most frequent reason class linguistic style (27%), e.g. typos. | PNAS Strategies & Reasons; Discussion | "small talk ... 61% of games"; "knowledge and reasoning abilities ... 12%"; "most frequent class of reason concerned witnesses' linguistic style (27%) — e.g. 'they had a typo'". | H |
| F6 | Authors: the test may be "a test of humanlikeness" rather than a direct test of intelligence; it measures substitutability in short conversation. | PNAS Significance + Discussion | "One interpretation ... is that the Turing test is not a direct test of intelligence, but a test of humanlikeness"; "can substitute for a real person in a short conversation". Script uses "may", matching "one interpretation". | H |

## Consciousness

| ID | Claim | Source | Says | Conf. |
|---|---|---|---|---|
| B1 | 2023, 19 researchers incl. Yoshua Bengio (neuroscientists and philosophers among them); derive "indicator properties" from theories such as global workspace theory. | Butlin, Long, et al., "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness", arXiv 2308.08708 (v3, 22 Aug 2023), https://arxiv.org/abs/2308.08708 (abstract + PDF opened) | 19 authors (Butlin + 18) incl. Bengio, Birch, Frith, Fleming, Mudrik, Peters, Schwitzgebel; theories surveyed: recurrent processing, global workspace, higher-order, predictive processing, attention schema; "derive 'indicator properties' of consciousness, elucidated in computational terms". | H |
| B2 | Their analysis suggested no current AI systems were conscious; no obvious technical barriers to building systems that satisfy the indicators; satisfying them would not mean a system is definitely conscious. | same, abstract + footnote 1 | Full sentence: "Our analysis suggests that no current AI systems are conscious, but also suggests that there are no obvious technical barriers to building AI systems which satisfy these indicators." Footnote: "satisfying the indicators would not mean that such an AI system would definitely be conscious." Script dates it "2023" and says "suggested". | H |
| B3 | Method rests on computational functionalism, "a mainstream—although disputed—position"; IIT proponents claim digital computers are unlikely to be conscious whatever programs they run. | same, §1 and §2.4 | "we adopt computational functionalism ... as a working hypothesis. This thesis is a mainstream—although disputed—position"; "proponents of IIT claim that the theory implies that digital computers are unlikely to be conscious, whatever programs they run (Albantakis & Tononi 2021)". | H |

## The thought and local examples

| ID | Claim | Source | Notes | Conf. |
|---|---|---|---|---|
| Q1 | Ghalib: «کہتے ہیں کہ غالبؔ کا ہے اندازِ بیاں اور» — "They say Ghalib's way of saying things is something else." Used only as a fitting thought; script says he meant his own poetry. | Rekhta, https://www.rekhta.org/couplets/hain-aur-bhii-duniyaa-men-sukhan-var-bahut-achchhe-mirza-ghalib-couplets (Urdu text on Rekhta's Urdu couplets page); F. Pritchett, Columbia, https://ftp.columbia.edu/itc/mealac/pritchett/00ghalib/062/62_11.html ("they say that Ghalib's is a style of expression [that is] other/more") | Second line of the couplet «ہیں اور بھی دنیا میں سخن ور بہت اچھے». English meaning is our translation, consistent with Pritchett. | H |
| L1 | "Ratta" = rote learning in Pakistani usage (our local link to Turing's "parrot fashion"). | Common Urdu usage (رٹا), no fact claim beyond the word | Local example per PLAYBOOK s4.4. | H |
| L2 | "Run a fire simulation all day; the room stays cold." (v2, replaces the Lahore monsoon line at owner request) | Searle 1980, Minds, Brains and Programs: "No one supposes that computer simulations of a five-alarm fire will burn the neighborhood down or that a computer simulation of a rainstorm will leave us all drenched." | Searle's own example, paraphrased. | H |

## What the script deliberately does NOT say
- That any AI is or is not conscious (only Butlin et al.'s 2023 "suggests no current AI systems are conscious", dated and attributed).
- That passing the Turing test proves thinking (the PNAS authors' own caution is quoted).
- Weizenbaum's secretary anecdote, ELIZA/PARRY history (The Archive's material); ELIZA appears once, only as the study's baseline.
- Bletchley/Enigma Turing material (published Enigma long).
- Tokens/embeddings/attention mechanics (published Inside ChatGPT long); next-token prediction is one clause.
- Current ARC-AGI scores (fast-moving; not verified for today).

## Re-check before publish
- Any newer replication or correction of Jones & Bergen (PNAS 2026) or a newer Butlin-style assessment (Butlin et al. published updates are possible; search before voicing).
- Image licences for every photo named in the visual notes (Turing, Manchester computer, Lovelace, Analytical Engine trial piece, Deep Blue, Kasparov, Lee Sedol, Searle, Ghalib, PNAS figure use).


## v2 notes (2026-10-18)
- Place names removed where not needed (San Diego -> 'in the United States'; Manchester, London, New York, Seoul, Berkeley, Harvard/MIT/Northeastern dropped). Facts unchanged.
- C0-02 Urdu/Pashto say '73% of people'; strictly it is 73% of games/verdicts. Close enough for narration, English keeps 'of the time'.
