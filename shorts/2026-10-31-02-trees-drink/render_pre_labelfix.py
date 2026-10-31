"""LATOON Short 2026-10-31 #2: How does a tree drink without a pump?  Frame renderer (PIL + ffmpeg), 1080x1920 @30.
python3 render.py still 1.0 5.2 ...      -> /tmp/tstill_<t>.jpg (540x960)
python3 render.py video out.mp4 n0 n1     -> frames n0..n1-1"""
import sys, json, math, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0,'/workspace/latoon/engine_next')
from brand import neuron_star
W,H=1080,1920; FPS=30
FOREST=(16,38,27); SAP=(247,181,56); CREAM=(244,239,225); WATER=(182,222,200); PAPER=(238,232,214); INK=(30,34,28); DRY=(196,92,52)
FD='/workspace/latoon/engine_next/fonts/'
_FC={}
def F(sz,w='Black'):
    k=(int(sz),w)
    if k not in _FC: _FC[k]=ImageFont.truetype(FD+f'Inter-{w}.ttf',int(sz))
    return _FC[k]
SEG='/workspace/latoon/shorts/2026-10-31-02-trees-drink/assets/stock/seg/'
def ease(x): x=min(1,max(0,x)); return x*x*x*(x*(6*x-15)+10)
def eio(x): x=min(1,max(0,x)); return 0.5-0.5*math.cos(math.pi*x)
def lerp(a,b,x): return a+(b-a)*x
# ---------------- footage
class Vid:
    def __init__(s,clip,ss):
        s.p=subprocess.Popen(['ffmpeg','-v','error','-ss',f'{ss:.3f}','-i',SEG+clip,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE); s.last=None
    def frame(s):
        b=s.p.stdout.read(W*H*3)
        if len(b)==W*H*3: s.last=Image.frombytes('RGB',(W,H),b)
        return s.last
VIDS={}
def vframe(key,clip,off,lt):
    if key not in VIDS: VIDS[key]=Vid(clip,off+lt)
    return VIDS[key].frame()
def zoom(im,z,cx=.5,cy=.5):
    bw=W/z; bh=H/z; x0=cx*W-bw/2; y0=cy*H-bh/2; x0=min(max(0,x0),W-bw); y0=min(max(0,y0),H-bh)
    return im.resize((W,H),Image.BICUBIC,box=(x0,y0,x0+bw,y0+bh))
def darken(im,k=0.55,col=FOREST):
    a=np.asarray(im,np.float32)*(1-k)+np.array(col,np.float32)*k; return Image.fromarray(a.astype(np.uint8))
def ground(col=FOREST):
    y=np.linspace(0,1,H)[:,None,None]; a=np.array(col,np.float32)*(0.82+0.32*(1-np.abs(y-.45)*1.5))
    return Image.fromarray(np.clip(np.repeat(np.repeat(a,1,0),W,1),0,255).astype(np.uint8))
GROUND=None
def gnd():
    global GROUND
    if GROUND is None: GROUND=ground()
    return GROUND.copy()
# ---------------- text
def kinetic(img,text,t,t0,acc=(),y=250,size=86,fade=0.18):
    if t<t0: return img
    a=min(1,(t-t0)/fade); sc=1+0.12*(1-ease((t-t0)/0.35))
    f=F(size*sc); words=text.split(' '); d0=ImageDraw.Draw(Image.new('RGB',(1,1)))
    sp=d0.textlength(' ',font=f); ws=[d0.textlength(w,font=f) for w in words]; tw=sum(ws)+sp*(len(words)-1)
    if tw>W-130:
        f=F(size*sc*(W-130)/tw); sp=d0.textlength(' ',font=f); ws=[d0.textlength(w,font=f) for w in words]; tw=sum(ws)+sp*(len(words)-1)
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay); x=(W-tw)/2; pad=28
    d.rounded_rectangle((x-pad,y-pad*0.6,x+tw+pad,y+f.size*1.08+pad*0.25),24,fill=FOREST+(int(225*a),))
    for w_,wl in zip(words,ws):
        col=SAP if w_.strip('.,?!:').upper() in acc else CREAM
        d.text((x,y),w_,font=f,fill=col+(int(255*a),)); x+=wl+sp
    img=img.convert('RGBA'); img.alpha_composite(lay); return img.convert('RGB')
