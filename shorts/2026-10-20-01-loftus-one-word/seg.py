# chunked render (sandbox commands time out at 120 s): python3 seg.py START_FRAME END_FRAME -> /tmp/lsegs/seg_<START>.mp4
import sys, os, subprocess
sys.argv = [sys.argv[0]] + sys.argv[1:]
a, b = int(sys.argv[1]), int(sys.argv[2])
import render as R
from multiprocessing import Pool
os.makedirs("/tmp/lsegs", exist_ok=True)
b = min(b, int(R.TOTAL * R.FPS))
out = f"/tmp/lsegs/seg_{a:05d}.mp4"
ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{R.W}x{R.H}", "-r", str(R.FPS),
                       "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
with Pool(2, initializer=R.load_imgs) as pool:
    for im in pool.imap(R.frame, range(a, b), chunksize=4): ff.stdin.write(im.tobytes())
ff.stdin.close(); ff.wait(); print("ok", a, b, out)
