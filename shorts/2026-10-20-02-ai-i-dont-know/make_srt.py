"""EN soft captions: text = the spoken script (script.json, sentence by sentence), timing = ASR word times of the edited voice
(voice/words_vo.json). Long sentences split at a comma; each cue ends just before the next sentence starts."""
import json, re, textwrap
S = [s for line in json.load(open('script.json')) for s in re.split(r'(?<=[.?])\s+(?=[A-Z"])', line)]
W = json.load(open('voice/words_vo.json'))
pass  # ASR hallucination ('Thank you for watching') on the trailing silence was removed from words_vo.json
G = []; cur = []
for w in W:
    cur.append(w)
    if w[0].endswith(('.', '?')): G.append(cur); cur = []
assert len(G) == len(S), (len(G), len(S))
def fmt(t): ms = int(round(t * 1000)); return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
cues = []
import wave, numpy as np
_wv = wave.open('vo_en_24k.wav'); _x = np.frombuffer(_wv.readframes(_wv.getnframes()), np.int16) / 32768.0
_db = np.array([20 * np.log10(np.sqrt(np.mean(_x[i:i + 240] ** 2)) + 1e-9) for i in range(0, len(_x), 240)])
def onset(t):      # ASR word starts drift after long pauses: snap a sentence start to the real speech onset (energy)
    i = int(max(0, t - 0.05) * 100)
    while i < len(_db) and _db[i] < -40: i += 1
    return i / 100 if i / 100 - t < 1.2 else t
for g in G: g[0] = [g[0][0], onset(g[0][1]), g[0][2]]
for i, (s, g) in enumerate(zip(S, G)):
    nxt = G[i + 1][0][1] if i + 1 < len(G) else g[-1][2] + 0.6
    parts = [s]
    if len(s) > 60 and ',' in s:                 # split at the comma nearest the middle
        idx = [m.end() for m in re.finditer(',', s) if 20 < m.end() < len(s) - 20] or [0]; k = min(idx, key=lambda x: abs(x - len(s) / 2)); parts = [s[:k].strip(), s[k:].strip()]
    if len(s) > 80 and not (len(parts) == 2 and parts[0]):
        ws = s.split(); cand = [i for i, x in enumerate(ws) if x in ('was', 'but', 'and', 'so') and 2 < i < len(ws) - 2] or [len(ws) // 2]; h = min(cand, key=lambda i: abs(i - len(ws) / 2)); parts = [' '.join(ws[:h]), ' '.join(ws[h:])]
    if len(parts) == 2 and parts[0]:
        frac = len(parts[0].split()) / len(s.split()); j = max(1, min(len(g) - 1, round(frac * len(g))))
        tsplit = g[j][1]
        cues += [(g[0][1] - 0.05, tsplit - 0.05, parts[0]), (tsplit - 0.05, nxt - 0.08, parts[1])]
    else: cues.append((g[0][1] - 0.05, nxt - 0.08, s))
with open('subs_en.srt', 'w') as f:
    for k, (a, b, s) in enumerate(cues, 1): f.write(f'{k}\n{fmt(max(0,a))} --> {fmt(b)}\n' + '\n'.join(textwrap.wrap(s, 42)) + '\n\n')
print(len(cues), 'cues')