def label(img,text,t,t0,t1,y=1480):
    if t<t0 or t>t1: return img
    a=min(1,(t-t0)/.3,(t1-t)/.3); lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay); f=F(32,'Bold')
    tw=d.textlength(text,font=f)
    if tw>W-100: f=F(32*(W-100)/tw,'Bold'); tw=d.textlength(text,font=f)
    d.rounded_rectangle((W/2-tw/2-22,y-10,W/2+tw/2+22,y+48),14,fill=FOREST+(int(200*a),))
    d.text((W/2-tw/2,y),text,font=f,fill=CREAM+(int(255*a),))
    img=img.convert('RGBA'); img.alpha_composite(lay); return img.convert('RGB')
def big_number(img,text,t,t0,sub=None,y=820):
    if t<t0: return img
    a=min(1,(t-t0)/.2); sc=1+0.18*(1-ease((t-t0)/0.4)); lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    f=F(190*sc); tw=d.textlength(text,font=f)
    d.rounded_rectangle((W/2-tw/2-40,y-30,W/2+tw/2+40,y+f.size*1.12),36,fill=FOREST+(int(215*a),))
    d.text((W/2-tw/2,y),text,font=f,fill=SAP+(int(255*a),))
    if sub:
        f2=F(46,'Bold'); s2=d.textlength(sub,font=f2); d.text((W/2-s2/2,y+f.size*1.12+22),sub,font=f2,fill=CREAM+(int(255*a),),stroke_width=3,stroke_fill=FOREST+(int(255*a),))
    img=img.convert('RGBA'); img.alpha_composite(lay); return img.convert('RGB')
# ---------------- graphics
def ruler(img,t,fill_m,top_mark,cam):
    """height ruler 0-120 m drawn on a tall virtual canvas; cam=(zoom, focus_m) maps it to screen"""
    z,fm=cam; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    ppm=13.0*z                     # px per metre
    def Y(m): return 960-(m-fm)*ppm
    x0=150
    d.line((x0,Y(0),x0,Y(118)),fill=CREAM+(255,),width=5)
    for m in range(0,121,5):
        L=34 if m%10==0 else 18; d.line((x0,Y(m),x0+L,Y(m)),fill=CREAM+(255,),width=4 if m%10==0 else 2)
        if m%20==0 or (m==10): d.text((x0-118,Y(m)-22),f'{m} m',font=F(34,'Bold'),fill=CREAM+(255,))
    # pipe
    px=300; d.rounded_rectangle((px-26,Y(118),px+26,Y(0)+8),20,outline=CREAM+(220,),width=5)
    if fill_m>0: d.rectangle((px-19,Y(fill_m),px+19,Y(0)),fill=WATER+(255,))
    if fill_m>=9.8:
        d.line((px-70,Y(10.4),W-60,Y(10.4)),fill=SAP+(255,),width=5)
        f=F(44,'ExtraBold'); d.text((px+50,Y(10.4)-62),'≈10 m: air pressure’s limit',font=f,fill=SAP+(255,),stroke_width=4,stroke_fill=FOREST+(255,))
    if top_mark>0:
        a=int(255*min(1,top_mark)); d.line((x0,Y(112.7),W-60,Y(112.7)),fill=SAP+(a,),width=6)
        d.text((x0+60,Y(112.7)-70),'112.7 m',font=F(64),fill=SAP+(a,),stroke_width=4,stroke_fill=FOREST+(a,))
    img=img.convert('RGBA'); img.alpha_composite(lay); return img.convert('RGB')
