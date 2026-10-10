def s0(cv, t, D):
    kinetic(cv, t, 300, "SO BRIGHT.", 104, INKC, -.2, "Black", .03)
    kinetic(cv, t, 420, "SO HARD TO CATCH.", 84, YEL, .1, "Black", .03)
    zoom = 1.0 + .09 * pr(t, 0, D)
    kb(cv, "fly", 540, 980, 900, 900, zoom, 34, 1, fx=.49 + .012 * t, fy=.52)
    # reticle lagging behind the butterfly
    p = pr(t, 2.9, 4.6)
    bx, by = 560 + 10 * math.sin(t * 3), 960 + 12 * math.cos(t * 2.4)
    rx = bx - 20 - 270 * eo(p); ry = by + 20 + 60 * eo(p)
    q = eo(pr(t, 2.6, 3.2))
    if q > 0:
        cv.circ(rx, ry, 74, outline=RED, w=7, oa=q)
        cv.line([(rx - 104, ry), (rx - 46, ry)], RED, 7, q); cv.line([(rx + 46, ry), (rx + 104, ry)], RED, 7, q)
        cv.line([(rx, ry - 104), (rx, ry - 46)], RED, 7, q); cv.line([(rx, ry + 46), (rx, ry + 104)], RED, 7, q)
    chip(cv, 380, 1290, 320, "MISSED", RED, eo(pr(t, 4.2, 4.7)), PAPER, 40, 78)
def s1(cv, t, D):
    head(cv, t, "NOT DECORATION", "a trick played on motion", YEL)
    kb(cv, "scarce", 540, 940, 900, 820, 1.0 + .12 * pr(t, 0, D), 34, 1, fx=.57, fy=.5)
    # sweeping bars imply stripes in motion
    for k in range(7):
        x = 150 + k * 130 + ((t * 120) % 130) - 130 * 0
        cv.line([(x, 560), (x - 90, 1320)], INKC, 5, .18 * eo(pr(t, .3, .8)))
    chip(cv, 140, 1250, 330, "NATURE · 2026", PAPER, eo(pr(t, .6, 1.1)), INK, 32, 66)
    chip(cv, 500, 1250, 440, "EXETER + ESSEX", YEL, eo(pr(t, 1.0, 1.5)), INK, 32, 66)
def s2(cv, t, D):
    head(cv, t, "MOTION DAZZLE", "an old idea, thin proof", YEL)
    kb(cv, "zebra", 540, 940, 900, 820, 1.0 + .1 * pr(t, 0, D), 34, 1, fx=.35, fy=.52)
    q = eo(pr(t, 1.5, 2.1))
    cv.rrect(250, 1210, 830, 1310, 24, fill=SHAD, a=.6 * q)
    cv.rrect(240, 1196, 820, 1296, 24, fill=PAPER, a=q)
    cv.text(530, 1246, "PROOF: THIN", 56, RED, q, "Black")
def s3(cv, t, D):
    head(cv, t, "1,000 FRAMES / SECOND", "real wings vs blank wings", YEL)
    n = int(1000 * eo(pr(t, .2, 2.2)))
    card(cv, 100, 470, 980, 880, 30)
    flap(cv, "pr", 540, 725, 560, t, 3.0)
    cv.text(190, 520, "REAL PATTERN", 30, mix(INK, PAPER, .25), 1, "Black", anchor="lm")
    cv.text(890, 520, "%04d fps" % n, 30, RED, eo(pr(t, .3, .8)), "Black", anchor="rm")
    q = eo(pr(t, 3.1, 3.8))
    card(cv, 100, 910, 980, 1320, 30, a=q)
    flap(cv, "pb", 540, 1165, 560, t, 3.0, a=q)
    cv.text(190, 960, "DIGITAL COPY, BLANK WINGS", 30, mix(INK, PAPER, .25), q, "Black", anchor="lm")
def stripes(cv, x0, y0, x1, y1, t, direction, col=INK, a=1):
    cv.done()
    w, h = int(x1 - x0), int(y1 - y0)
    im = Image.new("RGBA", (w, h), PAPER2 + (255,)); d = ImageDraw.Draw(im)
    per = 70; off = (t * 160 * direction) % per
    for k in range(-6, int(h / per) + 8):
        yy = k * per + off - 40
        d.polygon([(0, yy), (w, yy - 180), (w, yy - 180 + 34), (0, yy + 34)], fill=col + (255,))
    img(cv, None, (x0 + x1) / 2, (y0 + y1) / 2, 1, a, _rounded(im, 26))
