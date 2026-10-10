def s0(cv, t, D):
    kinetic(cv, t, 300, "THE RIGHT THING", 92, INKC, -.2, "Black", .03)
    kinetic(cv, t, 410, "IN THE WRONG WINDOW", 62, MUST, .35, "Black", .02)
    photo(cv, "aerial", 90, 500, 990, 1060, t / D, 1.0, 1.2, .5, .5)
    brackets(cv, 90, 500, 990, 1060, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Laptop and phone: Rawpixel Ltd, CC BY 2.0", 1100, eo(pr(t, .8, 1.3)))
    qa = eo(pr(t, .5, 1.0))
    card(cv, 70, 1130, 520, 1330, 26, PAPER, qa * .6)
    cv.text(295, 1172, "EMAIL TO BOSS", 28, INK, qa * .7, "Black")
    cv.rrect(110, 1210, 480, 1237, 8, fill=PAPER2, a=qa * .7); cv.rrect(110, 1260, 400, 1287, 8, fill=PAPER2, a=qa * .7)
    card(cv, 560, 1130, 1010, 1330, 26, PAPER, qa)
    cv.text(785, 1172, "CHAT WITH MUM", 28, INK, qa, "Black")
    cv.rrect(600, 1210, 970, 1237, 8, fill=PAPER2, a=qa); cv.rrect(600, 1260, 880, 1287, 8, fill=PAPER2, a=qa)
    # pasted file chip flies to the wrong card
    p = eio(pr(t, 1.4, 2.5))
    cx = lerp(220, 785, p); cy = lerp(1110, 1290, p) - math.sin(p * math.pi) * 60
    ca = eo(pr(t, 1.0, 1.4))
    chip(cv, cx - 120, cy - 34, 240, "REPORT.PDF", MUST, ca, INK, 28, 68)
    q = eback(pr(t, 2.7, 3.1), 2)
    cross(cv, 950, 1172, 20 * q, CORAL, cl(q * 1.4), 9)
    kk = eo(pr(t, 3.3, 3.8))
    chip(cv, 250, 1360, 580, "NOT JUST LOST FOCUS?", CORAL, kk, INKC, 32, 64)
def s1(cv, t, D):
    kinetic(cv, t, 300, "CHENG XUE", 100, INKC, -.2, "Black", .03)
    cv.text(540, 400, "neuroscientist  \u00b7  University of Chicago", 36, MUST, eo(pr(t, .3, .8)), "SemiBold")
    photo(cv, "harper", 110, 470, 970, 1050, t / D, 1.0, 1.2, .5, .4)
    brackets(cv, 110, 470, 970, 1050, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Harper Memorial Library: Warren LeMay, CC BY-SA 2.0", 1090, eo(pr(t, .8, 1.3)))
    qa = eo(pr(t, 1.0, 1.5))
    card(cv, 120, 1140, 960, 1300, 28, PAPER, qa)
    cv.text(540, 1220, "\u201cIt's lost focus.\u201d", 62, INK, qa, "Black")
    ln = eo(pr(t, 1.9, 2.4))
    cv.line([(220, 1222), (220 + 640 * ln, 1222)], CORAL, 8, qa)
    g = eback(pr(t, 3.0, 3.5), 2)
    chip(cv, 200, 1340, 680, "SO THEY BUILT A GAME", MUST, cl(g * 1.3), INK, 44, 96)
def s2(cv, t, D):
    kinetic(cv, t, 300, "THE GAME", 104, INKC, -.2, "Black", .03)
    # two striped circles: first, then the changed one
    ang1, per1 = .35, 34
    sw = eio(pr(t, 1.3, 2.3))
    ang2 = lerp(ang1, 1.0, sw); per2 = lerp(per1, 22, sw)
    qa = eo(pr(t, .2, .7))
    stripes(cv, 300, 640, 190, ang1, per1, qa)
    stripes(cv, 780, 640, 190, ang2, per2, eo(pr(t, .9, 1.4)))
    cv.text(300, 880, "FIRST", 34, PAPER, qa, "Black")
    cv.text(780, 880, "THEN", 34, PAPER, eo(pr(t, .9, 1.4)), "Black")
    cv.line([(500, 640), (580, 640)], MUST, 8, eo(pr(t, .9, 1.4)))
    cv.poly([(600, 640), (570, 618), (570, 662)], MUST, eo(pr(t, .9, 1.4)))
    # two things changed
    ra = eo(pr(t, 1.9, 2.4))
    chip(cv, 150, 950, 330, "TILT", TEAL, ra, INKC, 40, 84)
    chip(cv, 600, 950, 330, "SPACING", CORAL, ra, INKC, 40, 84)
    # only one counts: spotlight flips
    card(cv, 100, 1100, 980, 1400, 30, PAPER, eo(pr(t, 2.6, 3.0)))
    fa = eo(pr(t, 2.6, 3.0))
    cv.text(540, 1150, "THE RULE:  WHICH ONE COUNTS?", 30, INK, fa, "Black")
    flip = t > 4.3
    f2 = eback(pr(t, 4.3, 4.7), 2)
    cv.rrect(140, 1200, 520, 1340, 24, fill=TEAL if not flip else PAPER2, a=fa)
    cv.rrect(560, 1200, 940, 1340, 24, fill=PAPER2 if not flip else CORAL, a=fa)
    cv.text(330, 1270, "TILT", 52, INKC if not flip else DIM, fa, "Black")
    cv.text(750, 1270, "SPACING", 52, DIM if not flip else INKC, fa, "Black")
    if t > 3.4 and not flip:
        cv.text(540, 1375, "you're not told", 28, mix(INK, PAPER, .4), eo(pr(t, 3.4, 3.8)), "Bold")
    if flip:
        cv.text(540, 1375, "...and it flips without warning", 28, CORAL, f2, "Black")
def s3(cv, t, D):
    n = int(200 * eo(pr(t, .1, 1.6)))
    cv.text(540, 350, "%d+" % n, 150, INKC, 1, "Black")
    cv.text(540, 462, "PEOPLE, ONLINE", 44, MUST, eo(pr(t, .3, .8)), "Black")
    rs = random.Random(4)
    k = int(60 * eo(pr(t, .2, 1.8)))
    if t > 1.8: k = 60
    for i in range(60):
        if i >= k: break
        x = 135 + (i % 15) * 56; y = 545 + (i // 15) * 62
        icon_person(cv, x, y, 40, PAPER, 1)
    qm = eo(pr(t, 2.0, 2.6))
    photo(cv, "macaque", 110, 810, 970, 1290, t / D, 1.0, 1.25, .62, .45, qm)
    brackets(cv, 110, 810, 970, 1290, PAPER, qm * .9)
    credit(cv, "Rhesus macaque: Charles J. Sharp, CC BY-SA 4.0", 1322, qm)
    chip(cv, 140, 1350, 310, "2 MONKEYS", MUST, qm, INK, 38, 84)
    # spike trace card
    ta = eo(pr(t, 2.6, 3.0))
    cv.rrect(480, 1350, 940, 1434, 42, fill=PAPER, a=ta)
    pts = []
    for i in range(0, 41):
        x = 505 + i * 10.4
        ph = (x - 505) / 10.4 + t * 9
        y = 1392 + math.sin(ph * .9) * 8 + (-30 if (int(ph) % 11 == 0) else 0) * (1 if ta > .5 else 0)
        pts.append((x, y))
    cv.line(pts, CORAL, 4, ta)
def s4(cv, t, D):
    kinetic(cv, t, 300, "NOT RANDOM", 100, INKC, -.2, "Black", .03)
    # card 1: scatter noise
    a1 = eo(pr(t, .2, .6))
    card(cv, 70, 430, 1010, 900, 30, PAPER, a1)
    cv.text(120, 475, "IF IT WERE NOISE", 32, mix(TEAL, INK, .4), a1, "Black", "lm")
    rs = random.Random(11)
    for i in range(46):
        x = 130 + rs.random() * 820; y = 540 + rs.random() * 310
        s = eo(pr(t, .5 + i * .02, .8 + i * .02))
        cv.circ(x, y, 11 * s, fill=mix(TEAL, INK, .2), a=a1)
    # card 2: pattern emerges
    a2 = eo(pr(t, 2.5, 3.0))
    card(cv, 70, 960, 1010, 1430, 30, PAPER, a2)
    cv.text(120, 1005, "WHAT THEY SAW", 32, CORAL, a2, "Black", "lm")
    rs = random.Random(12)
    mv = eio(pr(t, 2.9, 3.9))
    for i in range(46):
        u = rs.random(); x0 = 130 + rs.random() * 820; y0 = 1070 + rs.random() * 310
        xt = 150 + u * 780; yt = 1370 - u * 270 + (rs.random() - .5) * 60
        x = lerp(x0, xt, mv); y = lerp(y0, yt, mv)
        cv.circ(x, y, 11, fill=CORAL, a=a2)
    if mv > .8:
        qq = eo(pr(t, 3.7, 4.1))
        cv.line([(150, 1370), (150 + 780 * qq, 1370 - 270 * qq)], INK, 5, .7)
def s5(cv, t, D):
    kinetic(cv, t, 300, "AFTER A MISS", 100, INKC, -.2, "Black", .03)
    cv.text(540, 405, "what people remembered", 38, MUST, eo(pr(t, .3, .8)), "SemiBold")
    card(cv, 70, 470, 1010, 1400, 30)
    qa = eo(pr(t, .2, .6))
    base = 1270
    cv.line([(130, base), (950, base)], mix(INK, PAPER, .3), 5, qa)
    # four bars: relevant after hit/miss (same), ignored after hit / miss (higher)
    bars = [("relevant", "after a hit", 330, TEAL, 1.0, .9), ("relevant", "after a miss", 460, TEAL, 1.0, .9),
            ("ignored", "after a hit", 640, CORAL, 1.6, .5), ("ignored", "after a miss", 770, CORAL, 2.2, 1.0)]
    hs = [280, 280, 180, 440]
    for i, (a, b, x, col, t0, _) in enumerate(bars):
        g = eo(pr(t, t0, t0 + .8))
        h = hs[i] * g
        cv.rrect(x - 50, base - h, x + 50, base, 10, fill=col if i != 2 else mix(col, PAPER, .45))
        cv.text(x, base + 34, a, 24, INK, g, "Black")
        cv.text(x, base + 62, b, 20, mix(INK, PAPER, .35), g, "Bold")
    pa = eo(pr(t, 2.4, 3.0))
    cv.text(540, 560, "the detail they should have ignored", 34, CORAL, pa, "Black")
    cv.text(540, 610, "stuck better", 54, INK, pa, "Black")
    cv.text(540, 1385, "schematic of the finding, not measured values", 20, mix(INK, PAPER, .45), eo(pr(t, 1.0, 1.5)), "SemiBold")
def s6(cv, t, D):
    kinetic(cv, t, 300, "IN THE MONKEYS", 90, INKC, -.2, "Black", .03)
    photo(cv, "neurons", 110, 430, 970, 880, t / D, 1.0, 1.25, .5, .4)
    brackets(cv, 110, 430, 970, 880, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Cortical neurons, stained: Ns takes photos, CC BY 4.0", 915, eo(pr(t, .6, 1.1)))
    qa = eo(pr(t, .9, 1.4))
    card(cv, 70, 960, 1010, 1420, 30, PAPER, qa)
    cv.text(540, 1005, "SIGNALS FOR TWO FEATURES", 28, INK, qa, "Black")
    mv = eio(pr(t, 1.6, 2.9))
    xa = lerp(360, 470, mv); xb = lerp(720, 610, mv)
    cv.circ(xa, 1200, 150, fill=TEAL, a=.62 * qa)
    cv.circ(xb, 1200, 150, fill=CORAL, a=.62 * qa)
    cv.circ(xa, 1200, 150, outline=INK, w=3, oa=.6 * qa); cv.circ(xb, 1200, 150, outline=INK, w=3, oa=.6 * qa)
    cv.text(xa - 60 - 20 * mv, 1200, "TILT", 38, INKC, qa, "Black")
    cv.text(xb + 60 + 10 * mv, 1200, "SPACING", 34, INKC, qa, "Black")
    ov = eo(pr(t, 2.6, 3.2))
    cv.text(540, 1200, "?", 70, INK, ov * .9, "Black")
    chip(cv, 260, 1355, 560, "THEY OVERLAP", INK, ov, INKC, 34, 62)
def s7(cv, t, D):
    kinetic(cv, t, 300, "CROSSTALK", 112, INKC, -.2, "Black", .03)
    photo(cv, "work", 130, 430, 950, 930, t / D, 1.0, 1.2, .45, .5)
    brackets(cv, 130, 430, 950, 930, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Working on a laptop: Shixart1985, CC BY 2.0", 962, eo(pr(t, .8, 1.3)))
    # NOT weak willpower, struck through
    wa = eo(pr(t, 3.0, 3.5))
    card(cv, 150, 1010, 930, 1130, 28, PAPER, wa)
    cv.text(540, 1070, "weak willpower", 56, INK, wa, "Black")
    ln = eo(pr(t, 3.6, 4.1))
    cv.line([(210, 1072), (210 + 660 * ln, 1072)], CORAL, 9, wa)
    # pause ring
    ra = eo(pr(t, 4.3, 4.8))
    cx, cy = 300, 1285
    cv.circ(cx, cy, 90, outline=PAPER2, w=14, oa=.35 * ra)
    prog = eio(pr(t, 4.5, 6.2))
    if prog > .01: cv.arc(cx, cy, 90, -90, -90 + 360 * prog, MUST, 14, ra)
    cv.text(cx, cy, "II", 60, PAPER, ra, "Black")
    cv.text(700, 1250, "A SHORT", 42, INKC, ra, "Black")
    cv.text(700, 1305, "PAUSE", 62, MUST, ra, "Black")
    cv.text(700, 1360, "between tasks", 32, ASH, ra, "SemiBold")
def s8(cv, t, D):
    rs = random.Random(21)
    for i in range(44):
        ang = i / 44 * 6.2832; u = rs.random()
        x0 = 140 + rs.random() * 800; y0 = 480 + rs.random() * 520
        xt = 540 + math.cos(ang) * 300; yt = 740 + math.sin(ang) * 300
        mv = eio(pr(t, .1, 1.8))
        cv.circ(lerp(x0, xt, mv), lerp(y0, yt, mv), 12, fill=mix(CORAL, MUST, u), a=.9)
    kinetic(cv, t, 740, "LATOON", 150, INKC, -.1, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, MUST, eo(pr(t, .9, 1.5)), "SemiBold")
    chip(cv, 280, 1110, 520, "FOLLOW", MUST, eo(pr(t, 1.6, 2.2)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
