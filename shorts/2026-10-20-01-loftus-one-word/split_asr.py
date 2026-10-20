# Split the one EN Gemini file at the silence between ASR-located line boundaries (PLAYBOOK s4.6.1: cut mid-silence,
# keep >=120 ms room tone each side). Replaces trim.py's char-proportional split, which mis-split this file.
import json, sys, os, numpy as np
sys.path.insert(0, "engine"); import timing as TM
SR = TM.SR
a = TM.load_wav("en_all.mp3"); W = json.load(open("asr_en_words.json")); lines = json.load(open("script.json"))
# first word index of each line: count words per script line
import re
def nw(s): return len(re.findall(r"[A-Za-z0-9']+(?:-[A-Za-z0-9']+)*", s.replace("car-crash","car crash")))
cnt = [nw(l) for l in lines]; idx = np.cumsum([0] + cnt)
assert idx[-1] == len(W), (idx[-1], len(W))
fr = int(.01 * SR); e = np.sqrt(np.convolve(a ** 2, np.ones(fr) / fr, "same"))
cuts = [0]
for k in range(1, len(lines)):
    t0 = W[idx[k] - 1][2]; t1 = W[idx[k]][1]
    i0, i1 = int(t0 * SR), int(t1 * SR)
    seg = e[i0:i1]; quiet = seg < seg.min() * 4 + 1e-4
    q = np.where(quiet)[0]; c = i0 + int((q[0] + q[-1]) / 2) if len(q) else (i0 + i1) // 2
    cuts.append(c); print(k, round(t0, 2), round(t1, 2), "cut", round(c / SR, 3), "gap", round(t1 - t0, 2))
cuts.append(len(a))
thr = 10 ** (-45 / 20); pad = int(.12 * SR)
for k in range(len(lines)):
    s = a[cuts[k]:cuts[k + 1]]; loud = np.where(np.abs(s) > thr)[0]
    s = s[max(0, loud[0] - pad): min(len(s), loud[-1] + pad)]
    TM.save_mono(TM.vo_path(".", "en", k), s)
d = [TM.wav_dur(TM.vo_path(".", "en", k)) for k in range(len(lines))]
open("durs.txt", "w").write(" ".join(f"{x:.4f}" for x in d)); print([round(x, 2) for x in d], round(sum(d), 2))
