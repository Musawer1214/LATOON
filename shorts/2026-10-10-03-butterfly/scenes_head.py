# butterfly motion dazzle: moss-charcoal, cream paper, amber/terracotta/sage
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (40, 50, 40), (24, 32, 27)
INKC = (246, 238, 220); WHT = (246, 238, 220)
PAPER, PAPER2, INK = (238, 228, 204), (222, 210, 182), (36, 34, 28)
YEL, RED, TEA = (232, 172, 52), (206, 98, 60), (70, 126, 112)
GRN, BRN, PLM = (122, 160, 100), (126, 84, 52), (120, 70, 110)
MUTE, SHAD, LINEC = (180, 172, 150), (10, 12, 8), (96, 94, 78)
GOLD = YEL; BL, BL2 = YEL, YEL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (30, 38, 30), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-8, 9, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k in ("fly", "scarce", "zebra", "aus", "fuj", "io"):
        IM[k] = Image.open(os.path.join(IMGDIR, k + ".jpg")).convert("RGB")
    for k, f in (("pr", "pea_real.png"), ("pb", "pea_blank.png")):
        s = Image.open(os.path.join(IMGDIR, f)).convert("RGBA"); IM[k] = s.resize((760, int(760 * s.height / s.width)), Image.LANCZOS)
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
def kb(cv, key, cx, cy, w, h, zoom, r, a=1, fx=.5, fy=.5, shadow=True):
    # crop centred on fractional point (fx, fy) of the source, zoom>=1 relative to cover-fit
    src = IM[key]; k = min(src.width / w, src.height / h) / zoom
    cw, ch = w * k, h * k
    x0 = cl(fx * src.width - cw / 2, 0, src.width - cw); y0 = cl(fy * src.height - ch / 2, 0, src.height - ch)
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BILINEAR)
    if shadow:
        cv.rrect(cx - w / 2 + 8, cy - h / 2 + 14, cx + w / 2 + 8, cy + h / 2 + 14, r, fill=SHAD, a=.55 * a)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
def flap(cv, key, cx, cy, wpx, t, f=2.2, a=1.0, ph=0.0, lo=.3):
    s = IM[key]; sx = lo + (1 - lo) * abs(math.cos(math.pi * (f * t + ph)))
    nw = max(8, int(wpx * sx)); nh = int(wpx * s.height / s.width)
    img(cv, None, cx, cy, 1, a, s.resize((nw, nh), Image.BILINEAR))
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
def arrow_v(cv, x, y0, y1, col, w=16, a=1):
    d = 1 if y1 > y0 else -1
    cv.line([(x, y0), (x, y1 - d * 10)], col, w, a)
    cv.poly([(x - 34, y1 - d * 46), (x + 34, y1 - d * 46), (x, y1)], col, a)
