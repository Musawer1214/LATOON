# Sources — "Why Can't AI Just Say 'I Don't Know'?" (sample Short, 2026-10-20)

Primary sources (opened 2026-10-20):
1. OpenAI, "Why language models hallucinate", blog post, 2025-09-05. https://openai.com/index/why-language-models-hallucinate/
2. Kalai, A. T., Nachum, O., Vempala, S. S., Zhang, E. et al., "Why Language Models Hallucinate", arXiv:2509.04664 (2025). https://arxiv.org/abs/2509.04664
3. SimpleQA table as reported in source 1 (from the GPT-5 system card): https://cdn.openai.com/gpt-5-system-card.pdf

| Claim (spoken or on screen) | Source wording | Confidence |
|---|---|---|
| Hallucinations = confident answers that are false ("answer confidently, and get it wrong") | "instances where a model confidently generates an answer that isn't true"; "plausible but false statements" (1) | verified |
| "A big reason is how we grade it" (hedged: a big reason, not the only one) | "Hallucinations persist partly because current evaluation methods set the wrong incentives"; "standard training and evaluation procedures reward guessing over acknowledging uncertainty" (1) | verified |
| Multiple-choice: a guess might score, a blank always scores zero | "If you do not know the answer but take a wild guess, you might get lucky and be right. Leaving it blank guarantees a zero." (1) | verified |
| So guessing beats "I don't know" (on accuracy-only scoring) | "when models are graded only on accuracy ... they are encouraged to guess rather than say 'I don't know.'" (1) | verified |
| Scoreboard: gpt-5-thinking-mini 52% abstain / 22% right / 26% wrong; OpenAI o4-mini 1% / 24% / 75% (SimpleQA) | table in (1) from the GPT-5 system card (3) | verified |
| "One that rarely held back got slightly more right, but was wrong 75 percent" | "In terms of accuracy, the older OpenAI o4-mini model performs slightly better. However, its error rate ... is significantly higher." (1) | verified |
| Birthday: a guess has a 1 in 365 chance; "I don't know" scores zero | "If it guesses 'September 10,' it has a 1-in-365 chance of being right. Saying 'I don't know' guarantees zero points." (1) | verified |
| The fix: penalise confident errors more than uncertainty, reward an honest "I don't know" | "Penalize confident errors more than you penalize uncertainty, and give partial credit for appropriate expressions of uncertainty." (1) | verified |
| Takeaway "for facts that matter, ask for the source, and check it" | LATOON's practical advice that follows from the paper (not a claim attributed to OpenAI) | advice |

Not said on purpose: that grading is the ONLY cause; that newer models never hallucinate; any made-up penalty numbers.
Cut from the voice for length (in the take, not used): "Most AI tests score the same way" and "Rare facts, like a birthday, can't be learned from patterns" (source 1, next-word-prediction section) — see README.

On-screen credit: "Data: OpenAI, Kalai et al. (2025)" (7-52 s) and "SimpleQA · GPT-5 system card" (22-36 s).
Images/footage: none. All visuals are original Three.js clay models made for this Short. Fonts: Inter (OFL), helvetiker (three.js examples, MIT) for the 3D "0" and "?".
Audio: original score synthesised in code; UI SFX from engine/sound/sfx (Mixkit SFX Free License, https://mixkit.co/license/#sfxFree); voice Gemini TTS prebuilt "Iapetus" (gemini-3.1-flash-tts-preview).
