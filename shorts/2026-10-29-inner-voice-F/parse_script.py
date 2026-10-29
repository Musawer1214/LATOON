import re,json
src=open('/workspace/latoon/research/2026-10-28-inner-voice/script_en_v2_OWNER.md').read()
src=re.sub(r'<!-- Page \d+ -->','',src)
src=src.replace('**THE HIDDEN MIND / SCRIPT V2**','').replace('Does Everyone Have a Voice in Their Head?\n','\n')
body=src.split('## 0:00 The Hook',1)[1]
parts=re.split(r'\n## (\d+:\d+) (.+)\n','\n## 0:00 The Hook\n'+body)
secs=[]
for i in range(1,len(parts),3):
    t,title,txt=parts[i],parts[i+1],parts[i+2]
    txt=re.sub(r'\*\[.*?\]\*','[[BEEP]]',txt)
    txt=txt.replace('**','')
    txt=re.sub(r'\s+',' ',txt).strip()
    secs.append(dict(time=t,title=title.strip(),text=txt))
n=0
for s in secs:
    w=len(s['text'].replace('[[BEEP]]','').split()); n+=w; print(s['time'],s['title'],w)
print('total',n)
json.dump(secs,open('sections.json','w'),indent=1,ensure_ascii=False)
