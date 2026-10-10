
def s0(cv, t, D):
    kinetic(cv, t, 300, "A HAND THAT", 110, INKC, -.2, "Black", .03)
    kinetic(cv, t, 430, "WALKS", 150, YEL, -.1, "Black", .03)
    p = eo(pr(t, .0, .6))
    img(cv, "full", 540, 1000, 1.0 + .03 * pr(t, 0, 3.5), p)
    chip(cv, 250, 1380, 580, "NO ARM ATTACHED", RED, eo(pr(t, 1.6, 2.2)), INKC, 38)
def s1(cv, t, D):
    head(cv, t, "THE BACKPACK", "80 grams, three parts", YEL)
    img(cv, "small", 540, 880, 1.0, eo(pr(t, .0, .5)))
    xs = [(100, 300), (410, 270), (700, 280)]
    # three compact chips side by side
    pos = [(70, 1270, 300, "BATTERY", YEL), (390, 1270, 300, "MOTION SENSOR", TEA), (710, 1270, 300, "PI ZERO", RED)]
    for i, (x, y, w, lab, c) in enumerate(pos):
        q = eo(pr(t, 1.2 + i * 1.3, 1.8 + i * 1.3))
        chip(cv, x, y + (1 - q) * 80, w, lab, c, q, INK if c != RED else INKC, 28, 80)
def s2(cv, t, D):
    head(cv, t, "BUILT TO GRASP", "not to walk", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    lens = [("thumb", 250, TEA), ("index", 420, YEL), ("middle", 480, RED), ("ring", 440, GRN), ("pinky", 330, PLM)]
    for i, (n, L, c) in enumerate(lens):
        q = eback(pr(t, .2 + i * .25, .8 + i * .25), 1.4)
        x = 215 + i * 150
        base = 1230
        cv.rrect(x - 48, base - L * q, x + 48, base, 44, fill=mix(c, (0, 0, 0), .3))
        cv.rrect(x - 42, base - L * q + 4, x + 38, base - 8, 40, fill=c)
        cv.rrect(x - 26, base - L * q + 16, x - 8, base - L * q + 70, 8, fill=mix(c, WHT, .4), a=.7)
        cv.text(x, base + 40, n, 26, INK, q, "Bold")
    chip(cv, 220, 640, 640, "UNEVEN FINGERS + A THUMB", RED, eo(pr(t, 1.8, 2.4)), INKC, 32)
def s3(cv, t, D):
    head(cv, t, "TRIAL AND ERROR", "in simulation first", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    rs = random.Random(8)
    n = 60
    pts = []
    for i in range(n + 1):
        x = 170 + i * (740 / n)
        y = 1260 - (1 - math.exp(-i / 22)) * 560 + math.sin(i * 1.7) * 28 + rs.uniform(-34, 34) * (1 - i / n * .7)
        pts.append((x, y))
    k = int(len(pts) * eo(pr(t, .2, 4.0)))
    cv.line([(170, 1290), (930, 1290)], mix(PAPER, INK, .5), 4)
    cv.line([(170, 640), (170, 1290)], mix(PAPER, INK, .5), 4)
    if k > 1: cv.line(pts[:k], TEA, 8)
    if k > 0: cv.circ(pts[k - 1][0], pts[k - 1][1], 16, fill=RED)
    cv.text(540, 620, "REWARD", 30, INK, 1, "Black")
    cv.text(540, 1335, "attempts  >", 30, INK, 1, "Bold")
    cv.text(780, 1180, "+ reward for moving well", 28, INK, eo(pr(t, 1.5, 2.2)), "Bold")
def s4(cv, t, D):
    head(cv, t, "VIRTUAL SPRINGS", "each finger has a home", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cv.rrect(250, 640, 830, 800, 30, fill=mix(INK, PAPER, .15))
    cv.text(540, 720, "PALM", 40, PAPER, 1, "Black")
    rs = random.Random(2)
    for i in range(5):
        hx = 230 + i * 155; hy = 1180
        pull = eo(pr(t, 1.5, 3.2))
        dx = math.sin(t * 5 + i * 2) * 70 * (1 - pull) + (i - 2) * 30 * (1 - pull)
        dy = math.cos(t * 4 + i) * 50 * (1 - pull)
        fx, fy = hx + dx, hy + dy
        sx = 540 + (i - 2) * 105
        n = 14
        zz = [(sx, 800)]
        for j in range(1, n):
            q = j / n
            zz.append((lerp(sx, fx, q) + (14 if j % 2 else -14), lerp(800, fy - 40, q)))
        zz.append((fx, fy - 40))
        cv.line(zz, mix(PAPER, INK, .45), 4)
        cv.circ(hx, hy, 14, fill=None, outline=GRN, w=4)
        cv.circ(fx, fy, 34, fill=mix(YEL, (0, 0, 0), .3)); cv.circ(fx - 2, fy - 3, 30, fill=YEL)
    chip(cv, 200, 1290, 680, "DRIFTING AWAY COSTS POINTS", RED, eo(pr(t, 2.4, 3.0)), INKC, 30, 66)
def s5(cv, t, D):
    head(cv, t, "REAL HARDWARE", "14 surfaces, one hand", YEL)
    img(cv, "small", 540, 880, .96, eo(pr(t, .0, .5)))
    names = ["GRASS", "GRAVEL", "METAL GRATE"]
    for i, (nm, c) in enumerate(zip(names, (GRN, MUTE, TEA))):
        q = eo(pr(t, .9 + i * .9, 1.4 + i * .9))
        chip(cv, 70 + i * 320, 1270 + (1 - q) * 80, 300, nm, c, q, INK, 28, 80)
    cv.text(540, 1440, "14 surfaces tested", 36, YEL, eo(pr(t, 3.6, 4.2)), "Black")
def s6(cv, t, D):
    kinetic(cv, t, 470, "RIGHTED ITSELF", 100, INKC, 0, "Black", .03)
    card(cv, 100, 620, 980, 1380, 34)
    for i in range(25):
        r_, c_ = divmod(i, 5)
        x, y = 240 + c_ * 150, 740 + r_ * 120
        q = eback(pr(t, .3 + i * .05, .7 + i * .05), 1.6)
        ok = i < 21
        col = GRN if ok else RED
        cv.circ(x, y, 42 * q, fill=mix(col, (0, 0, 0), .3)); cv.circ(x - 1, y - 2, 38 * q, fill=col)
    n = int(21 * eo(pr(t, .3, 1.8)))
    cv.text(540, 1330, f"{n} / 25 tries", 56, INK, 1, "Black")
def s7(cv, t, D):
    head(cv, t, "NOT STUCK IN ONE JOB", "", YEL)
    img(cv, "big", 540, 960, .9, eo(pr(t, .0, .5)))
    chip(cv, 140, 1360, 800, "DETACH AND EXPLORE TIGHT SPACES", YEL, eo(pr(t, 1.8, 2.4)), INK, 30, 70)
def s8(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, YEL, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
