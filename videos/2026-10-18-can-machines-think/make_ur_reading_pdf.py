import json,html,sys
from weasyprint import HTML
d=json.load(open('script.json')); ur={l['id']:l['text'] for l in json.load(open('dub/script_ur.json'))['lines']}
e=html.escape; rows=[]; ch=None
for l in d['lines']:
    if l['chapter_title']!=ch:
        ch=l['chapter_title']; rows.append(f"<h2>{e(ch)}</h2>")
    rows.append(f"<div class=card><div class=id>{l['id']}</div><div class=rtl>{e(ur[l['id']])}</div></div>")
box="""<div class=box><b>How to use this</b><ul>
<li>Read it aloud in your own words. Change sentences, add dialogue, add or drop lines freely.</li>
<li>Before a changed line, say the card number (e.g. "C3-04") so I can match it. For a new line, say "new line after C3-04".</li>
<li>This is a draft read, not the final recording. I write the final Urdu from it, then English and Pashto follow it, and you record the final Urdu and Pashto after you confirm.</li></ul></div>"""
css="""@page{size:A4;margin:15mm;@bottom-center{content:counter(page);font-size:8pt;color:#9a8a78}}
body{font-family:Inter;color:#2b2420}h1{font-size:20pt;margin:0}.sub{color:#7a6a5a;font-size:9pt;margin:2px 0 10px}
h2{font-size:12pt;color:#8a3b2e;border-bottom:1px solid #d9c9b0;margin-top:16px;padding-bottom:3px}
.box{border:1px solid #d9c9b0;background:#fbf7f0;border-radius:6px;padding:8px 12px;font-size:9pt}.box ul{margin:4px 0 0 0;padding-left:16px}
.card{border:1px solid #e6dccb;border-radius:6px;padding:7px 10px;margin:8px 0;page-break-inside:avoid;background:#fdfbf7}
.id{font-size:8pt;color:#8a3b2e;font-weight:600}
.rtl{direction:rtl;text-align:right;font-family:'Noto Naskh Arabic';font-size:15pt;line-height:1.9}"""
st=d['meta']['stats']
h=f"<html><head><meta charset=utf-8><style>{css}</style></head><body><h1>Can Machines Think? · اردو</h1><div class=sub>Urdu script v2 · {st['lines']} cards · read-through for your revisions · 2026-10-24</div>{box}{''.join(rows)}</body></html>"
HTML(string=h).write_pdf(sys.argv[1])
