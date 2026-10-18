import json,html,sys
from weasyprint import HTML
d=json.load(open('script.json')); ur={l['id']:l['text'] for l in json.load(open('dub/script_ur.json'))['lines']}
ps={l['id']:l['text'] for l in json.load(open('dub/script_ps.json'))['lines']}
e=html.escape; rows=[]; ch=None
for l in d['lines']:
    if l['chapter_title']!=ch:
        ch=l['chapter_title']; rows.append(f"<h2>{e(ch)}</h2>")
    rows.append(f"""<div class=card><div class=id>{l['id']}</div>
<div class=lab>اردو</div><div class=rtl>{e(ur[l['id']])}</div>
<div class=lab>پښتو</div><div class=rtl>{e(ps[l['id']])}</div>
<div class=lab2>English</div><div class=en>{e(l['text'])}</div></div>""")
changes="""<div class=box><b>What changed in v2</b><ul>
<li>Urdu is your revised version, with your four sticky notes applied (C0-01 “someone you know” instead of a student from a city, C0-02 “feesad” without “baar”, C1-07 exam centre instead of cities, C4-09 new example).</li>
<li>C4-09 now uses Searle’s own example: a fire simulation that never warms the room.</li>
<li>Unneeded place names removed everywhere (San Diego, Manchester, London, New York, Seoul, Berkeley, Harvard/MIT). Years stay.</li>
<li>English and Pashto rewritten line by line to follow your Urdu flow: full, connected sentences, short explanations after technical terms.</li>
<li>Longer, clearer sentences mean the English now runs about 17:30 instead of 13:20.</li></ul></div>"""
css="""@page{size:A4;margin:15mm;@bottom-center{content:counter(page);font-size:8pt;color:#9a8a78}}
body{font-family:Inter;color:#2b2420}h1{font-size:20pt;margin:0}.sub{color:#7a6a5a;font-size:9pt;margin:2px 0 10px}
h2{font-size:12pt;color:#8a3b2e;border-bottom:1px solid #d9c9b0;margin-top:16px;padding-bottom:3px}
.box{border:1px solid #d9c9b0;background:#fbf7f0;border-radius:6px;padding:8px 12px;font-size:9pt}.box ul{margin:4px 0 0 0;padding-left:16px}
.card{border:1px solid #e6dccb;border-radius:6px;padding:7px 10px;margin:8px 0;page-break-inside:avoid;background:#fdfbf7}
.id{font-size:8pt;color:#8a3b2e;font-weight:600}
.lab{font-family:'Noto Naskh Arabic';font-size:8pt;color:#9a8a78;text-align:right;margin-top:3px}
.lab2{font-size:7.5pt;color:#9a8a78;margin-top:4px}
.rtl{direction:rtl;text-align:right;font-family:'Noto Naskh Arabic';font-size:14pt;line-height:1.85}
.en{font-size:9.5pt;color:#4a3f36;line-height:1.45}"""
st=d['meta']['stats']
h=f"<html><head><meta charset=utf-8><style>{css}</style></head><body><h1>Can Machines Think?</h1><div class=sub>Script v2 · Urdu, Pashto and English · {st['lines']} lines · for voice recording · 2026-10-18</div>{changes}{''.join(rows)}</body></html>"
HTML(string=h).write_pdf(sys.argv[1])
