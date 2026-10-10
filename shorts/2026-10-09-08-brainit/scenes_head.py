# Brain-IT: warm stone paper, ink, forest, terracotta, amber
import random
BG0, BG1 = (226, 224, 208), (210, 207, 188)
INKC = (30, 32, 34); WHT = (250, 246, 234)
FOR, TERRA, AMB, SLATE = (44, 84, 72), (190, 88, 58), (226, 166, 56), (88, 92, 110)
PAPER, EDGE, SHAD = (250, 246, 234), (140, 130, 108), (188, 182, 160)
GOLD = TERRA; BL, BL2 = TERRA, TERRA
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def _grain(im, amt=10, seed=1):
    rs = np.random.RandomState(seed); a = np.asarray(im.convert("RGB")).astype(np.int16)
    n = rs.randint(-amt, amt + 1, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
def pic(variant=0, S=420):
    k = 3; im = Image.new("RGB", (S * k, S * k)); d = ImageDraw.Draw(im)
    top, bot = (244, 196, 120), (250, 232, 196)
    for y in range(S * k):
        u = y / (S * k * .7); u = min(1, u)
        d.line([(0, y), (S * k, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * u) for i in range(3)))
    sx, sy = (300, 120) if variant == 0 else (290, 135)
    d.ellipse([(sx - 52) * k, (sy - 52) * k, (sx + 52) * k, (sy + 52) * k], fill=(222, 108, 66))
    h1 = [(0, 270), (90, 220), (200, 250), (300, 215), (S, 255), (S, S), (0, S)]
    h2 = [(0, 330), (140, 290), (260, 320), (S, 285), (S, S), (0, S)]
    if variant: h1 = [(0, 275), (110, 232), (210, 246), (310, 224), (S, 262), (S, S), (0, S)]
    d.polygon([(x * k, y * k) for x, y in h1], fill=(96, 128, 98))
    d.polygon([(x * k, y * k) for x, y in h2], fill=(52, 90, 74))
    hx, hy = 110, 238
    hc = (176, 76, 52) if variant == 0 else (190, 96, 66)
    d.rectangle([hx * k, (hy + 20) * k, (hx + 78) * k, (hy + 78) * k], fill=(246, 236, 214))
    d.polygon([((hx - 12) * k, (hy + 22) * k), ((hx + 39) * k, hy * k - 28 * k), ((hx + 90) * k, (hy + 22) * k)], fill=hc)
    d.rectangle([(hx + 30) * k, (hy + 44) * k, (hx + 50) * k, (hy + 78) * k], fill=(70, 52, 44))
    tx = 330 if variant == 0 else 322
    d.rectangle([tx * k, 292 * k, (tx + 10) * k, 330 * k], fill=(80, 58, 46))
    d.ellipse([(tx - 26) * k, 244 * k, (tx + 36) * k, 304 * k], fill=(36, 74, 60))
    im = im.resize((S, S), Image.LANCZOS)
    return _grain(im, 8, 3 + variant)
def pix(src, level, S=420):
    n = int(6 + (S - 6) * level ** 2.2)
    return src.resize((max(2, n), max(2, n)), Image.BILINEAR).resize((S, S), Image.NEAREST)
def tub(animal, S=420):
    k = 3; im = Image.new("RGB", (S * k, S * k)); d = ImageDraw.Draw(im)
    for y in range(S * k):
        u = y / (S * k); d.line([(0, y), (S * k, y)], fill=(int(214 + 20 * u), int(222 + 8 * u), int(214 - 10 * u)))
    d.rectangle([0, 300 * k, S * k, S * k], fill=(168, 176, 158))
    c = (196, 150, 98) if animal == "dog" else (214, 200, 172)
    cx = 210
    d.rectangle([(cx - 14) * k, 170 * k, (cx + 14) * k, 260 * k], fill=c)  # neck/body
    d.ellipse([(cx - 70) * k, 100 * k, (cx + 70) * k, 220 * k], fill=c)       # head
    if animal == "dog":
        d.ellipse([(cx - 100) * k, 110 * k, (cx - 50) * k, 215 * k], fill=(118, 80, 52))
        d.ellipse([(cx + 50) * k, 110 * k, (cx + 100) * k, 215 * k], fill=(118, 80, 52))
        d.ellipse([(cx - 34) * k, 160 * k, (cx + 34) * k, 214 * k], fill=(228, 196, 150))
        d.ellipse([(cx - 12) * k, 166 * k, (cx + 12) * k, 182 * k], fill=(36, 30, 30))
    else:
        d.polygon([((cx - 40) * k, 108 * k), ((cx - 66) * k, 40 * k), ((cx - 22) * k, 100 * k)], fill=(70, 60, 52))
        d.polygon([((cx + 40) * k, 108 * k), ((cx + 66) * k, 40 * k), ((cx + 22) * k, 100 * k)], fill=(70, 60, 52))
        d.ellipse([(cx - 112) * k, 130 * k, (cx - 60) * k, 160 * k], fill=(190, 176, 150))
        d.ellipse([(cx + 60) * k, 130 * k, (cx + 112) * k, 160 * k], fill=(190, 176, 150))
        d.polygon([((cx - 14) * k, 205 * k), ((cx + 14) * k, 205 * k), (cx * k, 262 * k)], fill=(236, 230, 214))
        d.ellipse([(cx - 20) * k, 176 * k, (cx + 20) * k, 206 * k], fill=(232, 222, 202))
    for ex in (-30, 30):
        d.ellipse([(cx + ex - 9) * k, 136 * k, (cx + ex + 9) * k, 154 * k], fill=(246, 240, 224))
        if animal == "dog": d.ellipse([(cx + ex - 5) * k, 140 * k, (cx + ex + 5) * k, 152 * k], fill=(30, 26, 26))
        else: d.rectangle([(cx + ex - 8) * k, 143 * k, (cx + ex + 8) * k, 149 * k], fill=(30, 26, 26))
    d.rounded_rectangle([60 * k, 250 * k, 360 * k, 350 * k], 46 * k, fill=(244, 242, 232), outline=(120, 120, 120), width=3 * k)
    d.rectangle([70 * k, 262 * k, 350 * k, 276 * k], fill=(120, 168, 190))
    for fx in (96, 324): d.ellipse([(fx - 16) * k, 344 * k, (fx + 16) * k, 372 * k], fill=(190, 150, 70))
    return _grain(im.resize((S, S), Image.LANCZOS), 8, 9)
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (226, 224, 208), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["mri"] = L("mri.jpg"); IM["wz"] = L("wz.jpg")
    IM["p0"] = pic(0); IM["p1"] = pic(1); IM["dog"] = tub("dog"); IM["goat"] = tub("goat")
    rs = np.random.RandomState(5)
    nz = rs.randint(60, 220, (420, 420, 1)).repeat(3, 2) * np.array([1.0, .95, .85]) 
    IM["noise"] = Image.fromarray(np.clip(nz, 0, 255).astype(np.uint8))
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
def kenburns(cv, key, cx, cy, w, h, zoom, r, a=1, panx=0, pany=0):
    src = IM[key]; k = min(src.width / w, src.height / h) / zoom
    cw, ch = w * k, h * k
    x0 = (src.width - cw) / 2 + panx * (src.width - cw) / 2; y0 = (src.height - ch) / 2 + pany * (src.height - ch) / 2
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BILINEAR)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, outline=EDGE, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.55 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or TERRA, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or PAPER, a, "Black")
def arrow(cv, x, y, a=1, c=INKC):
    cv.line([(x - 26, y), (x + 26, y)], c, 9, a); cv.line([(x + 6, y - 20), (x + 28, y), (x + 6, y + 20)], c, 9, a)
def pcard(cv, key, cx, cy, S, a=1, src=None, border=EDGE):
    h = S / 2
    cv.rrect(cx - h + 8, cy - h + 12, cx + h + 8, cy + h + 12, 22, fill=SHAD, a=.55 * a)
    s = src if src is not None else IM[key]
    s = s.resize((int(S), int(S)), Image.BILINEAR)
    img(cv, None, cx, cy, 1, a, _rounded(s, 22))
    cv.rrect(cx - h, cy - h, cx + h, cy + h, 22, outline=border, w=4, oa=a)
