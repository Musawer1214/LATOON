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
