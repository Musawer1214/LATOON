
def ell(cv, cx, cy, rx, ry, col, a=1):
    if rx < 1 or ry < 1: return
    cv.poly([(cx + rx * math.cos(i * math.pi / 18), cy + ry * math.sin(i * math.pi / 18)) for i in range(36)], col, a)
def ball(cv, x, y, r, col, a=1):
    ell(cv, x + r * .25, y + r * 1.05, r * .9, r * .28, SHAD, .35 * a)
    cv.circ(x, y, r, fill=mix(col, (0, 0, 0), .35), a=a)
    cv.circ(x - r * .08, y - r * .08, r * .88, fill=col, a=a)
    cv.circ(x - r * .22, y - r * .26, r * .6, fill=mix(col, WHT, .25), a=a)
    cv.circ(x - r * .36, y - r * .4, r * .2, fill=WHT, a=a * .85)
SUB = [((-1, -1), RED), ((1, -1), YEL), ((-.65, 1.1), TEA), ((.95, .8), GRN)]
def mol(cv, cx, cy, s, flip=1, a=1, rot=0.0):
    pts = []
    for (dx, dy), c in SUB:
        x, y = dx * 105 * s * flip, dy * 95 * s
        cr, sr = math.cos(rot), math.sin(rot)
        pts.append((cx + x * cr - y * sr * 0.0, cy + y, c))
    for x, y, c in pts:
        cv.line([(cx, cy), (x, y)], mix(PAPER, INK, .55), max(5, 14 * s), a)
    for x, y, c in pts[:3] + [pts[3]]:
        ball(cv, x, y, 34 * s, c, a)
    ball(cv, cx, cy, 44 * s, (70, 62, 58), a)
def fadectx(cv, a):
    g = cv.ga; cv.ga = g * cl(a); return g
def s0(cv, t, D):
    kinetic(cv, t, 320, "LIFE IS", 120, INKC, -.2, "Black", .03)
    kinetic(cv, t, 455, "ONE-HANDED", 112, YEL, -.1, "Black", .03)
    p = eo(pr(t, .0, .5))
    card(cv, 100, 580, 980, 1380, 34, a=p)
    mol(cv, 330, 960, 1.15, 1, p)
    cv.line([(540, 640), (540, 1320)], mix(PAPER, INK, .5), 4, .9 * p)
    mol(cv, 750, 960, 1.15, -1, eo(pr(t, .5, 1.2)))
    cv.text(330, 1290, "LEFT", 34, INK, p, "Black"); cv.text(750, 1290, "RIGHT", 34, INK, eo(pr(t, .5, 1.2)), "Black")
