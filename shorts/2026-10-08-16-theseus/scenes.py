# Ship of Theseus: cream paper, ink, walnut, teal, ochre
import math
BG0, BG1 = (240, 229, 208), (226, 211, 185)
INKC = (43, 33, 28); WHT = INKC
TERRA, MUST, TEAL, PLUM = (176, 70, 48), (204, 146, 44), (36, 104, 106), (92, 66, 96)
PAPER, EDGE, SHAD = (251, 245, 230), (140, 118, 92), (170, 150, 120)
OLD, OLD2, NEW, NEW2 = (104, 66, 40), (84, 52, 32), (214, 170, 110), (196, 152, 94)
GOLD = TERRA; BL, BL2 = TERRA, TERRA
NOFADE_IN, NOFADE_OUT = {0}, set()
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (240, 229, 208), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, outline=EDGE, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.5 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)
def head(cv, t, a, b=None, c=None):
    kinetic(cv, t, 310, a, 64, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or TERRA, eo(pr(t, .3, .7)), "SemiBold")
def ship(cv, cx, cy, s, st, a=1, sail=True):
    for r in range(3):
        y0 = cy + r * 50 * s; y1 = y0 + 50 * s
        def xs(y):
            f = (y - cy) / (150 * s)
            return cx - (300 - 110 * f * f - 40 * f) * s, cx + (300 - 110 * f * f - 40 * f) * s
        a0, b0 = xs(y0); a1, b1 = xs(y1)
        for c in range(6):
            u0, u1 = c / 6, (c + 1) / 6
            p = [(lerp(a0, b0, u0), y0), (lerp(a0, b0, u1), y0), (lerp(a1, b1, u1), y1), (lerp(a1, b1, u0), y1)]
            v = cl(st(r, c))
            col = mix(OLD if (r + c) % 2 else OLD2, NEW if (r + c) % 2 else NEW2, v)
            cv.poly(p, col, a)
            cv.line(p + [p[0]], mix(INKC, col, .45), 2, a * .8)
    cv.line([(cx - 300 * s, cy - 6 * s), (cx + 300 * s, cy - 6 * s)], INKC, 7 * s, a)
    if sail:
        cv.line([(cx, cy - 6 * s), (cx, cy - 330 * s)], INKC, 9 * s, a)
        sp = [(cx + 14 * s, cy - 320 * s), (cx + 14 * s, cy - 60 * s), (cx + 190 * s, cy - 80 * s), (cx + 150 * s, cy - 200 * s)]
        cv.poly(sp, mix(PAPER, (225, 205, 170), .5), a)
        cv.line(sp + [sp[0]], INKC, 3 * s, a * .7)
        cv.poly([(cx, cy - 330 * s), (cx - 60 * s, cy - 305 * s), (cx, cy - 285 * s)], TERRA, a)
    for k in range(3):
        yy = cy + 165 * s + k * 26 * s
        cv.line([(cx - 330 * s + k * 30, yy), (cx - 160 * s, yy + 8), (cx, yy), (cx + 160 * s, yy + 8), (cx + 330 * s - k * 30, yy)], TEAL, 5, a * (.7 - k * .2))
def s0(cv, t, D):
    cv.rrect(240, 380, 840, 440, 30, fill=TERRA, a=eo(pr(t, 0, .3)))
    cv.text(540, 408, "PHILOSOPHY PUZZLE", 32, PAPER, eo(pr(t, 0, .3)), "Black")
    kinetic(cv, t, 560, "SAME SHIP?", 130, INKC, -.2, "Black", .02)
    n = int(pr(t, .3, 2.2) * 18)
    ship(cv, 540, 980, .95, lambda r, c: 1 if r * 6 + c < n else 0)
    cv.text(540, 1380, "every plank replaced", 46, TERRA, eo(pr(t, 1.8, 2.4)), "Bold")
def s1(cv, t, D):
    head(cv, t, "SHIP OF THESEUS", "Plutarch, about 2,000 years ago")
    p = eo(pr(t, .3, 1))
    card(cv, 120, 520, 960, 1000, 34, a=p)
    cv.text(540, 600, "PLUTARCH", 52, INKC, p, "Black"); cv.text(540, 660, "Greek writer, c. 46-119 AD", 32, PLUM, p, "SemiBold")
    for k, ln in enumerate(["“...the ship wherein Theseus", "and the youth of Athens returned...”"]):
        cv.text(540, 790 + k * 62, ln, 38, INKC, eo(pr(t, 1.0 + k * .5, 1.6 + k * .5)), "Bold")
    cv.text(540, 930, "Life of Theseus", 34, TERRA, eo(pr(t, 2.4, 3.0)), "SemiBold")
    ship(cv, 540, 1180, .5, lambda r, c: 0, a=eo(pr(t, 2.0, 2.8)))
def s2(cv, t, D):
    head(cv, t, "ONE PLANK AT A TIME", "rotten out, fresh in")
    n = int(pr(t, .6, 3.8) * 18)
    ship(cv, 540, 900, .9, lambda r, c: 1 if (c * 3 + r) < n else 0)
    q = pr(t, .6, 3.8); cv.rrect(180, 1290, 900, 1320, 15, fill=SHAD, a=.5)
    cv.rrect(180, 1290, 180 + max(1, 720 * q), 1320, 15, fill=TEAL)
    cv.text(540, 1370, f"{int(q*100)}% replaced", 42, INKC, 1, "Black")
