# Dialogue pacing (owner rule, 2026-10-15) — binding for all Archive voice work

Owner: this video is about dialogues; earlier videos sometimes came out too fast as generations sped up.
Every sentence must land: normal, steady conversational speed (not slow, not fast) with proper breaks.

## Targets
- Speech rate: ~140-155 wpm English per line (normal conversation). Urdu/Pashto: match the English line's duration within ±15%.
- Hard reject: any line > 165 wpm, or > 10% faster than that speaker's median, or audibly accelerating inside a line → regenerate (shorter request), never keep.
- Never time-compress voice (no atempo/speed-up) to fit picture. Picture timing follows the voice.
- Slight slowing is allowed only on weighty lines (casualty line, Weizenbaum quotes, closing lines); never slower than ~125 wpm.

## Breaks (silence, cut only in real silences per PLAYBOOK s16)
- Between speakers in an exchange: 0.6-0.9 s.
- After a factual/weighty line or a question meant to make the viewer think: 1.0-1.5 s.
- Between sentences of the same speaker: 0.3-0.5 s (keep the natural pause the TTS gives; don't trim).
- Scene changes: 1.5-2 s with room tone.
- Minab casualty line: 2.5 s silence, no music.

## Generation
- Delivery style per line includes "unhurried, natural conversational pace".
- Small requests (about 3 paragraphs / ≤8 short lines) to stop mid-request speed-up; measure wpm per line on every take (s16 checks) before joining.
- Runtime will grow from the 11:01 estimate (likely ~11.5-12.5 min). That's fine; don't cut owner lines to compensate.