def s4(cv, t, D):
    head(cv, t, "FALSE SIGNALS", "flapping wings + bold stripes", YEL)
    card(cv, 100, 470, 980, 1380, 34)
    cv.text(320, 540, "REALITY", 34, mix(INK, PAPER, .25), 1, "Black")
    cv.text(760, 540, "PREDATOR'S VIEW", 34, mix(INK, PAPER, .25), 1, "Black")
    cv.line([(540, 520), (540, 1330)], mix(PAPER, INK, .3), 3, .6)
    yb = 1160 - 360 * eo(pr(t, .3, 3.6))
    flap(cv, "pr", 320, yb, 340, t, 3.4)
    arrow_v(cv, 320, 1290, 700, YEL, 16, eo(pr(t, .6, 1.2)))
    cv.text(320, 640, "UP", 64, YEL, eo(pr(t, .9, 1.4)), "Black")
    q = eo(pr(t, 3.4, 4.0))
    stripes(cv, 600, 600, 920, 1050, t, 1, a=1)
    cv.text(760, 640, "?", 5, INK, 0)
    arrow_v(cv, 760, 1090, 1290, RED, 16, q)
    cv.text(760, 1345 - 0, "DOWN", 64, RED, q, "Black")
def s5(cv, t, D):
    head(cv, t, "397 SPECIES", "757 wing types simulated", YEL)
    card(cv, 100, 470, 980, 1380, 34)
    p = pr(t, .1, 1.8)
    cnt = 0
    for r in range(10):
        for c in range(40):
            i = r * 40 + c
            if i >= 397: break
            x, y = 150 + c * 20.5, 530 + r * 21
            on = i < p * 397
            hot = (i * 7919) % 5 == 0 and pr(t, 3.0, 3.6) > 0
            cv.circ(x, y, 7, fill=(YEL if hot and on else (GRN if on else mix(PAPER2, INK, .15))), a=1)
    rows = [("bold forewing contrast", "io", .5, .45, 2.5), ("vertical hindwing stripes", "scarce", .55, .45, 3.7), ("hindwing tails", "scarce", .3, .78, 4.9)]
    for k, (lab, key, fx, fy, t0) in enumerate(rows):
        y = 880 + k * 160; q = eo(pr(t, t0 - .2, t0 + .4))
        if q <= 0: continue
        kb(cv, key, 260, y, 240, 130, 2.4 if k != 0 else 2.0, 20, q, fx=fx if k else .22, fy=fy if k else .35, shadow=False)
        cv.text(410, y - 18, lab, 36, INK, q, "Black", anchor="lm")
        cv.text(410, y + 28, "adds the most confusion" if k == 0 else "more motion confusion", 26, mix(INK, PAPER, .35), q, "SemiBold", anchor="lm")
WING = [(0, -.30), (.35, -.62), (.98, -.78), (1.02, -.25), (.62, .02), (.92, .42), (.55, .78), (.12, .42), (0, .36)]
def mini_wing(cv, cx, cy, s, c, seed, a=1):
    w, h = int(2.2 * s * 1.1), int(1.7 * s * 1.1)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); m = Image.new("L", (w, h), 0); md = ImageDraw.Draw(m)
    ox, oy = w / 2, h * .46
    pts = [(ox + x * s, oy + y * s) for x, y in WING] + [(ox - x * s, oy + y * s) for x, y in reversed(WING)]
    md.polygon(pts, fill=255)
    base = mix(PAPER2, TEA, .45 * (1 - c)); tile = Image.new("RGBA", (w, h), base + (255,)); d = ImageDraw.Draw(tile)
    rr = random.Random(seed)
    for k in range(9):
        x, y, r = rr.uniform(.1, .9) * w, rr.uniform(.1, .9) * h, rr.uniform(.08, .2) * s * 2
        cc = mix(base, rr.choice([BRN, GRN, YEL, PLM]), .5 * (1 - c))
        d.ellipse((x - r, y - r, x + r, y + r), fill=cc + (255,))
    nb = 3 + seed % 3
    for k in range(nb):
        xx = ox + (k - (nb - 1) / 2) * s * .42
        wd = (.03 + .06 * c) * s
        d.polygon([(xx - wd, 0), (xx + wd, 0), (xx + wd * .6, h), (xx - wd * .6, h)], fill=mix(base, INK, .25 + .75 * c) + (int(255 * c),))
    im.paste(tile, (0, 0), m)
    ImageDraw.Draw(im).line(pts + [pts[0]], fill=INK + (200,), width=2)
    ImageDraw.Draw(im).rounded_rectangle((ox - 4, oy - .55 * s, ox + 4, oy + .7 * s), 3, fill=INK + (255,))
    img(cv, None, cx, cy, 1, a, im)