def s1(cv, t, D):
    head(cv, t, "MIRROR TWINS", "same atoms, opposite shape", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    sl = eio(pr(t, .3, 1.3))
    mol(cv, 300, 940, 1.2, 1, 1)
    cv.line([(540, 620), (540, 1320)], mix(PAPER, INK, .5), 4, .9)
    ghost = eo(pr(t, 1.2, 1.9))
    mol(cv, lerp(300, 780, sl), 940, 1.2, -1 if sl > .5 else 1, eo(pr(t, .3, .8)) * (1 if sl > 0 else 0))
    if ghost > 0:
        chip(cv, 215, 1250, 650, "CAN'T BE STACKED", RED, ghost, INKC, 36)
def s2(cv, t, D):
    head(cv, t, "IN A TEST TUBE", "chemists got both, always", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    b = eo(pr(t, .3, 1.2))
    cv.text(300, 640, "LAB", 36, INK, b, "Black"); cv.text(780, 640, "LIFE", 36, INK, b, "Black")
    for x, vals in ((300, (.5, .5)), (780, (1.0, .0))):
        hh = 560
        base = 1230
        for i, (v, c) in enumerate(zip(vals, (RED, TEA))):
            hgt = hh * v * b
            if hgt > 2:
                y0 = base - hgt if i == 0 else base - hh * vals[0] * b - hgt
                cv.rrect(x - 90, y0, x + 90, y0 + hgt, 8, fill=c)
        cv.rrect(x - 90, base - hh, x + 90, base, 8, outline=INK, w=3)
    cv.text(300, 1290, "50 : 50", 44, INK, b, "Black"); cv.text(780, 1290, "ONLY ONE", 44, RED, b, "Black")
def pill(cv, x, y, s, col, a=1, rot=0):
    cv.rrect(x - 90 * s + 5, y - 40 * s + 10, x + 90 * s + 5, y + 40 * s + 10, 40 * s, fill=SHAD, a=.4 * a)
    cv.rrect(x - 90 * s, y - 40 * s, x + 90 * s, y + 40 * s, 40 * s, fill=PAPER, a=a, outline=INK, w=3, oa=a)
    cv.rrect(x - 90 * s, y - 40 * s, x, y + 40 * s, 40 * s, fill=col, a=a)
    cv.rrect(x - 60 * s, y - 28 * s, x - 10 * s, y - 14 * s, 7 * s, fill=mix(col, WHT, .45), a=a * .8)
def s3(cv, t, D):
    head(cv, t, "IN MEDICINE", "usually only one twin does the job", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    for y, c, ok, d0 in ((800, TEA, True, .2), (1100, RED, False, .8)):
        q = eback(pr(t, d0, d0 + .6), 1.6)
        pill(cv, 380 + (1 - q) * 500, y, 1.2, c, cl(q * 1.4))
        mol(cv, 270 + (1 - q) * 500, y - 4, .0001, 1, 0)
        r = eo(pr(t, d0 + .7, d0 + 1.3))
        if ok:
            cv.circ(780, y, 62 * r, fill=GRN)
            check(cv, 780, y, 30, r, INKC, 10)
        else:
            cv.circ(780, y, 62 * r, fill=RED)
            cv.line([(755, y - 25), (805, y + 25)], INKC, 10, r); cv.line([(805, y - 25), (755, y + 25)], INKC, 10, r)
    cv.text(540, 1250, "same atoms, different effect", 38, INK, eo(pr(t, 2.2, 2.9)), "Bold")
def s4(cv, t, D):
    head(cv, t, "1986", "Henri Kagan", YEL)
    q = eback(pr(t, .1, .8), 1.5)
    img(cv, None, lerp(-300, 290, q), 930, .95, a=eo(pr(t, .1, .4)), src=IM["p_kagan"])
    card(cv, 560, 700, 990, 1270, 28)
    cv.text(775, 760, "SHARE OF ONE TWIN", 26, INK, 1, "Black")
    b = eo(pr(t, 1.8, 3.8))
    for i, (lab, v, c) in enumerate((("old limit", .60, MUTE), ("Kagan", .90, YEL))):
        x = 650 + i * 250
        hh = 380 * v * (1 if i == 0 else b)
        cv.rrect(x - 55, 1190 - hh, x + 55, 1190, 8, fill=c, outline=INK, w=3)
        cv.text(x, 1235, lab, 28, INK, 1, "Bold")
    cv.text(775, 1190 - 380 * (.6 + .3 * b) - 30 if b > 0 else 900, "", 20, INK, 0)
    chip(cv, 110, 1310, 860, "A NEW WAY TO STEER REACTIONS", YEL, eo(pr(t, 3.0, 3.6)), INK, 34)
def s5(cv, t, D):
    head(cv, t, "KENSO SOAI", "1995 design, 2003 success", YEL)
    q = eback(pr(t, .1, .8), 1.5)
    img(cv, None, lerp(1380, 790, q), 880, .92, a=eo(pr(t, .1, .4)), src=IM["p_soai"])
    cv.line([(190, 760), (190, 1250)], mix(PAPER, INK, .3), 6, eo(pr(t, 1.0, 1.6)))
    for y, yr, lab, d0 in ((820, "1995", "design", 1.2), (1100, "2003", "ONE twin only", 3.0)):
        r = eo(pr(t, d0, d0 + .5))
        cv.circ(190, y, 24 * r, fill=YEL if yr == "2003" else MUTE, outline=INKC, w=4)
        cv.text(250, y - 20, yr, 52, YEL if yr == "2003" else INKC, r, "Black", anchor="lm")
        cv.text(250, y + 34, lab, 30, INKC, r, "Bold", anchor="lm")
    chip(cv, 110, 1330, 860, "FIRST REACTION TO PICK A HAND", GRN, eo(pr(t, 4.4, 5.0)), INK, 32)
def s6(cv, t, D):
    head(cv, t, "AUTOCATALYSIS", "the product helps make more of itself", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    rs = random.Random(3)
    cols, rows = 14, 9
    steps = ((0, .55), (1.3, .70), (2.5, .88), (3.7, 1.0))
    frac = .55
    for st, f in steps:
        if t >= st: frac = f
    for r_ in range(rows):
        for c_ in range(cols):
            x, y = 160 + c_ * 58, 650 + r_ * 66
            k = rs.random()
            col = RED if k < frac else TEA
            q = eback(pr(t, .1 + (r_ * cols + c_) * .004, .5 + (r_ * cols + c_) * .004), 1.6)
            cv.circ(x, y, 22 * q, fill=mix(col, (0, 0, 0), .3)); cv.circ(x - 1, y - 2, 19 * q, fill=col)
    cv.text(540, 1290, "tiny edge  >  snowball", 44, INK, eo(pr(t, 1.0, 1.7)), "Black")
def s7(cv, t, D):
    kinetic(cv, t, 560, "OTHER THAN", 100, INKC, 0, "Black", .03)
    kinetic(cv, t, 690, "LIFE ITSELF,", 104, YEL, .2, "Black", .03)
    kinetic(cv, t, 850, "NO ONE HAD", 100, INKC, .5, "Black", .03)
    kinetic(cv, t, 980, "DONE THIS", 100, INKC, .7, "Black", .03)
    chip(cv, 170, 1180, 740, "NOBEL COMMITTEE, 2026", RED, eo(pr(t, 1.8, 2.4)), INKC, 34)
def s8(cv, t, D):
    head(cv, t, "WHAT IT UNLOCKS", "", YEL)
    for i, (lab, sub, c) in enumerate((("DRUG REACTIONS", "that pick a hand", TEA), ("ORIGIN OF LIFE", "a clue to handedness", RED))):
        q = eback(pr(t, .3 + i * 1.0, .9 + i * 1.0), 1.5)
        y = 650 + i * 360
        card(cv, 120 + (1 - q) * 900, y, 960 + (1 - q) * 900, y + 300, 30)
        cv.rrect(120 + (1 - q) * 900, y, 160 + (1 - q) * 900, y + 300, 20, fill=c)
        cv.text(560 + (1 - q) * 900, y + 120, lab, 54, INK, 1, "Black")
        cv.text(560 + (1 - q) * 900, y + 200, sub, 36, mix(INK, PAPER, .3), 1, "SemiBold")
    chip(cv, 215, 1340, 650, "KAGAN + SOAI  ·  NOBEL 2026", YEL, eo(pr(t, 2.6, 3.2)), INK, 30)
def s9(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, YEL, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