def card(img,lines,t,t0,box=(90,1080,990,1460),push=(1.0,1.2)):
    """evidence inset card (paper) with a highlight underline on the last line"""
    if t<t0: return img
    a=ease((t-t0)/0.35); x0,y0,x1,y1=box; s=0.92+0.08*a
    cw,ch=int((x1-x0)),int((y1-y0)); c=Image.new('RGBA',(cw,ch),(0,0,0,0)); d=ImageDraw.Draw(c)
    d.rounded_rectangle((0,0,cw-1,ch-1),26,fill=PAPER+(255,)); y=34
    for i,(txt,sz,w,col) in enumerate(lines):
        f=F(sz,w); d.text((40,y),txt,font=f,fill=col+(255,)); 
        if i==len(lines)-1:
            hl=ease((t-t0-0.5)/0.8); tw=d.textlength(txt,font=f); d.rectangle((40,y+sz*1.08,40+tw*hl,y+sz*1.08+8),fill=SAP+(255,))
        y+=int(sz*1.32)
    c=c.resize((int(cw*s),int(ch*s)),Image.BICUBIC)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((x0+14,y0+18,x0+14+c.width,y0+18+c.height),26,fill=(0,0,0,int(110*a)))
    sh=sh.filter(ImageFilter.GaussianBlur(14))
    img=img.convert('RGBA'); img.alpha_composite(sh)
    arr=np.asarray(c,np.float32); arr[...,3]*=a; c=Image.fromarray(arr.astype(np.uint8),'RGBA')
    img.alpha_composite(c,(int(x0+(cw-c.width)/2),int(y0+(ch-c.height)/2))); return img.convert('RGB')
def molecules(t,lt):
    """leaf pore at top, chain of water molecules in a tube pulled up; top one escapes"""
    img=gnd(); d=ImageDraw.Draw(img,'RGBA')
    # leaf surface band
    d.rectangle((0,360,W,520),fill=(52,98,58,255)); d.rectangle((0,520,W,540),fill=(36,72,44,255))
    d.text((60,388),'LEAF SURFACE',font=F(40,'ExtraBold'),fill=CREAM)
    d.rectangle((W/2-60,360,W/2+60,540),fill=(16,38,27,255))  # pore
    d.text((W/2+80,560),'pore',font=F(38,'Bold'),fill=CREAM)
    tx0,tx1=W/2-60,W/2+60; d.rectangle((tx0,540,tx1,H),fill=(22,52,36,255)); d.line((tx0,540,tx0,H),fill=CREAM,width=4); d.line((tx1,540,tx1,H),fill=CREAM,width=4)
    step=0.62; k=lt/step; ph=k-int(k); sp=118; r=40
    base=ph*sp  # chain shifts up each step
    ys=[600+i*sp-base*ease(ph*1.6) for i in range(0,14)]
    for i in range(len(ys)-1): d.line((W/2,ys[i],W/2,ys[i+1]),fill=SAP+(200,),width=8)
    for y in ys: d.ellipse((W/2-r,y-r,W/2+r,y+r),fill=WATER+(255,),outline=CREAM,width=3)
    # escaping molecule(s)
    for j in range(3):
        q=(k-j)
        if q<0: continue
        e=q-int(q); ex=W/2+math.sin((int(q)+j)*2.1)*220*e; ey=470-e*360; a=int(255*(1-e))
        d.ellipse((ex-r,ey-r,ex+r,ey+r),fill=WATER+(a,),outline=CREAM+(a,),width=3)
    d.text((60,250),'vapour escapes',font=F(44,'Bold'),fill=CREAM)
    # up arrow
    ay=1080; d.polygon([(230,ay-200),(280,ay-110),(180,ay-110)],fill=SAP); d.rectangle((215,ay-110,245,ay+60),fill=SAP)
    d.text((60,ay+90),'each one tugs',font=F(44,'Bold'),fill=SAP); d.text((60,ay+145),'the next',font=F(44,'Bold'),fill=SAP)
    return img
