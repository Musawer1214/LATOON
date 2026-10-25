import json,html
from weasyprint import HTML
e=html.escape
en=json.load(open('v3_en.json')); ps=json.load(open('v3_ps.json'))
ur=json.load(open('v3_ur.json'))
psd={c['id']:c['ps'] for s in ps['sections'] for c in s['cards']}
rows=[]
for i,s in enumerate(en['sections']):
    rows.append(f"<h2>{e(s['title'])}<span class=rt>{e(ps['sections'][i].get('title_ur',''))}</span></h2>")
    for c in s['cards']:
        rows.append(f"<div class=card><div class=id>{c['id']}</div><div class=lab>اردو</div><div class=rtl>{e(ur[c['id']])}</div><div class=lab>پښتو</div><div class=rtl>{e(psd[c['id']])}</div><div class=lab2>English</div><div class=en>{e(c['en'])}</div></div>")
css="""@page{size:A4;margin:15mm;@bottom-center{content:counter(page);font-size:8pt;color:#9a8a78}}
body{font-family:Inter;color:#2b2420}h1{font-size:20pt;margin:0}.sub{color:#7a6a5a;font-size:9pt;margin:2px 0 10px}
h2{font-size:12pt;color:#8a3b2e;border-bottom:1px solid #d9c9b0;margin-top:16px;padding-bottom:3px}.rt{float:right;font-family:'Noto Naskh Arabic';font-weight:normal}
.box{border:1px solid #d9c9b0;background:#fbf7f0;border-radius:6px;padding:8px 12px;font-size:9pt}.box ul{margin:4px 0 0;padding-left:16px}
.card{border:1px solid #e6dccb;border-radius:6px;padding:7px 10px;margin:8px 0;page-break-inside:avoid;background:#fdfbf7}
.id{font-size:8pt;color:#8a3b2e;font-weight:600}.lab{font-family:'Noto Naskh Arabic';font-size:8pt;color:#9a8a78;text-align:right;margin-top:3px}
.lab2{font-size:7.5pt;color:#9a8a78;margin-top:4px}.rtl{direction:rtl;text-align:right;font-family:'Noto Naskh Arabic';font-size:14pt;line-height:1.85}
.en{font-size:9.5pt;color:#4a3f36;line-height:1.45}"""
box="""<div class=box><b>Recording notes</b><ul><li>Urdu is your final v3 text, unchanged. Pashto and English follow it card by card.</li>
<li>Say the card number before each line; 2 s between lines; repeat the whole line after a mistake.</li>
<li>Please check the Pashto spellings: ایډا لَولېس، اوتهیلو، مېري لي فائیفر، چیني کوټه. Change anything freely while recording and tell me, so subtitles match.</li>
<li>English runs about 16 minutes at the narrator's pace.</li></ul></div>"""
h=f"<html><head><meta charset=utf-8><style>{css}</style></head><body><h1>Can Machines Think?</h1><div class=sub>Final script v3 · Urdu, Pashto, English · 52 cards · 2026-10-26</div>{box}{''.join(rows)}</body></html>"
HTML(string=h).write_pdf('Can_Machines_Think_v3_UR_PS_EN.pdf')
