#!/usr/bin/env python3
"""LATOON roaming watermark (owner-approved 2026-10-10).
Usage: apply_watermark.py input.mp4 output.mp4
Small cream LATOON mark, 22% opacity, switches position only on scene cuts
(min 5 s dwell; forced switch after 30 s with no cut). Audio copied untouched.
"""
import subprocess, sys, re, os
MARK = '/workspace/latoon/branding/watermark_mark.png'
src, dst = sys.argv[1], sys.argv[2]

def probe(k):
    return subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries',
        k,'-of','csv=p=0',src]).decode().strip()
W, H = map(int, probe('stream=width,height').split(','))
dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src]).decode())

log = subprocess.run(['ffmpeg','-i',src,'-vf',"select='gt(scene,0.12)',showinfo",'-an','-f','null','-'],
                     capture_output=True, text=True).stderr
raw = [float(x) for x in re.findall(r'pts_time:([0-9.]+)', log)]
cuts, last = [], 0.0
for t in raw:
    while t - last > 30:          # no cut for 30 s: force a switch
        last += 30; cuts.append(round(last, 2))
    if t - last >= 5:
        cuts.append(round(t, 2)); last = t
while dur - last > 30:
    last += 30; cuts.append(round(last, 2))

vertical = H > W
mw = 210 if vertical else 200
mh = round(80 * mw / 254)
if vertical:   # top-left, top-right (above titles), lower-left (above captions)
    pos = [(64, 110), (W - mw - 64, 110), (64, 1340)]
else:          # landscape: top corners only, captions own the bottom
    pos = [(W - mw - 56, 44), (W - mw - 56, H - mh - 40)]  # this build: chapter tag sits top-left
seq = [pos[i % len(pos)] for i in range(len(cuts) + 1)]
x, y = str(seq[-1][0]), str(seq[-1][1])
for c, p in reversed(list(zip(cuts, seq))):
    x = f"if(lt(t\\,{c})\\,{p[0]}\\,{x})"; y = f"if(lt(t\\,{c})\\,{p[1]}\\,{y})"
fc = (f"[1:v]format=rgba,scale={mw}:-1,colorchannelmixer=aa=0.22[m];"
      f"[0:v][m]overlay=x='{x}':y='{y}':shortest=1:eval=frame[v]")
subprocess.check_call(['ffmpeg','-y','-v','error','-i',src,'-loop','1','-i',MARK,'-filter_complex',fc,
    '-map','[v]','-map','0:a?','-c:v','libx264','-preset','veryfast','-crf','20','-maxrate','4500k','-bufsize','9000k','-pix_fmt','yuv420p',
    '-c:a','aac','-b:a','192k','-movflags','+faststart',dst])
print(f'watermarked {dst}: {len(cuts)} switches')
