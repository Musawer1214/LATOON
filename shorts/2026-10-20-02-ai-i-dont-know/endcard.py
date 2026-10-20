"""End card clip (engine end_card, PLAYBOOK s1.5/s5.4) from 57.05 s to 59.5 s; card built from 57.25 s; the last 0.6 s dissolve
into the hook's first frame (loop). Needs three/first.png (frame 0 of the 3D render)."""
import os, sys, subprocess
os.environ['LATOON_FMT'] = 'short'; sys.path.insert(0, '/workspace/latoon/engine')
from core import *
from components import end_card, loop_blend
first = Image.open('three/first.png').convert('RGB')
T0, T1, TC, D = 57.05, 59.5, 57.25, 59.5
os.makedirs('endcard/f', exist_ok=True)
n = int(round((T1 - T0) * 30))
for i in range(n):
    t = T0 + i / 30
    im = ground('paper'); cv = Cv(im); end_card(cv, t - TC); cv.done(); im = grain(im, int(t * 10) % 3).convert('RGB')
    im = loop_blend(im, first, t + 1 / 30, D)
    im.save(f'endcard/f/{i:04d}.png')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-framerate', '30', '-i', 'endcard/f/%04d.png', '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', 'endcard/endcard.mp4'], check=True)
print('frames', n)
