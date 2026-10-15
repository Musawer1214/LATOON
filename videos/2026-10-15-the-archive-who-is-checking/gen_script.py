"""Builds script_en.json/.md and dub/dub_script_{ur,ps}.json from script_src.py; reports words, runtime,
per-speaker load, TTS request units (<=90 s per request per s16.2) and dub length checks."""
import json, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from script_src import L, BASE_STYLE, PROMPTS, RECORDS, HOLDS, OWNER_MASTER, OWNER_FIXES, END_TAIL
HERE = os.path.dirname(os.path.abspath(__file__))
WPM = {"NARRATOR": 152, "CHATGPT": 170, "CLAUDE": 160, "PARRY": 158, "ELIZA": 120}   # character pace (s16: 150-170)
SCENES = {"S1": "The Archive", "S2": "The Corridor", "S3": "The Long Way Here", "S4": "ELIZA's Room", "S5": "The Table", "S6": "What We Know"}
GAP = 0.35            # breath between turns
OPEN_IMAGE_ONLY = 22.0
END_SCREEN = 12.0

def words(s): return len(re.findall(r"[A-Za-z0-9'\u2019.]*[A-Za-z0-9]|[\u0600-\u06FF]+", s))
def scene_of(i): return "S6" if i.startswith("E-") else i.split("-")[0]   # E- = added end beats inside Scene 6

# ---- owner-verbatim gate: every owner line present, same speaker, same order, word for word (3 approved fixes only)
OWNER = json.load(open(OWNER_MASTER))["lines"]
_cur = {x[0]: x for x in L}
_bad = []
for o in OWNER:
    c = _cur.get(o["id"])
    want = OWNER_FIXES[o["id"]][1] if o["id"] in OWNER_FIXES else o["text"]
    if o["id"] in OWNER_FIXES: assert OWNER_FIXES[o["id"]][0] == o["text"], ("fix base drifted", o["id"])
    if not c or c[1] != o["speaker"] or c[2] != want: _bad.append(o["id"])
_order = [x[0] for x in L if x[0] in {o["id"] for o in OWNER}]
assert _order == [o["id"] for o in OWNER], "owner line order changed"
assert not _bad, ("owner lines not verbatim", _bad)
OWNER_IDS = {o["id"] for o in OWNER}

lines, t, signoff_end = [], OPEN_IMAGE_ONLY, None
for (i, spk, en, tweak, ur, ps, src) in L:
    w = words(en); d = w / WPM[spk] * 60 + (0.6 if spk == "ELIZA" else 0)
    style = BASE_STYLE[spk] + ("; " + tweak if tweak else "")
    lines.append(dict(id=i, scene=scene_of(i), speaker=spk, text=en, delivery=style, words=w, est_sec=round(d, 2),
                      start=round(t, 2), src=src, prompt_after=PROMPTS.get(i), record_after=RECORDS.get(i), hold_after=HOLDS.get(i, 0),
                      ur=ur, ps=ps))
    lines[-1]["tag"] = "FIX" if i in OWNER_FIXES else ("OWNER" if i in OWNER_IDS else "ADDED")
    if i == "S6-06": signoff_end = t + d
    t += d + GAP + HOLDS.get(i, 0)
total_words = sum(l["words"] for l in lines)
owner_words = sum(l["words"] for l in lines if l["tag"] != "ADDED")
runtime = max(t, signoff_end + END_SCREEN)      # end-tail lines play inside the end screen

# TTS request units: per speaker, lines in script order split into the fewest requests of <= 88 s, balanced
import math
units = {}
for spk in WPM:
    ls = [l for l in lines if l["speaker"] == spk]
    if not ls: continue
    tot = sum(l["est_sec"] for l in ls); n = max(1, math.ceil(tot / 80)); target = tot / n
    units[spk] = []; acc = 0.0
    for l in ls:
        if not units[spk] or (acc >= target * len(units[spk]) - 1e-6 and len(units[spk]) < n):
            units[spk].append(dict(name="archive_%s_u%d" % (spk.lower(), len(units[spk])), lines=[], sec=0.0, words=0))
        u = units[spk][-1]; u["lines"].append(l["id"]); u["sec"] = round(u["sec"] + l["est_sec"], 1); u["words"] += l["words"]; acc += l["est_sec"]

# dub length check: script-character ratio vs English (Urdu/Pashto scripts are denser; >1.0 chars and
# >1.15x words flags a line to shorten), plus est. speaking time at 2.6 words/s UR, 2.5 PS
flags = []
def chars(x): return len(re.sub(r"[\s\.,;:!?\"'\u060c\u061f\u06d4\-\u2014]", "", x))
for l in lines:
    en_t = chars(l["text"]) / 14.5
    for lang in ("ur", "ps"):
        tx = l[lang]
        if l["speaker"] == "ELIZA" or tx == l["text"]: continue
        dl = chars(tx) / 13.0
        if dl > en_t * 1.08 + 0.25: flags.append((l["id"], lang, round(dl, 1), round(en_t, 1)))