def xylem(t,lt,dur):
    """many thin tubes, water threads moving up; camera pans from canopy to roots"""
    img=gnd(); d=ImageDraw.Draw(img,'RGBA')
    off=lerp(0,1500,eio(lt/dur))  # virtual canvas 3400 tall
    def Y(v): return v-off
    # canopy blob top, roots bottom
    for i in range(9): d.ellipse((i*140-80,Y(-160),i*140+240,Y(260)),fill=(48,104,60,255))
    for i in range(12):
        x=110+i*78; d.rectangle((x-14,Y(200),x+14,Y(3050)),fill=(26,58,40,255)); d.line((x-14,Y(200),x-14,Y(3050)),fill=CREAM+(160,),width=2); d.line((x+14,Y(200),x+14,Y(3050)),fill=CREAM+(160,),width=2)
        # water thread with moving dashes
        d.rectangle((x-8,Y(200),x+8,Y(3050)),fill=WATER+(140,))
        ph=(t*170+i*37)%120
        yy=3050-ph
        while yy>200:
            d.rectangle((x-8,Y(yy-40),x+8,Y(yy)),fill=WATER+(255,)); yy-=120
    # roots
    for i in range(14):
        x=110+(i%12)*78; d.line((x,Y(3050),x+math.sin(i)*160,Y(3350)),fill=(120,86,52,255),width=10)
    d.rectangle((0,Y(3040),W,Y(3060)),fill=(94,70,44,255))
    d.text((60,Y(3100)),'ROOTS',font=F(56),fill=CREAM)
    d.text((60,Y(300)),'LEAVES',font=F(56),fill=CREAM)
    return img
def pressure_bar(t,lt,dur):
    img=gnd(); d=ImageDraw.Draw(img,'RGBA')
    x0,x1=380,700; y0,y1=520,1600; zero=900
    d.rounded_rectangle((x0,y0,x1,y1),40,outline=CREAM,width=6)
    d.line((x0-80,zero,x1+80,zero),fill=CREAM,width=6); d.text((x1+100,zero-30),'0',font=F(64),fill=CREAM)
    d.text((x1+100,y0+20),'push +',font=F(46,'Bold'),fill=CREAM); d.text((x1+100,y1-80),'pull −',font=F(46,'Bold'),fill=SAP)
    lvl=lerp(0.0,1.0,ease((lt-0.2)/1.6))  # 0 at zero line -> deep negative
    yb=zero+lvl*(y1-60-zero)
    d.rectangle((x0+16,zero,x1-16,yb),fill=SAP+(255,))
    if lvl>0.6: d.text((90,yb-10),'below zero',font=F(52),fill=SAP)
    return img
def stretch(t,lt,dur):
    img=gnd(); d=ImageDraw.Draw(img,'RGBA')
    s=ease(lt/1.6)
    top=760-200*s; bot=1260+200*s
    d.rectangle((300,top-60,780,top),fill=(120,86,52,255)); d.rectangle((300,bot,780,bot+60),fill=(120,86,52,255))
    n=9
    for i in range(n):
        y=lerp(top+40,bot-40,i/(n-1)); r=48-14*s*(1-abs(i-(n-1)/2)/((n-1)/2))
        d.ellipse((540-r,y-r,540+r,y+r),fill=WATER+(255,),outline=CREAM,width=3)
        if i<n-1:
            y2=lerp(top+40,bot-40,(i+1)/(n-1)); d.line((540,y+r,540,y2-r),fill=SAP+(230,),width=int(8-3*s))
    d.polygon([(540,top-80-60*s),(500,top-20-60*s),(580,top-20-60*s)],fill=SAP) if False else None
    return img
