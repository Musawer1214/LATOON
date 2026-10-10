ASH = (176, 162, 146)
def credit(cv, txt, y, a=1):
    cv.text(540, y, txt, 24, ASH, a, "SemiBold")
def tile(cv, x, y, w, h, num, sym, name, fill, tc, a=1):
    card(cv, x, y, x + w, y + h, 22, fill, a)
    cv.text(x + 24, y + 34, str(num), 30, tc, a, "Bold", "lm")
    cv.text(x + w / 2, y + h / 2 + 6, sym, 104, tc, a, "Black")
    cv.text(x + w / 2, y + h - 34, name, 26, tc, a, "Bold")
def s0(cv, t, D):
    kinetic(cv, t, 300, "A STAR DIED.", 108, INKC, -.2, "Black", .03)
    kinetic(cv, t, 430, "A PLANET WAS BORN?", 66, COP, .45, "Black", .02)
    photo(cv, "a", 90, 560, 990, 1230, t / D, 1.0, 1.3, .62, .5)
    brackets(cv, 90, 560, 990, 1230, PAPER, eo(pr(t, .4, .9)) * .9)
    credit(cv, "Artist's concept: NASA, ESA, L. Hustak (STScI)", 1275, eo(pr(t, .8, 1.3)))
    chip(cv, 190, 1330, 700, "NATURE ASTRONOMY \u00b7 OCT 5, 2026", PAPER, eo(pr(t, 1.6, 2.1)), INK, 30, 74)
def s1(cv, t, D):
    head(cv, t, "HS 0209+0832", "a white dwarf: a star's dead core", COP)
    photo(cv, "q3", 100, 540, 980, 1090, t / D, 1.0, 1.2, .5, .5)
    brackets(cv, 100, 540, 980, 1090, PAPER, eo(pr(t, .3, .8)) * .9)
    p = eo(pr(t, .5, 2.6))
    cv.text(540, 1220, "%d" % round(270 * p), 180, INKC, eo(pr(t, .3, .7)), "Black")
    cv.text(540, 1352, "LIGHT-YEARS AWAY", 50, COP, eo(pr(t, 1.2, 1.8)), "Black")
def s2(cv, t, D):
    head(cv, t, "HUBBLE, 1999", "a spectrum nobody could read", COP)
    photo(cv, "hst", 250, 520, 830, 955, t / D, 1.0, 1.12, .5, .5)
    brackets(cv, 250, 520, 830, 955, PAPER, eo(pr(t, .2, .7)) * .9)
    card(cv, 80, 1010, 1000, 1400, 30)
    cv.rrect(120, 1050, 960, 1210, 14, fill=INK)
    rs = random.Random(11)
    n = 100
    for i in range(n):
        x = 126 + rs.random() * 828
        h = 40 + rs.random() * 100
        t0 = 1.0 + (i / n) * 2.6
        q = eo(pr(t, t0, t0 + .15))
        if q > 0:
            col = RED if i % 7 == 0 else mix(PAPER, INK, .15)
            cv.line([(x, 1130 - h / 2 * q), (x, 1130 + h / 2 * q)], col, 3, .95)
    cnt = int(n * eo(pr(t, 1.0, 3.6)))
    cv.text(120, 1300, "~%d" % cnt, 84, RED, eo(pr(t, .9, 1.3)), "Black", "lm")
    cv.text(380, 1288, "spectral lines", 38, INK, eo(pr(t, 1.2, 1.7)), "Black", "lm")
    cv.text(380, 1336, "no one could identify", 34, INK, eo(pr(t, 1.2, 1.7)), "SemiBold", "lm")
def s3(cv, t, D):
    head(cv, t, "RECHECKED, 2026", "against an updated chemical database", COP)
    photo(cv, "spec", 80, 540, 1000, 940, 0, 1.0, 1.0, .5, .5)
    q = eo(pr(t, 1.0, 1.5)); pulse = .75 + .25 * math.sin(t * 7)
    cv.rrect(300, 548, 382, 934, 12, outline=RED, w=6, oa=q * pulse)
    chip(cv, 150, 1050, 780, "Nb  \u00b7  NIOBIUM", RED, eo(pr(t, 1.3, 1.9)), INKC, 70, 130)
    cv.text(540, 1270, "never reported in a white dwarf before", 38, INKC, eo(pr(t, 2.3, 2.9)), "Bold")
    credit(cv, "Hubble spectrum: NASA, ESA, L. Hustak (STScI)", 1360, eo(pr(t, 1.0, 1.5)))
