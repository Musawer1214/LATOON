T_PIX = ["#####", "..#..", "..#..", "..#..", "..#.."]
def pixgrid(cv, x0, y0, cell, noise_p, seed, a=1, col=AMB, t_p=1.0):
    rs = random.Random(seed)
    for r in range(8):
        for c in range(8):
            on = (1 <= r <= 5 and 1 <= c <= 5 and T_PIX[r - 1][c - 1] == "#")
            flip = rs.random() < .42
            if flip and noise_p > 0.5: on = not on
            x, y = x0 + c * cell, y0 + r * cell
            cv.rrect(x + 3, y + 3, x + cell - 3, y + cell - 3, 8, fill=col if on else mix(CARDC, SHAD, .4), a=a, outline=LINEC, w=1, oa=.5 * a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "AI MEMORY", 110, INKC, -.2, "Black", .03)
    kinetic(cv, t, 460, "MADE OF ATOMS + LIGHT", 54, AMB, -.1, "Black", .02)
    p = eo(pr(t, .1, .8))
    card(cv, 110, 600, 970, 1260, 34, a=p)
    kenburns(cv, "atoms", 540, 930, 800, 600, 1.0 + .12 * pr(t, 0, D), 26, a=p)
    cv.text(540, 1330, "Stanford · Science · Oct 2026", 36, MUTE, eo(pr(t, 1.2, 1.8)), "Bold")
