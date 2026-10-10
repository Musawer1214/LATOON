# ---------- scenes: Gradient descent explainer (all code-drawn)
BG0, BG1 = (14, 6, 24), (34, 14, 46)
AMB, AMB2 = (255, 176, 60), (255, 222, 150)
YEL, PINK, SKY, VIO, MINT = (255, 208, 80), (255, 112, 160), (110, 190, 255), (180, 140, 255), (90, 235, 180)
CREAM = (250, 242, 252)
INK = (18, 8, 28)
CARDC = (36, 18, 52)
RED = (255, 90, 100)
GOLD = AMB
BL, BL2 = AMB, PINK
NOFADE_IN, NOFADE_OUT = {0}, set()
IM = {}
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S
    GLOW_O = radial(520, (255, 150, 60), 0.14); GLOW_B = radial(560, (170, 90, 255), 0.20); GLOW_S = radial(260, (255, 222, 150), 0.6)
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def chip(cv, x, y, txt, size, fg, bg, a=1, outline=None, w="Bold"):
    tw = cv.tw(txt, size, w); pw, ph = tw / 2 + size * .8, size * .95
    cv.rrect(x - pw, y - ph, x + pw, y + ph, ph, fill=bg, a=a, outline=outline, w=3)
    cv.text(x, y, txt, size, fg, a, w)
DIMC = (110, 80, 140)
def Lf(u): return 2.6 * (u - .68) ** 2 + .07 * math.sin(13 * u) + .06
def dL(u): return 5.2 * (u - .68) + .07 * 13 * math.cos(13 * u)
X0, X1, YB, YT = 90, 990, 1400, 780
def lx(u): return X0 + u * (X1 - X0)
def ly(u): return YB - (Lf(u) - .0) / 1.0 * (YB - YT) * .78 + 0 
def land(cv, upto=1.0, col=AMB, a=1, w=8):
    n = 90; pts = [(lx(i / n * upto), ly(i / n * upto)) for i in range(n + 1)]
    cv.line(pts, col, w, a)
# gradient descent path from u=.08
PATH = [.08]
for _ in range(60):
    u = PATH[-1]; PATH.append(min(.98, max(.02, u - .045 * dL(u))))
def ball(cv, u, r=26, col=PINK, a=1):
    cv.circ(lx(u), ly(u) - r, r + 10, fill=col, a=.25 * a)
    cv.circ(lx(u), ly(u) - r, r, fill=col, a=a)
def pathpos(k):  # fractional step index -> u
    i = int(k); f = k - i; i = min(i, len(PATH) - 2)
    return PATH[i] + (PATH[i + 1] - PATH[i]) * eio(cl(f))

def s0(cv, t, D):
    chip(cv, 540, 290, "HOW AI ACTUALLY LEARNS", 28, INK, AMB, 1)
    kinetic(cv, t, 440, "WALKING", 150, WHT, -.3, "Black", .02)
    kinetic(cv, t, 600, "DOWNHILL", 150, AMB2, -.2, "Black", .02)
    land(cv, eo(pr(t, .1, 1.0)))
    if t > .3: ball(cv, pathpos(cl((t - .3) * 4, 0, 14)))
    cv.text(540, 1400, "in the dark", 44, CREAM, eo(pr(t, 1.2, 1.8)), "SemiBold")

def s1(cv, t, D):
    kinetic(cv, t, 330, "START: RANDOM", 100, AMB2, 0, "Black", .03)
    cv.text(540, 440, "a model that gets everything wrong", 36, CREAM, eo(pr(t, .3, .8)), "SemiBold")
    qs = [("2 + 2 = ?", "banana"), ("capital of France?", "7%^q"), ("say hello", "zzzzz")]
    for i, (q, a_) in enumerate(qs):
        y = 640 + i * 190; p = eback(pr(t, .5 + i * .5, 1 + i * .5), 2)
        cv.rrect(110, y - 70, 970, y + 70, 30, fill=CARDC, a=cl(p), outline=DIMC, w=3, oa=cl(p))
        cv.text(130 + cv.tw(q, 40, "Bold") / 2, y - 6, q, 40, CREAM, cl(p), "Bold")
        cv.text(740, y - 6, a_, 44, RED, cl(p), "Black")
        r = eo(pr(t, 1.1 + i * .5, 1.4 + i * .5))
        cv.line([(920 - 20, y - 26), (920 + 20, y + 14)], RED, 8, r); cv.line([(920 + 20, y - 26), (920 - 20, y + 14)], RED, 8, r)

