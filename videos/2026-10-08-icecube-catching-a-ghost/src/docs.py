import re, os
import timeline as TL
R = TL.ROOT; S = TL.SCRIPT; D = TL.DUR
def ts(x, srt=False):
    if srt:
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    return f"{int(x // 60)}:{int(x % 60):02d}"
TITLES = {"hook": "Ghosts through your fingernail", "ghost": "A desperate remedy: Pauli to 1956", "bigger": "Build a bigger trap",
 "ice": "Halzen's idea: Antarctic ice", "drill": "Melting holes 2.5 km deep", "array": "5,160 sensors in a cubic kilometre",
 "light": "Cherenkov light: the faint blue flash", "direction": "Tracing the direction + the Earth as a shield",
 "f2013": "2013: neutrinos from beyond", "txs": "2017: one neutrino, one blazar", "ngc": "2022: NGC 1068, hidden behind dust",
 "milky": "2023: the Milky Way in neutrinos", "nobel": "The 2026 Nobel Prize", "future": "What comes next: Upgrade and Gen2", "close": "Look at your fingernail again"}
md = ["# Catching a Ghost: IceCube — English narration (LATOON long-form)", "",
      "Voice: en-US-AndrewNeural, rate -3% (edge-tts). Timestamps = when each paragraph's voice starts in the final video.",
      f"Total runtime {ts(TL.TOTAL)} ({TL.TOTAL:.1f} s). Words: {sum(len(s[1].split()) for s in S)}.",
      "Each slot = English read x 1.06 + 0.75 s gap. A dub up to ~10% longer fits using gaps and holds. Title card 0:28.5-0:32.5 has no narration.", ""]
for name, paras in TL.SCENE_PARAS:
    if not paras: continue
    sc = [s for s in TL.SCENES if s["name"] == name][0]
    md += [f"## {ts(sc['start'])} — {TITLES[name]}", ""]
    for p in paras:
        md += [f"**[{ts(TL.VO_START[p])}] P{p+1:02d}** (read {D[p]:.1f} s, slot {D[p]*TL.SLACK+TL.GAP:.1f} s)  ", S[p][2], ""]
open(os.path.join(R, "script_en.md"), "w").write("\n".join(md))
cues = []
for p in range(len(S)):
    vo_txt = S[p][1]; disp = S[p][2]
    sents = [x.strip() for x in re.findall(r"[^.?!:]+[.?!:]+|[^.?!:]+$", disp) if x.strip()]
    # merge very short fragments
    merged = []
    for x in sents:
        if merged and (len(x) < 18 or len(merged[-1]) < 18) and len(merged[-1]) + len(x) < 80: merged[-1] += " " + x
        else: merged.append(x)
    tot = sum(len(x) for x in merged); st = TL.VO_START[p] + .05; dur = D[p] - .25; acc = 0
    for x in merged:
        a = st + dur * acc / tot; acc += len(x); b = st + dur * acc / tot
        cues.append((a, b, x))
with open(os.path.join(R, "script_en.srt"), "w") as f:
    for i, (a, b, x) in enumerate(cues, 1):
        # wrap to 2 lines max ~42 chars
        words = x.split(); lines = [""]
        for w in words:
            if len(lines[-1]) + len(w) + 1 > 44 and lines[-1]: lines.append(w)
            else: lines[-1] = (lines[-1] + " " + w).strip()
        f.write(f"{i}\n{ts(a, True)} --> {ts(b, True)}\n" + "\n".join(lines) + "\n\n")
chap = [f"{ts(0 if i == 0 else s['start'])} {TITLES[s['name']]}" for i, s in enumerate(TL.SCENES) if s["name"] != "sting"]
open(os.path.join(R, "chapters.txt"), "w").write("\n".join(chap) + "\n")
print("\n".join(chap)); print(len(cues), "cues")
