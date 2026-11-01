"""Music + SFX mix for the tickle Short (v2.0 recipe from research/2026-10-31-audio-v2/audio/mix_v2.py, as used in the airplane Short)."""
import json,subprocess,numpy as np,soundfile as sf,pyloudnorm as pyln,pedalboard as pb
from scipy import signal
SR=48000; DUR=52.0; N=int(DUR*SR)
H='/workspace/latoon/research/2026-10-31-audio-v2/music/cand/'; SF='/workspace/latoon/engine_next/sound/sfx/'
def load(f):
    a=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(a,np.float32).reshape(-1,2).copy()
v,_=sf.read('voice/voice_proc.wav',dtype='float32'); V=np.zeros((N,2),np.float32); n=min(len(v),N); V[:n,0]=v[:n]; V[:n,1]=v[:n]
M=np.zeros((N,2),np.float32)
def place(src,o,t0,t1,fi=.3,fo=.8):
    a=src[int(o*SR):int(o*SR)+int((t1-t0)*SR)].copy(); n=len(a); g=np.ones(n,np.float32)
    fi_n,fo_n=int(fi*SR),int(fo*SR); g[:fi_n]=np.linspace(0,1,fi_n); g[-fo_n:]*=np.linspace(1,0,fo_n); i=int(t0*SR); M[i:i+n]+=a*g[:,None]
m1=load(H+'1168.mp3'); m2=load(H+'727.mp3')
place(m1,4.0,0.0,20.1,fi=.05,fo=0.9)      # cue 1: the puzzle and the idea (squirm, dull, prediction, forecast)
place(m2,6.0,19.5,DUR,fi=0.6,fo=1.6)      # cue 2: the evidence and the test (1998, robot arm, delay, twist, payoff)
auto=np.zeros(N,np.float32)
def ramp(t0,t1,db):
    i0,i1=int(t0*SR),int(t1*SR); auto[i0:i1]=np.linspace(auto[i0-1] if i0>0 else 0,db,i1-i0); auto[i1:]=db
ramp(0,0.01,0)
ramp(5.0,5.3,-4)         # 'your own finger ... feels dull': thinner
ramp(8.7,9.1,0)          # lift on 'that's because your brain predicts'
ramp(17.4,17.8,-5)       # thin under 'turns that feeling down'
ramp(19.6,20.0,0)        # evidence
ramp(27.5,27.9,1)        # 'got clever' lift
ramp(33.0,33.4,0)
ramp(39.4,39.8,-4)       # 'the forecast missed'
ramp(42.9,43.4,-18)      # near-silence before the payoff
ramp(43.95,44.4,-2)      # lift on the last line
ramp(49.6,50.4,-4)
env=np.sqrt(np.convolve(V[:,0]**2,np.ones(1440)/1440,'same')); sp=(env>10**(-48/20)).astype(np.float32)
k=int(0.35*SR); sp=np.convolve(sp,np.ones(k)/k,'same'); sp=np.clip(sp*2,0,1)
g=10**((auto-19.5*sp)/20); M*=g[:,None]
mus=M*1.6
S=np.zeros((N,2),np.float32)
def sfx(name,t,gain=0.5):
    a=load(SF+name); a=a[:int(1.6*SR)]; b,a2=signal.butter(2,9000,'low',fs=SR); a=signal.lfilter(b,a2,a,axis=0).astype(np.float32)
    i=int(t*SR); n=min(len(a),N-i); S[i:i+n]+=a[:n]*gain
sfx('ui_pop_light.wav',0.15,0.35)   # hook keyword
sfx('soft_click.wav',14.14,0.4)      # the copy splits off
sfx('paper_rustle.wav',25.05,0.3)    # 1998 evidence card
sfx('ui_tick.wav',34.38,0.4)         # delay slider reaches 0.2 s
sfx('ui_pop_dry.wav',40.18,0.3)      # 'missed': the gap opens
sfx('chime.wav',50.25,0.35)          # end card
mix=V+mus+S
m=pyln.Meter(SR); mix*=10**((-14-m.integrated_loudness(mix))/20)
tp=lambda x: np.max(np.abs(signal.resample_poly(x,4,1,axis=0)))
if tp(mix)>10**(-1.1/20): mix=pb.Pedalboard([pb.Limiter(threshold_db=-1.6,release_ms=80)])(mix.T.copy(),SR).T
mix*=10**((-14-m.integrated_loudness(mix))/20)
sf.write('mix.wav',mix,SR,subtype='PCM_16')
sel=sp>0.5
print('LUFS',round(m.integrated_loudness(mix),2),'TP',round(20*np.log10(tp(mix)),2),
      'music under speech dB rel voice',round(20*np.log10(np.sqrt(np.mean(mus[sel]**2))/np.sqrt(np.mean(V[sel]**2))),1),
      'music in gaps',round(20*np.log10(np.sqrt(np.mean(mus[~sel]**2))+1e-9),1))
