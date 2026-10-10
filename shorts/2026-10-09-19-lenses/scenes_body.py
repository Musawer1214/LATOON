def credit(cv, t, txt="NSF NOIRLab · DESI Legacy Imaging Surveys"):
    cv.text(540, 1385, txt, 28, MUTE, eo(pr(t, .8, 1.4)), "SemiBold")
def s0(cv, t, D):
    kinetic(cv, t, 330, "70 NATURAL", 110, INKC, -.2, "Black", .03)
    kinetic(cv, t, 460, "TELESCOPES FOUND", 66, AMB, -.1, "Black", .02)
    p = eo(pr(t, .1, .8)); card(cv, 150, 580, 930, 1360, 34, a=p)
    kenburns(cv, "l1", 540, 970, 720, 720, 1.0 + .25 * pr(t, 0, D), 26, a=p)
    credit(cv, t)
def s1(cv, t, D):
    head(cv, t, "GRAVITATIONAL LENS", "a galaxy that bends light", AMB)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1330, 34, a=p)
    kenburns(cv, "info", 540, 945, 840, 472, 1.0 + .12 * pr(t, 0, D), 20, a=p, panx=-.3 + .6 * pr(t, 0, D))
    cv.text(540, 1230, "heavy galaxy = cosmic magnifying glass", 34, INKC, eo(pr(t, 1.6, 2.2)), "Bold")
def s2(cv, t, D):
    head(cv, t, "RINGS AND ARCS", "the same galaxy, smeared round", AMB)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1360, 34, a=p)
    kenburns(cv, "l2", 540, 960, 760, 760, 1.0 + .3 * pr(t, 0, D), 26, a=p)
    cx, cy = 540, 960
    q = eo(pr(t, 1.2, 2.4)); cv.arc(cx, cy, 150 * q + 10, 0, 360 * q, AMB, 4, .9 * q)
def s3(cv, t, D):
    head(cv, t, "4 BILLION OBJECTS", "too many to scroll by eye", ROSE)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1330, 34, a=p)
    kenburns(cv, "col", 540, 880, 840, 385, 1.0 + .15 * pr(t, 0, D), 20, a=p, panx=-.5 + pr(t, 0, D))
    n = int(3_900_000_000 * eo(pr(t, .8, 5.5)))
    cv.text(540, 1140, f"{n:,}".replace(",", " "), 84, AMB, eo(pr(t, .6, 1.2)), "Black")
    cv.text(540, 1240, "5.6-trillion-pixel sky map", 34, MUTE, eo(pr(t, 1.4, 2.0)), "Bold")
def s4(cv, t, D):
    head(cv, t, "A NEURAL NETWORK", "hunting for ring-shaped patterns", AMB)
    card(cv, 90, 560, 990, 1330, 34)
    rs = random.Random(5)
    g = 14; cell = 42; x0, y0 = 150, 660
    cx = x0 + g * cell / 2; cy = y0 + g * cell / 2
    for r in range(g):
        for c in range(g):
            d = math.hypot(c - g / 2 + .5, r - g / 2 + .5)
            ring = abs(d - 4.6) < .9
            q = eo(pr(t, .1 + (r + c) * .02, .5 + (r + c) * .02))
            col = mix(CARDC, AMB, .85) if ring and t > 2.0 else mix(CARDC, LINEC, .35 + rs.random() * .3)
            cv.rrect(x0 + c * cell + 2, y0 + r * cell + 2, x0 + (c + 1) * cell - 2, y0 + (r + 1) * cell - 2, 6, fill=col, a=q)
    sc = eo(pr(t, 2.4, 3.2))
    chip(cv, 770, 880, 190, "RING", COP, sc, INKC, 34)
    cv.line([(740, 920), (770, 920)], AMB, 4, sc)
    cv.text(540, 1290, "residual neural network", 34, MUTE, eo(pr(t, 1.0, 1.6)), "Bold")
def s5(cv, t, D):
    head(cv, t, "76 CANDIDATES", "a pattern isn't proof", ROSE)
    card(cv, 90, 560, 990, 1330, 34)
    for i in range(76):
        r, c = divmod(i, 12)
        x, y = 160 + c * 66, 700 + r * 78
        q = eback(pr(t, .1 + i * .02, .5 + i * .02), 2)
        cv.circ(x, y, 24 * q, fill=mix(CARDC, AMB, .6), outline=AMB, w=2, oa=cl(q))
    kinetic(cv, t, 1285, "STILL JUST GUESSES", 56, ROSE, 2.2, "Black", .03)
def s6(cv, t, D):
    head(cv, t, "VLT · MUSE", "measure both distances", AMB)
    card(cv, 90, 560, 990, 1330, 34)
    ys = [790, 1100]
    q = eo(pr(t, .3, 1.2))
    cv.circ(540, 940, 44 * q, fill=AMB, outline=INKC, w=3)
    cv.circ(540, 790 - 120, 24 * q, fill=COP, outline=INKC, w=3)
    cv.line([(540, 670), (540, lerp(670, 1180, eo(pr(t, 1.2, 2.4))))], mix(CARDC, AMB, .5), 4, .9)
    cv.text(540, 1230, "light from each galaxy, split into a spectrum", 30, MUTE, eo(pr(t, 1.8, 2.4)), "Bold")
    for i in range(24):
        x = 200 + i * 32
        h = 30 + 90 * abs(math.sin(i * .7 + 1))
        qq = eo(pr(t, 2.4 + i * .05, 3.0 + i * .05))
        cv.line([(x, 1160), (x, 1160 - h * qq)], [AMB, COP, SAGE, ROSE][i % 4], 10, .85)
def s7(cv, t, D):
    kinetic(cv, t, 480, "70", 360, AMB, -.2, "Black", .08)
    kinetic(cv, t, 760, "CONFIRMED", 90, INKC, .2, "Black", .03)
    q = eo(pr(t, .6, 1.4)); card(cv, 150, 900, 930, 1330, 34, a=q)
    kenburns(cv, "l1", 540, 1115, 740, 380, 1.1, 22, a=q, pany=-.3)
def s8(cv, t, D):
    head(cv, t, "WHY IT MATTERS", "magnify the early universe", AMB)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1330, 34, a=p)
    kenburns(cv, "info", 540, 940, 840, 472, 1.15, 20, a=p, panx=.4 - .8 * pr(t, 0, D))
    chip(cv, 190, 1190, 700, "DARK MATTER BENDS LIGHT TOO", COP, eo(pr(t, 2.2, 3.0)), INKC, 32)
def s9(cv, t, D):
    head(cv, t, "AI NARROWED THE SKY", "humans spend the telescope time", AMB)
    card(cv, 90, 560, 990, 1330, 34)
    cv.text(300, 760, "4 BILLION", 54, MUTE, eo(pr(t, .2, .8)), "Black")
    cv.text(780, 760, "76", 54, AMB, eo(pr(t, 1.6, 2.2)), "Black")
    cv.text(540, 760, "→", 54, INKC, eo(pr(t, 1.0, 1.6)), "Black")
    cv.text(780, 860, "→ 70", 70, SAGE, eo(pr(t, 3.0, 3.6)), "Black")
    kenburns(cv, "l2", 540, 1090, 600, 340, 1.4, 22, a=eo(pr(t, .4, 1.0)))
def s10(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, AMB, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