def doc_callout(t,lt,dur):
    page=Image.new('RGB',(W,H),(214,206,186)); d=ImageDraw.Draw(page)
    px0,py0,px1,py1=70,260,1010,1660; d.rectangle((px0+12,py0+16,px1+12,py1+16),fill=(170,160,140)); d.rectangle((px0,py0,px1,py1),fill=PAPER)
    d.text((px0+50,py0+50),'SCIENCE · 16 April 1965 · Vol 148',font=F(30,'Bold'),fill=(110,100,84))
    d.text((px0+50,py0+110),'Sap Pressure in',font=F(66,'ExtraBold'),fill=INK); d.text((px0+50,py0+190),'Vascular Plants',font=F(66,'ExtraBold'),fill=INK)
    d.text((px0+50,py0+290),'Scholander, Bradstreet, Hemmingsen, Hammel',font=F(32,'Medium'),fill=(80,76,66))
    body=['“As long predicted, sap pressures','during transpiration are normally','negative, ranging from −4 or −5','atmospheres in a damp forest to','−80 atmospheres in the desert.”']
    y=py0+420; hl_rows={2:(0.62,1.0),3:(0,0.53),4:(0,1.0)}
    hlp=ease((lt-0.7)/1.2)
    for i,l in enumerate(body):
        f=F(50,'Medium')
        if i in (2,3,4):
            xa=d.textlength('negative, ranging from ',font=f) if i==2 else 0
            xb=d.textlength('atmospheres in a damp forest',font=f) if i==3 else d.textlength(l,font=f)
            seg=(i-2)/3; q=min(1,max(0,(hlp-seg)*3))
            if q>0: d.rectangle((px0+50+xa,y+6,px0+50+xa+(xb-xa)*q,y+62),fill=(250,214,120))
        d.text((px0+50,y),l,font=f,fill=INK); y+=84
    d.text((px0+50,py1-90),'doi:10.1126/science.148.3668.339',font=F(30,'Medium'),fill=(110,100,84))
    z=lerp(1.0,1.22,eio(min(1,lt/2.2))); return zoom(page,z,0.47,0.58)
def gel_tree(t,lt,dur):
    img=gnd(); d=ImageDraw.Draw(img,'RGBA')
    d.rounded_rectangle((120,420,960,1560),60,fill=(200,226,212,70),outline=CREAM,width=5)
    d.text((150,330),'gel “synthetic tree” (illustration)',font=F(42,'Bold'),fill=CREAM)
    # leaf serpentine top, root serpentine bottom, trunk channel
    def serp(y0,yrows,col):
        pts=[]
        for r in range(yrows):
            y=y0+r*60; xa,xb=(260,820) if r%2==0 else (820,260); pts+= [(xa,y),(xb,y)]
        d.line(pts,fill=col,width=14,joint='curve'); return pts
    lp=serp(520,5,WATER+(255,)); rp=serp(1220,5,WATER+(255,))
    d.line((540,800,540,1220),fill=WATER+(255,),width=14)
    # flow dashes up the trunk
    for k in range(6):
        y=1220-((t*260+k*70)%420); d.rectangle((530,y-24,550,y),fill=SAP+(255,))
    # vapour wisps above leaf
    for k in range(5):
        e=((t*0.8+k*0.2)%1.0); x=280+k*130; y=480-e*130; a=int(200*(1-e)); d.ellipse((x-16,y-16,x+16,y+16),fill=CREAM+(a,))
    d.text((150,1590),'water in (root)',font=F(40,'Bold'),fill=CREAM); d.text((620,440-60),'',font=F(10))
    d.text((640,1590),'flow at −1.0 MPa',font=F(40,'Bold'),fill=SAP)
    d.text((838,590),'LEAF',font=F(40),fill=CREAM) ; d.text((838,1290),'ROOT',font=F(40),fill=CREAM)
    return img
