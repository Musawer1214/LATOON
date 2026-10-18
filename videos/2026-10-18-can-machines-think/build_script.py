# Generates script.json, script_en.md, dub/script_ur.json, dub/script_ps.json from lines.py
import json, re, sys
sys.path.insert(0, '.')
from lines import L, CHAPTERS
WPM = 155.0          # English narration target (PLAYBOOK s4.6: 150-170)
TITLE_CARD = 3.0     # after C0-05
END_CARD = 18.0      # end card + end-screen space (shown, never spoken)
chn = {c[0]: c[1] for c in CHAPTERS}
t = 0.0; rows = []
for i, l in enumerate(L):
    w = len(re.findall(r"[A-Za-z0-9'\-\.%]+", l['en']))
    dur = w / WPM * 60
    p = l.get('pause', 0.5)
    rows.append(dict(id=l['id'], chapter=l['ch'], chapter_title=chn[l['ch']], start_s=round(t, 1),
                     est_dur_s=round(dur, 1), pause_after_s=p, words=w, text=l['en'],
                     visual=l['vis'], layer=l['layer'], claims=l['src']))
    t += dur + p
    if l['id'] == 'C0-05': t += TITLE_CARD
speech_end = t; total = t + END_CARD
def mmss(s): return f"{int(s//60)}:{int(s%60):02d}"
words = sum(r['words'] for r in rows)
meta = dict(title_working="Can Machines Think?", series="Big Questions", world="Ideas + Machines (bridge)",
            version="v2 2026-10-18", status="SCRIPT v2 (owner Urdu flow applied), awaiting owner final approval",
            narrator="single narrator (Gemini Iapetus EN later; owner records UR/PS himself)",
            closing_line_rule="'LATOON. Voyaging the Unseen.' is SHOWN on the end card, never spoken (PLAYBOOK s4.3)",
            visual_rule="language-neutral: on-screen text only numbers, years, names, English terms, short labels; quotes as cards; no burned narration captions",
            stats=dict(spoken_words=words, wpm_assumed=WPM, lines=len(rows), title_card_s=TITLE_CARD,
                       speech_ends=mmss(speech_end), end_card_s=END_CARD, est_runtime=mmss(total), est_runtime_s=round(total)),
            chapters=[dict(id=c[0], title=c[1], start=mmss(next(r['start_s'] for r in rows if r['chapter']==c[0]))) for c in CHAPTERS])
json.dump(dict(meta=meta, lines=rows), open('script.json','w'), ensure_ascii=False, indent=1)
for lang in ('ur','ps'):
    out = dict(lang=lang, version="v2 2026-10-18", note="line-by-line with script.json ids; everyday spoken Pakistani style; technical terms in English; numbers as digits; closing line never spoken; recorded by the owner after approval",
               lines=[dict(id=l['id'], chapter=l['ch'], text=l[lang], en=l['en']) for l in L])
    json.dump(out, open(f'dub/script_{lang}.json','w'), ensure_ascii=False, indent=1)
# markdown
md = ["# Can Machines Think? — script v2 (English)", "",
      f"- **Status:** SCRIPT v2 (owner Urdu flow applied), awaiting owner final approval · **Series:** Big Questions · **Version:** 2026-10-18",
      f"- **Narration:** single narrator · **Spoken words:** {words} · **Est. runtime:** ~{mmss(total)} (speech ends ~{mmss(speech_end)} at {int(WPM)} wpm, + {int(END_CARD)} s end card) · times are approximate", "",
      "Visual notes are in script.json (one per line). The closing channel line is shown on the end card only, never spoken. Claim tags like [T3] point to FACTCHECK.md.", ""]
md.append("## Chapters"); md.append("")
for c in meta['chapters']: md.append(f"- {c['start']}  {c['title']}")
md.append("")
n = 0; cur = None
for r in rows:
    if r['chapter'] != cur:
        cur = r['chapter']; md += ["", f"## {chn[cur]}  (~{mmss(r['start_s'])})", ""]
    n += 1
    tags = (" " + " ".join(f"[{c}]" for c in r['claims'])) if r['claims'] else ""
    md.append(f"**{n:02d}** · `{r['id']}` · ~{mmss(r['start_s'])} — {r['text']}{tags}")
    md.append("")
    if r['id']=='C0-05': md += ["*(Title card: CAN MACHINES THINK? · Big Questions)*", ""]
md += ["*(End card shown, never spoken: Neuron star · L A T O O N · Voyaging the Unseen · end-screen space)*", ""]
open('script_en.md','w').write("\n".join(md))
print(words, 'words', mmss(speech_end), mmss(total)); [print(c) for c in meta['chapters']]
