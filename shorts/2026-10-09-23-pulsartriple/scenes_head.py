# Pulsar triple: oxblood-umber, cream cards, amber/rust/sage
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (52, 32, 30), (34, 20, 20)
INKC = (246, 238, 220); WHT = (246, 238, 220)
PAPER, PAPER2, INK = (238, 226, 200), (224, 210, 180), (40, 32, 28)
YEL, RED, TEA = (230, 170, 50), (204, 92, 56), (70, 126, 112)
GRN, BRN, PLM = (112, 154, 96), (126, 84, 52), (120, 70, 110)
MUTE, SHAD, LINEC = (180, 168, 148), (12, 8, 8), (96, 84, 74)
GOLD = YEL; BL, BL2 = YEL, YEL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (40, 24, 24), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-8, 9, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    im = Image.open(os.path.join(IMGDIR, "fast.jpg")).convert("RGB")
    IM["fast"] = _rounded(ImageOps.fit(im, (880, 640), Image.LANCZOS, centering=(.45, .5)), 30)
    ar = Image.open(os.path.join(IMGDIR, "art.jpg")).convert("RGB").crop((0, 205, 1200, 720))
    IM["art"] = _rounded(ImageOps.fit(ar, (940, 560), Image.LANCZOS), 30)
    IM["artR"] = _rounded(ImageOps.fit(ar.crop((560, 40, 1200, 515)), (760, 700), Image.LANCZOS), 30)
    IM["artL"] = _rounded(ImageOps.fit(ar.crop((0, 0, 760, 515)), (860, 580), Image.LANCZOS), 30)
def img(cv, key, cx, cy, sc=1.0, a=1.0, src=None):
    a = cl(a * cv.ga)
    if a <= 0.01 or sc <= 0.02: return
    cv.done()
    s = src if src is not None else IM[key]
    s = s.convert("RGBA")
    if abs(sc - 1) > 0.003:
        s = s.resize((max(1, int(s.width * sc)), max(1, int(s.height * sc))), Image.BILINEAR)
    if a < 0.99:
        s = s.copy(); s.putalpha(s.getchannel("A").point(lambda v: int(v * a)))
    x, y = int(cv.X(cx) - s.width / 2), int(cv.Y(cy) - s.height / 2)
    sx0, sy0 = max(0, -x), max(0, -y); x0, y0 = max(0, x), max(0, y)
    sx1, sy1 = min(s.width, W - x), min(s.height, H - y)
    if sx1 <= sx0 or sy1 <= sy0: return
    cv.im.alpha_composite(s.crop((sx0, sy0, sx1, sy1)), dest=(x0, y0))
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, a=1):
    cv.rrect(x0 + 8, y0 + 14, x1 + 8, y1 + 14, r, fill=SHAD, a=.55 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a)
    cv.rrect(x0 + 10, y0 + 10, x1 - 10, y1 - 10, max(4, r - 8), outline=mix(fill, INK, .18), w=2, oa=.7 * a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or YEL, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or INK, a, "Black")