def s4(cv, t, D):
    head(cv, t, "HEAVIER THAN IRON", "made inside dying stars", COP)
    els = [(26, "Fe", "IRON", PAPER2, INK, 2.5), (29, "Cu", "COPPER", RED, INKC, 1.5), (30, "Zn", "ZINC", RED, INKC, .9), (41, "Nb", "NIOBIUM", COP, INK, .1)]
    for i, (num, sym, nm, fill, tc, t0) in enumerate(els):
        q = eback(pr(t, t0, t0 + .45), 2)
        dy = (1 - eo(pr(t, t0, t0 + .45))) * 60
        tile(cv, 92 + i * 238, 540 + dy, 218, 280, num, sym, nm, fill, tc, cl(q * 1.3))
    card(cv, 80, 880, 1000, 1410, 30)
    cv.text(540, 935, "ATOMIC NUMBER", 28, mix(INK, PAPER, .4), eo(pr(t, .3, .7)), "Bold")
    X = lambda n: 130 + (n - 24) * 45.5
    qa = eo(pr(t, .4, 1.0))
    cv.line([(110, 1130), (970, 1130)], mix(INK, PAPER, .3), 5, qa)
    xs = X(26)
    sh = eo(pr(t, 2.6, 3.4))
    cv.rrect(xs, 1040, xs + (960 - xs) * sh, 1130, 10, fill=RED, a=.22)
    cv.line([(xs, 1000), (xs, 1170)], INK, 5, eo(pr(t, 2.4, 2.9)))
    cv.text(xs, 1200, "IRON", 28, INK, eo(pr(t, 2.4, 2.9)), "Black")
    for num, sym, nm, fill, tc, t0 in [els[3], els[2], els[1]]:
        q = eback(pr(t, t0 + .3, t0 + .7), 2)
        x = X(num); up = (sym != "Zn")
        cv.circ(x, 1130, 17 * cl(q, 0, 1.2), fill=RED if sym != "Nb" else COP)
        cv.text(x, 1130 - 52 if up else 1130 + 52, sym, 34, INK, cl(q * 1.4), "Black")
    cv.text(540, 1330, "built in dying stars", 54, RED, eo(pr(t, 3.6, 4.2)), "Black")
def elchip(cv, x, y, sym, name, col, tc, a=1, dead=False):
    cv.rrect(x, y + 6, x + 190, y + 166, 24, fill=SHAD, a=.5 * a)
    cv.rrect(x, y, x + 190, y + 160, 24, fill=col, a=a)
    cv.text(x + 95, y + 70, sym, 80, tc, a, "Black")
    cv.text(x + 95, y + 132, name, 24, tc, a, "Bold")
    if dead:
        q = a
        cross(cv, x + 95, y + 80, 60, RED, q, 10)
def s5(cv, t, D):
    head(cv, t, "ROCK, OR ASHES?", None)
    card(cv, 80, 500, 1000, 900, 30)
    cv.text(540, 548, "A PLANET BORN WITH ITS STAR", 34, INK, eo(pr(t, .1, .6)), "Black")
    elchip(cv, 250, 600, "Si", "SILICON", INK, PAPER, eback(pr(t, 1.3, 1.8), 2) * 1.0)
    elchip(cv, 640, 600, "Fe", "IRON", INK, PAPER, eback(pr(t, 2.0, 2.5), 2) * 1.0)
    cv.text(540, 868, "rocky: lots of both", 30, mix(INK, PAPER, .35), eo(pr(t, 2.4, 2.9)), "Bold")
    qc = eo(pr(t, 3.0, 3.4))
    card(cv, 80, 950, 1000, 1400, 30, PAPER, qc)
    cv.text(540, 998, "THIS MATERIAL", 34, INK, qc, "Black")
    for i, (s, nm, dead, col, tc) in enumerate([("Si", "SILICON", True, PAPER2, mix(INK, PAPER, .5)), ("Fe", "IRON", True, PAPER2, mix(INK, PAPER, .5))]):
        elchip(cv, 100 + i * 205, 1050, s, nm, col, tc, qc, False)
        qx = eo(pr(t, 3.5, 3.8))
        if qx > .01: cross(cv, 195 + i * 205, 1115, 42 * qx, RED, qx, 9)
    for i, (s, nm, col, tc) in enumerate([("Nb", "NIOBIUM", COP, INK)]):
        q = eback(pr(t, 3.9, 4.4), 2)
        elchip(cv, 700, 1050, s, nm, col, tc, cl(q * 1.3))
    cv.text(540, 1300, "almost none", 40, RED, eo(pr(t, 3.5, 4.0)), "Black")
    cv.text(540, 1352, "rich in zinc, copper, niobium instead", 28, mix(INK, PAPER, .35), eo(pr(t, 4.0, 4.5)), "Bold")
