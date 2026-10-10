import math, os, io, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import aggdraw
W, H, FPS = 1920, 1080, 25
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_DIR = "/workspace/latoon/template/inter/extras/ttf"
MONO = "/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Regular.otf"
MONOB = "/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Bold.otf"
SERIF = "/workspace/latoon/branding/fonts/PlayfairDisplay.ttf"
# ---------------- palette: archival dossier (manila paper, ink, oxblood, brass, bakelite)
PAPER = (234, 225, 205); PAPER2 = (224, 213, 189); PAPER3 = (208, 195, 168)
INK = (33, 30, 28); INK2 = (80, 72, 64); MUT = (138, 126, 110); RULE = (198, 185, 160)
SNOW = (247, 243, 233)
OX = (146, 40, 34); OX2 = (196, 116, 98); OX3 = (226, 182, 166)
BRASS = (168, 128, 62); BRASS2 = (212, 180, 118); BRASS3 = (120, 88, 40)
STEEL = (92, 98, 102); STEEL2 = (146, 152, 154); STEEL3 = (198, 200, 198)
BAKE = (40, 37, 35); BAKE2 = (62, 58, 55)
GREEN = (72, 90, 76); GREEN2 = (122, 140, 120)
LAMP = (250, 214, 140); LAMP2 = (236, 168, 72)
LOGO = (255, 77, 0)
BG0 = PAPER
def cl(x, a=0.0, b=1.0): return a if x < a else b if x > b else x
def pr(t, a, b): return cl((t - a) / (b - a)) if b > a else float(t >= a)
def eo(x): x = cl(x); return 1 - (1 - x) ** 3
def ei(x): x = cl(x); return x ** 3
def eio(x): x = cl(x); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def esm(x): x = cl(x); return x * x * (3 - 2 * x)
def eback(x, s=1.4):
    x = cl(x); c3 = s + 1; return 1 + c3 * (x - 1) ** 3 + s * (x - 1) ** 2
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): t = cl(t); return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))
def win(t, a, b, fi=.6, fo=.6):
    return eo(pr(t, a, a + fi)) * (1 - eio(pr(t, b - fo, b)))
_fc = {}
def F(size, w="Medium"):
    k = (max(6, int(size)), w)
    if k not in _fc:
        path = {"mono": MONO, "monob": MONOB, "serif": SERIF, "math": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"}.get(w) or os.path.join(FONT_DIR, f"Inter-{w}.ttf")
        _fc[k] = ImageFont.truetype(path, k[0])
    return _fc[k]
def math_mask(*a, **k): raise NotImplementedError
