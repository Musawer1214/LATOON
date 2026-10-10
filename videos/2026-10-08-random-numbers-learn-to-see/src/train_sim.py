# Real tiny network trained on synthetic 16x16 "cat face" vs "not cat" images (procedural).
import numpy as np, json
from PIL import Image, ImageDraw
R=np.random.default_rng(7)
def cat_img(rng, hi=False, base=False):
    S=256; im=Image.new("L",(S,S),0); d=ImageDraw.Draw(im)
    if base: cx,cy,r,eh,tilt=128,140,78,1.0,0
    else:
        cx=128+rng.uniform(-22,22); cy=140+rng.uniform(-18,18); r=rng.uniform(60,88); eh=rng.uniform(.8,1.25); tilt=rng.uniform(-8,8)
    g=int(200 if base else rng.uniform(150,255))
    # ears
    for s in (-1,1):
        bx=cx+s*r*.62; by=cy-r*.55
        d.polygon([(bx-s*r*.42,by+r*.18),(bx+s*r*.28,by+r*.05),(bx+s*r*.12+s*tilt,by-r*.72*eh)],fill=g)
    d.ellipse([cx-r,cy-r*.85,cx+r,cy+r*.85],fill=g)
    # eyes, nose (dark)
    for s in (-1,1):
        d.ellipse([cx+s*r*.38-r*.15,cy-r*.22-r*.11,cx+s*r*.38+r*.15,cy-r*.22+r*.11],fill=int(g*.15))
    d.polygon([(cx-r*.1,cy+r*.12),(cx+r*.1,cy+r*.12),(cx,cy+r*.24)],fill=int(g*.2))
    if hi: return np.asarray(im,np.float32)/255
    a=np.asarray(im.resize((16,16),Image.BOX),np.float32)/255
    return a
def noncat(rng):
    S=256; im=Image.new("L",(S,S),0); d=ImageDraw.Draw(im)
    k=rng.integers(4)
    cx=128+rng.uniform(-30,30); cy=128+rng.uniform(-30,30); r=rng.uniform(50,95); g=int(rng.uniform(150,255))
    if k==0: d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=g)
    elif k==1: d.rectangle([cx-r,cy-r*.8,cx+r,cy+r*.8],fill=g)
    elif k==2: d.polygon([(cx,cy-r),(cx+r,cy+r*.8),(cx-r,cy+r*.8)],fill=g)
    else:
        for _ in range(6):
            x,y=rng.uniform(30,226,2); rr=rng.uniform(15,45); d.ellipse([x-rr,y-rr,x+rr,y+rr],fill=int(rng.uniform(100,255)))
    if rng.random()<.5:  # distractor dots
        for _ in range(2):
            x,y=rng.uniform(60,200,2); d.ellipse([x-12,y-9,x+12,y+9],fill=int(g*.2))
    return np.asarray(im.resize((16,16),Image.BOX),np.float32)/255
N=3000
X=[];Y=[]
for i in range(N):
    if i%2==0: X.append(cat_img(R)); Y.append(1)
    else: X.append(noncat(R)); Y.append(0)
X=np.array(X).reshape(N,256); Y=np.array(Y,np.float32)
ours=cat_img(R,base=True).reshape(256)
def init(seed):
    r=np.random.default_rng(seed)
    return [r.normal(0,np.sqrt(2/256),(256,16)),np.zeros(16),r.normal(0,np.sqrt(2/16),(16,8)),np.zeros(8),r.normal(0,np.sqrt(1/8),(8,1)),np.zeros(1)]
def fwd(P,x):
    z1=x@P[0]+P[1]; h1=np.maximum(z1,0); z2=h1@P[2]+P[3]; h2=np.maximum(z2,0); z3=h2@P[4]+P[5]; y=1/(1+np.exp(-z3))
    return z1,h1,z2,h2,z3,y[...,0]
# choose seed so our cat starts near 0.48
best=None
for s in range(4000):
    P=init(s); y=fwd(P,ours[None])[-1][0]
    if abs(y-.48)<.004: best=s; break
P=init(best); print("seed",best,fwd(P,ours[None])[-1][0])
snaps=[];losses=[];ourp=[]
lr=.05; step=0
for ep in range(6):
    idx=R.permutation(N)
    for b in range(0,N,32):
        bi=idx[b:b+32]; x=X[bi]; y=Y[bi]
        z1,h1,z2,h2,z3,p=fwd(P,x)
        L=-np.mean(y*np.log(p+1e-9)+(1-y)*np.log(1-p+1e-9))
        g3=((p-y)/len(bi))[:,None]
        gW3=h2.T@g3; gb3=g3.sum(0); gh2=g3@P[4].T; gz2=gh2*(z2>0)
        gW2=h1.T@gz2; gb2=gz2.sum(0); gh1=gz2@P[2].T; gz1=gh1*(z1>0)
        gW1=x.T@gz1; gb1=gz1.sum(0)
        for k,g in enumerate([gW1,gb1,gW2,gb2,gW3,gb3]): P[k]=P[k]-lr*g
        losses.append(float(L)); ourp.append(float(fwd(P,ours[None])[-1][0]))
        if step%10==0: snaps.append([p_.tolist() for p_ in P])
        step+=1
# accuracy on fresh
Xt=[];Yt=[]
for i in range(600):
    if i%2==0: Xt.append(cat_img(R)); Yt.append(1)
    else: Xt.append(noncat(R)); Yt.append(0)
Xt=np.array(Xt).reshape(600,256); acc=np.mean((fwd(P,Xt)[-1]>.5)==np.array(Yt))
print("steps",step,"final loss",np.mean(losses[-50:]),"ours",ourp[-1],"test acc",acc)
print("ourp samples",[round(ourp[i],3) for i in range(0,step,step//12)])
json.dump(dict(seed=best,losses=losses,ourp=ourp,snaps=snaps,ours=ours.tolist(),hi=cat_img(R,hi=True,base=True)[::2,::2].tolist(),
  thumbs=[X[i].tolist() for i in range(64)],thumbY=Y[:64].tolist(),testacc=float(acc)),open("train.json","w"))
