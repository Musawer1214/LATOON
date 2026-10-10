ASH = (176, 170, 150)
def credit(cv, txt, y, a=1):
    cv.text(540, y, txt, 24, ASH, a, "SemiBold")
def qubit(cv, x, y, ang, r=34, col=PAPER, a=1, nc=None):
    cv.circ(x, y, r, fill=mix(INK, PAPER, .12), a=a)
    cv.circ(x, y, r, outline=col, w=4, oa=a)
    dx, dy = math.cos(ang) * (r - 8), math.sin(ang) * (r - 8)
    cv.line([(x - dx * .4, y - dy * .4), (x + dx, y + dy)], nc or COP, 6, a)
    cv.circ(x + dx, y + dy, 6, fill=nc or COP, a=a)
UP = -math.pi / 2
def grid(cv, t, x0, y0, n, m, gap, frac_chaos, a=1, seed=3, r=32, flip_t=None):
    rs = random.Random(seed)
    for j in range(m):
        for i in range(n):
            u = rs.random(); ph = rs.random() * 6.28; sp = 2.5 + rs.random() * 3
            x = x0 + i * gap; y = y0 + j * gap
            chaotic = u < frac_chaos
            ang = ph + t * sp + math.sin(t * 3 + ph) * 1.5 if chaotic else UP + .06 * math.sin(t * 2 + ph)
            qubit(cv, x, y, ang, r, PAPER if chaotic else SAGE, a, RED if chaotic else COP)
