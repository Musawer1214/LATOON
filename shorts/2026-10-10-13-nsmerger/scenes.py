# nsmerger: umber + cream, gold / copper / clay
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (58, 38, 28), (20, 12, 10)
INKC = (248, 238, 218); WHT = (248, 238, 218)
PAPER, PAPER2, INK = (246, 234, 212), (230, 212, 182), (32, 20, 16)
MUST, CORAL, TEAL = (238, 174, 62), (204, 92, 52), (150, 166, 128)
YEL = MUST; COP = CORAL; RED = CORAL; SAGE = TEAL
MUTE, SHAD, LINEC = (176, 156, 140), (10, 4, 2), (120, 88, 70)
GOLD = MUST; BL, BL2 = CORAL, CORAL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
_MASK = {}
def warm(im):
    r, g, b = im.split()
    g2 = g.point(lambda v: int(v * .78))
    r2 = b.point(lambda v: min(255, int(v * 1.02)))
    b2 = r.point(lambda v: int(v * .8))
    return Image.merge("RGB", (r2, g2, b2))
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (20, 12, 10), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(7)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k in ["gold", "merge", "vlt", "ep", "magnetar", "stront"]:
        im = Image.open(os.path.join(IMGDIR, k + "_s.jpg")).convert("RGB")
        if k in ("merge", "magnetar", "stront"): im = warm(im)
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

DIM = mix(INK, PAPER, .35)
ASH = (200, 180, 170)
def credit(cv, txt, y, a=1, x=540, anc="mm"):
    cv.text(x, y, txt, 23, ASH, a, "SemiBold", anc)
def bubble(cv, x0, y0, x1, y1, lines, fill, tc, a=1, size=32, r=30, w="Bold"):
    cv.rrect(x0 + 5, y0 + 9, x1 + 5, y1 + 9, r, fill=SHAD, a=.45 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a)
    n = len(lines); cy = (y0 + y1) / 2
    for k, ln in enumerate(lines):
        cv.text((x0 + x1) / 2, cy + (k - (n - 1) / 2) * size * 1.25, ln, size, tc, a, w)
def frac(cv, x, y, n, d, size, col, a=1):
    cv.text(x, y - size * .58, n, size, col, a, "Black")
    cw = max(cv.tw(n, size, "Black"), cv.tw(d, size, "Black")) + 12
    cv.line([(x - cw / 2, y), (x + cw / 2, y)], col, max(4, size // 12), a)
    cv.text(x, y + size * .62, d, size, col, a, "Black")
def stopwatch(cv, cx, cy, r, prog, a=1):
    cv.circ(cx + 8, cy + 14, r, fill=SHAD, a=.5 * a)
    cv.rrect(cx - 20, cy - r - 30, cx + 20, cy - r + 8, 8, fill=MUST, a=a)
    cv.circ(cx, cy, r, fill=mix(MUST, INK, .25), a=a)
    cv.circ(cx, cy, r - 14, fill=PAPER, a=a)
    for k in range(60):
        ang = math.radians(k * 6 - 90); big = k % 5 == 0
        r0 = r - 22; r1 = r - (50 if big else 36)
        cv.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)), (cx + r1 * math.cos(ang), cy + r1 * math.sin(ang))], INK, 5 if big else 2, a * .85)
    if prog > .005: cv.arc(cx, cy, r - 60, 0, 360 * prog, CORAL, 12, a * .9)
    ang = math.radians(360 * prog - 90)
    cv.line([(cx, cy), (cx + (r - 40) * math.cos(ang), cy + (r - 40) * math.sin(ang))], INK, 7, a)
    cv.circ(cx, cy, 11, fill=INK, a=a)
    m = prog * 10
    cv.text(cx, cy + r * .45, "%d:%02d" % (int(m), int((m - int(m)) * 60)), int(r * .30), INK, a, "Black")
def arrow(cv, x0, y0, x1, y1, col, w=8, a=1, head=26):
    cv.line([(x0, y0), (x1, y1)], col, w, a)
    ang = math.atan2(y1 - y0, x1 - x0)
    p = [(x1, y1), (x1 - head * math.cos(ang - .45), y1 - head * math.sin(ang - .45)), (x1 - head * math.cos(ang + .45), y1 - head * math.sin(ang + .45))]
    cv.poly(p, col, a)
