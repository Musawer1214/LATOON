# freewill: deep wine/oxblood + cream paper, brass / terracotta / slate
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (64, 30, 38), (26, 12, 18)
INKC = (246, 238, 222); WHT = (246, 238, 222)
PAPER, PAPER2, INK = (246, 234, 214), (228, 212, 186), (42, 24, 28)
MUST, CORAL, TEAL = (228, 174, 86), (214, 96, 80), (116, 150, 170)
YEL = MUST; COP = MUST; RED = CORAL; SAGE = TEAL
MUTE, SHAD, LINEC = (176, 156, 146), (12, 4, 6), (110, 84, 90)
GOLD = MUST; BL, BL2 = CORAL, CORAL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
_MASK = {}
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (26, 12, 18), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(7)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k in ["kandel", "navarra", "reil"]:
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
def domino(cv, x, y, ang, col, a=1, w=44, h=150):
    # pivot at bottom-right corner of tile; ang in degrees (0 upright, 90 flat)
    th = math.radians(ang)
    pts0 = [(-w, -h), (0, -h), (0, 0), (-w, 0)]
    pts = []
    for (px, py) in pts0:
        pts.append((x + px * math.cos(th) - py * math.sin(th), y + px * math.sin(th) + py * math.cos(th)))
    sh = [(px + 7, py + 8) for (px, py) in pts]
    cv.poly(sh, SHAD, .4 * a); cv.poly(pts, col, a)
    # pips
    for k in range(3):
        qx, qy = -w / 2, -h * (.22 + k * .28)
        cv.circ(x + qx * math.cos(th) - qy * math.sin(th), y + qx * math.sin(th) + qy * math.cos(th), 6, fill=INK, a=a * .85)
