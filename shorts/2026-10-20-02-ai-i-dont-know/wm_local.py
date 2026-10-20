#!/usr/bin/env python3
"""LATOON roaming watermark (owner-approved 2026-10-10).
Usage: apply_watermark.py input.mp4 output.mp4 [--corners tr,br]
Small cream LATOON mark, 22% opacity, switches position only on scene cuts
(min 5 s dwell; forced switch after 30 s with no cut). Audio copied untouched.
"""
import subprocess, sys, re, os
MARK = '/workspace/latoon/engine/assets/watermark_mark.png'
src, dst = sys.argv[1], sys.argv[2]
# optional: --corners tr,br  (long videos whose chapter tag sits top-left: top-right + bottom-right)
CORNERS = sys.argv[sys.argv.index('--corners') + 1].split(',') if '--corners' in sys.argv else None
# optional: --avoid br:0-34.2,br:599.3-616  never use that corner while a segment overlaps the time range
# (e.g. the scene's own small LATOON maker mark sits there: cold-open diagram, end card)
AVOID = [(a.split(':')[0], *map(float, a.split(':')[1].split('-'))) for a in
         sys.argv[sys.argv.index('--avoid') + 1].split(',')] if '--avoid' in sys.argv else []
TMP = f'/tmp/wm_{os.getpid()}.mp4'

def probe(k):
    return subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries',
        k,'-of','csv=p=0',src]).decode().strip()
W, H = [int(v) for v in probe('stream=width,height').split(',') if v.strip()][:2]  # local copy: newer ffprobe prints a trailing comma
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
    pos = [(56, 44), (W - mw - 56, 44)]
if CORNERS:
    P = {'tl': (56, 44), 'tr': (W - mw - 56, 44), 'br': (W - mw - 56, H - mh - 70), 'bl': (56, H - mh - 70)}
    pos = [P[c] for c in CORNERS]
seq = [pos[i % len(pos)] for i in range(len(cuts) + 1)]
if AVOID and CORNERS:
    name = {v: k for k, v in P.items()}; bounds = [0.0] + cuts + [dur]
    for i in range(len(seq)):
        bad = {c for c, t0, t1 in AVOID if bounds[i] < t1 and bounds[i + 1] > t0}
        if name.get(seq[i]) in bad:
            alt = [p for p in pos if name[p] not in bad]
            if alt: seq[i] = alt[0]
x, y = str(seq[-1][0]), str(seq[-1][1])
for c, p in reversed(list(zip(cuts, seq))):
    x = f"if(lt(t\\,{c})\\,{p[0]}\\,{x})"; y = f"if(lt(t\\,{c})\\,{p[1]}\\,{y})"
fc = (f"[1:v]format=rgba,scale={mw}:-1,colorchannelmixer=aa=0.22[m];"
      f"[0:v][m]overlay=x='{x}':y='{y}':shortest=1:eval=frame[v]")
subprocess.check_call(['ffmpeg','-y','-v','error','-i',src,'-loop','1','-i',MARK,'-filter_complex',fc,
    '-map','[v]','-map','0:a?','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',
    '-c:a','copy','-movflags','+faststart',TMP])
import shutil; shutil.move(TMP, dst)   # faststart on local disk (JuiceFS I/O errors)
print(f'watermarked {dst}: {len(cuts)} switches')