out = dict(title_candidates=["AI Went From Chatbot to Battlefield. Who's Checking?", "From ELIZA to AI at War: Who Is Still Checking?"],
           title_status="owner decides at publish", disclosure="Fictional dialogue. Facts sourced in the video description.",
           status="FINAL (owner approved 2026-10-15 17:24 'go ahead with video completion')", version="v3 2026-10-15 (v2 + who's-who intro S1-00x2..x6; owner lines verbatim + 3 approved fixes; additions tagged)",
           stats=dict(spoken_words=total_words, owner_line_words=owner_words, added_words=total_words - owner_words,
                      owner_lines=sum(1 for l in lines if l["tag"] != "ADDED"), added_lines=sum(1 for l in lines if l["tag"] == "ADDED"),
                      signoff_ends_at=f"{int(signoff_end//60)}:{int(signoff_end%60):02d}", est_runtime_sec=round(runtime), est_runtime=f"{int(runtime//60)}:{int(runtime%60):02d}",
                      image_only_open_sec=OPEN_IMAGE_ONLY, end_screen_sec=END_SCREEN,
                      words_by_speaker={s: sum(l["words"] for l in lines if l["speaker"] == s) for s in WPM}),
           characters=BASE_STYLE, scenes=SCENES,
           lines=[{k: v for k, v in l.items() if k not in ("ur", "ps")} for l in lines],
           tts_units={s: u for s, u in units.items()})
json.dump(out, open(os.path.join(HERE, "script_en.json"), "w"), ensure_ascii=False, indent=1)
os.makedirs(os.path.join(HERE, "dub"), exist_ok=True)
for lang in ("ur", "ps"):
    json.dump(dict(lang=lang, status="FINAL (owner approved 2026-10-15 17:24)", version="v3 2026-10-15", note="ELIZA lines stay English in every track (her 1966 script spoke only English). The owner's files (Idea_Final_Dialogue.md, Idea_Master_Script.json, Idea.pdf) contain no Urdu or Pashto, so owner lines are Hark translations of his English, kept faithful to it; tag OWNER/FIX/ADDED mirrors script_en.md.",
                   lines=[dict(id=l["id"], speaker=l["speaker"], tag=l["tag"], text=l[lang], delivery=l["delivery"], en_sec=l["est_sec"]) for l in lines],
                   tts_units={s: [dict(name=u["name"].replace("archive_", "archive_%s_" % lang), lines=u["lines"]) for u in us] for s, us in units.items()}),
              open(os.path.join(HERE, "dub", "dub_script_%s.json" % lang), "w"), ensure_ascii=False, indent=1)
# markdown
md = ["# The Archive: Who Is Still Checking? (English script v3, FINAL: owner approved 2026-10-15 17:24)", "",
      f"*{out['disclosure']}* (on screen throughout the open and at every scene change)", "",
      f"**Spoken words:** {total_words} ({owner_words} in the owner's {out['stats']['owner_lines']} lines + {total_words - owner_words} in {out['stats']['added_lines']} added lines)  |  **Estimated runtime:** {out['stats']['est_runtime']} (22 s image-only open, character pace 120-170 wpm, breaths, owner holds, 12 s end screen; sign-off ends ~{out['stats']['signoff_ends_at']})", "",
      "**Owner rule (2026-10-15):** every owner line is word for word from Idea_Final_Dialogue.md / Idea_Master_Script.json, except three approved factual fixes marked **[FIX]** (S2-05, S3-01, S5-24). Everything marked **[ADDED]** is new and sits between owner lines; no owner line was cut, merged or reordered. Untagged lines are the owner's. Diff and decisions: SCRIPT_RECONCILE.md.", "",
      "**Title:** not chosen (owner decides at publish): " + " / ".join(out["title_candidates"]), "",
      "Speaker voices and style prompts: VOICE_MAP.md. Added lines carry an `x` or `E-` id. Fact sources: FACTCHECK.md.", ""]
cur = None
for l in lines:
    if l["scene"] != cur:
        cur = l["scene"]; st = l["start"]; md += ["", f"## {cur} · {SCENES[cur]}  (~{int(st//60)}:{int(st%60):02d})", ""]
        if cur == "S1": md.append("*0:00-0:22 image only: low room hum, a tiny match strike, no triumphant cue.*\n")
    tag = {"ADDED": " **[ADDED]**", "FIX": " **[FIX]** (approved factual fix; owner text: \"" + OWNER_FIXES.get(l["id"], ("", ""))[0] + "\")", "OWNER": ""}[l["tag"]]
    if l["id"] in END_TAIL and l["id"] == END_TAIL[0]: md.append("*[end screen begins; the next lines play over the end card]*\n")
    md.append(f"**{l['id']} {l['speaker']}:** {l['text']}{tag}  \n*delivery: {l['delivery']}*" + (f"  \n*src: {l['src']}*" if l["src"] else ""))
    if l["hold_after"]: md.append(f"\n*[hold {l['hold_after']} s]*")
    if l["record_after"]: md.append(f"\n> **RECORD INSERT** (monochrome engraved plate): {l['record_after'][0]} | {l['record_after'][1]} | *{l['record_after'][2]}*")
    if l["prompt_after"]: md.append(f"\n> **VIEWER PROMPT (on screen):** {l['prompt_after']}")
    md.append("")
md += ["", "## TTS request units (per character, <=85 s each)", ""]
for s, us in units.items():
    for u in us: md.append(f"- `{u['name']}` {u['sec']} s, {u['words']} words: {', '.join(u['lines'])}")
open(os.path.join(HERE, "script_en.md"), "w").write("\n".join(md) + "\n")
print(json.dumps(out["stats"], indent=1)); print("units:", {s: len(u) for s, u in units.items()}, "total", sum(len(u) for u in units.values()))
print("dub length flags:", len(flags)); [print(" ", f) for f in flags]
# scene timing
for sc in SCENES:
    ls = [l for l in lines if l["scene"] == sc]; print(sc, "%d:%02d" % (ls[0]["start"] // 60, ls[0]["start"] % 60), sum(l["words"] for l in ls), "words")
