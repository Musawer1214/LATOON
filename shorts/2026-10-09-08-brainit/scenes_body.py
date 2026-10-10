def vox_slice(cv, cx, cy, rx, ry, t, reveal=1.0, cell=30, a=1):
    cv.circ(cx, cy, 1, fill=INKC, a=0)
    cv.rrect(cx - rx - 14, cy - ry - 14, cx + rx + 14, cy + ry + 14, min(rx, ry) * .9, fill=PAPER, a=a, outline=INKC, w=5, oa=a)
    nx, ny = int(rx * 2 / cell), int(ry * 2 / cell)
    x0 = cx - nx * cell / 2; y0 = cy - ny * cell / 2; k = 0
    for j in range(ny):
        for i in range(nx):
            u = (i + .5) / nx * 2 - 1; v = (j + .5) / ny * 2 - 1
            if u * u + v * v > 1: continue
            k += 1
            v_ = .5 + .5 * math.sin(i * 1.1 + j * .6 + t * 2.0) * math.cos(j * .9 - i * .3 + t * 1.3)
            q = eback(pr(reveal, (i + j) / (nx + ny) * .8, (i + j) / (nx + ny) * .8 + .2), 2)
            col = mix((236, 226, 196), TERRA, v_) if v_ < .6 else mix(TERRA, AMB, (v_ - .6) / .4)
            s = cell * .86 * cl(q)
            cv.rrect(x0 + i * cell + (cell - s) / 2, y0 + j * cell + (cell - s) / 2, x0 + i * cell + (cell + s) / 2, y0 + j * cell + (cell + s) / 2, 5, fill=col, a=a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "AN AI REDRAWS", 90, INKC, -.2, "Black", .02)
    kinetic(cv, t, 440, "WHAT YOU SEE", 90, TERRA, -.1, "Black", .02)
    p = eback(pr(t, .1, .7), 2)
    pcard(cv, "p0", 290, 880, 400, cl(p))
    cv.text(290, 1120, "WHAT THEY SAW", 36, INKC, cl(p), "Black")
    arrow(cv, 540, 880, cl(eo(pr(t, .7, 1.1))))
    lvl = eio(pr(t, 1.0, 3.2))
    q = eo(pr(t, .8, 1.2))
    pcard(cv, None, 790, 880, 400, cl(q), src=pix(IM["p1"], lvl) if lvl < 1 else IM["p1"])
    cv.text(790, 1120, "DRAWN FROM THE SCAN", 36, TERRA, cl(q), "Black")
    chip(cv, 300, 1230, 480, "BRAIN-IT · NEW STUDY", FOR, eo(pr(t, 2.2, 2.8)), size=34, h=76)
def s1(cv, t, D):
    head(cv, t, "MEET BRAIN-IT", "Michal Irani's lab · Weizmann Institute")
    p = eback(pr(t, .2, .8), 2)
    zoom = 1.0 + .12 * pr(t, 0, D)
    cv.rrect(80 + 8, 560 + 12, 1000 + 8, 1180 + 12, 30, fill=SHAD, a=.55 * cl(p))
    kenburns(cv, "wz", 540, 870, 920, 620, zoom, 30, cl(p), panx=0.1 * pr(t, 0, D))
    cv.rrect(80, 560, 1000, 1180, 30, outline=EDGE, w=4, oa=cl(p))
    cv.text(540, 1230, "Photo: Hoshvilim, CC BY-SA 4.0", 28, EDGE, eo(pr(t, 1.0, 1.5)), "SemiBold")
    chip(cv, 380, 1290, 320, "ICLR 2026", FOR, eo(pr(t, 1.5, 2.1)))
def s2(cv, t, D):
    head(cv, t, "INSIDE AN fMRI SCANNER", "thousands of photos, one brain")
    p = eback(pr(t, .2, .8), 2)
    cv.rrect(70 + 8, 520 + 12, 460 + 8, 1040 + 12, 26, fill=SHAD, a=.55 * cl(p))
    kenburns(cv, "mri", 265, 780, 390, 520, 1.0 + .1 * pr(t, 0, D), 26, cl(p), pany=-.3 + .4 * pr(t, 0, D))
    cv.rrect(70, 520, 460, 1040, 26, outline=EDGE, w=4, oa=cl(p))
    cv.text(265, 1075, "Photo: NIH/NINDS, public domain", 24, EDGE, cl(p), "SemiBold")
    q = eo(pr(t, 1.2, 1.8))
    if q > .02: vox_slice(cv, 760, 780, 190, 250, t, pr(t, 2.0, 4.6), 30, cl(q))
    cv.text(760, 1100, "VOXELS · 1.8 mm cubes", 32, INKC, eo(pr(t, 3.0, 3.6)), "Black")
    n = int(9000 * eo(pr(t, 3.8, 5.8)))
    cv.text(540, 1230, f"{n:,}+", 120, TERRA, eo(pr(t, 3.6, 4.0)), "Black")
    cv.text(540, 1330, "photos per person, over a year", 40, INKC, eo(pr(t, 4.2, 4.8)), "Bold")