def sphere(cv, cx, cy, r, col, a=1):
    cv.circ(cx + 6, cy + 10, r, fill=SHAD, a=.4 * a)
    cv.circ(cx, cy, r, fill=mix(col, INK, .55), a=a)
    cv.circ(cx - r * .1, cy - r * .12, r * .88, fill=mix(col, INK, .2), a=a)
    cv.circ(cx - r * .2, cy - r * .25, r * .6, fill=col, a=a)
    cv.circ(cx - r * .32, cy - r * .38, r * .28, fill=mix(col, PAPER, .55), a=a)
def fieldlines(cv, cx, cy, r, a=1, col=None):
    col = col or MUST
    for k in range(1, 4):
        L = r * (1.5 + k * 0.95)
        for sx in (1, -1):
            pts = []
            for i in range(0, 41):
                th = math.pi * (.06 + .88 * i / 40)
                rr = L * math.sin(th) ** 2
                pts.append((cx + sx * rr * math.sin(th), cy - rr * math.cos(th) * 1.0))
            cv.line(pts, col, 4, a * (.85 - k * .12))
def tl_axis(cv, x0, x1, y, a=1):
    cv.line([(x0, y), (x1, y)], mix(PAPER, INK, .35), 4, a)
    cv.poly([(x1 + 14, y), (x1 - 8, y - 11), (x1 - 8, y + 11)], mix(PAPER, INK, .35), a)

