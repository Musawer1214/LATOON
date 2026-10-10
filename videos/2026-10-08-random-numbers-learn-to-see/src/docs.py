import json, re, os
import timeline as TL
R = TL.ROOT; S = TL.SCRIPT; D = TL.DUR
def ts(x, srt=False):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    if srt:
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    return f"{m}:{int(s):02d}"
TITLES = {"hook": "Cold open: your phone sees you", "pixels": "Pixels are numbers", "neuron": "One neuron: weighted sum + ReLU",
 "layers": "Layers", "random": "Random at first", "loss": "The loss: one number of wrongness", "landscape": "The loss landscape",
 "gradient": "Gradient descent and the learning rate", "backprop": "Backpropagation (the chain rule)", "sgd": "Mini-batches and SGD",
 "train": "Training run", "features": "What the layers learn", "open": "Honest open questions", "close": "Payoff"}
md = ["# How a pile of random numbers learns to see — English narration (LATOON long-form)", "",
      "Voice: en-US-AndrewNeural, rate -5% (edge-tts). Timestamps = when each paragraph's voice starts in the final video.",
      f"Total runtime {ts(TL.TOTAL)} ({TL.TOTAL:.1f} s). Words: {sum(len(s[1].split()) for s in S)}.",
      "Each paragraph slot = English read x 1.10 + 0.7 s gap; section changes add ~0.7 s camera transitions. A dub up to ~15% longer fits by using the gaps and holds.",
      "The LATOON brand sting at 0:31.8-0:36.0 has no narration.", ""]
for name, paras in TL.SCENE_PARAS:
    if not paras: continue
    sc = [s for s in TL.SCENES if s["name"] == name][0]
    md.append(f"## {ts(sc['start'])} — {TITLES[name]}"); md.append("")
    for p in paras:
        st = TL.VO_START[p]
        md.append(f"**[{ts(st)}] P{p+1:02d}** (English read {D[p]:.1f} s, slot {D[p] * TL.SLACK + TL.GAP:.1f} s)  ")
        md.append(S[p][1]); md.append("")
open(os.path.join(R, "script_en.md"), "w").write("\n".join(md))
cues = []
for p in range(len(S)):
    txt = S[p][1]; sents = [x.strip() for x in re.findall(r"[^.?!]+[.?!]+|[^.?!]+$", txt) if x.strip()]
    tot = sum(len(x) for x in sents); st = TL.VO_START[p] + .05; dur = D[p] - .25; acc = 0
    for x in sents:
        a = st + dur * acc / tot; acc += len(x); b = st + dur * acc / tot
        cues.append((a, b, x))
with open(os.path.join(R, "script_en.srt"), "w") as f:
    for i, (a, b, x) in enumerate(cues, 1):
        f.write(f"{i}\n{ts(a, True)} --> {ts(b, True)}\n{x}\n\n")
chap = [f"{ts(0 if i == 0 else s['start'])} {TITLES[s['name']]}" for i, s in enumerate(TL.SCENES) if s["name"] != "sting"]
open(os.path.join(R, "chapters.txt"), "w").write("\n".join(chap) + "\n")
print("\n".join(chap)); print(len(cues), "cues")
