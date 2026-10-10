
# ---- S0 hook
def s0(cv, t, D):
    chip(cv, 540, 290, "NEW BRAIN-SCAN STUDY  ·  OCT 5", 28, INK, ORG, 1)
    kinetic(cv, t, 420, "THE GOOGLE", 130, WHT, -.3, "Black", .02)
    kinetic(cv, t, 560, "EFFECT", 130, ORG2, -.2, "Black", .02)
    p = eo(pr(t, .1, .6))
    z = lerp(1.0, 1.25, eo(pr(t, 0, 2.3)))
    cardimg(cv, "goog", 540, 960, 920, 420, 800, 440, z, p)
    # typing caret + brain pulse
    cv.text(540, 1230, "now scanned in the brain", 42, CREAM, eo(pr(t, .7, 1.2)), "Bold")
    q = eback(pr(t, .9, 1.5), 2)
    brain(cv, 540, 1345, 120 * q, ORG2, cl(q), t)

# ---- S1 UCL / journal
def s1(cv, t, D):
    chip(cv, 540, 300, "UCL  ·  QUEEN SQUARE, LONDON", 28, INK, ICE, eo(pr(t, 0, .3)))
    kinetic(cv, t, 400, "PUBLISHED", 100, WHT, 0, "Black", .03)
    u = eio(pr(t, .1, 4.8))
    cardimg(cv, "ucl", 540, 800, 920, 560, lerp(1150, 1500, u), lerp(1000, 900, u), lerp(1.0, 1.35, u), eo(pr(t, .15, .5)))
    credit(cv, 1100, "photo: Montano336, CC BY-SA 3.0 (Wikimedia Commons)", eo(pr(t, .4, .8)))
    chip(cv, 540, 1190, "SCIENTIFIC REPORTS", 38, INK, AMB, eback(pr(t, 1.3, 1.8), 2))
    chip(cv, 540, 1290, "5 OCTOBER 2026", 38, INK, ORG, eback(pr(t, 2.2, 2.7), 2))
    cv.text(540, 1375, "Institute of Cognitive Neuroscience", 30, ORG2, eo(pr(t, 3.0, 3.5)), "SemiBold")

# ---- S2 scanner
def s2(cv, t, D):
    cv.text(540, 320, "INSIDE AN fMRI SCANNER", 54, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "faces and scenes on screen", 36, ICE, eo(pr(t, .3, .7)), "SemiBold")
    u = eio(pr(t, .1, 4.5))
    cardimg(cv, "mri", 540, 760, 920, 520, lerp(2000, 3000, u), 1500, lerp(1.0, 1.25, u), eo(pr(t, .1, .5)))
    credit(cv, 1045, "photo: GeorgeWilliams21, CC BY-SA 4.0 (Wikimedia Commons)", eo(pr(t, .4, .8)))
    # face and scene cards flipping
    for k, (lab, c) in enumerate([("FACES", ORG), ("SCENES", AMB)]):
        q = eback(pr(t, 1.2 + k * .5, 1.8 + k * .5), 2)
        x0 = 120 + k * 450
        cv.rrect(x0, 1100, x0 + 400, 1340, 34, fill=CARDC, a=q, outline=c, w=4, oa=q)
        if k == 0:
            icon_person(cv, x0 + 200, 1190, 90, c, q)
        else:
            cv.circ(x0 + 290, 1155, 24, fill=c, a=q)
            cv.poly([(x0 + 60, 1275), (x0 + 160, 1165), (x0 + 240, 1235), (x0 + 300, 1190), (x0 + 340, 1275)], c, q * .9)
        cv.text(x0 + 200, 1312, lab, 34, CREAM, q, "Black")

