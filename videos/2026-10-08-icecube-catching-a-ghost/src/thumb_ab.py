from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess
F="/workspace/latoon/template/inter/extras/ttf/Inter-%s.ttf"
def f(w,s): return ImageFont.truetype(F%w,s)
PAPER=(239,232,217);INK=(40,35,32);TERRA=(188,84,54);CREAM=(250,244,230);OCHRE=(206,150,56)
def outline_text(d,xy,t,font,fill,stroke=(25,22,20),sw=6,anchor="lm"):
    d.text(xy,t,font=font,fill=fill,stroke_width=sw,stroke_fill=stroke,anchor=anchor)
# B: real photo
im=Image.open("img/icl_2023.jpg").convert("RGB")
W,H=1920,1080
r=max(W/im.width,H/im.height);im=im.resize((int(im.width*r)+1,int(im.height*r)+1),Image.LANCZOS)
x0=0
im=im.crop((x0,0,x0+W,H))
g=Image.new("L",(W,H));gd=ImageDraw.Draw(g)
for x in range(W): gd.line([(x,0),(x,H)],fill=int(max(0,200*(1-x/(W*0.75)))))
im=Image.composite(Image.new("RGB",(W,H),(22,24,28)),im,g)
d=ImageDraw.Draw(im)
outline_text(d,(100,560),"A TELESCOPE",f("Black",150),CREAM)
outline_text(d,(100,730),"MADE OF ICE",f("Black",150),(232,120,84))
d.rounded_rectangle((100,860,640,960),50,fill=CREAM)
d.text((370,910),"NOBEL 2026",font=f("Black",54),fill=INK,anchor="mm")
d.text((1820,1030),"LATOON",font=f("Black",44),fill=CREAM,anchor="rm")
im.resize((1280,720),Image.LANCZOS).save("thumbnail_B.png")
# C: fingernail frame
subprocess.run(["ffmpeg","-v","error","-y","-ss","15","-i","icecube-catching-a-ghost_final.mp4","-frames:v","1","/tmp/f15full.png"],check=True)
im=Image.open("/tmp/f15full.png").convert("RGB")
# cover old counter box
d=ImageDraw.Draw(im)
sh=Image.new("RGBA",im.size,(0,0,0,0));sd=ImageDraw.Draw(sh)
sd.rounded_rectangle((52,632,1222,1002),34,fill=(60,45,30,60));sh=sh.filter(ImageFilter.GaussianBlur(14))
im=Image.alpha_composite(im.convert("RGBA"),sh).convert("RGB")
d=ImageDraw.Draw(im)
d.rounded_rectangle((40,620,1210,990),34,fill=(244,238,224),outline=(205,194,173),width=3)
d.text((90,745),"65 BILLION",font=f("Black",150),fill=TERRA,anchor="lm")
d.text((95,895),"through your fingernail. Every second.",font=f("Bold",58),fill=INK,anchor="lm")
d.text((1820,1030),"LATOON",font=f("Black",44),fill=(88,79,70),anchor="rm")
im.resize((1280,720),Image.LANCZOS).save("thumbnail_C.png")
print("ok")
