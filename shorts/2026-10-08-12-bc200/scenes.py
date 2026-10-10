# BC200 jumping gene: sand paper, deep ink, teal + coral + ochre
BG0, BG1 = (238, 226, 204), (222, 207, 180)
INKC = (28, 38, 36); WHT = INKC
TEAL, CORAL, OCH, PLUM = (31, 106, 102), (206, 82, 58), (214, 154, 46), (104, 64, 90)
PAPER, EDGE, SHAD = (251, 246, 234), (146, 128, 102), (188, 170, 142)
GOLD = CORAL; BL, BL2 = CORAL, CORAL
NOFADE_IN, NOFADE_OUT = {0}, set()
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (238, 226, 204), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, outline=EDGE, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.55 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 66, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or CORAL, eo(pr(t, .3, .7)), "SemiBold")
def helix(cv, y, x0, x1, t, amp=70, k=.03, hl=None, a=1, ph=0):
    # hl = (xa, xb) highlighted coral segment
    n = int((x1 - x0) / 6)
    A = []; B = []
    for i in range(n + 1):
        x = x0 + i * 6; s = math.sin(x * k + ph + t * 1.2)
        A.append((x, y + amp * s)); B.append((x, y - amp * s))
    for i in range(0, n + 1, 3):
        x = A[i][0]
        inh = hl and hl[0] <= x <= hl[1]
        c = [TEAL, OCH, PLUM, TEAL][(i // 3) % 4]
        cv.line([A[i], B[i]], CORAL if inh else c, 4, .75 * a)
    cv.line(A, CORAL if False else INKC, 8, a); cv.line(B, INKC, 8, a)
    if hl:
        sa = [p for p in A if hl[0] <= p[0] <= hl[1]]; sb = [p for p in B if hl[0] <= p[0] <= hl[1]]
        if len(sa) > 1: cv.line(sa, CORAL, 10, a); cv.line(sb, CORAL, 10, a)
def neuron(cv, cx, cy, s, t, a=1):
    for k in range(7):
        ang = k * math.pi * 2 / 7 + .3
        x1, y1 = cx + math.cos(ang) * 230 * s, cy + math.sin(ang) * 230 * s
        mx, my = cx + math.cos(ang + .25) * 130 * s, cy + math.sin(ang + .25) * 130 * s
        f = eo(pr(t, .1 + k * .06, .7 + k * .06))
        cv.line([(cx, cy), (mx, my), (cx + (x1 - cx) * f, cy + (y1 - cy) * f)], TEAL, 14 * s, a * .9)
        if f > .8:
            for d in (-.5, .5):
                cv.line([(x1, y1), (x1 + math.cos(ang + d) * 60 * s, y1 + math.sin(ang + d) * 60 * s)], TEAL, 7 * s, a * .8)
    cv.circ(cx, cy, 90 * s, fill=TEAL, a=a, outline=INKC, w=5, oa=a)
    cv.circ(cx - 14 * s, cy - 14 * s, 36 * s, fill=(60, 140, 134), a=a * .8)
    cv.circ(cx + 10 * s, cy + 6 * s, 30 * s, fill=CORAL, a=a)
def seg(cv, x, y, w=150, h=44, a=1, lab=None):
    card(cv, x - w / 2, y - h / 2, x + w / 2, y + h / 2, h / 2, fill=CORAL, outline=INKC, a=a)
    if lab: cv.text(x, y - 2, lab, 28, PAPER, a, "Black")
def hop(p0, p1, u, hgt=260):
    return (lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u) - hgt * math.sin(math.pi * u))
def s0(cv, t, D):
    kinetic(cv, t, 330, "YOUR NEURONS", 100, INKC, -.2, "Black", .02)
    kinetic(cv, t, 450, "USE A GENE THAT", 66, TEAL, .1, "Black", .02)
    kinetic(cv, t, 540, "CAN STILL JUMP", 96, CORAL, .3, "Black", .02)
    neuron(cv, 540, 900, 1.05, t)
    helix(cv, 1280, 80, 1000, t, 55, .035, (400, 560), eo(pr(t, .5, 1.0)))
    u = pr(t, 1.2, 2.4)
    if u > 0: seg(cv, *hop((480, 1280), (800, 1280), eio(u), 140), 120, 36)
def s1(cv, t, D):
    head(cv, t, "HALF YOUR DNA", "is old jumping genes")
    card(cv, 100, 560, 980, 1340, 36, a=eo(pr(t, 0, .4)))
    cols, rows = 10, 10
    for i in range(100):
        r, c = divmod(i, cols); p = eback(pr(t, .3 + i * .012, .7 + i * .012), 1.5)
        x = 190 + c * 78; y = 640 + r * 58
        jump = i < 50
        cv.rrect(x - 30, y - 24, x + 30, y + 24, 10, fill=CORAL if jump else (214, 202, 178), a=cl(p), outline=INKC if jump else EDGE, w=2, oa=cl(p) * .6)
    q = eo(pr(t, 1.8, 2.4))
    cv.text(540, 1295, "about 50% transposon-derived", 40, INKC, q, "Black")
def s2(cv, t, D):
    head(cv, t, "ALMOST ALL OF THEM", "are frozen", TEAL)
    for k in range(5):
        p = eback(pr(t, .2 + k * .2, .7 + k * .2), 1.8)
        x = 160 + k * 190; y = 780 + (k % 2) * 220
        seg(cv, x + 40, y, 160, 48, cl(p) * .85)
        f = eo(pr(t, 1.2 + k * .25, 1.7 + k * .25))
        # padlock
        lx, ly = x + 40, y + 62
        cv.arc(lx, ly + 2, 17, 180, 360, INKC, 6, f)
        cv.rrect(lx - 25, ly + 2, lx + 25, ly + 46, 8, fill=OCH, a=f, outline=INKC, w=3, oa=f)
        cv.circ(lx, ly + 24, 5, fill=INKC, a=f)
    cv.text(540, 1330, "most can no longer move", 46, INKC, eo(pr(t, 2.4, 3.0)), "Black")
def s3(cv, t, D):
    head(cv, t, "BC200", "a brain gene that still moves")
    card(cv, 70, 560, 1010, 1380, 36, a=eo(pr(t, 0, .4)))
    neuron(cv, 330, 800, .55, t)
    cv.text(700, 700, "BC200", 110, CORAL, eo(pr(t, .3, .8)), "Black")
    cv.text(700, 790, "works in neurons", 38, INKC, eo(pr(t, .8, 1.3)), "Bold")
    helix(cv, 1150, 110, 970, t, 60, .034, (480, 600), eo(pr(t, .6, 1.1)))
    u = pr(t, 2.0, 3.6)
    seg(cv, *hop((540, 1150), (820, 1150), eio(u), 200), 150, 44, 1, "BC200") if u > 0 else seg(cv, 540, 1150, 150, 44, eo(pr(t, .8, 1.2)), "BC200")
    cv.text(540, 1310, "…and it hops", 44, TEAL, eo(pr(t, 3.3, 3.9)), "Black")
def virus(cv, cx, cy, s, a=1, t=0):
    for k in range(18):
        ang = k * math.pi * 2 / 18
        cv.circ(cx + math.cos(ang) * 150 * s, cy + math.sin(ang) * 105 * s, 9 * s, fill=PLUM, a=a * .8)
    cv.rrect(cx - 140 * s, cy - 95 * s, cx + 140 * s, cy + 95 * s, 60 * s, fill=(190, 156, 120), a=a, outline=INKC, w=5, oa=a)
    cv.rrect(cx - 90 * s, cy - 40 * s, cx + 90 * s, cy + 40 * s, 36 * s, fill=(120, 80, 70), a=a, outline=INKC, w=3, oa=a)
def s4(cv, t, D):
    head(cv, t, "FOUND INSIDE A VIRUS", "a human poxvirus", PLUM)
    p = eback(pr(t, .2, .8), 1.6)
    virus(cv, 540, 900, 2.0 * p, cl(p), t)
    q = eo(pr(t, 1.2, 1.8))
    seg(cv, 540, 900, 240, 56, q, "BC200")
    cv.text(540, 1170, "molluscum contagiosum virus", 38, INKC, eo(pr(t, 1.8, 2.4)), "Bold")
    cv.text(540, 1230, "Cornell · Science, Sept 2026", 32, EDGE, eo(pr(t, 2.2, 2.8)), "SemiBold")
def s5(cv, t, D):
    head(cv, t, "SKIN → VIRUS", "the likely jump", CORAL)
    cv.circ(260, 940, 190, fill=(236, 190, 160), a=eo(pr(t, 0, .4)), outline=INKC, w=5, oa=eo(pr(t, 0, .4)))
    cv.circ(260, 940, 70, fill=(190, 120, 100), a=eo(pr(t, 0, .4)))
    virus(cv, 820, 940, .9, eo(pr(t, .3, .8)))
    cv.text(260, 1190, "skin cell", 40, INKC, eo(pr(t, .6, 1.0)), "Bold")
    cv.text(820, 1190, "virus", 40, INKC, eo(pr(t, .6, 1.0)), "Bold")
    u = pr(t, 1.2, 3.0)
    if u > 0:
        for j in range(8):
            v = eio(max(0, u - j * .04)); 
            if v > 0 and j: cv.circ(*hop((290, 940), (800, 940), v, 330), 10 - j, fill=CORAL, a=.35)
        seg(cv, *hop((290, 940), (800, 940), eio(u), 330), 120, 36)
    else: seg(cv, 290, 940, 120, 36, eo(pr(t, .6, 1)))
    cv.text(540, 1330, "at least, that's the team's best read", 38, PLUM, eo(pr(t, 3.5, 4.1)), "Bold")
def s6(cv, t, D):
    head(cv, t, "THE RULE", "a gene with a job stops jumping", TEAL)
    for k, (a_, b_, ok) in enumerate([("has a job", "stays put", True), ("jumps", "no job", True), ("BC200", "does both", False)]):
        y = 700 + k * 230; p = eback(pr(t, .3 + k * .7, .8 + k * .7), 1.6)
        card(cv, 120, y - 90, 960, y + 90, 34, fill=CORAL if k == 2 else PAPER, outline=INKC if k == 2 else EDGE, a=cl(p))
        cv.text(330, y, a_, 52, PAPER if k == 2 else INKC, cl(p), "Black")
        cv.text(700, y, ("= " if k < 2 else "= ") + b_, 46, PAPER if k == 2 else TEAL, cl(p), "Bold")
    cv.text(540, 1390, "evolution hasn't untangled the two", 38, INKC, eo(pr(t, 3.8, 4.4)), "Black")
def s7(cv, t, D):
    head(cv, t, "ONLY IN PRIMATES", "and in the cells that pass genes on", OCH)
    for k, (n_, s_, c) in enumerate([("HUMANS", "and close primate relatives", TEAL), ("NEURONS", "where it's most abundant", CORAL), ("SPERM & EGG", "at low levels", PLUM)]):
        y = 700 + k * 230; p = eback(pr(t, .4 + k * .8, .9 + k * .8), 1.6)
        card(cv, 110, y - 90, 970, y + 90, 34, a=cl(p))
        cv.circ(220, y, 46, fill=c, a=cl(p), outline=INKC, w=4, oa=cl(p))
        cv.text(300, y - 22, n_, 50, INKC, cl(p), "Black", anchor="lm")
        cv.text(300, y + 34, s_, 32, c, cl(p), "SemiBold", anchor="lm")
def s8(cv, t, D):
    head(cv, t, "WHAT'S NEXT?", "is it jumping in tumors?", CORAL)
    import random
    rnd = random.Random(4)
    cells = [(rnd.uniform(200, 880), rnd.uniform(650, 1250), rnd.uniform(46, 80)) for _ in range(22)]
    for i, (x, y, r) in enumerate(cells):
        p = eo(pr(t, .1 + i * .04, .5 + i * .04))
        cv.circ(x, y, r * p, fill=(222, 170, 150) if i % 3 else (200, 130, 120), a=.9, outline=INKC, w=3, oa=.7 * p)
        cv.circ(x + 6, y + 4, r * .4 * p, fill=(150, 80, 80), a=.8)
    for k in range(3):
        u = ((t * .5 + k / 3) % 1)
        a_ = cells[k * 5][:2]; b_ = cells[k * 5 + 3][:2]
        seg(cv, *hop(a_, b_, u, 120), 90, 28, eo(pr(t, 1.0, 1.6)))
    kinetic(cv, t, 1340, "?", 220, CORAL, 1.4, "Black")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=CORAL, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=CORAL, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, CORAL, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