# ---- S3 three cues
CUES = [("REMEMBER", "memory test coming", ICE, 0.3), ("FORGET", "no test at all", PUR, 1.55), ("SAVE", "a reminder will be provided", ORG, 2.75)]
def s3(cv, t, D):
    cv.text(540, 320, "THREE CUES", 62, WHT, eo(pr(t, .05, .4)), "Black")
    for i, (a_, b_, c, s_) in enumerate(CUES):
        p = eback(pr(t, s_, s_ + .5), 1.6)
        y = 440 + i * 300
        x = lerp(1200, 0, cl(p))
        cv.rrect(90 + x, y, 990 + x, y + 250, 40, fill=CARDC, a=1, outline=c, w=5)
        cv.text(380 + x, y + 95, a_, 72, c, 1, "Black", anchor="lm")
        cv.text(380 + x, y + 170, b_, 34, MUT, 1, "Medium", anchor="lm")
        cx_, cy_ = 220 + x, y + 125
        cv.circ(cx_, cy_, 70, fill=mix(CARDC, c, .22), a=1, outline=c, w=4)
        if i == 0:
            check(cv, cx_, cy_, 60, pr(t, s_ + .3, s_ + .7), c, 10)
        elif i == 1:
            q = pr(t, s_ + .3, s_ + .7)
            cv.line([(cx_ - 28, cy_ - 28), (cx_ - 28 + 56 * q, cy_ - 28 + 56 * q)], c, 10)
            cv.line([(cx_ + 28, cy_ - 28), (cx_ + 28 - 56 * q, cy_ - 28 + 56 * q)], c, 10)
        else:
            cv.rrect(cx_ - 30, cy_ - 38, cx_ + 30, cy_ + 38, 10, outline=c, w=7)
            for k in range(3):
                q = pr(t, s_ + .3 + k * .12, s_ + .5 + k * .12)
                cv.line([(cx_ - 16, cy_ - 18 + k * 18), (cx_ - 16 + 32 * q, cy_ - 18 + k * 18)], c, 6)

# ---- S4 save ~ forget
def s4(cv, t, D):
    cv.text(540, 320, "SAVE  ≈  FORGET", 70, WHT, eo(pr(t, .05, .45)), "Black")
    cv.text(540, 388, "brain activity closely resembled", 36, ICE, eo(pr(t, .3, .7)), "SemiBold")
    for k, (lab, c, fy) in enumerate([("FORGET CUE", PUR, 150), ("SAVE CUE", ORG, 150)]):
        p = eback(pr(t, .3 + k * .35, .85 + k * .35), 1.8)
        cx = 285 + k * 510
        s = 1 + .02 * math.sin(t * 4 + k)
        cardimg(cv, "fmri", cx, 800, 420 * p, 420 * p, 320, 320, 1.0, cl(p), 36, c)
        cv.text(cx, 1060, lab, 40, c, cl(p), "Black")
    q = eback(pr(t, 1.2, 1.7), 2.5)
    cv.circ(540, 800, 56 * q, fill=INK, a=1, outline=AMB, w=5)
    cv.text(540, 800, "≈", 80, AMB, cl(q), "Black")
    chip(cv, 540, 1200, "SIMILAR BRAIN ACTIVITY", 38, INK, AMB, eback(pr(t, 2.0, 2.5), 2))
    credit(cv, 1300, "illustration: fMRI maps, finger-tapping (Wikimedia, public domain). Not the study's data.", eo(pr(t, 2.2, 2.7)))

# ---- chart helper
CX0, CX1, CY0, CY1 = 150, 930, 520, 1120
def chart_axes(cv, a, lab="neural trace of the picture"):
    cv.line([(CX0, CY0), (CX0, CY1), (CX1, CY1)], MUT, 4, a)
    cv.text(CX0, CY0 - 40, lab, 30, MUT, a, "SemiBold", anchor="lm")
    cv.text(CX1, CY1 + 40, "time →", 26, MUT, a, "Medium", anchor="rm")
    cv.text(CX0 - 14, CY1 - 4, "0", 24, MUT, a, "Medium", anchor="rm")

def rem_curve(u):  return 520 + 0 * u + 40 * (1 - math.exp(-u * 3)) * -1 + 40 * u if False else CY0 + 70 + 25 * math.sin(u * 3)
def dec_curve(u):  return CY0 + 70 + (CY1 - CY0 - 70 - 12) * (1 - math.exp(-u * 3.2)) / (1 - math.exp(-3.2))
def curve(cv, fn, p, col, w=12, a=1):
    n = 40; pts = [(CX0 + (CX1 - CX0) * i / n, fn(i / n)) for i in range(int(n * p) + 1)]
    cv.line(pts, col, w, a)
    if pts: cv.circ(pts[-1][0], pts[-1][1], 16, fill=WHT, a=a)

