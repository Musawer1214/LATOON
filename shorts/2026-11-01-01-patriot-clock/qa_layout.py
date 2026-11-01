"""Write qa_layout.json (text boxes per time) for engine_next/contrast_check.py by wrapping render.py's text helpers."""
import json, render as R
from PIL import ImageDraw, Image
items=[]; CUR={'T':0}
ok,ol,ob=R.kinetic,R.label,R.big_number
def kin(img,text,t,t0,acc=(),y=290,size=92,fade=0.18):
    out=ok(img,text,t,t0,acc,y,size,fade)
    if t>=t0+0.4:
        f=R.F(size); d=ImageDraw.Draw(Image.new('RGB',(1,1))); tw=d.textlength(text,font=f)
        if tw>R.W-150: s=size*(R.W-150)/tw; f=R.F(s); tw=d.textlength(text,font=f)
        x=(R.W-tw)/2; items.append(dict(kind='text',role='kinetic',txt=text,T=t,size=f.size,box=[int(x),int(y),int(x+tw),int(y+f.size*1.1)]))
    return out
def lab(img,text,t,t0,t1,y=1500):
    out=ol(img,text,t,t0,t1,y)
    if t0+0.35<=t<=t1-0.35:
        f=R.F(32,'Bold'); d=ImageDraw.Draw(Image.new('RGB',(1,1))); tw=d.textlength(text,font=f)
        if tw>R.W-120: f=R.F(32*(R.W-120)/tw,'Bold'); tw=d.textlength(text,font=f)
        items.append(dict(kind='text',role='label',txt=text,T=t,size=f.size,box=[int(R.W/2-tw/2),int(y),int(R.W/2+tw/2),int(y+40)]))
    return out
def big(img,text,t,t0,sub=None,y=800,col=None,size=190):
    out=ob(img,text,t,t0,sub,y,col,size)
    if t>=t0+0.45:
        f=R.F(size); d=ImageDraw.Draw(Image.new('RGB',(1,1))); tw=d.textlength(text,font=f)
        if tw>R.W-140: f=R.F(size*(R.W-140)/tw); tw=d.textlength(text,font=f)
        items.append(dict(kind='text',role='big',txt=text,T=t,size=f.size,box=[int(R.W/2-tw/2),int(y+20),int(R.W/2+tw/2),int(y+f.size)]))
    return out
R.kinetic,R.label,R.big_number=kin,lab,big
t=0.0
while t<R.CUTS[-2]:
    i=R.idx(t); lt=t-R.CUTS[i]
    # zoom wrappers change positions after drawing in a few shots (punch/zoom after text); those are flagged by the check if off
    R.shot(t,i); t=round(t+0.25,2)
json.dump(dict(items=items),open('qa_layout.json','w')); print(len(items),'items')