def s2(cv, t, D):
    cv.text(540, 360, "THE WRONGNESS", 70, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 440, "becomes one number", 40, AMB2, eo(pr(t, .3, .7)), "SemiBold")
    v = 2.31 + .04 * math.sin(t * 9)
    q = eback(pr(t, .4, 1.0), 2)
    cv.rrect(180, 650, 900, 1010, 50, fill=CARDC, a=cl(q), outline=AMB, w=5, oa=cl(q))
    cv.text(540, 740, "LOSS", 56, AMB, cl(q), "Black")
    cv.text(540, 890, f"{v:.2f}", 190 * q, WHT, cl(q), "Black")
    cv.text(540, 1130, "lower = better", 44, CREAM, eo(pr(t, 1.5, 2.0)), "SemiBold")

def s3(cv, t, D):
    cv.text(540, 330, "PICTURE THE LOSS", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 405, "as a landscape", 52, AMB2, eo(pr(t, .2, .6)), "Black")
    land(cv, eo(pr(t, .3, 1.8)))
    cv.text(lx(.08), ly(.08) - 130, "HIGH GROUND", 34, RED, eo(pr(t, 2.2, 2.7)), "Black")
    cv.text(lx(.08), ly(.08) - 85, "bad answers", 30, CREAM, eo(pr(t, 2.4, 2.9)), "Medium")
    cv.text(lx(.68), ly(.68) + 70, "LOW GROUND", 34, MINT, eo(pr(t, 3.2, 3.7)), "Black")
    cv.text(lx(.68), ly(.68) + 115, "good answers", 30, CREAM, eo(pr(t, 3.4, 3.9)), "Medium")

def s4(cv, t, D):
    cv.text(540, 330, "BUT IT'S DARK", 66, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 405, "no map, only the slope underfoot", 36, AMB2, eo(pr(t, .3, .8)), "SemiBold")
    u = PATH[0]
    land(cv, 1, DIMC, .6, 6)
    # visible window around the ball
    for k in range(40):
        uu = u - .1 + k / 39 * .2
        f = 1 - abs(uu - u) / .1
        if 0 <= uu <= 1: cv.circ(lx(uu), ly(uu), 6 + 6 * f, fill=AMB, a=.9 * f * eo(pr(t, .2, .8)))
    ball(cv, u)
    sl = eo(pr(t, 1.5, 2.3)); m = dL(u) * (YB - YT) * .78 / (X1 - X0)
    cx, cy = lx(u), ly(u)
    cv.line([(cx - 110, cy - m * -110 * -1 if False else cy + (-110) * m), (cx + 110 * sl, cy + 110 * sl * m)], YEL, 7, sl)
    cv.text(cx + 150, cy - 130, "slope here", 34, YEL, eo(pr(t, 2.0, 2.6)), "Black")

def s5(cv, t, D):
    cv.text(540, 330, "ONE SMALL STEP", 66, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 405, "downhill", 52, AMB2, eo(pr(t, .2, .6)), "Black")
    land(cv, 1, AMB, .8, 7)
    k = cl((t - 1.0) * 1.3, 0, 1)
    ball(cv, PATH[0] + (PATH[1] - PATH[0]) * eio(k) * 1.0)
    a = eo(pr(t, 1.4, 2.1))
    cx, cy = lx(PATH[0]) + 40, ly(PATH[0]) - 140
    cv.line([(cx, cy), (cx + 110 * a, cy + 60 * a)], MINT, 10, a)
    cv.poly([(cx + 110 * a - 8, cy + 60 * a - 26), (cx + 140 * a, cy + 76 * a), (cx + 110 * a + 22, cy + 60 * a - 6)], MINT, a)
    chip(cv, 540, 1130 - 520 if False else 540 + 0, "", 1, INK, INK, 0)
    q = eback(pr(t, 2.8, 3.4), 2)
    chip(cv, 540, 560, "THE GRADIENT", 46, INK, MINT, q)
    cv.text(540, 635, "the direction of steepest slope", 32, CREAM, eo(pr(t, 3.4, 3.9)), "SemiBold")

