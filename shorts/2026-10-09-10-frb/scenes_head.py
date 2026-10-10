# FRB: warm night ink, cream, copper, amber, sage
import random
BG0, BG1 = (26, 22, 21), (40, 33, 29)
INKC = (244, 236, 218); WHT = (244, 236, 218)
COP, AMB, SAGE, ROSE = (214, 112, 62), (236, 178, 70), (124, 168, 146), (190, 96, 90)
CARDC, LINEC, MUTE, SHAD = (48, 41, 37), (96, 84, 74), (160, 148, 132), (14, 11, 10)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (26, 22, 21), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(11)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["jwst"] = L("jwst.png"); IM["spec"] = L("spec.jpg"); IM["mk"] = L("meerkat.jpg")
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
def card(cv, x0, y0, x1, y1, r=26, fill=CARDC, outline=LINEC, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.5 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or AMB, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or (30, 24, 22), a, "Black")
def zbox(cv, key, cx, cy, w, h, b0, b1, p, r, a=1):
    src = IM[key]; q = eio(p)
    bx = [lerp(b0[i], b1[i], q) for i in range(4)]
    crop = src.crop(tuple(int(v) for v in bx)).resize((int(w), int(h)), Image.LANCZOS)
    from PIL import ImageEnhance
    if q > .02: crop = ImageEnhance.Brightness(crop).enhance(1 + 1.0 * q)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
def stars(cv, n, x0, y0, x1, y1, t, seed=3, a=1):
    rs = random.Random(seed)
    for i in range(n):
        x = rs.uniform(x0, x1); y = rs.uniform(y0, y1); r = rs.choice([1.5, 1.5, 2, 2.5]); ph = rs.uniform(0, 6.28)
        cv.circ(x, y, r, fill=(240, 226, 196), a=a * (.45 + .4 * math.sin(t * 1.7 + ph)))
def galaxy(cv, cx, cy, s, rot, a=1, col=AMB):
    for k in range(5):
        r = s * (1 - k * .16)
        for arm in range(2):
            pts = []
            for j in range(26):
                u = j / 25; ang = rot + arm * math.pi + u * 3.6; rr = r * (.1 + .9 * u)
                pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang) * .62))
            cv.line(pts, mix(col, (250, 230, 190), k / 5), max(2, s * .09 * (1 - k * .15)), a * (.35 + .12 * k))
    cv.circ(cx, cy, s * .17, fill=(252, 232, 190), a=a)
def earth(cv, cx, cy, r, a=1):
    cv.circ(cx + 5, cy + 7, r, fill=SHAD, a=.5 * a)
    cv.circ(cx, cy, r, fill=(70, 112, 118), a=a)
    for (dx, dy, rr, c) in [(-.35, -.2, .38, (122, 150, 100)), (.3, .25, .3, (140, 160, 108)), (.1, -.5, .2, (200, 190, 150)), (-.1, .45, .22, (196, 188, 150))]:
        cv.circ(cx + dx * r, cy + dy * r, rr * r, fill=c, a=a)
    cv.circ(cx - r * .3, cy - r * .3, r * .55, fill=(255, 245, 220), a=.12 * a)
    cv.circ(cx, cy, r, outline=(236, 224, 196), w=3, oa=.6 * a)
def dish(cv, cx, cy, s, a=1):
    cv.line([(cx, cy), (cx, cy + s * .9)], MUTE, max(3, s * .08), a)
    cv.line([(cx - s * .4, cy + s * .9), (cx + s * .4, cy + s * .9)], MUTE, max(3, s * .08), a)
    pts = [(cx + s * .75 * math.cos(math.radians(a_)), cy - s * .1 + s * .75 * math.sin(math.radians(a_))) for a_ in range(20, 161, 10)]
    cv.line(pts, INKC, max(4, s * .1), a)
    cv.line([(cx, cy - s * .1), (cx - s * .3, cy - s * .75)], MUTE, 3, a)