def thread(t,lt,dur,mode):
    img=gnd(); d=ImageDraw.Draw(img,'RGBA')
    x0,x1=470,610; d.rectangle((x0,200,x1,1750),fill=(22,52,36,255)); d.line((x0,200,x0,1750),fill=CREAM,width=5); d.line((x1,200,x1,1750),fill=CREAM,width=5)
    if mode=='wobble':
        pts=[(540+math.sin(y/55+t*9)*10*min(1,lt/0.5),y) for y in range(200,1751,10)]
        d.line(pts,fill=WATER+(255,),width=46)
    else:
        b=ease((lt-0.3)/0.8); gapc=980; r=10+120*b
        sep=ease((lt-1.0)/0.7)*220
        d.rectangle((520,200,560,gapc-r-sep),fill=WATER+(255,)); d.rectangle((520,gapc+r+sep,560,1750),fill=WATER+(255,))
        if b>0: d.ellipse((540-r,gapc-r,540+r,gapc+r),outline=CREAM,width=6,fill=(16,38,27,255))
        if sep>0: d.text((660,gapc-40),'snap',font=F(70),fill=SAP)
        d.text((660,gapc-150),'air bubble',font=F(48,'Bold'),fill=CREAM) if b>0.3 else None
    return img
# ---------------- end card
def endcard(t):
    img=gnd(); a=ease(t/0.5)
    st=neuron_star(int(300*(0.9+0.1*ease(t/0.6))),ink=CREAM,core=SAP)
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); lay.alpha_composite(st,((W-st.width)//2,700)); d=ImageDraw.Draw(lay)
    word='LATOON'; fp=F(110); ws=[d.textlength(c,font=fp) for c in word]; tr=26; tw=sum(ws)+tr*5; x=(W-tw)/2
    for c,w_ in zip(word,ws): d.text((x,1050),c,font=fp,fill=CREAM+(255,)); x+=w_+tr
    f2=F(46,'Bold'); s='Voyaging the Unseen'; l=d.textlength(s,font=f2); d.text(((W-l)/2,1200),s,font=f2,fill=SAP+(255,))
    arr=np.asarray(lay,np.float32); arr[...,3]*=a; lay=Image.fromarray(arr.astype(np.uint8),'RGBA')
    img=img.convert('RGBA'); img.alpha_composite(lay); return zoom(img.convert('RGB'),1.0+0.03*t/1.8)
# ---------------- shots
DUR=56.6
CUTS=[0,1.95,3.95,6.1,8.0,10.2,11.85,14.05,16.4,19.15,21.4,23.85,25.55,28.15,30.3,33.0,35.2,37.9,40.4,43.1,45.4,47.5,49.85,54.9,DUR]
PX='Footage · Pexels '
def push(lt,dur,z0,z1): return lerp(z0,z1,eio(lt/dur))
def punch(t,tk,amt=0.15): return 1+amt*ease((t-tk)/0.3) if t>tk else 1.0
def shot(t,i):
    t0=CUTS[i]; lt=t-t0; dur=CUTS[i+1]-t0
    if i==0:
        im=zoom(vframe('s0','seq.mp4',0,lt),push(lt,dur,1.0,1.22),.5,.45)
        im=kinetic(im,'A 100 m tree. No pump?',t,0.25,acc={'100','PUMP?'})
        return label(im,PX+'8552289',t,0.3,1.9)
    if i==1:
        im=zoom(vframe('s1','red.mp4',0,lt),push(lt,dur,1.18,1.0)*punch(t,2.9,0.12),.5,.4)
        return label(im,PX+'19950424',t,2.0,3.9)
    if i in (2,3,4):
        if i==4: bg=darken(zoom(vframe('s4','red.mp4',2.0,lt),push(lt,dur,1.0,1.15),.5,.5),0.5)
        else: bg=darken(zoom(vframe('s2','trunk.mp4',0,t-CUTS[2]),push(t-CUTS[2],CUTS[4]-CUTS[2],1.0,1.25),.5,.6),0.55)
        fill=10.4*ease((t-4.3)/1.8)
        if i==2: cam=(1.0,40)  # whole lower part
        elif i==3: cam=(lerp(1.0,3.2,eio(lt/1.0)),lerp(40,10,eio(lt/1.0)))
        else: x=eio(lt/1.9); cam=(lerp(3.2,0.95,x),lerp(10,60,x))
        im=ruler(bg,t,fill,ease((t-9.4)/0.4) if i==4 else 0,cam)
        if i==2: im=kinetic(im,'Suction tops out near 10 m',t,4.3,acc={'10'})
        if i==4: im=kinetic(im,'Redwoods: past 110 m',t,8.4,acc={'110'},y=560)
        return label(im,'Illustration',t,t0+0.3,CUTS[i+1]-0.1,420)
    if i==5:
        bg=zoom(vframe('s5','seq.mp4',3.0,lt),push(lt,dur,1.1,1.3),.5,.35)
        im=card(bg,[('Koch, Sillett, Jennings & Davis',34,'Bold',(90,84,70)),('Nature 428, 851 (2004)',34,'Bold',(90,84,70)),('Tallest known tree:',54,'ExtraBold',INK),('a redwood, 112.7 m',54,'ExtraBold',INK)],t,t0+0.05,(90,1000,990,1430))
        return zoom(im,push(lt,dur,1.0,1.2),.5,.63)
    if i==6:
        im=zoom(vframe('s6','canopy.mp4',0,lt),push(lt,dur,1.0,1.25),.5,.35)
        im=kinetic(im,'Start: the leaves',t,12.0,acc={'LEAVES'})
        return label(im,PX+'34106794',t,12.0,14.0)
    if i==7:
        im=zoom(vframe('s7','leaf.mp4',0,lt),push(lt,dur,1.0,1.3)*punch(t,15.2,0.12),.5,.5)
        im=kinetic(im,'Sun evaporates leaf water',t,14.25,acc={'SUN'})
        return label(im,PX+'30833644',t,14.2,16.3)
    if i==8:
        im=zoom(molecules(t,lt),push(lt,dur,1.0,1.18),.5,.4)
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==9:
        im=darken(zoom(vframe('s9','trunk.mp4',3.0,lt),push(lt,dur,1.0,1.3),.5,.5),0.25)
        im=kinetic(im,'Thin tubes: xylem',t,19.4,acc={'XYLEM'})
        return label(im,PX+'8552812',t,19.3,21.3)
    if i==10:
        im=xylem(t,lt,dur)
        im=kinetic(im,'Unbroken threads',t,21.6,acc={'UNBROKEN'})
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==11:
        bg=darken(zoom(vframe('s11','trunk.mp4',5.0,lt),push(lt,dur,1.15,1.0),.5,.5),0.62)
        im=kinetic(bg,'Not pushed.',t,23.95,acc={'PUSHED.'},y=700,size=110)
        if t>25.0:
            d=ImageDraw.Draw(im); p=ease((t-25.0)/0.25); d.line((200,770,200+680*p,770),fill=DRY,width=16)
        return zoom(im,punch(t,24.6,0.1),.5,.4)
    if i==12:
        im=zoom(pressure_bar(t,lt,dur),push(lt,dur,1.0,1.2),.5,.55)
        im=kinetic(im,'Pulled: negative pressure',t,25.65,acc={'PULLED:','NEGATIVE'})
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==13:
        im=zoom(stretch(t,lt,dur),push(lt,dur,1.0,1.25),.5,.5)
        im=kinetic(im,'Water under tension',t,28.3,acc={'TENSION'},y=230)
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==14:
        im=doc_callout(t,lt,dur)
        return label(im,'Science, 1965 · abstract',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==15:
        im=zoom(vframe('s15','mist.mp4',0,lt),push(lt,dur,1.0,1.2),.5,.5)
        im=big_number(im,'−5 atm',t,33.5,'about, in a damp forest')
        return label(im,PX+'11514996',t,33.1,35.1,1480)
    if i==16:
        im=zoom(vframe('s16','dry.mp4',0,lt),push(lt,dur,1.2,1.0),.5,.5)
        im=big_number(im,'−80 atm',t,35.9,'in the desert')
        return label(im,PX+'36249169',t,35.3,37.8,1480)
    if i==17:
        bg=zoom(vframe('s17','drop.mp4',0,lt),push(lt,dur,1.0,1.2),.5,.4)
        im=card(bg,[('Wheeler & Stroock',36,'Bold',(90,84,70)),('Nature 455, 208 (2008)',36,'Bold',(90,84,70)),('A gel “synthetic tree”',54,'ExtraBold',INK),('pulls water the same way',50,'ExtraBold',INK)],t,t0+0.1,(90,1050,990,1480))
        im=zoom(im,push(lt,dur,1.0,1.2),.5,.66)
        return label(im,PX+'8374012',t,38.0,40.3,300)
    if i==18:
        im=zoom(gel_tree(t,lt,dur),push(lt,dur,1.15,1.0),.5,.5)
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==19:
        im=zoom(thread(t,lt,dur,'wobble'),push(lt,dur,1.0,1.3),.5,.5)
        im=kinetic(im,'Fragile',t,43.25,acc={'FRAGILE'})
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==20:
        im=zoom(vframe('s20','dry.mp4',4.0,lt),push(lt,dur,1.0,1.25),.5,.55)
        im=kinetic(im,'Severe drought',t,45.55,acc={'DROUGHT'})
        return label(im,PX+'36249169',t,45.5,47.4,1480)
    if i==21:
        im=zoom(thread(t,lt,dur,'snap'),push(lt,dur,1.0,1.35),.5,.5)
        im=kinetic(im,'Snap.',t,48.5,acc={'SNAP.'})
        return label(im,'Illustration',t,t0+0.2,CUTS[i+1]-0.1,1480)
    if i==22:
        im=zoom(vframe('s22','canopy.mp4',4.5,lt),push(lt,dur,1.4,1.0)*punch(t,52.9,0.12),.5,.45)
        im=kinetic(im,'Sun-powered',t,52.7,acc={'SUN-POWERED'})
        return label(im,PX+'34106794',t,50.0,52.6,1480)
    return endcard(t-CUTS[23])
VIG=None
def finish(img,fr):
    global VIG
    if VIG is None:
        y,x=np.mgrid[0:H,0:W]; r=np.sqrt(((x-W/2)/(W/2))**2+((y-H/2)/(H/2))**2); VIG=(1-0.28*np.clip(r-0.55,0,1)**1.5)[...,None].astype(np.float32)
    a=np.asarray(img,np.float32)*VIG
    # one whole-frame grade: slight warm lift
    a=a*np.array([1.02,1.0,0.97],np.float32)+np.array([3,2,0],np.float32)
    rng=np.random.default_rng(fr//3); a+=rng.normal(0,2.0,(H//4,W//4,1)).repeat(4,0).repeat(4,1)[:H,:W]
    return np.clip(a,0,255).astype(np.uint8)
def idx(t): return max(k for k in range(len(CUTS)-1) if CUTS[k]<=t)
if __name__=='__main__':
    if sys.argv[1]=='still':
        for a in sys.argv[2:]:
            t=float(a); VIDS.clear()
            Image.fromarray(finish(shot(t,idx(t)),int(t*30))).resize((540,960)).save(f'/tmp/tstill_{a}.jpg'); print('saved',a)
    else:
        out=sys.argv[2]; n0=int(sys.argv[3]); n1=int(sys.argv[4])
        p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
        cur=None
        for n in range(n0,n1):
            t=n/FPS; i=idx(t)
            p.stdin.write(finish(shot(t,i),n).tobytes())
        p.stdin.close(); p.wait()