def s6(cv, t, D):
    head(cv, t, "57,600 PATTERNS", "bred for maximum confusion", YEL)
    card(cv, 100, 470, 980, 1380, 34)
    g = pr(t, .3, 3.7)
    for r in range(5):
        for c in range(4):
            seed = r * 4 + c + 3
            cx, cy = 200 + c * 227, 600 + r * 150
            ct = cl(g * 1.15 - (r + c) * .02 + .05 * (seed % 3))
            q = eo(pr(t, .1 + (r * 4 + c) * .03, .4 + (r * 4 + c) * .03))
            mini_wing(cv, cx, cy, 58, ct, seed, q)
    cnt = int(57600 * eo(pr(t, .2, 3.6)))
    q = eo(pr(t, 3.8, 4.4))
    cv.text(540, 1332, "{:,} designs tested".format(cnt), 34, RED, 1 - q, "Black")
    chip(cv, 200, 1290, 680, "→ bold, butterfly-like", YEL, q, INK, 36, 70)
def s7(cv, t, D):
    head(cv, t, "100 VOLUNTEERS", "tap the virtual butterfly", YEL)
    cv.rrect(250 + 8, 480 + 14, 830 + 8, 1390 + 14, 60, fill=SHAD, a=.55)
    cv.rrect(250, 480, 830, 1390, 60, fill=(24, 24, 22))
    cv.rrect(268, 504, 812, 1366, 40, fill=mix(PAPER, TEA, .25))
    # butterfly path left->right-up
    u = pr(t, .2, 5.0)
    def pos(u): return 330 + 400 * u, 1250 - 600 * u + 40 * math.sin(u * 9)
    for tt, lab in ((.8, 0), (1.9, 1), (3.0, 2), (4.1, 3)):
        uu = pr(tt, .2, 5.0); px, py = pos(uu - .13)
        q = eo(pr(t, tt, tt + .3))
        if q > 0:
            cv.circ(px, py, 26 + 24 * (1 - q), outline=RED, w=6, oa=q * .9)
            cv.circ(px, py, 8, fill=RED, a=q)
    bx, by = pos(u)
    flap(cv, "pr", bx, by, 230, t, 3.2)
    cv.text(540, 560, "3,000 trials", 34, INK, eo(pr(t, 1, 1.5)), "Black")
    q = eo(pr(t, 3.5, 4.2))
    chip(cv, 300, 1270, 480, "AIMED BEHIND", RED, q, PAPER, 40, 80)
def s8(cv, t, D):
    kinetic(cv, t, 330, "THE FLASH THAT", 76, INKC, 0, "Black", .03)
    kinetic(cv, t, 430, "GIVES IT AWAY", 100, YEL, .15, "Black", .03)
    kinetic(cv, t, 560, "MAY SAVE IT", 76, INKC, .8, "Black", .03)
    flap(cv, "pr", 540, 840 + 14 * math.sin(t * 2), 640, t, 1.6, eo(pr(t, .2, .8)), lo=.55)
    kinetic(cv, t, 1120, "LATOON", 130, INKC, 4.0, "Black", .05)
    cv.text(540, 1245, "Voyaging the unseen", 48, YEL, eo(pr(t, 5.0, 5.6)), "SemiBold")
    chip(cv, 280, 1310, 520, "FOLLOW", YEL, eo(pr(t, 5.6, 6.2)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