def s6(cv, t, D):
    cv.text(540, 360, "MEASURE", 100, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 480, "STEP.  AGAIN.", 100, AMB2, eo(pr(t, .3, .7)), "Black")
    land(cv, 1, AMB, .8, 7)
    ball(cv, pathpos(cl(1 + (t) * 2.5, 0, 14)))

def s7(cv, t, D):
    cv.text(540, 330, "BILLIONS OF STEPS", 62, WHT, eo(pr(t, .05, .4)), "Black")
    f = eio(pr(t, .2, 2.5))
    v = 2.31 * (1 - f) + .05 * f
    cv.text(540, 520, f"loss {v:.2f}", 90, MINT if f > .9 else AMB2, 1, "Black")
    land(cv, 1, DIMC, .5, 6)
    ball(cv, pathpos(f * 40 + 0))
    n = int(f * 9e9)
    cv.text(540, 1420 - 40, "steps repeated again and again", 30, CREAM, eo(pr(t, .6, 1.1)), "Medium")

def mini(cv, cx, title, col, kind, t):
    cv.rrect(cx - 160, 560, cx + 160, 1160, 30, fill=CARDC, a=1, outline=col, w=4, oa=.8)
    cv.text(cx, 620, title, 36, col, 1, "Black")
    # parabola bowl
    pts = [(cx - 120 + i * 240 / 30, 1080 - 330 * (1 - ((i / 15) - 1) ** 2 * 1.0) * -1 * -1) for i in range(31)]
    pts = [(cx - 120 + i * 240 / 30, 780 + 260 * (1 - (1 - (i / 15 - 1) ** 2))) for i in range(31)]
    pts = [(cx - 120 + i * 240 / 30, 780 + 260 * ((i / 15 - 1) ** 2) * -1 + 260) for i in range(31)]
    cv.line(pts, WHT, 5, .8)
    def pos(x): return 780 + 260 - 260 * (x ** 2) * -1 * -1 if False else 780 + 260 * (x ** 2)
    if kind == "big": xs = [-.9, .95, -.98, .99, -.99]; 
    elif kind == "small": xs = [-.9, -.88, -.86, -.84, -.82]
    else: xs = [-.9, -.5, -.25, -.1, -.03]
    k = min(len(xs) - 1.001, t * 1.4); i = int(k); f = eio(k - i)
    x = xs[i] + (xs[i + 1] - xs[i]) * f
    cv.circ(cx + x * 120, pos(x) - 20 + 0, 18, fill=PINK)

def s8(cv, t, D):
    cv.text(540, 330, "STEP SIZE MATTERS", 62, WHT, eo(pr(t, .05, .4)), "Black")
    mini(cv, 200, "TOO BIG", RED, "big", cl(t - .3, 0, 9) if False else max(0, t - .5))
    mini(cv, 540, "TOO SMALL", SKY, "small", max(0, t - .5))
    mini(cv, 880, "JUST RIGHT", MINT, "ok", max(0, t - .5))
    cv.text(200, 1230, "overshoots", 30, CREAM, eo(pr(t, 1.5, 2.0)), "SemiBold")
    cv.text(540, 1230, "never arrives", 30, CREAM, eo(pr(t, 2.5, 3.0)), "SemiBold")
    cv.text(880, 1230, "settles in", 30, CREAM, eo(pr(t, 3.5, 4.0)), "SemiBold")

def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(5):
        u = (t * .35 + k / 5) % 1
        cv.circ(540, 640, 60 + u * 330, outline=AMB, w=4, oa=(1 - u) * .7 * p)
    land(cv, 1, AMB2, p, 8) if False else None
    cv.circ(540, 640, 70 * p, fill=PINK, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, YEL, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1210, "all learning is just walking downhill.", 32, AMB2, eo(pr(t, 1.8, 2.3)), "Medium")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