def s3(cv, t, D):
    head(cv, t, "IT NEVER SEES A PICTURE", "only blood oxygen")
    card(cv, 90, 500, 990, 1300, 36)
    a_ = eo(pr(t, .3, .8))
    pcard(cv, "p0", 230, 650, 150, a_)
    cv.line([(150, 570), (310, 730)], TERRA, 12, a_); cv.line([(310, 570), (150, 730)], TERRA, 12, a_)
    cv.text(640, 620, "no picture reaches", 42, INKC, a_, "Black"); cv.text(640, 680, "the scanner's output", 42, INKC, a_, "Black")
    cv.text(540, 830, "BLOOD-OXYGEN SIGNAL", 34, SLATE, eo(pr(t, .8, 1.3)), "Black")
    base = 1110; amp = 250; x0, x1 = 160, 920
    cv.line([(x0, base), (x1, base)], EDGE, 5, eo(pr(t, .8, 1.3)))
    pts = []
    for i in range(61):
        u = i / 60
        y = math.exp(-((u - .32) / .13) ** 2) - .32 * math.exp(-((u - .66) / .17) ** 2)
        pts.append((x0 + u * (x1 - x0), base - y * amp))
    n = int(2 + 59 * eo(pr(t, 1.0, 3.6)))
    cv.line(pts[:n], TERRA, 11, 1)
    cv.circ(pts[n - 1][0], pts[n - 1][1], 15, fill=AMB, outline=INKC, w=4)
    cv.text(540, 1252, "oxygen use rises and falls", 32, INKC, eo(pr(t, 2.8, 3.4)), "Bold")
def s4(cv, t, D):
    head(cv, t, "THE AI MAKES TWO GUESSES", None)
    a_ = eback(pr(t, .2, .8), 2)
    card(cv, 60, 680, 300, 920, 28, a=cl(a_))
    vox_slice(cv, 180, 800, 78, 78, t, 1, 26, cl(a_) * .0 + cl(a_)) if False else None
    for j in range(5):
        for i in range(5):
            v_ = .5 + .5 * math.sin(i * 1.4 + j * .8 + t * 2)
            cv.rrect(98 + i * 26, 718 + j * 26, 98 + i * 26 + 22, 718 + j * 26 + 22, 4, fill=mix((236, 226, 196), TERRA, v_), a=cl(a_))
    cv.text(180, 960, "SCAN", 32, INKC, cl(a_), "Black")
    b1 = eio(pr(t, .9, 1.5)); b2 = eio(pr(t, 2.3, 2.9))
    cv.line([(300, 790), (360, 790), (360, 560)], INKC, 7, b1); cv.line([(360, 560), (360 + 30 * b1, 560)], INKC, 7, b1)
    cv.line([(300, 810), (360, 810), (360, 1010)], INKC, 7, b2); cv.line([(360, 1010), (360 + 30 * b2, 1010)], INKC, 7, b2)
    q = eback(pr(t, 1.3, 1.9), 2)
    card(cv, 400, 440, 1010, 700, 30, a=cl(q))
    cv.text(705, 500, "WHAT is in it?", 44, FOR, cl(q), "Black")
    for k, (w_, lab) in enumerate([(150, "house"), (130, "hills"), (110, "sun")]):
        chip(cv, 430 + [0, 170, 320][k], 560, w_ + 20, lab, FOR, eo(pr(t, 1.8 + k * .3, 2.3 + k * .3)) * cl(q), size=30, h=64)
    r = eback(pr(t, 2.8, 3.4), 2)
    card(cv, 400, 880, 1010, 1180, 30, a=cl(r))
    cv.text(705, 935, "WHERE, in what colors?", 44, TERRA, cl(r), "Black")
    pcard(cv, None, 560, 1060, 160, cl(r), src=pix(IM["p0"], 0.0))
    cv.text(820, 1040, "coarse layout", 34, INKC, cl(r), "Bold"); cv.text(820, 1090, "and outlines", 34, INKC, cl(r), "Bold")
    kinetic(cv, t, 1300, "TWO CLUES", 78, INKC, 4.2, "Black", .03)