def s6(cv, t, D):
    head(cv, t, "FROM THE ASHES", "the team's explanation", COP)
    spec = [("q1", "SUN-LIKE STAR", 0.0), ("q2", "RED GIANT", .5), ("q3", "WHITE DWARF + DISK", 2.2), ("q4", "NEW PLANET?", 3.6)]
    for i, (k, lab, t0) in enumerate(spec):
        x0 = 80 + (i % 2) * 500; y0 = 520 + (i // 2) * 420
        q = eo(pr(t, t0, t0 + .5))
        if q <= .01: continue
        dy = (1 - q) * 40
        photo(cv, k, x0, y0 + dy, x0 + 420, y0 + 330 + dy, (t - t0) / 3.0, 1.0, 1.15, .5 if i < 3 else .3, .5, q, 22)
        cv.rrect(x0 + 14, y0 + 14 + dy, x0 + 66, y0 + 66 + dy, 26, fill=RED, a=q)
        cv.text(x0 + 40, y0 + 40 + dy, str(i + 1), 34, INKC, q, "Black")
        cv.text(x0 + 210, y0 + 362 + dy, lab, 30, INKC if i < 3 else COP, q, "Black")
    credit(cv, "Artist's concepts, not to scale: NASA, ESA, L. Hustak (STScI)", 1385, eo(pr(t, 1.0, 1.5)))
def s7(cv, t, D):
    head(cv, t, "NASA'S TESS", None)
    photo(cv, "tess", 140, 440, 940, 820, t / D, 1.0, 1.18, .5, .5)
    brackets(cv, 140, 440, 940, 820, PAPER, eo(pr(t, .2, .7)) * .9)
    chip(cv, 330, 758, 420, "JUPITER-SIZED?", RED, eo(pr(t, 4.0, 4.5)), INKC, 34, 70)
    card(cv, 80, 850, 1000, 1150, 28)
    cv.text(120, 886, "BRIGHTNESS OVER TIME", 24, mix(INK, PAPER, .4), eo(pr(t, .3, .8)), "Bold", "lm")
    cv.line([(110, 1070), (970, 1070)], mix(INK, PAPER, .3), 3, eo(pr(t, .3, .8)))
    pw = eo(pr(t, .6, 3.0))
    pts = []
    for x in range(130, int(130 + 820 * pw), 6):
        pts.append((x, 990 - 52 * math.sin((x - 130) / 410.0 * 2 * math.pi + math.pi / 2 * 0) * 1.0))
    # peak positions at x=130+102.5 and 130+512.5
    if len(pts) > 2: cv.line(pts, RED, 7, 1)
    qb = eo(pr(t, 2.4, 3.0))
    xa, xb = 130 + 102.5, 130 + 512.5
    cv.line([(xa, 925), (xb, 925)], INK, 4, qb)
    cv.line([(xa, 913), (xa, 937)], INK, 4, qb); cv.line([(xb, 913), (xb, 937)], INK, 4, qb)
    cv.text((xa + xb) / 2, 1122, "every 4.4 days", 34, INK, qb, "Black")
    qo = eo(pr(t, 5.0, 5.6))
    if qo > .01:
        card(cv, 80, 1180, 1000, 1430, 28, PAPER, qo)
        cv.text(120, 1215, "DISTANCE TO THE STAR", 24, mix(INK, PAPER, .4), qo, "Bold", "lm")
        cv.text(110, 1285, "Mercury \u2192 Sun", 28, INK, qo, "Bold", "lm")
        cv.text(110, 1365, "This planet \u2192 star", 28, INK, qo, "Bold", "lm")
        p1 = eo(pr(t, 5.3, 6.6)); p2 = eo(pr(t, 6.4, 6.9))
        cv.rrect(410, 1265, 410 + 540 * p1, 1305, 12, fill=mix(INK, PAPER, .45), a=qo)
        cv.rrect(410, 1345, 410 + 56 * p2, 1385, 12, fill=RED, a=qo * p2)
        cv.text(940, 1245, "about 58 million km", 24, mix(INK, PAPER, .35), qo * p1, "Bold", "rm")
        cv.text(490, 1365, "~6 million km", 26, RED, qo * p2, "Black", "lm")
def s8(cv, t, D):
    head(cv, t, "A STRIPPED WORLD", None)
    fx = lerp(.88, .04, eio(pr(t, 1.6, 4.2)))
    photo(cv, "a", 90, 450, 990, 1050, 0, 1.3, 1.3, fx, .5)
    brackets(cv, 90, 450, 990, 1050, PAPER, .9)
    card(cv, 80, 1090, 1000, 1420, 28)
    cv.text(540, 1128, "AIR LOST \u2192 FALLS ON THE STAR \u2192 HUBBLE", 26, mix(INK, PAPER, .4), eo(pr(t, .3, .8)), "Bold")
    qa = eo(pr(t, .2, .7))
    cv.circ(220, 1260, 58, fill=mix(INK, PAPER, .1), a=qa)
    cv.circ(220, 1260, 58, outline=RED, w=7, oa=qa)
    cv.circ(780, 1260, 24, fill=PAPER2, a=qa); cv.circ(780, 1260, 24, outline=INK, w=3, oa=qa)
    cv.text(220, 1345, "planet?", 26, INK, qa, "Bold"); cv.text(780, 1345, "white dwarf", 26, INK, qa, "Bold")
    qs = eo(pr(t, .9, 1.4))
    for i in range(16):
        ph = (t * .45 + i / 16.0) % 1.0
        x = lerp(285, 750, ph); y = 1260 - math.sin(ph * math.pi) * 48 + math.sin(i * 2.1) * 10
        cv.circ(x, y, 7 * (1 - .4 * ph), fill=mix(RED, COP, ph), a=qs * (1 if ph < .92 else (1 - ph) * 12))
    qh = eback(pr(t, 4.0, 4.5), 2)
    q = eo(pr(t, 4.0, 4.5))
    cv.rrect(640, 1160, 960, 1214, 27, fill=RED, a=q)
    cv.text(800, 1187, "HUBBLE READS IT", 26, INKC, q, "Black")
def s9(cv, t, D):
    a1 = 1 - eio(pr(t, 2.1, 2.5))
    if a1 > .02:
        card(cv, 150, 520, 930, 960, 44, PAPER, a1)
        cv.rrect(176, 546, 904, 934, 32, outline=RED, w=5, oa=a1 * .8)
        cv.text(540, 690, "STILL ONLY A", 66, INK, a1 * eo(pr(t, .1, .5)), "Black")
        cv.text(540, 810, "CANDIDATE", 112, RED, a1 * eo(pr(t, .3, .9)), "Black")
        cv.text(540, 1040, "more Hubble and Chandra data ahead", 34, INKC, a1 * eo(pr(t, 1.0, 1.5)), "Bold")
    a2 = eo(pr(t, 2.4, 2.9)) * (1 - eio(pr(t, 4.5, 4.9)))
    if a2 > .02:
        kinetic(cv, t, 320, "OUR OWN SUN?", 84, INKC, 2.4, "Black", .03)
        photo(cv, "sun", 290, 520, 790, 1020, (t - 2.4) / 2.5, 1.0, 1.12, .5, .5, a2, 250)
        credit(cv, "The Sun: NASA/SDO (AIA)", 1070, a2)
        cv.text(540, 1190, "could its ashes do this too?", 46, COP, a2 * eo(pr(t, 3.1, 3.7)), "Black")
    kinetic(cv, t, 740, "LATOON", 150, INKC, 5.0, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, COP, eo(pr(t, 5.8, 6.4)), "SemiBold")
    chip(cv, 280, 990, 520, "FOLLOW", COP, eo(pr(t, 6.5, 7.1)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
