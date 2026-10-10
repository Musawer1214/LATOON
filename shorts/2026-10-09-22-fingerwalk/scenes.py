# Chirality Nobel: warm brown, cream cards, terracotta/sage/mustard
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (40, 42, 34), (28, 30, 25)
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
    z = radial(40, (36, 38, 32), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-8, 9, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    im = Image.open(os.path.join(IMGDIR, "hand.jpg")).convert("RGB")
    IM["full"] = _rounded(ImageOps.fit(im, (860, 700), Image.LANCZOS, centering=(.5, .5)), 30)
    IM["big"] = _rounded(ImageOps.fit(im.crop((520, 0, 1245, 934)), (640, 820), Image.LANCZOS), 30)
    IM["small"] = _rounded(ImageOps.fit(im.crop((60, 360, 620, 860)), (860, 700), Image.LANCZOS), 30)
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

def s0(cv, t, D):
    kinetic(cv, t, 300, "A HAND THAT", 110, INKC, -.2, "Black", .03)
    kinetic(cv, t, 430, "WALKS", 150, YEL, -.1, "Black", .03)
    p = eo(pr(t, .0, .6))
    img(cv, "full", 540, 1000, 1.0 + .03 * pr(t, 0, 3.5), p)
    chip(cv, 250, 1380, 580, "NO ARM ATTACHED", RED, eo(pr(t, 1.6, 2.2)), INKC, 38)
def s1(cv, t, D):
    head(cv, t, "THE BACKPACK", "80 grams, three parts", YEL)
    img(cv, "small", 540, 880, 1.0, eo(pr(t, .0, .5)))
    xs = [(100, 300), (410, 270), (700, 280)]
    # three compact chips side by side
    pos = [(70, 1270, 300, "BATTERY", YEL), (390, 1270, 300, "MOTION SENSOR", TEA), (710, 1270, 300, "PI ZERO", RED)]
    for i, (x, y, w, lab, c) in enumerate(pos):
        q = eo(pr(t, 1.2 + i * 1.3, 1.8 + i * 1.3))
        chip(cv, x, y + (1 - q) * 80, w, lab, c, q, INK if c != RED else INKC, 28, 80)
def s2(cv, t, D):
    head(cv, t, "BUILT TO GRASP", "not to walk", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    lens = [("thumb", 250, TEA), ("index", 420, YEL), ("middle", 480, RED), ("ring", 440, GRN), ("pinky", 330, PLM)]
    for i, (n, L, c) in enumerate(lens):
        q = eback(pr(t, .2 + i * .25, .8 + i * .25), 1.4)
        x = 215 + i * 150
        base = 1230
        cv.rrect(x - 48, base - L * q, x + 48, base, 44, fill=mix(c, (0, 0, 0), .3))
        cv.rrect(x - 42, base - L * q + 4, x + 38, base - 8, 40, fill=c)
        cv.rrect(x - 26, base - L * q + 16, x - 8, base - L * q + 70, 8, fill=mix(c, WHT, .4), a=.7)
        cv.text(x, base + 40, n, 26, INK, q, "Bold")
    chip(cv, 220, 640, 640, "UNEVEN FINGERS + A THUMB", RED, eo(pr(t, 1.8, 2.4)), INKC, 32)
def s3(cv, t, D):
    head(cv, t, "TRIAL AND ERROR", "in simulation first", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    rs = random.Random(8)
    n = 60
    pts = []
    for i in range(n + 1):
        x = 170 + i * (740 / n)
        y = 1260 - (1 - math.exp(-i / 22)) * 560 + math.sin(i * 1.7) * 28 + rs.uniform(-34, 34) * (1 - i / n * .7)
        pts.append((x, y))
    k = int(len(pts) * eo(pr(t, .2, 4.0)))
    cv.line([(170, 1290), (930, 1290)], mix(PAPER, INK, .5), 4)
    cv.line([(170, 640), (170, 1290)], mix(PAPER, INK, .5), 4)
    if k > 1: cv.line(pts[:k], TEA, 8)
    if k > 0: cv.circ(pts[k - 1][0], pts[k - 1][1], 16, fill=RED)
    cv.text(540, 620, "REWARD", 30, INK, 1, "Black")
    cv.text(540, 1335, "attempts  >", 30, INK, 1, "Bold")
    cv.text(780, 1180, "+ reward for moving well", 28, INK, eo(pr(t, 1.5, 2.2)), "Bold")
def s4(cv, t, D):
    head(cv, t, "VIRTUAL SPRINGS", "each finger has a home", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cv.rrect(250, 640, 830, 800, 30, fill=mix(INK, PAPER, .15))
    cv.text(540, 720, "PALM", 40, PAPER, 1, "Black")
    rs = random.Random(2)
    for i in range(5):
        hx = 230 + i * 155; hy = 1180
        pull = eo(pr(t, 1.5, 3.2))
        dx = math.sin(t * 5 + i * 2) * 70 * (1 - pull) + (i - 2) * 30 * (1 - pull)
        dy = math.cos(t * 4 + i) * 50 * (1 - pull)
        fx, fy = hx + dx, hy + dy
        sx = 540 + (i - 2) * 105
        n = 14
        zz = [(sx, 800)]
        for j in range(1, n):
            q = j / n
            zz.append((lerp(sx, fx, q) + (14 if j % 2 else -14), lerp(800, fy - 40, q)))
        zz.append((fx, fy - 40))
        cv.line(zz, mix(PAPER, INK, .45), 4)
        cv.circ(hx, hy, 14, fill=None, outline=GRN, w=4)
        cv.circ(fx, fy, 34, fill=mix(YEL, (0, 0, 0), .3)); cv.circ(fx - 2, fy - 3, 30, fill=YEL)
    chip(cv, 200, 1290, 680, "DRIFTING AWAY COSTS POINTS", RED, eo(pr(t, 2.4, 3.0)), INKC, 30, 66)
def s5(cv, t, D):
    head(cv, t, "REAL HARDWARE", "14 surfaces, one hand", YEL)
    img(cv, "small", 540, 880, .96, eo(pr(t, .0, .5)))
    names = ["GRASS", "GRAVEL", "METAL GRATE"]
    for i, (nm, c) in enumerate(zip(names, (GRN, MUTE, TEA))):
        q = eo(pr(t, .9 + i * .9, 1.4 + i * .9))
        chip(cv, 70 + i * 320, 1270 + (1 - q) * 80, 300, nm, c, q, INK, 28, 80)
    cv.text(540, 1440, "14 surfaces tested", 36, YEL, eo(pr(t, 3.6, 4.2)), "Black")
def s6(cv, t, D):
    kinetic(cv, t, 470, "RIGHTED ITSELF", 100, INKC, 0, "Black", .03)
    card(cv, 100, 620, 980, 1380, 34)
    for i in range(25):
        r_, c_ = divmod(i, 5)
        x, y = 240 + c_ * 150, 740 + r_ * 120
        q = eback(pr(t, .3 + i * .05, .7 + i * .05), 1.6)
        ok = i < 21
        col = GRN if ok else RED
        cv.circ(x, y, 42 * q, fill=mix(col, (0, 0, 0), .3)); cv.circ(x - 1, y - 2, 38 * q, fill=col)
    n = int(21 * eo(pr(t, .3, 1.8)))
    cv.text(540, 1330, f"{n} / 25 tries", 56, INK, 1, "Black")
def s7(cv, t, D):
    head(cv, t, "NOT STUCK IN ONE JOB", "", YEL)
    img(cv, "big", 540, 960, .9, eo(pr(t, .0, .5)))
    chip(cv, 140, 1360, 800, "DETACH AND EXPLORE TIGHT SPACES", YEL, eo(pr(t, 1.8, 2.4)), INK, 30, 70)
def s8(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, YEL, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