def s0(cv, t, D):
    kinetic(cv, t, 300, "SHUFFLE IT", 112, INKC, -.2, "Black", .03)
    kinetic(cv, t, 420, "LONG ENOUGH", 70, COP, .35, "Black", .02)
    photo(cv, "riffle", 90, 520, 990, 1180, t / D, 1.0, 1.22, .45, .5)
    brackets(cv, 90, 520, 990, 1180, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Riffle shuffle: Alexey Musulev, CC BY-SA 4.0", 1225, eo(pr(t, .8, 1.3)))
    # ordered strip that scrambles
    rs = random.Random(8); perm = list(range(10)); rs.shuffle(perm)
    p = eio(pr(t, 1.0, 3.0))
    for k in range(10):
        pos = lerp(k, perm[k], p)
        x = 120 + pos * 84
        card_col = mix(COP, RED, k / 9.0)
        cv.rrect(x - 34, 1290, x + 34, 1400, 10, fill=SHAD, a=.5)
        cv.rrect(x - 34, 1284, x + 34, 1394, 10, fill=card_col)
        cv.text(x, 1339, str(k + 1), 44, INK, 1, "Black")
def s1(cv, t, D):
    head(cv, t, "INSIDE A QUANTUM COMPUTER", "that same chaos is the enemy", COP)
    photo(cv, "sys1", 230, 500, 850, 1340, t / D, 1.0, 1.2, .5, .35)
    brackets(cv, 230, 500, 850, 1340, PAPER, eo(pr(t, .3, .8)) * .9)
    chip(cv, 300, 1360, 480, "CHAOS = ERRORS", RED, eo(pr(t, 1.2, 1.8)), INKC, 38, 76)
    credit(cv, "IBM Quantum System One: OJB Quantum, CC BY 4.0", 1438, eo(pr(t, .6, 1.1)))
def s2(cv, t, D):
    head(cv, t, "QUBITS ARE FRAGILE", None)
    card(cv, 80, 460, 1000, 1000, 30)
    cv.text(540, 504, "ONE ROW OF QUBITS", 26, mix(INK, PAPER, .4), eo(pr(t, .1, .5)), "Bold")
    # needles go from steady to jittery as noise enters
    for i in range(7):
        x = 160 + i * 127; y = 700
        noise = cl((t - .9 - i * .08) / 3.0)
        ang = UP + noise * (math.sin(t * (4 + i) + i) * 1.1 + noise * math.sin(t * 9 + i * 2) * .9)
        qubit(cv, x, y, ang, 44, PAPER if noise < .3 else PAPER2, 1, COP if noise < .4 else RED)
        if noise > .5:
            cv.text(x, y + 86, "?", 40, RED, cl((noise - .5) * 3), "Black")
    cv.text(540, 900, "tiny errors drift in", 36, INK, eo(pr(t, 1.2, 1.8)), "Black")
    chip(cv, 100, 1070, 230, "HEAT", COP, cl(eback(pr(t, 1.0, 1.4), 2) * 1.3), INK, 34, 76)
    chip(cv, 360, 1070, 380, "STRAY SIGNALS", RED, cl(eback(pr(t, 2.0, 2.4), 2) * 1.3), INKC, 34, 76)
    chip(cv, 280, 1170, 360, "TINY FLAWS", PAPER, cl(eback(pr(t, 3.0, 3.4), 2) * 1.3), INK, 34, 76)
    cv.text(540, 1330, "answers can't be trusted", 54, RED, eo(pr(t, 3.9, 4.4)), "Black")
def s3(cv, t, D):
    head(cv, t, "RUTGERS  \u00d7  IBM", "a tug of war on a real chip", COP)
    photo(cv, "heron1", 140, 480, 940, 1010, t / D, 1.0, 1.15, .5, .35)
    brackets(cv, 140, 480, 940, 1010, PAPER, eo(pr(t, .3, .8)) * .9)
    p = eo(pr(t, .6, 3.0))
    cv.text(540, 1100, "%d" % round(100 * p), 130, INKC, eo(pr(t, .4, .8)), "Black")
    cv.text(540, 1196, "QUBITS", 44, COP, eo(pr(t, 1.0, 1.5)), "Black")
    # rope
    qa = eo(pr(t, 1.4, 2.0))
    off = math.sin(t * 5) * 14 * qa
    cv.line([(130, 1300), (950, 1300)], PAPER2, 10, qa)
    cv.rrect(500 + off, 1270, 580 + off, 1330, 12, fill=COP, a=qa)
    chip(cv, 80, 1350, 380, "SCRAMBLE", RED, qa, INKC, 34, 70)
    chip(cv, 620, 1350, 380, "RESET", SAGE, qa, INK, 34, 70)
    credit(cv, "IBM Quantum Heron: \u00a9 IBM", 1440, eo(pr(t, .8, 1.3)))
def s4(cv, t, D):
    head(cv, t, "TWO MOVES", None)
    # card 1: scramble
    card(cv, 70, 470, 1010, 930, 30)
    cv.text(120, 515, "1  SCRAMBLE", 38, RED, eo(pr(t, .1, .5)), "Black", "lm")
    cv.text(960, 515, "like a shuffle", 28, mix(INK, PAPER, .4), eo(pr(t, .3, .7)), "Bold", "rm")
    photo(cv, "cards", 110, 560, 480, 880, t / D, 1.0, 1.2, .5, .5, eo(pr(t, .2, .7)), 18)
    for i in range(4):
        x = 560 + i * 118; y = 720
        sw = eo(pr(t, .6, 2.2))
        qubit(cv, x, y, UP + sw * (2.2 + i * 1.7) + math.sin(t * 4 + i) * .5 * sw, 40, PAPER, 1, RED)
        if i < 3:
            q = eo(pr(t, .8 + i * .3, 1.3 + i * .3))
            cv.line([(x + 44, y - 6 * (1 if i % 2 else -1)), (x + 74, y + 6 * (1 if i % 2 else -1))], RED, 5, q)
    # card 2: check + reset
    qc = eo(pr(t, 2.5, 3.0))
    card(cv, 70, 970, 1010, 1430, 30, PAPER, qc)
    cv.text(120, 1015, "2  CHECK + RESET", 38, mix(SAGE, INK, .35), qc, "Black", "lm")
    cv.text(960, 1015, "put one back", 28, mix(INK, PAPER, .4), qc, "Bold", "rm")
    for i in range(4):
        x = 190 + i * 215; y = 1180
        tt = 3.0 + i * .5
        rs_ = eo(pr(t, tt, tt + .35))
        ang0 = 1.0 + i * 1.8 + t * 3
        ang = lerp(ang0, UP, rs_)
        qubit(cv, x, y, ang, 56, PAPER, qc, mix(RED, SAGE, rs_) if rs_ > .5 else RED)
        if 0 < rs_ < .98 or (t > tt and t < tt + .6):
            cv.circ(x, y, 56 + 30 * eo(pr(t, tt - .1, tt + .4)), outline=SAGE, w=5, oa=(1 - eo(pr(t, tt, tt + .6))) * qc)
        cv.text(x, y + 100, "checked" if rs_ < .5 else "reset", 24, mix(INK, PAPER, .35), qc, "Bold")
    cv.text(540, 1350, "again and again, mid-calculation", 30, INK, eo(pr(t, 4.2, 4.8)), "Bold")
def s5(cv, t, D):
    head(cv, t, "ON IBM'S HERON", "156-qubit processor", COP)
    photo(cv, "heron2", 210, 470, 870, 970, t / D, 1.0, 1.12, .5, .5)
    brackets(cv, 210, 470, 870, 970, PAPER, eo(pr(t, .2, .7)) * .9)
    for k, (lab, col, x) in enumerate([("SCRAMBLES", RED, 290), ("RESETS", SAGE, 790)]):
        q = eo(pr(t, .6 + k * .4, 1.2 + k * .4))
        p = eo(pr(t, 1.0 + k * .3, 3.0 + k * .3))
        cv.rrect(x - 200, 1030, x + 200, 1330, 28, fill=SHAD, a=.5 * q)
        cv.rrect(x - 200, 1020, x + 200, 1320, 28, fill=PAPER, a=q)
        cv.text(x, 1130, "~%s" % format(int(5000 * p / 100) * 100, ","), 82, col if col != SAGE else mix(SAGE, INK, .4), q, "Black")
        cv.text(x, 1230, lab, 36, INK, q, "Black")
        cv.text(x, 1275, "nearly 5,000 in the paper", 22, mix(INK, PAPER, .4), q, "Bold")
    credit(cv, "Heron chip: \u00a9 IBM", 1385, eo(pr(t, .8, 1.3)))
def phase(cv, t, pos, qa, chaos_frac, title):
    card(cv, 70, 460, 1010, 1010, 30, PAPER, qa)
    cv.text(540, 505, title, 30, INK, qa, "Black")
    grid(cv, t, 220, 590, 6, 4, 128, chaos_frac, qa, 3, 36)
    # axis
    cv.line([(130, 1120), (950, 1120)], mix(INK, PAPER, .2), 6, qa)
    cv.rrect(540, 1090, 950, 1150, 8, fill=RED, a=.25 * qa)
    cv.text(130, 1190, "0%", 28, INKC, qa, "Bold"); cv.text(950, 1190, "100%", 28, INKC, qa, "Bold")
    cv.text(540, 1190, "50%", 28, COP, qa, "Black")
    cv.text(540, 1250, "share of time spent scrambling", 30, INKC, qa, "Bold")
    x = lerp(130, 950, pos)
    cv.poly([(x, 1112), (x - 20, 1066), (x + 20, 1066)], COP, qa)
    cv.line([(540, 1060), (540, 1130)], COP, 3, qa * .8)
def s6(cv, t, D):
    head(cv, t, "SCRAMBLE > 50%", None)
    q = eo(pr(t, 0, .4))
    pos = lerp(.5, .78, eio(pr(t, .3, 1.4)))
    phase(cv, t, pos, q, 1.0, "THE QUBITS")
    qr = eo(pr(t, 1.2, 1.7))
    chip(cv, 250, 1310, 580, "CHAOS WINS", RED, qr, INKC, 56, 110)
def s7(cv, t, D):
    head(cv, t, "RESET > 50%", None)
    q = eo(pr(t, 0, .4))
    pos = lerp(.5, .22, eio(pr(t, .3, 1.4)))
    fr = lerp(1.0, 0.0, eio(pr(t, 1.0, 2.0)))
    phase(cv, t, pos, q, fr, "THE QUBITS")
    qr = eo(pr(t, 1.8, 2.3))
    chip(cv, 200, 1310, 680, "ORDER IS REACHED", SAGE, qr, INK, 54, 110)
def s8(cv, t, D):
    head(cv, t, "RIGHT AT 50 / 50", "a phase transition", COP)
    photo(cv, "ice", 90, 470, 990, 1010, t / D, 1.0, 1.2, .5, .5)
    brackets(cv, 90, 470, 990, 1010, PAPER, eo(pr(t, .2, .7)) * .9)
    # needle wobbling around the tipping point
    sw = 1 if t < 2.2 else -1
    x = 540 + math.sin(t * 4.5) * 40 * (1 if t < 2.6 else .2)
    card(cv, 70, 1060, 1010, 1420, 30)
    cv.text(540, 1105, "ONE SMALL NUDGE", 30, INK, eo(pr(t, .6, 1.0)), "Black")
    qa = eo(pr(t, .6, 1.0))
    cv.line([(130, 1280), (950, 1280)], mix(INK, PAPER, .25), 6, qa)
    cv.rrect(540, 1252, 950, 1308, 8, fill=RED, a=.28 * qa)
    flip = eio(pr(t, 2.0, 2.4))
    xm = lerp(500, 585, flip) + (1 - flip) * math.sin(t * 6) * 10
    cv.poly([(xm, 1268), (xm - 20, 1220), (xm + 20, 1220)], COP, qa)
    cv.text(300, 1350, "CONTROL", 34, mix(SAGE, INK, .4), qa * (1 - .6 * flip), "Black")
    cv.text(780, 1350, "CHAOS", 34, RED, qa * (.4 + .6 * flip), "Black")
    credit(cv, "Frozen bubble: spurekar, CC BY 2.0", 1448, eo(pr(t, 1.0, 1.5)))
def s9(cv, t, D):
    a1 = 1 - eio(pr(t, 3.0, 3.4))
    if a1 > .02:
        kinetic(cv, t, 300, "FAULT-TOLERANT", 78, INKC, -.2, "Black", .025)
        kinetic(cv, t, 400, "QUANTUM COMPUTERS", 60, COP, .3, "Black", .02)
        photo(cv, "sys1", 300, 480, 780, 1160, t / 3.4, 1.0, 1.15, .5, .4, a1)
        brackets(cv, 300, 480, 780, 1160, PAPER, a1 * .9)
        chip(cv, 230, 1220, 620, "NOBODY HAS BUILT ONE YET", PAPER, a1 * eo(pr(t, 1.0, 1.5)), INK, 30, 74)
        credit(cv, "Nature Physics \u00b7 Rutgers + IBM \u00b7 Oct 9, 2026", 1340, a1 * eo(pr(t, 1.4, 1.9)))
    kinetic(cv, t, 740, "LATOON", 150, INKC, 4.2, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, COP, eo(pr(t, 5.0, 5.6)), "SemiBold")
    chip(cv, 280, 990, 520, "FOLLOW", COP, eo(pr(t, 5.7, 6.3)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
