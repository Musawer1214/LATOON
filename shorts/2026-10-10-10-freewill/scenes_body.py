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
