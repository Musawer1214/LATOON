import os, json
import timeline as TL
from lib import build_caps
R = TL.ROOT
def ts(x, srt=False):
    if srt:
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    return f"{int(x // 60)}:{int(x % 60):02d}"
TITLES = {"hook": "A message with no L", "machine": "Inside the Enigma machine", "mirror": "The reflector's blind spot",
          "poland": "Poland breaks Enigma first", "crib": "Bletchley Park and the crib", "bombe": "Turing's Bombe",
          "lever": "The missing L", "lesson": "How Enigma really fell", "close": "What it never does"}
caps = build_caps()
with open(os.path.join(R, "script_en.srt"), "w") as f:
    for i, (s, e, ch) in enumerate(caps, 1):
        f.write(f"{i}\n{ts(s, True)} --> {ts(e, True)}\n" + " ".join(w for w, _, _ in ch) + "\n\n")
chap = [f"{ts(0 if i == 0 else s['start'])} {TITLES[s['name']]}" for i, s in enumerate(TL.SCENES) if s["name"] != "sting"]
open(os.path.join(R, "chapters.txt"), "w").write("\n".join(chap) + "\n")
md = ["# How Enigma Was Broken: A Letter Could Never Be Itself (LATOON long-form)", "",
      f"Voice: Gemini TTS "Iapetus" (gemini-3.8-flash-tts; last chunk gemini-3.1-flash-tts-preview). Runtime {ts(TL.TOTAL)} ({TL.TOTAL:.1f} s). Timestamps = where each paragraph's voice starts.", ""]
for name, paras in TL.SCENE_PARAS:
    if not paras: continue
    sc = [s for s in TL.SCENES if s["name"] == name][0]
    md += [f"## {ts(sc['start'])} {TITLES[name]}", ""]
    for p in paras: md += [f"**[{ts(TL.VO_START[p])}] P{p+1:02d}** (read {TL.DUR[p]:.1f} s)  ", TL.SCRIPT[p][2], ""]
open(os.path.join(R, "script_en.md"), "w").write("\n".join(md))
print("\n".join(chap)); print(len(caps), "cues")