def s3(cv, t, D):
    head(cv, t, "ZERO ORIGINAL PLANKS", "still his ship?")
    ship(cv, 540, 860, .9, lambda r, c: 1)
    q = eback(pr(t, 1.2, 1.8), 2)
    card(cv, 200, 1230, 880, 1370, 40, fill=TERRA, outline=TERRA, a=cl(q))
    cv.text(540, 1300, "STILL THE SAME?", 62 * q, PAPER, cl(q), "Black")
def s4(cv, t, D):
    head(cv, t, "NOW IT GETS WORSE", "someone saves the old planks")
    ship(cv, 540, 740, .5, lambda r, c: 1, a=.9)
    pp = pr(t, .5, 2.2)
    for k in range(12):
        x = lerp(160 + (k % 6) * 150, 240 + (k % 6) * 120, eio(pp)); y = lerp(1000 + (k // 6) * 70, 1060 + (k // 6) * 55, eio(pp))
        cv.rrect(x - 55, y - 22, x + 55, y + 22, 8, fill=OLD if k % 2 else OLD2, a=eo(pr(t, .3 + k * .03, .7 + k * .03)), outline=INKC, w=2)
    cv.text(540, 1250, "rebuilt from the originals", 44, INKC, eo(pr(t, 2.6, 3.4)), "Bold")
def s5(cv, t, D):
    head(cv, t, "NOW THERE ARE TWO", None)
    p = eo(pr(t, .3, 1.0)); q = eo(pr(t, 1.6, 2.3))
    card(cv, 70, 470, 1010, 880, 34, a=p)
    ship(cv, 540, 680, .52, lambda r, c: 0, a=p)
    cv.text(540, 840, "original parts", 46, OLD, p, "Black")
    card(cv, 70, 930, 1010, 1340, 34, a=q)
    ship(cv, 540, 1140, .52, lambda r, c: 1, a=q)
    cv.text(540, 1300, "original history", 46, TEAL, q, "Black")
def s6(cv, t, D):
    head(cv, t, "PHILOSOPHERS SPLIT", None)
    p = eback(pr(t, .4, 1.0), 2); q = eback(pr(t, 2.4, 3.0), 2)
    card(cv, 70, 470, 1010, 900, 36, fill=OLD, outline=OLD, a=cl(p))
    cv.text(540, 560, "MATTER", 84 * p, PAPER, cl(p), "Black")
    cv.text(540, 680, "identity is the stuff", 44, PAPER, cl(p), "SemiBold")
    cv.text(540, 770, "you are your atoms", 38, NEW, cl(p), "Bold")
    card(cv, 70, 960, 1010, 1390, 36, fill=TEAL, outline=TEAL, a=cl(q))
    cv.text(540, 1050, "FORM", 84 * q, PAPER, cl(q), "Black")
    cv.text(540, 1170, "identity is continuity", 44, PAPER, cl(q), "SemiBold")
    cv.text(540, 1260, "you are the pattern", 38, (200, 230, 220), cl(q), "Bold")
def s7(cv, t, D):
    head(cv, t, "YOU ARE THE SHIP", "your cells swap too")
    p = eo(pr(t, .3, .9))
    for i in range(48):
        r_ = 200 + (i % 4) * 60; ang = i / 48 * 6.283 + t * .2 * (1 if i % 2 else -1)
        x = 540 + math.cos(ang) * r_; y = 900 + math.sin(ang) * r_ * .9
        sw = pr(t, 1.2 + (i % 12) * .22, 1.7 + (i % 12) * .22)
        cv.circ(x, y, 22, fill=mix(OLD, TEAL, sw), a=p * .9, outline=INKC, w=2, oa=p * .6)
    cv.circ(540, 900, 110, fill=PAPER, a=p, outline=INKC, w=4, oa=p)
    cv.circ(540, 868, 28, fill=INKC, a=p); cv.rrect(496, 906, 584, 972, 30, fill=INKC, a=p)
    cv.text(540, 1360, "still feels like one person", 44, INKC, eo(pr(t, 3.4, 4.0)), "Bold")
def s8(cv, t, D):
    head(cv, t, "A LINE WE DRAW", None)
    p = eo(pr(t, .3, 1.0))
    ship(cv, 540, 820, .62, lambda r, c: c / 5, a=p)
    x = 160 + 760 * eio(pr(t, 1.4, 3.6))
    cv.line([(x, 480), (x, 1100)], TERRA, 8, eo(pr(t, 1.2, 1.6)))
    cv.circ(x, 470, 20, fill=TERRA, a=eo(pr(t, 1.2, 1.6)))
    cv.text(540, 1230, "“same” is a choice", 62, INKC, eo(pr(t, 3.0, 3.7)), "Black")
    cv.text(540, 1320, "not a fact we're handed", 40, TERRA, eo(pr(t, 3.4, 4.0)), "SemiBold")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    ship(cv, 540, 700, .7, lambda r, c: 0, a=p)
    kinetic(cv, t, 1090, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1200, "Voyaging the Unseen", 46, TERRA, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
