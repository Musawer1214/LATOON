import json,subprocess,numpy as np,soundfile as sf,pyloudnorm as pyln
from scipy import signal
SR=48000; DUR=58.7; N=int(DUR*SR)
H='/workspace/latoon/research/2026-10-31-audio-v2/music/cand/'; SF='/workspace/latoon/engine_next/sound/sfx/'
def load(f):
    a=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(a,np.float32).reshape(-1,2).copy()
v,_=sf.read('voice/voice_proc.wav',dtype='float32'); V=np.zeros((N,2),np.float32); V[:len(v),0]=v[:N]; V[:len(v),1]=v[:N]
TL=json.load(open('voice/timeline.json'))
M=np.zeros((N,2),np.float32)
def place(src,o,t0,t1,fi=.3,fo=.8):
    a=src[int(o*SR):int(o*SR)+int((t1-t0)*SR)].copy(); n=len(a); g=np.ones(n,np.float32)
    fi_n,fo_n=int(fi*SR),int(fo*SR); g[:fi_n]=np.linspace(0,1,fi_n); g[-fo_n:]*=np.linspace(1,0,fo_n); i=int(t0*SR); M[i:i+n]+=a*g[:,None]
m1=load(H+'1168.mp3'); m2=load(H+'727.mp3')
place(m1,16.0,0.0,21.4,fi=.05,fo=1.0)       # hook + history + test: cue 1
place(m2,30.0,20.9,DUR,fi=1.0,fo=1.6)       # force-lines + inquiry: cue 2
auto=np.zeros(N,np.float32)
def ramp(t0,t1,db):
    i0,i1=int(t0*SR),int(t1*SR); auto[i0:i1]=np.linspace(auto[i0-1] if i0>0 else 0,db,i1-i0); auto[i1:]=db
ramp(0,0.01,0)
ramp(15.6,16.1,-6)     # crack opens: music thins
ramp(18.2,18.6,-3)
ramp(21.0,21.5,0)      # lift for the force lines
ramp(38.0,38.5,-8)     # before 'That's fatigue'
ramp(39.9,40.5,-1)
ramp(45.8,46.4,-18)    # near-silence before the payoff
ramp(51.0,51.5,-2)     # lift on the last lines
ramp(56.4,57.2,-4)
# sidechain duck under speech
env=np.sqrt(np.convolve(V[:,0]**2,np.ones(1440)/1440,'same')); sp=(env>10**(-48/20)).astype(np.float32)
k=int(0.35*SR); sp=np.convolve(sp,np.ones(k)/k,'same'); sp=np.clip(sp*2,0,1)
duck=-19.5*sp
g=10**((auto+duck)/20); M*=g[:,None]
# base level: music rel to voice
mus=M*1.25
S=np.zeros((N,2),np.float32)
def sfx(name,t,gain=0.5):
    a=load(SF+name); a=a[:int(1.6*SR)]; i=int(t*SR); n=min(len(a),N-i); S[i:i+n]+=a[:n]*gain
sfx('ui_pop_light.wav',0.35,0.35)      # hook text
sfx('soft_click.wav',4.5,0.35)         # 1954
sfx('paper_rustle.wav',10.5,0.3)       # tank
sfx('ui_tick.wav',18.3,0.5)            # crack ring
sfx('low_swell.wav',20.6,0.4)          # into force lines
sfx('ui_pop_dry.wav',28.5,0.4)         # x3
sfx('ui_tick.wav',36.2,0.45); sfx('ui_tick.wav',36.9,0.45)  # crack steps
sfx('stamp.wav',38.75,0.35)            # fatigue
sfx('ui_tick.wav',43.4,0.5)            # inquiry ring
sfx('chime.wav',56.95,0.35)            # end card
mix=V+mus+S
m=pyln.Meter(SR); L=m.integrated_loudness(mix); mix*=10**((-14-L)/20)
tp=lambda x: np.max(np.abs(signal.resample_poly(x,4,1,axis=0)))
import pedalboard as pb
if tp(mix)>10**(-1.1/20): mix=pb.Pedalboard([pb.Limiter(threshold_db=-1.6,release_ms=80)])(mix.T,SR).T
mix*=10**((-14-m.integrated_loudness(mix))/20)
sf.write('mix.wav',mix,SR,subtype='PCM_16')
print('LUFS',round(m.integrated_loudness(mix),2),'TP',round(20*np.log10(tp(mix)),2))
# voice vs music level
vm=np.sqrt(np.mean(V[V!=0]**2)); 
sel=sp>0.5; print('music under speech dB rel voice',round(20*np.log10(np.sqrt(np.mean((mus[sel])**2))/np.sqrt(np.mean(V[sel]**2))),1))
