"""Motion check for the PIL-rendered tickle Short: every footage shot must move in the final (mean frame-to-frame luma diff
over the shot vs a frozen floor measured on a paper/illustration shot). python3 motion_check.py final.mp4"""
import sys, subprocess, json, numpy as np
sys.path.insert(0, '.')
import render as R
V = sys.argv[1]
FOOT = {0:'tk1',1:'palm',2:'self',4:'hand',8:'mri',9:'scans',10:'scans',11:'robot',15:'tk2',17:'fingers',18:'feather',19:'tk3'}
def yavg(ss, t, crop='crop=1080:700:0:600'):
    out = subprocess.run(['ffmpeg','-v','error','-ss',f'{ss:.3f}','-t',f'{t:.3f}','-i',V,'-an','-vf',
                          f'{crop},format=yuv420p,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-','-f','null','-'],
                         capture_output=True, text=True).stdout
    v = [float(l.split('=')[1]) for l in out.splitlines() if 'YAVG' in l]
    return float(np.mean(v)) if v else 0.0
floor = yavg(R.CUTS[20] + 0.6, 1.0)   # end card (grain + slow push only)
rows = []; ok = True
for i, clip in FOOT.items():
    a, b = R.CUTS[i] + 0.15, R.CUTS[i + 1] - 0.15
    d = yavg(a, b - a); p = d >= 2.5 * max(floor, 0.05)
    ok &= p; rows.append((i, clip, round(a, 2), round(b, 2), round(d, 3), 'PASS' if p else 'FAIL'))
print('floor', round(floor, 3))
for r in rows: print(r)
print('MOTION', 'PASS' if ok else 'FAIL')
json.dump(dict(floor=floor, rows=rows, ok=ok), open('qa/motion.json', 'w'), indent=1)