def s1(cv, t, D):
    head(cv, t, "HOPFIELD NETWORK", "switches that recall", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    rs = random.Random(3)
    pts = [(540 + 260 * math.cos(i * 2 * math.pi / 8 + .3), 940 + 260 * math.sin(i * 2 * math.pi / 8 + .3)) for i in range(8)]
    k = 0
    for i in range(8):
        for j in range(i + 1, 8):
            q = eo(pr(t, .4 + k * .04, .8 + k * .04)); k += 1
            cv.line([pts[i], (lerp(pts[i][0], pts[j][0], q), lerp(pts[i][1], pts[j][1], q))], LINEC, 2, .8)
    for i, (x, y) in enumerate(pts):
        q = eback(pr(t, .2 + i * .1, .6 + i * .1), 2)
        cv.circ(x + 4, y + 7, 34 * q, fill=SHAD, a=.5)
        cv.circ(x, y, 34 * q, fill=AMB if i % 3 else COP, outline=INKC, w=3, oa=cl(q))
    cv.text(540, 1260, "everything connected to everything", 34, MUTE, eo(pr(t, 2.4, 3.0)), "Bold")
def s2(cv, t, D):
    head(cv, t, "BLURRY IN, CLEAN OUT", "a smudged letter recalls itself", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    n = 1 - eio(pr(t, 1.8, 3.8))
    cell = 74
    pixgrid(cv, 540 - 4 * cell, 640, cell, n, 7)
    chip(cv, 250, 1260, 580, "NOBEL PRIZE IN PHYSICS 2024", COP, eo(pr(t, 4.4, 5.0)), INKC, 32)
def s3(cv, t, D):
    head(cv, t, "TOO MANY MEMORIES", "frustration = false patterns", ROSE)
    card(cv, 100, 560, 980, 1330, 34)
    rs = random.Random(9)
    for r in range(6):
        for c in range(6):
            x, y = 220 + c * 128, 660 + r * 96
            up = rs.random() < .5
            ang = (-1 if up else 1) * 1
            q = eback(pr(t, .2 + (r + c) * .06, .6 + (r + c) * .06), 2)
            col = ROSE if (r + c) % 3 == 0 else AMB
            cv.circ(x, y, 34 * q, fill=mix(CARDC, col, .35), outline=col, w=3, oa=cl(q))
            dy = 22 * (-1 if up else 1) * q
            cv.line([(x, y - dy), (x, y + dy)], col, 8, cl(q))
            cv.circ(x, y - dy, 9 * q, fill=INKC)
    q = eo(pr(t, 3.6, 4.4))
    kinetic(cv, t, 1295, "SPIN GLASS", 80, ROSE, 3.8, "Black", .04)
def s4(cv, t, D):
    head(cv, t, "STANFORD · LEV LAB", "cold atoms + an optical cavity", AMB)
    p = eo(pr(t, .1, .7))
    card(cv, 100, 560, 980, 1260, 34, a=p)
    kenburns(cv, "mot", 540, 910, 820, 560, 1.0 + .15 * pr(t, 0, D), 26, a=p, panx=-.3 + .5 * pr(t, 0, D))
    cv.text(540, 1330, "atoms trade photons back and forth", 38, INKC, eo(pr(t, 1.6, 2.2)), "Bold")
def s5(cv, t, D):
    head(cv, t, "FALSE → TRUE", "spurious patterns become memories", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    rs = random.Random(5)
    q = eio(pr(t, 1.2, 3.0))
    for i in range(14):
        x, y = 200 + rs.random() * 680, 650 + rs.random() * 560
        col = mix(ROSE, AMB, q)
        r = 22 + 12 * q
        cv.circ(x + 3, y + 6, r, fill=SHAD, a=.45 * eo(pr(t, i * .05, .4 + i * .05)))
        cv.circ(x, y, r * eback(pr(t, i * .05, .4 + i * .05), 2), fill=col, outline=INKC, w=3, oa=eo(pr(t, i * .05, .4 + i * .05)))
    cv.text(540, 1270, "reliable memories" if q > .5 else "spurious patterns", 40, AMB if q > .5 else ROSE, 1, "Black")
def s6(cv, t, D):
    head(cv, t, "UP TO 7× MORE", "than the classic Hopfield limit", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    q = eo(pr(t, .6, 2.4))
    cv.rrect(200, 1190, 440, 1250, 14, fill=mix(CARDC, MUTE, .5))
    cv.text(320, 1280, "Hopfield", 32, MUTE, 1, "Bold")
    h = 60 + (7 * 60 - 60) * q
    cv.rrect(600, 1250 - h, 840, 1250, 14, fill=COP)
    cv.text(720, 1280, "atoms + light", 32, AMB, 1, "Bold")
    kinetic(cv, t, 760, "7×", 150, AMB, 2.4, "Black", .1)
    cv.text(540, 1370, "16-spin network", 36, MUTE, eo(pr(t, 2.8, 3.4)), "Bold")
def s7(cv, t, D):
    head(cv, t, "ATOMS MOVE", "like synapses rewiring", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    for i in range(6):
        a = i * math.pi / 3
        bx, by = 540 + 250 * math.cos(a), 920 + 250 * math.sin(a)
        mv = .5 + .5 * math.sin(t * 2.2 + i)
        x, y = bx + 28 * mv * math.cos(a), by + 28 * mv * math.sin(a)
        cv.line([(540, 920), (x, y)], COP, 3 + int(5 * mv), .9)
        cv.circ(x + 3, y + 6, 36, fill=SHAD, a=.5)
        cv.circ(x, y, 36, fill=AMB, outline=INKC, w=3)
    cv.circ(540, 920, 46, fill=COP, outline=INKC, w=3)
    kinetic(cv, t, 1260, "2× MEMORY", 80, AMB, 2.6, "Black", .04)
def s8(cv, t, D):
    head(cv, t, "A PROTOTYPE", "not a product, but a hint", AMB)
    p = eo(pr(t, .1, .7))
    card(cv, 110, 560, 970, 1280, 34, a=p)
    kenburns(cv, "stan", 540, 920, 820, 620, 1.0 + .1 * pr(t, 0, D), 26, a=p, panx=.2 - .4 * pr(t, 0, D))
    cv.text(540, 1360, "memory that runs on physics itself", 38, INKC, eo(pr(t, 2.4, 3.0)), "Bold")
def s9(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, AMB, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