def s0(cv, t, D):
    kinetic(cv, t, 300, "FREE WILL?", 128, INKC, -.2, "Black", .03)
    kinetic(cv, t, 425, "ask a neuroscientist", 48, MUST, .3, "Bold", .02)
    photo(cv, "reil", 90, 490, 990, 1050, t / D, 1.0, 1.25, .5, .25)
    brackets(cv, 90, 490, 990, 1050, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Brain dissection, J. C. Reil, 1812 (public domain)", 1078, eo(pr(t, .8, 1.3)))
    q = eback(pr(t, 1.8, 2.3), 2)
    chip(cv, 70, 1160, 940, "THE MIND IS JUST THE BRAIN", CORAL, cl(q * 1.4), INKC, 52, 104)
    q2 = eback(pr(t, 3.3, 3.8), 2)
    chip(cv, 130, 1300, 820, "...AND YET: FREE WILL", MUST, cl(q2 * 1.4), INK, 48, 100)
def s1(cv, t, D):
    kinetic(cv, t, 300, "THE SURVEY", 96, INKC, -.2, "Black", .03)
    A = 1 - eo(pr(t, 3.2, 3.6))
    if A > .01:
        photo(cv, "navarra", 90, 450, 990, 830, t / D, 1.0, 1.15, .5, .6, a=A)
        brackets(cv, 90, 450, 990, 830, PAPER, eo(pr(t, .2, .7)) * .9 * A)
        credit(cv, "University of Navarra campus: Anass Sedrati, CC BY-SA 4.0", 858, eo(pr(t, .6, 1.1)) * A)
        n = int(2657 * eo(pr(t, .4, 1.9)))
        cv.text(540, 990, "{:,}".format(n), 170, INKC, eo(pr(t, .3, .7)) * A, "Black")
        cv.text(540, 1112, "NEUROSCIENTISTS ANSWERED", 40, MUST, eo(pr(t, 1.0, 1.5)) * A, "Black")
        cv.text(540, 1175, "PNAS  \u00b7  survey of 280,225 invited researchers", 28, ASH, eo(pr(t, 1.4, 1.9)) * A, "SemiBold")
    B = eo(pr(t, 3.4, 3.9))
    if B > .01:
        cx, cy, r = 330, 760, 160
        cv.circ(cx + 8, cy + 14, r + 22, fill=SHAD, a=.5 * B)
        cv.circ(cx, cy, r + 22, fill=PAPER, a=B)
        cv.circ(cx, cy, r - 24, fill=mix(BG1, PAPER, .12), a=B)
        cv.arc(cx, cy, r - 2, 0, 360, mix(INK, PAPER, .15), 40, B * .9)
        pg = eio(pr(t, 3.6, 5.6))
        cv.arc(cx, cy, r - 2, 0, 360 * .6362 * pg, CORAL, 40, B)
        cv.text(cx, cy - 6, "%d%%" % round(63.62 * pg), 92, INKC, B, "Black")
        cv.text(cx, cy + 62, "agree", 30, MUST, B, "Bold")
        cv.text(cx, cy + 215, "THE MIND IS REDUCIBLE", 28, INKC, B, "Black")
        cv.text(cx, cy + 250, "TO THE BRAIN", 28, INKC, B, "Black")
        ca = eo(pr(t, 5.4, 6.0))
        photo(cv, "kandel", 600, 520, 990, 960, t / D, 1.0, 1.12, .5, .22, a=ca * B)
        brackets(cv, 600, 520, 990, 960, PAPER, ca * .9)
        credit(cv, "Eric Kandel: Boberger, CC BY-SA 4.0", 988, ca * .9, 795)
        card(cv, 70, 1090, 1010, 1380, 30, PAPER, ca)
        cv.text(540, 1150, "\u201cWhat we commonly call the mind is a set", 32, INK, ca, "Bold")
        cv.text(540, 1196, "of operations carried out by the brain.\u201d", 32, INK, ca, "Bold")
        cv.text(540, 1262, "Kandel, Principles of Neural Science", 28, CORAL, ca, "Black")
        cv.text(540, 1312, "the textbook the survey opens with", 24, mix(INK, PAPER, .35), ca, "SemiBold")
def s2(cv, t, D):
    kinetic(cv, t, 300, "YET ONLY", 100, INKC, -.2, "Black", .03)
    n = 17.5 * eo(pr(t, .4, 1.7))
    cv.text(540, 560, "%.1f%%" % n, 220, MUST, eo(pr(t, .3, .7)), "Black")
    # 40 person icons, 7 highlighted (17.5% of 40)
    for i in range(40):
        col = CORAL if i < 7 else PAPER
        a = eo(pr(t, 1.0 + i * .02, 1.4 + i * .02))
        icon_person(cv, 140 + (i % 10) * 86, 800 + (i // 10) * 118, 78, col if i < 7 else mix(PAPER, BG1, .25), a)
    chip(cv, 70, 1290, 940, "SAID: NO FREEDOM IN OUR ACTIONS", CORAL, eo(pr(t, 2.2, 2.7)), INKC, 42, 90)
    cv.text(540, 1415, "the survey's wording: the nervous system determines behavior", 24, ASH, eo(pr(t, 2.6, 3.1)), "SemiBold")
def s3(cv, t, D):
    kinetic(cv, t, 300, "TWO LEVELS", 104, INKC, -.2, "Black", .03)
    a1 = eo(pr(t, .6, 1.0)); a2 = eo(pr(t, 3.5, 3.9))
    card(cv, 60, 440, 1020, 880, 30, PAPER, a1)
    cv.text(110, 488, "ZOOM IN: NEURONS", 30, INK, a1, "Black", "lm")
    # falling dominoes
    for i in range(9):
        ang = 90 * eio(pr(t, 1.3 + i * .22, 1.9 + i * .22))
        domino(cv, 150 + i * 82, 780, min(ang, 78), mix(CORAL, INK, .1) if i else MUST, a1, 36, 150)
    cv.line([(110, 786), (950, 786)], mix(INK, PAPER, .3), 4, a1)
    cv.text(540, 840, "every step has a cause", 28, mix(INK, PAPER, .3), eo(pr(t, 2.2, 2.7)), "Bold")
    card(cv, 60, 910, 1020, 1390, 30, PAPER, a2)
    cv.text(110, 958, "ZOOM OUT: A PERSON", 30, INK, a2, "Black", "lm")
    icon_person(cv, 250, 1180, 170, mix(INK, TEAL, .35), a2)
    ch = eio(pr(t, 4.4, 6.2))
    for k, (ey, lab, col) in enumerate([(1060, "stay in", mix(PAPER2, INK, .1)), (1300, "go out", MUST)]):
        pts = [(330, 1180), (500, 1180 + (ey - 1180) * .5), (640, ey)]
        qq = eo(pr(t, 4.0 + k * .3, 4.7 + k * .3))
        cv.line([(330, 1180), (lerp(330, 640, qq), lerp(1180, ey, qq))], mix(INK, PAPER, .25), 6, a2)
        chosen = (k == 1)
        cv.rrect(640, ey - 42, 980, ey + 42, 42, fill=col if (not chosen or ch > .3) else PAPER2, a=a2 * (1 if chosen else .75) * qq)
        cv.text(810, ey, lab.upper(), 32, INK, a2 * qq, "Black")
    if ch > .3:
        check(cv, 940, 1300, 16, eo(pr(t, 5.0, 5.5)), INK, 7, a2)
    cv.text(540, 1360, "someone weighs options", 26, mix(INK, PAPER, .3), eo(pr(t, 5.3, 5.8)), "Bold")
def s4(cv, t, D):
    kinetic(cv, t, 640, "COMPATIBILISM", 108, INKC, -.1, "Black", .03)
    cv.text(540, 780, "philosophy's name for the pairing", 40, MUST, eo(pr(t, .6, 1.1)), "Bold")
    pa = eo(pr(t, .9, 1.4))
    chip(cv, 90, 900, 420, "DETERMINISM", TEAL, pa, INK, 38, 90)
    chip(cv, 570, 900, 420, "FREE WILL", CORAL, pa, INKC, 38, 90)
    cv.text(540, 945, "+", 70, INKC, pa, "Black")
    cv.line([(300, 1010), (300, 1090), (540, 1090), (540, 1130)], PAPER, 5, pa * .8)
    cv.line([(780, 1010), (780, 1090), (540, 1090)], PAPER, 5, pa * .8)
    cv.text(540, 1180, "can both be true", 48, INKC, eo(pr(t, 1.2, 1.7)), "Black")
def s5(cv, t, D):
    kinetic(cv, t, 300, "1 IN 72", 128, INKC, -.2, "Black", .03)
    cv.text(540, 410, "invited researchers replied", 44, MUST, eo(pr(t, .3, .8)), "Bold")
    for i in range(72):
        r, c = divmod(i, 12)
        a = eo(pr(t, .4 + i * .012, .8 + i * .012))
        me = (i == 40)
        x = 120 + c * 76; y = 560 + r * 100
        icon_person(cv, x, y, 70, MUST if me else mix(PAPER, BG1, .35), a)
    ring = eo(pr(t, 1.9, 2.6))
    cv.circ(120 + 4 * 76, 560 + 3 * 100, 58, outline=MUST, w=5, oa=ring)
    chip(cv, 110, 1230, 860, "A SNAPSHOT, NOT A VERDICT", PAPER, eo(pr(t, 2.9, 3.4)), INK, 46, 96)
    cv.text(540, 1370, "mostly Western, male and over 40, as the authors note", 25, ASH, eo(pr(t, 3.6, 4.1)), "SemiBold")
def s6(cv, t, D):
    kinetic(cv, t, 300, "NOT THE MAJORITY", 88, INKC, -.2, "Black", .02)
    cv.text(540, 410, "\u201cthe nervous system determines behavior\u201d", 34, MUST, eo(pr(t, .3, .8)), "Bold")
    x0, x1, y0, y1 = 80, 1000, 600, 760
    parts = [(17.52, CORAL, "AGREE", INKC), (23.22, mix(PAPER2, BG1, .3), "NEUTRAL", INK), (59.26, TEAL, "DISAGREE", INK)]
    pg = eio(pr(t, .6, 2.2))
    cx = x0
    cv.rrect(x0 + 6, y0 + 12, x1 + 6, y1 + 12, 30, fill=SHAD, a=.45)
    for v, col, lab, tc in parts:
        w = (x1 - x0) * v / 100 * pg
        if w > 2:
            cv.rrect(cx, y0, cx + w, y1, 4, fill=col)
            if w > 130: cv.text(cx + w / 2, (y0 + y1) / 2 - 18, "%.1f%%" % v if v < 20 else "%d%%" % round(v), 44 if v > 20 else 36, tc, 1, "Black")
            if w > 130: cv.text(cx + w / 2, (y0 + y1) / 2 + 28, lab, 24, tc, 1, "Black")
        cx += w
    cv.rrect(x0, y0, x1, y1, 30, outline=PAPER, w=5, oa=.9)
    ca = eback(pr(t, 2.6, 3.1), 2)
    chip(cv, 60, 930, 960, "FREE WILL: NOT KILLED", MUST, cl(ca * 1.4), INK, 54, 110)
    cv.text(540, 1110, "by neuroscience, in this survey", 40, INKC, eo(pr(t, 3.2, 3.7)), "Bold")
    cv.text(540, 1250, "PNAS 123(29), Navarro-Pe\u00f1a et al., 2026", 26, ASH, eo(pr(t, 3.6, 4.1)), "SemiBold")
def s7(cv, t, D):
    p = eio(pr(t, 0, 1.6))
    for k in range(72):
        ang = math.radians(k * 5 - 90 + 30 * p); r0 = 330; r1 = 330 + (46 if k % 6 == 0 else 24)
        cv.line([(540 + r0 * math.cos(ang), 760 + r0 * math.sin(ang)), (540 + r1 * math.cos(ang), 760 + r1 * math.sin(ang))],
                MUST if k % 6 == 0 else PAPER, 5 if k % 6 == 0 else 3, eo(pr(t, k * .01, k * .01 + .4)) * .9)
    kinetic(cv, t, 740, "LATOON", 150, INKC, -.1, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, MUST, eo(pr(t, .9, 1.5)), "SemiBold")
    chip(cv, 280, 1110, 520, "FOLLOW", MUST, eo(pr(t, 1.6, 2.2)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