def s5(cv, t, D):
    head(cv, t, "A DIFFUSION MODEL PAINTS IT", "noise removed, step by step")
    a_ = eback(pr(t, .2, .8), 2)
    chip(cv, 110, 500, 300, "WHAT", FOR, cl(a_)); chip(cv, 670, 500, 300, "WHERE", TERRA, cl(a_))
    lvl = eio(pr(t, 1.0, 4.4))
    src = Image.blend(IM["noise"], IM["p1"], lvl)
    src = pix(src, min(1, .15 + lvl * 1.0)) if lvl < .98 else src
    for xx in (260, 820):
        ps = (t * 1.6) % 1
        cv.line([(xx, 600 + 20 * ps), (xx + (540 - xx) * .25, 650 + 20 * ps)], INKC, 6, .5 * a_)
    pcard(cv, None, 540, 930, 520, cl(eo(pr(t, .4, 1.0))), src=src)
    cv.text(540, 1260, "static  →  a picture", 52, INKC, eo(pr(t, 2.4, 3.0)), "Black")
def s6(cv, t, D):
    head(cv, t, "ONE HOUR, NOT FORTY", "similar quality for a new person")
    card(cv, 70, 520, 1010, 1260, 36)
    cv.text(110, 600, "OLDER METHODS", 36, SLATE, 1, "Black", anchor="lm")
    cv.text(110, 650, "trained on 40 h per person", 32, INKC, 1, "Bold", anchor="lm")
    w1 = 860 * eio(pr(t, .5, 2.0))
    cv.rrect(110, 700, 110 + w1, 790, 16, fill=SLATE)
    cv.text(110, 890, "BRAIN-IT", 36, TERRA, eo(pr(t, 2.0, 2.4)), "Black", anchor="lm")
    cv.text(110, 940, "new person, ~1 h of scanning", 32, INKC, eo(pr(t, 2.0, 2.4)), "Bold", anchor="lm")
    w2 = max(14, 860 / 40 * eio(pr(t, 2.4, 3.2)))
    cv.rrect(110, 990, 110 + w2, 1080, 12, fill=TERRA, a=eo(pr(t, 2.2, 2.6)))
    cv.text(110 + w2 + 30, 1035, "1 h", 54, TERRA, eo(pr(t, 3.0, 3.5)), "Black", anchor="lm")
    cv.text(540, 1180, "reported as comparable results", 32, EDGE, eo(pr(t, 3.4, 3.9)), "SemiBold")
def s7(cv, t, D):
    head(cv, t, "IT STILL SLIPS", None)
    a_ = eback(pr(t, .2, .8), 2); b_ = eback(pr(t, 1.6, 2.2), 2)
    pcard(cv, "dog", 285, 760, 410, cl(a_)); cv.text(285, 1000, "SAW: dog in a bathtub", 32, INKC, cl(a_), "Black")
    arrow(cv, 540, 760, cl(eo(pr(t, 1.2, 1.6))))
    pcard(cv, "goat", 795, 760, 410, cl(b_)); cv.text(795, 1000, "DREW: a goat", 32, TERRA, cl(b_), "Black")
    c1 = eback(pr(t, 3.4, 4.0), 2); c2 = eback(pr(t, 4.4, 5.0), 2)
    chip(cv, 110, 1100, 860, "WORKS: pictures people saw", FOR, cl(c1), size=38, h=84)
    chip(cv, 110, 1220, 860, "NOT YET: dreams or thoughts", TERRA, cl(c2), size=38, h=84)
def s8(cv, t, D):
    kinetic(cv, t, 400, "WHO GETS TO", 84, INKC, .0, "Black", .03)
    kinetic(cv, t, 500, "READ A BRAIN?", 84, TERRA, .2, "Black", .03)
    cx, cy = 540, 960
    for k in range(3):
        u = (t * .35 + k / 3) % 1
        cv.circ(cx, cy, 150 + u * 260, outline=TERRA, w=4, oa=(1 - u) * .45)
    op = 1 - eio(pr(t, 1.0, 1.8))
    sh = 70 * op
    cv.arc(cx, cy - 120 - sh * .0, 100, -90 - 90, 90 + (0), INKC, 26, 1) if False else None
    cv.line([(cx - 100, cy - 80), (cx - 100, cy - 190 - sh * .6), (cx - 60, cy - 245 - sh * .6), (cx + 60, cy - 245 - sh * .6), (cx + 100, cy - 190 - sh * .6), (cx + 100, cy - 80 - sh * (1 if op > .5 else 0))], INKC, 28, 1)
    cv.rrect(cx - 170 + 8, cy - 90 + 12, cx + 170 + 8, cy + 170 + 12, 40, fill=SHAD, a=.6)
    cv.rrect(cx - 170, cy - 90, cx + 170, cy + 170, 40, fill=AMB, outline=INKC, w=6)
    cv.circ(cx, cy + 20, 32, fill=INKC); cv.rrect(cx - 12, cy + 30, cx + 12, cy + 110, 8, fill=INKC)
    cv.text(540, 1250, "mental privacy", 56, FOR, eo(pr(t, 1.8, 2.4)), "Black")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=TERRA, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=TERRA, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