def s0(cv, t, D):
    kinetic(cv, t, 300, "FORGED IN A CRASH", 84, INKC, -.2, "Black", .02)
    cv.text(540, 396, "NEUTRON STAR MERGER", 40, MUST, eo(pr(t, .3, .7)), "Bold")
    c = eio(pr(t, 2.3, 3.3))
    photo(cv, "gold", 70, 470, 1010, 1130, t / D, 1.0, 1.12, .5, .5, a=1 - c)
    photo(cv, "merge", 70, 470, 1010, 1130, t / D, 1.0, 1.18, .5, .5, a=c)
    brackets(cv, 70, 470, 1010, 1130, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Gold nugget: James St. John, CC BY 2.0", 1165, (1 - c) * eo(pr(t, .6, 1.0)))
    credit(cv, "Artist's impression: ESO / Univ. of Warwick / M. Garlick, CC BY 4.0 (colour-graded)", 1165, c)
    chip(cv, 140, 1230, 800, "TWO DEAD STARS COLLIDE", MUST, eo(pr(t, 2.9, 3.4)), INK, 46, 96)

def s1(cv, t, D):
    kinetic(cv, t, 300, "JULY 4, 2025", 104, INKC, -.2, "Black", .03)
    photo(cv, "ep", 70, 440, 1010, 940, t / D, 1.0, 1.15, .55, .5)
    brackets(cv, 70, 440, 1010, 940, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Einstein Probe illustration: China News Service, CC BY 4.0", 972, eo(pr(t, .8, 1.3)))
    card(cv, 70, 1030, 1010, 1400, 30, mix(BG1, PAPER, .1), eo(pr(t, .6, 1.0)))
    y0 = 1290; tl_axis(cv, 130, 940, y0, eo(pr(t, .9, 1.4)))
    cv.text(880, y0 + 44, "time", 28, MUTE, eo(pr(t, .9, 1.4)), "SemiBold")
    g = pr(t, 2.3, 3.0)
    if g > 0:
        pts = [(160, y0), (170, y0 - 230 * eo(min(1, g * 2))), (184, y0 - 40 * g), (200, y0)] if g > 0 else []
        pts = [(160, y0), (172, y0 - 230 * eo(g)), (200, y0)]
        cv.line(pts, MUST, 9, eo(g))
        cv.text(300, y0 - 190, "GAMMA RAYS", 38, MUST, eo(pr(t, 2.8, 3.3)), "Black", "lm")
        cv.text(300, y0 - 140, "about half a second", 32, PAPER, eo(pr(t, 3.1, 3.6)), "SemiBold", "lm")

def s2(cv, t, D):
    kinetic(cv, t, 300, "IT WOULDN'T FADE", 92, INKC, -.2, "Black", .02)
    cv.text(540, 396, "X-rays kept pouring out", 40, MUST, eo(pr(t, .3, .7)), "Bold")
    card(cv, 70, 450, 1010, 800, 30, PAPER, eo(pr(t, .2, .6)))
    k = eio(pr(t, 1.0, 4.7))
    cv.text(540, 610, "%d" % round(560 * k), 190, INK, 1, "Black")
    cv.text(540, 740, "seconds of X-rays", 40, CORAL, 1, "Black")
    cv.text(110, 910, "gamma rays", 34, PAPER, eo(pr(t, .6, 1.0)), "Bold", "lm")
    cv.rrect(350, 896, 354, 924, 2, fill=MUST, a=eo(pr(t, .8, 1.2)))
    cv.text(380, 910, "0.4 s", 32, MUST, eo(pr(t, 1.0, 1.4)), "Black", "lm")
    cv.text(110, 1050, "X-rays", 34, PAPER, eo(pr(t, .6, 1.0)), "Bold", "lm")
    cv.rrect(350, 1022, 350 + 640 * (560 * k) / 560, 1078, 14, fill=CORAL, a=1)
    cv.rrect(350, 1022, 350 + 640 * k, 1040, 8, fill=mix(CORAL, PAPER, .35), a=.7)
    chip(cv, 100, 1190, 880, "LONGEST EVER SEEN FROM A MERGER", MUST, eo(pr(t, 4.4, 4.9)), INK, 38, 96)
    cv.text(540, 1330, "Einstein Probe, Chinese-European X-ray mission", 30, MUTE, eo(pr(t, 4.8, 5.3)), "SemiBold")

def s3(cv, t, D):
    kinetic(cv, t, 300, "6 BILLION YEARS", 96, INKC, -.2, "Black", .02)
    cv.text(540, 396, "Very Large Telescope, Chile", 40, MUST, eo(pr(t, .3, .7)), "Bold")
    photo(cv, "vlt", 70, 450, 1010, 960, t / D, 1.0, 1.16, .55, .45)
    brackets(cv, 70, 450, 1010, 960, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "ESO's VLT at Paranal: ESO / Y. Beletsky, CC BY 4.0", 992, eo(pr(t, .8, 1.3)))
    k = eio(pr(t, 1.3, 4.6))
    cv.text(540, 1110, "light travelled %.1f billion years" % (6.0 * k), 40, PAPER, 1, "Black")
    cv.rrect(110, 1170, 970, 1196, 13, fill=mix(BG1, PAPER, .25))
    cv.rrect(110, 1170, 110 + 860 * k, 1196, 13, fill=MUST)
    cv.circ(110 + 860 * k, 1183, 20, fill=PAPER)
    s = eo(pr(t, 4.7, 5.2))
    chip(cv, 170, 1260, 740, "SUPERNOVA: RULED OUT", CORAL, s, INK, 42, 100)
    cross(cv, 215, 1310, 20, INK, s, 8)

def s4(cv, t, D):
    kinetic(cv, t, 300, "TWO NEUTRON STARS", 88, INKC, -.2, "Black", .02)
    c = eio(pr(t, 5.3, 6.4))
    photo(cv, "merge", 70, 440, 1010, 950, t / D, 1.0, 1.15, .5, .5, a=1 - c)
    photo(cv, "magnetar", 70, 440, 1010, 950, t / D, 1.0, 1.15, .5, .5, a=c)
    brackets(cv, 70, 440, 1010, 950, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "ESO / Univ. of Warwick / M. Garlick, CC BY 4.0 (colour-graded)", 978, 1 - c)
    credit(cv, "Magnetar, artist's impression: ESA, CC BY 4.0 (colour-graded)", 978, c)
    card(cv, 70, 1010, 1010, 1440, 30, mix(BG1, PAPER, .1), eo(pr(t, .6, 1.0)))
    cx, cy = 540, 1210
    q = eio(pr(t, 1.4, 5.0))
    R = 300 * (1 - q) + 0
    ang = (t * 1.2 + 2.4 * q * q * 4) * 1.0
    if q < .985:
        for j in range(26):
            tt = t - j * .035
            qq = eio(pr(tt, 1.4, 5.0)); RR = 300 * (1 - qq)
            aa = (tt * 1.2 + 2.4 * qq * qq * 4)
            for sgn in (1, -1):
                cv.circ(cx + sgn * RR * math.cos(aa), cy + sgn * RR * .5 * math.sin(aa), 7, fill=MUST, a=.35 * (1 - j / 26))
        for sgn in (1, -1):
            sphere(cv, cx + sgn * R * math.cos(ang), cy + sgn * R * .5 * math.sin(ang), 54, mix(MUST, PAPER, .15), eo(pr(t, .7, 1.1)))
        cv.text(540, 1400, "each one as wide as a city", 34, MUST, eo(pr(t, 1.8, 2.3)) * (1 - eo(pr(t, 4.3, 4.8))), "Black")
    else:
        m = eo(pr(t, 5.0, 5.6))
        fieldlines(cv, cx, cy, 64, eo(pr(t, 5.6, 6.4)))
        sphere(cv, cx, cy, 64, MUST, m)
    chip(cv, 240, 1362, 600, "MAGNETAR", CORAL, eo(pr(t, 6.5, 7.0)), INK, 44, 72)

def s5(cv, t, D):
    kinetic(cv, t, 300, "FEEDING THE BLAST", 88, INKC, -.2, "Black", .02)
    photo(cv, "magnetar", 70, 430, 1010, 870, t / D, 1.0, 1.2, .5, .5)
    brackets(cv, 70, 430, 1010, 870, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Magnetar, artist's impression: ESA, CC BY 4.0 (colour-graded)", 900, eo(pr(t, .8, 1.3)))
    a = eo(pr(t, 1.0, 1.5))
    card(cv, 70, 950, 1010, 1260, 30, PAPER, a)
    for i, ln in enumerate(["\u201cThey can make any explosion", "brighter and longer-lasting.\u201d"]):
        cv.text(540, 1030 + i * 60, ln, 42, INK, a, "Black")
    cv.text(540, 1160, "Eleonora Troja, University of Rome Tor Vergata", 28, CORAL, a, "Black")
    cv.text(540, 1205, "on the magnetar idea", 26, mix(INK, PAPER, .35), a, "SemiBold")
    chip(cv, 110, 1310, 860, "STILL A HYPOTHESIS: ONE EVENT", MUST, eo(pr(t, 3.3, 3.8)), INK, 38, 96)

def s6(cv, t, D):
    kinetic(cv, t, 300, "WHERE GOLD COMES FROM", 74, INKC, -.2, "Black", .015)
    photo(cv, "stront", 70, 430, 1010, 870, t / D, 1.0, 1.15, .5, .5)
    brackets(cv, 70, 430, 1010, 870, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Merger artist's impression: ESO / L. Calçada / M. Kornmesser, CC BY 4.0 (colour-graded)", 898, eo(pr(t, .6, 1.1)), anc="mm")
    g = eo(pr(t, 1.3, 1.9))
    arrow(cv, 540, 922, 540, 962, MUST, 8, g, 20)
    photo(cv, "gold", 200, 978, 880, 1330, t / D, 1.0, 1.12, .5, .5, a=g)
    credit(cv, "Gold: James St. John, CC BY 2.0", 1352, g)
    chip(cv, 200, 1372, 680, "THOUGHT TO FORGE GOLD", MUST, eo(pr(t, 2.2, 2.7)), INK, 38, 72)

def s7(cv, t, D):
    kinetic(cv, t, 560, "LATOON", 150, INKC, -.1, "Black", .05)
    cv.text(540, 690, "Voyaging the unseen", 52, MUST, eo(pr(t, .9, 1.5)), "SemiBold")
    a = eo(pr(t, .5, 1.3)); cx, cy, r = 540, 960, 130
    cv.circ(cx + 8, cy + 14, r + 22, fill=SHAD, a=.4 * a)
    cv.circ(cx, cy, r + 22, fill=mix(MUST, INK, .45), a=a)
    cv.circ(cx, cy, r - 22, fill=mix(BG1, INK, .2), a=a)
    cv.arc(cx, cy, r, 200, 340, mix(MUST, PAPER, .6), 10, a)
    cv.arc(cx, cy, r, 20, 160, mix(MUST, INK, .25), 14, a)
    cv.circ(cx, cy, r + 22, outline=MUST, w=5, oa=a)
    cv.circ(cx, cy, r - 22, outline=mix(MUST, INK, .4), w=4, oa=a)
    chip(cv, 280, 1190, 520, "FOLLOW", MUST, eo(pr(t, 1.6, 2.2)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
