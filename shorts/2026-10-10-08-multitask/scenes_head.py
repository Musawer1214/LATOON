# multitask: oxblood-brown + cream paper, mustard / teal / coral
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (70, 32, 30), (30, 14, 16)
INKC = (246, 238, 222); WHT = (246, 238, 222)
PAPER, PAPER2, INK = (244, 234, 214), (226, 212, 184), (40, 24, 24)
MUST, CORAL, TEAL = (236, 184, 64), (220, 94, 72), (72, 148, 136)
YEL = MUST; COP = MUST; RED = CORAL; SAGE = TEAL
MUTE, SHAD, LINEC = (170, 150, 130), (10, 4, 4), (110, 80, 70)
GOLD = MUST; BL, BL2 = CORAL, CORAL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
_MASK = {}
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (30, 14, 16), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(7)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k in ["aerial", "harper", "macaque", "neurons", "work"]:
        im = Image.open(os.path.join(IMGDIR, k + ".jpg")).convert("RGB")
        im.thumbnail((1500, 1500)); IM[k] = im
def photo(cv, key, x0, y0, x1, y1, p, z0=1.0, z1=1.15, fx=.5, fy=.5, a=1.0, r=26):
    a = cl(a * cv.ga)
    if a <= .01: return
    cv.done()
    s = IM[key]; w, h = int(x1 - x0), int(y1 - y0)
    base = min(s.width / w, s.height / h); z = lerp(z0, z1, cl(p))
    cw, ch = w * base / z, h * base / z
    cx = lerp(cw / 2, s.width - cw / 2, fx); cy = lerp(ch / 2, s.height - ch / 2, fy)
    im = s.crop((int(cx - cw / 2), int(cy - ch / 2), int(cx + cw / 2), int(cy + ch / 2))).resize((w, h), Image.BILINEAR).convert("RGBA")
    k = (w, h, r)
    if k not in _MASK:
        m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255); _MASK[k] = m
    m = _MASK[k]
    if a < .99: m = m.point(lambda v: int(v * a))
    im.putalpha(m)
    X, Y = int(cv.X(x0)), int(cv.Y(y0))
    # soft shadow
    sh = Image.new("RGBA", (w, h), SHAD + (0,)); sh.putalpha(_MASK[k].point(lambda v: int(v * .5 * a)))
    cv.im.alpha_composite(sh, dest=(max(0, X + 8), max(0, Y + 14))) if X + 8 >= 0 and Y + 14 >= 0 else None
    sx0, sy0 = max(0, -X), max(0, -Y); x0_, y0_ = max(0, X), max(0, Y)
    sx1, sy1 = min(w, W - X), min(h, H - Y)
    if sx1 > sx0 and sy1 > sy0: cv.im.alpha_composite(im.crop((sx0, sy0, sx1, sy1)), dest=(x0_, y0_))
    cv.rrect(x0, y0, x1, y1, r, outline=PAPER, w=4, oa=.9 * a / max(cv.ga, .01) if cv.ga > .01 else 0)
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
def brackets(cv, x0, y0, x1, y1, col, a=1, L=46, w=5, pad=18):
    for (x, y, dx, dy) in [(x0 + pad, y0 + pad, 1, 1), (x1 - pad, y0 + pad, -1, 1), (x0 + pad, y1 - pad, 1, -1), (x1 - pad, y1 - pad, -1, -1)]:
        cv.line([(x + dx * L, y), (x, y), (x, y + dy * L)], col, w, a)
def cross(cv, x, y, s, col, a=1, w=7):
    cv.line([(x - s, y - s), (x + s, y + s)], col, w, a); cv.line([(x - s, y + s), (x + s, y - s)], col, w, a)
DIM = mix(INK, PAPER, .35)
def stripes(cv, cx, cy, r, ang, period, a=1.0, ph=0.0):
    a = cl(a * cv.ga)
    if a <= .01: return
    cv.done()
    yy, xx = np.mgrid[-r:r, -r:r].astype(np.float32)
    u = xx * math.cos(ang) + yy * math.sin(ang)
    v = .5 + .5 * np.sin(2 * math.pi * u / period + ph)
    v = np.clip((v - .5) * 3.2 + .5, 0, 1)
    c1 = np.array(INK, np.float32); c2 = np.array(PAPER, np.float32)
    rgb = c1[None, None, :] * (1 - v[..., None]) + c2[None, None, :] * v[..., None]
    d = np.hypot(xx + .5, yy + .5)
    al = np.clip(r - d, 0, 1) * a * 255
    im = Image.fromarray(np.dstack([rgb, al]).astype(np.uint8), "RGBA")
    X, Y = int(cv.X(cx - r)), int(cv.Y(cy - r))
    sh = Image.new("RGBA", im.size, SHAD + (0,)); sh.putalpha(Image.fromarray((np.clip(r - d, 0, 1) * a * 110).astype(np.uint8)))
    if X + 8 >= 0 and Y + 14 >= 0: cv.im.alpha_composite(sh, dest=(X + 8, Y + 14))
    if X >= 0 and Y >= 0 and X + 2 * r <= W and Y + 2 * r <= H: cv.im.alpha_composite(im, dest=(X, Y))
    cv.circ(cx, cy, r, outline=PAPER, w=5, oa=a / max(cv.ga, .01) if cv.ga > .01 else 0)
DIM = mix(INK, PAPER, .35)
ASH = (190, 170, 150)
def credit(cv, txt, y, a=1):
    cv.text(540, y, txt, 24, ASH, a, "SemiBold")
def typew(txt, t, t0, cps=22):
    n = int(max(0, t - t0) * cps)
    return txt[:n]
