# SANDO: forest-charcoal, paper cards, amber/rust/sage
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (34, 44, 40), (22, 30, 28)
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
    z = radial(40, (24, 30, 28), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-8, 9, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
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
def drone(cv, x, y, s, t, a=1, ang=0):
    ca, sa = math.cos(ang), math.sin(ang)
    arms = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    for ax, ay in arms:
        px, py = x + (ax * ca - ay * sa) * s * .9, y + (ax * sa + ay * ca) * s * .9
        cv.line([(x, y), (px, py)], INK, max(3, s * .12), a)
        cv.circ(px, py, s * .5, fill=mix(PAPER, INK, .35), a=.55 * a)
        cv.circ(px, py, s * .12, fill=INK, a=a)
        rr = s * .5; th = t * 40 + ax * 2
        cv.line([(px - rr * math.cos(th), py - rr * math.sin(th)), (px + rr * math.cos(th), py + rr * math.sin(th))], YEL, 3, .7 * a)
    cv.circ(x, y, s * .42, fill=INK, a=a)
    cv.circ(x - s * .06, y - s * .08, s * .34, fill=TEA, a=a)
    cv.circ(x - s * .12, y - s * .16, s * .1, fill=mix(TEA, WHT, .6), a=.8 * a)
def ob(cv, x, y, r, a=1, col=RED):
    cv.circ(x + 4, y + 8, r, fill=SHAD, a=.5 * a)
    cv.circ(x, y, r, fill=mix(col, (0, 0, 0), .4), a=a)
    cv.circ(x - r * .06, y - r * .08, r * .88, fill=col, a=a)
    cv.circ(x - r * .3, y - r * .32, r * .26, fill=mix(col, WHT, .5), a=.6 * a)
def bub(cv, x, y, r, a=1, col=RED):
    cv.circ(x, y, r, fill=col, a=.16 * a, outline=col, w=3, oa=.9 * a)
def s0(cv, t, D):
    kinetic(cv, t, 300, "CAN'T CRASH", 128, INKC, -.2, "Black", .03)
    kinetic(cv, t, 430, "MATHEMATICALLY PROVEN", 54, YEL, -.1, "Black", .02)
    card(cv, 100, 540, 980, 1380, 34)
    for i, (ox, oy, r) in enumerate([(280, 800, 46), (760, 1000, 54), (440, 1220, 40)]):
        mv = math.sin(t * 2 + i * 2) * 40
        bub(cv, ox + mv, oy, r + 50 + 20 * math.sin(t * 3 + i), eo(pr(t, .6, 1.2)))
        ob(cv, ox + mv, oy, r)
    drone(cv, 540 + 120 * math.sin(t * 1.6), 960 + 60 * math.cos(t * 1.1), 70, t, 1, math.sin(t) * .2)
    chip(cv, 250, 1440 - 50, 580, "MIT  .  SANDO", YEL, eo(pr(t, 1.6, 2.2)), INK, 36)
def s1(cv, t, D):
    head(cv, t, "NO MAP. NO WARNING.", "unknown things moving", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    # fog of unknown: dotted explored trail
    p = pr(t, .3, 5.6)
    pts = [(180 + 700 * u + 70 * math.sin(u * 9), 1250 - 560 * u + 40 * math.cos(u * 6)) for u in [k / 60 for k in range(61)]]
    n = int(60 * p)
    for k in range(0, n, 3): cv.circ(pts[k][0], pts[k][1], 7, fill=mix(PAPER, INK, .45), a=.9)
    for i, (ox, oy) in enumerate([(420, 1000), (700, 900), (330, 800)]):
        q = eo(pr(t, 1.0 + i * .5, 1.6 + i * .5))
        cv.text(ox + 20 * math.sin(t * 2 + i), oy + 20 * math.cos(t * 2.3 + i), "?", 84, RED, q, "Black")
    dx, dy = pts[min(60, n)]
    drone(cv, dx, dy, 60, t)
    cv.text(540, 1330, "unmapped  .  unpredictable", 32, INK, eo(pr(t, 3, 3.6)), "Bold")
def s2(cv, t, D):
    head(cv, t, "MOST PLANNERS", "only promise safety if...", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    for i, (txt, sub) in enumerate([("obstacles stand still", "static world"), ("the map is known", "obstacles known in advance")]):
        q = eo(pr(t, .6 + i * 1.2, 1.2 + i * 1.2)); y = 760 + i * 250
        cv.rrect(160, y - 80, 920, y + 80, 28, fill=PAPER2, a=q)
        cv.text(540, y - 18, txt.upper(), 46, INK, q, "Black"); cv.text(540, y + 38, sub, 30, MUTE if False else mix(INK, PAPER, .35), q, "SemiBold")
    q = eo(pr(t, 3.0, 3.6))
    chip(cv, 200, 1250, 680, "SANDO: NEITHER", TEA, q, INKC, 42, 84)
def s3(cv, t, D):
    head(cv, t, "THE TRICK", "know the top speed", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    q = eo(pr(t, .4, 1.0))
    ob(cv, 400, 960, 64, q)
    cv.text(400, 960, "?", 70, WHT, q, "Black")
    for k, ang in enumerate([-.5, 0, .5]):
        L = 260 * eo(pr(t, 1.2, 2.2))
        x1, y1 = 480 + L * math.cos(ang), 960 + L * math.sin(ang)
        cv.line([(480, 960), (x1, y1)], mix(RED, INK, .2), 6, eo(pr(t, 1.2, 1.6)))
    n = int(12 * eo(pr(t, 2.0, 3.0)))
    cv.text(540, 1230, f"max speed: {n} m/s".replace("12", "12") if False else "only needs: MAX SPEED", 44, INK, eo(pr(t, 2.2, 2.8)), "Black")
    cv.text(540, 1300, "not where it goes", 30, mix(INK, PAPER, .35), eo(pr(t, 3.2, 3.8)), "SemiBold")
def s4(cv, t, D):
    head(cv, t, "A GROWING BUBBLE", "farthest it could travel", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cx, cy = 540, 960
    r = 56 + 190 * eio(pr(t, .6, 3.6))
    for k in range(1, 4):
        rk = 56 + 190 * k / 3 * eio(pr(t, .6, 3.6))
        cv.circ(cx, cy, rk, fill=None, outline=RED, w=3, oa=.5)
    bub(cv, cx, cy, r, 1)
    ob(cv, cx, cy, 56)
    cv.text(cx, 1300, f"t + {pr(t,.6,3.6)*3:.1f} s", 44, INK, eo(pr(t, .6, 1.0)), "Black")
def s5(cv, t, D):
    head(cv, t, "SAFE CORRIDOR", "through space AND time", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    segs = [(170, 1190, 380, 1000), (360, 1030, 600, 840), (580, 880, 800, 800), (770, 830, 900, 700)]
    for i, (x0, y0, x1, y1) in enumerate(segs):
        q = eo(pr(t, .5 + i * .6, 1.0 + i * .6))
        cv.rrect(x0, min(y0, y1) - 40, x1, max(y0, y1) + 40, 30, fill=TEA, a=.28 * q, outline=TEA, w=3, oa=.9 * q)
    for i, (ox, oy) in enumerate([(300, 820), (560, 1180), (780, 1050)]):
        mv = math.sin(t * 1.5 + i) * 30
        bub(cv, ox, oy + mv, 90); ob(cv, ox, oy + mv, 30)
    u = pr(t, 2.2, 3.9); xs = [170, 400, 640, 860]; ys = [1190, 940, 840, 700]
    k = min(2, int(u * 3)); f = u * 3 - k
    drone(cv, lerp(xs[k], xs[k + 1], f), lerp(ys[k], ys[k + 1], f), 44, t, 1, -.5)
def s6(cv, t, D):
    head(cv, t, "HEAT MAP", "steers around crowds", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    rs = np.random.RandomState(3); g = 8
    hot = [(2, 2), (3, 2), (2, 3), (5, 4), (5, 5), (6, 5), (3, 5)]
    cw = 84
    for gx in range(g):
        for gy in range(g):
            d = min(math.hypot(gx - a, gy - b) for a, b in hot)
            v = max(0, 1 - d / 2.2)
            q = eo(pr(t, .2 + (gx + gy) * .05, .7 + (gx + gy) * .05))
            c = mix(PAPER2, RED, v * .9)
            x0, y0 = 540 - 4 * (cw + 4) + 2 + gx * (cw + 4), 640 + gy * (cw + 4)
            cv.rrect(x0, y0, x0 + cw, y0 + cw, 10, fill=c, a=q)
    path = [(200, 1290), (330, 1190), (420, 1090), (420, 900), (590, 800), (730, 900), (850, 780)]
    u = pr(t, 1.8, 4.2) * (len(path) - 1); k = min(len(path) - 2, int(u)); f = u - k
    for j in range(1, k + 1): cv.line(path[:j + 1], TEA, 8, 1)
    px, py = lerp(path[k][0], path[k + 1][0], f), lerp(path[k][1], path[k + 1][1], f)
    cv.line(path[:k + 1] + [(px, py)], TEA, 8, 1)
    drone(cv, px, py, 40, t)
def s7(cv, t, D):
    head(cv, t, "THE RESULT", "simulation + real flights", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    n = int(12 * eo(pr(t, .8, 2.4)))
    cv.text(540, 780, "0", 220, TEA, eo(pr(t, .3, .8)), "Black")
    cv.text(540, 930, "COLLISIONS IN SIMULATION", 36, INK, eo(pr(t, .6, 1.1)), "Black")
    cv.line([(220, 1020), (860, 1020)], mix(PAPER, INK, .4), 4)
    cv.text(380, 1160, f"{n}", 150, RED, eo(pr(t, 2.6, 3.0)), "Black")
    cv.text(700, 1130, "REAL FLIGHTS", 38, INK, eo(pr(t, 3.2, 3.8)), "Black")
    cv.text(700, 1185, "none hit anything", 30, mix(INK, PAPER, .35), eo(pr(t, 4.2, 4.8)), "SemiBold")
    cv.text(540, 1300, "and faster to the goal", 34, INK, eo(pr(t, 4.8, 5.4)), "Bold")
def s8(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, INKC, 0, "Black", .05)
    cv.text(540, 930, "Voyaging the unseen", 52, YEL, eo(pr(t, .6, 1.2)), "SemiBold")
    chip(cv, 280, 1060, 520, "FOLLOW", YEL, eo(pr(t, 1.2, 1.8)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