def s5(cv, t, D):
    cv.text(540, 320, "WHEN THEY HAD TO REMEMBER", 46, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 380, "the neural trace persisted", 40, ICE, eo(pr(t, .3, .7)), "SemiBold")
    chart_axes(cv, eo(pr(t, 0, .4)))
    p = eio(pr(t, .4, 2.2))
    curve(cv, rem_curve, p, ICE, 14)
    cv.text(CX1 - 20, CY0 + 20, "REMEMBER", 34, ICE, eo(pr(t, 1.2, 1.7)), "Black", anchor="rm")
    chip(cv, 540, 1260, "STILL THERE", 46, INK, ICE, eback(pr(t, 2.2, 2.7), 2))
    cv.text(540, 1345, "schematic of the paper's finding, not raw data", 24, MUT, .85 * eo(pr(t, 2.6, 3.0)), "Medium")

def s6(cv, t, D):
    cv.text(540, 320, "AFTER SAVE OR FORGET", 54, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 380, "it faded until statistically gone", 38, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    chart_axes(cv, 1)
    curve(cv, rem_curve, 1, ICE, 14, .9)
    cv.text(CX1 - 20, CY0 + 20, "REMEMBER", 34, ICE, 1, "Black", anchor="rm")
    p = eio(pr(t, .3, 2.4))
    curve(cv, dec_curve, p, ORG, 14)
    curve(cv, lambda u: dec_curve(u) - 6, p, PUR, 8)
    cv.text(CX0 + 40, CY1 - 60, "SAVE = FORGET", 34, ORG2, eo(pr(t, 1.8, 2.3)), "Black", anchor="lm")
    q = eback(pr(t, 2.5, 3.0), 2)
    chip(cv, 540, 1260, "STATISTICALLY ABSENT", 42, INK, ORG, q)
    cv.text(540, 1345, "schematic of the paper's finding, not raw data", 24, MUT, .85 * eo(pr(t, 2.8, 3.2)), "Medium")

# ---- S7 adaptive
def s7(cv, t, D):
    cv.text(540, 320, "MAYBE IT'S A FEATURE", 56, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "the authors' suggestion", 36, ICE, eo(pr(t, .3, .7)), "SemiBold")
    # phone card (left) -> brain slots (right)
    p = eback(pr(t, .3, .9), 1.8)
    cardimg(cv, "phone", 300, 760, 400 * p, 520 * p, 900, 480, 1.0, cl(p), 36, AMB)
    credit(cv, 1060, "phone photo: Dennis Cortés, CC0", eo(pr(t, .6, 1))); 
    cv.text(300, 1110, "stored outside", 34, AMB, eo(pr(t, 1.0, 1.5)), "Black")
    # brain slot grid
    cv.rrect(560, 500, 1000, 1020, 40, fill=CARDC, a=eo(pr(t, .5, .9)), outline=ORG, w=4, oa=eo(pr(t, .5, .9)))
    cv.text(780, 545, "LIMITED CAPACITY", 28, ORG2, eo(pr(t, .8, 1.2)), "Black")
    n = 0
    for r_ in range(4):
        for c_ in range(3):
            x = 620 + c_ * 130; y = 600 + r_ * 100
            keep = (r_, c_) in [(0, 1), (1, 0), (2, 2), (3, 1)]
            q = eo(pr(t, 1.2 + n * .08, 1.5 + n * .08)); n += 1
            col = AMB if keep else DIM
            pulse = (.5 + .5 * math.sin(t * 4 + n)) if keep else 0
            cv.rrect(x, y, x + 110, y + 80, 18, fill=mix(CARDC, col, .6 + .3 * pulse if keep else .5), a=q)
            if keep: star(cv, x + 55, y + 40, 24, INK, q)
    dotted(cv, (420, 1180), (700, 1180), t, 6, AMB, eo(pr(t, 2.0, 2.4)), 7, .5)
    chip(cv, 540, 1290, "SPACE FOR WHAT MATTERS", 40, INK, AMB, eback(pr(t, 2.6, 3.1), 2))

# ---- S8 outro
def s8(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(5):
        u = (t * .35 + k / 5) % 1
        cv.circ(540, 700, 60 + u * 330, outline=ORG, w=4, oa=(1 - u) * .7 * p)
    brain(cv, 540, 700, 300 * p, ORG2, p, t)
    kinetic(cv, t, 1090, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1200, "Voyaging the Unseen", 46, AMB, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1290, "save it, and your brain may let go.", 32, ORG2, eo(pr(t, 1.8, 2.3)), "Medium")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
