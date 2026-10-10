def brackets(cv, x0, y0, x1, y1, col, a=1, L=46, w=5, pad=18):
    for (x, y, dx, dy) in [(x0 + pad, y0 + pad, 1, 1), (x1 - pad, y0 + pad, -1, 1), (x0 + pad, y1 - pad, 1, -1), (x1 - pad, y1 - pad, -1, -1)]:
        cv.line([(x + dx * L, y), (x, y), (x, y + dy * L)], col, w, a)
def cross(cv, x, y, s, col, a=1, w=7):
    cv.line([(x - s, y - s), (x + s, y + s)], col, w, a); cv.line([(x - s, y + s), (x + s, y - s)], col, w, a)
def s0(cv, t, D):
    kinetic(cv, t, 300, "AI CHIPS MUST", 100, INKC, -.2, "Black", .03)
    kinetic(cv, t, 420, "BE PERFECT", 118, COP, -.1, "Black", .04)
    photo(cv, "die1", 120, 520, 960, 1160, t / D, 1.0, 1.35, .35, .5)
    brackets(cv, 120, 520, 960, 1160, PAPER, eo(pr(t, .4, .9)) * .9)
    for k, (txt, col) in enumerate([("ZERO ERRORS", SAGE), ("HIGH VOLTAGE", COP), ("HIGH ENERGY", RED)]):
        q = eo(pr(t, 1.2 + k * .55, 1.7 + k * .55))
        x = 120 + k * 290
        chip(cv, x, 1240, 260, txt, col, q, INK, 27, 80)
    cv.text(540, 1370, "reliability is paid for in power", 36, INKC, eo(pr(t, 3.2, 3.8)), "SemiBold")
def s1(cv, t, D):
    head(cv, t, "LOWER THE VOLTAGE", "less power, more mistakes", COP)
    card(cv, 100, 540, 980, 1400, 34)
    p = eio(pr(t, .6, 3.6)); v = lerp(1.0, 0.4, p)
    cv.text(190, 640, "VOLTAGE", 30, mix(INK, PAPER, .35), 1, "Bold", "lm")
    cv.text(890, 640, "%.1f V" % v, 56, INK, 1, "Black", "rm")
    cv.rrect(190, 700, 890, 724, 12, fill=PAPER2)
    kx = lerp(890, 190 + 700 * .1, p)
    cv.rrect(kx, 700, 890, 724, 12, fill=mix(COP, PAPER, .0), a=0)
    cv.rrect(190, 700, kx, 724, 12, fill=SAGE)
    cv.circ(kx + 3, 716, 26, fill=SHAD, a=.5); cv.circ(kx, 712, 26, fill=COP); cv.circ(kx - 6, 704, 8, fill=mix(COP, WHT, .6), a=.7)
    cv.text(190, 800, "ENERGY USED", 30, mix(INK, PAPER, .35), 1, "Bold", "lm")
    cv.rrect(190, 840, 890, 880, 20, fill=PAPER2)
    cv.rrect(190, 840, 190 + 700 * (0.12 + 0.88 * v * v), 880, 20, fill=COP)
    rows = [("6 × 7", "42", "44", .85), ("9 + 5", "14", "15", .7), ("8 × 8", "64", "62", .55), ("12 × 3", "36", "38", .45)]
    for k, (q_, ok, bad, th) in enumerate(rows):
        y = 990 + k * 92
        wrong = v < th
        flick = wrong and int(t * 7 + k * 3) % 5 == 0
        col = RED if wrong else SAGE
        ans = bad if wrong else ok
        qa = eo(pr(t, .3 + k * .15, .8 + k * .15))
        cv.rrect(190, y - 36, 890, y + 36, 20, fill=PAPER2, a=qa)
        cv.text(230, y, q_ + "  =  " + (ans if not flick else "?"), 46, INK, qa, "Black", "lm")
        if wrong: cross(cv, 830, y, 17, RED, qa)
        else: check(cv, 830, y + 2, 34, qa, SAGE, 8)
    cv.text(540, 1360, "random arithmetic slips", 34, RED, eo(pr(t, 3.8, 4.4)), "Bold")
def s2(cv, t, D):
    head(cv, t, "NORMAL MODELS", "one hit can wreck the output", RED)
    card(cv, 100, 540, 980, 1400, 34)
    rr = random.Random(11)
    hit = pr(t, 1.7, 1.75) > 0
    for k in range(26):
        x = 150 + k * 31.5
        hgt = 40 + rr.random() * 110
        if k == 16: hgt = 330
        q = eo(pr(t, .1 + k * .025, .6 + k * .025))
        col = mix(PAPER2, INK, .45)
        if k == 16:
            col = RED if hit else COP
            if hit: hgt = 330 - 130 * eo(pr(t, 1.75, 2.1))
        cv.rrect(x - 11, 900 - hgt * q, x + 11, 900, 6, fill=col)
    cv.text(540, 960, "weights", 28, mix(INK, PAPER, .35), 1, "SemiBold")
    qa = eo(pr(t, .7, 1.2))
    cv.text(740, 560 + 20, "one \"super weight\"", 30, COP, qa * (0 if hit else 1), "Black")
    if hit:
        u = pr(t, 1.7, 2.4)
        for rad in (60, 110):
            cv.circ(16 * 31.5 + 150, 900 - 330 + 20, rad * eo(u), outline=RED, w=6, oa=1 - u)
    # output text corrupts
    cv.rrect(160, 1040, 920, 1330, 24, fill=PAPER2)
    cv.text(190, 1085, "MODEL OUTPUT", 26, mix(INK, PAPER, .35), 1, "Bold", "lm")
    txt = ["The capital of France", "is Paris, home of the", "Eiffel Tower."]
    u = pr(t, 1.9, 4.2)
    rs = random.Random(5); junk = "#@%&?~x7_/<"
    for li, ln in enumerate(txt):
        out = ""
        for ci, c in enumerate(ln):
            if c != " " and rs.random() < u * 1.15 and rs.random() < .85: out += rs.choice(junk)
            else: out += c
        cv.text(190, 1150 + li * 62, out, 44, RED if u > .3 else INK, 1, "Black", "lm")
def s3(cv, t, D):
    kinetic(cv, t, 300, "BROKEN ON", 96, INKC, -.2, "Black", .03)
    kinetic(cv, t, 410, "PURPOSE", 110, COP, -.1, "Black", .04)
    photo(cv, "dome", 120, 500, 960, 840, t / D, 1.0, 1.25, .5, .55)
    cv.text(540, 880, "MIT  ·  preprint, Oct 2026", 30, INKC, eo(pr(t, .5, 1.0)), "SemiBold")
    card(cv, 100, 930, 980, 1400, 30)
    cols, rows_ = 12, 6; cs = 60; gx = 540 - cols * cs / 2; gy = 975
    seed = int(t / .45); rg = random.Random(seed * 7 + 1)
    on = eo(pr(t, 1.2, 1.8))
    drop = set()
    for r_ in range(rows_):
        for b in range(cols // 4):
            if rg.random() < .26 and on > .5:
                for c in range(b * 4, b * 4 + 4): drop.add((r_, c))
    for r_ in range(rows_):
        for c in range(cols):
            x0 = gx + c * cs; y0 = gy + r_ * cs
            if (r_, c) in drop:
                cv.rrect(x0 + 3, y0 + 3, x0 + cs - 3, y0 + cs - 3, 10, fill=mix(INK, PAPER, .75), a=.9)
                cross(cv, x0 + cs / 2, y0 + cs / 2, 9, RED, 1, 4)
            else:
                cv.rrect(x0 + 3, y0 + 3, x0 + cs - 3, y0 + cs - 3, 10, fill=mix(PAPER2, SAGE, .35 + .3 * ((r_ * 5 + c * 3) % 4) / 3))
    cv.text(540, 1370, "random blocks of 4 numbers dropped, every pass", 28, mix(INK, PAPER, .2), eo(pr(t, 2.6, 3.2)), "Bold")
def s4(cv, t, D):
    head(cv, t, "BIGGER MODELS RECOVER", "useful share of the model", SAGE)
    card(cv, 100, 540, 980, 1400, 34)
    x0, x1, yb, yt = 190, 900, 1230, 700
    cv.line([(x0, yt - 20), (x0, yb), (x1 + 10, yb)], mix(INK, PAPER, .3), 4)
    cv.text(x0, 640, "share doing useful work", 28, mix(INK, PAPER, .3), 1, "SemiBold", "lm")
    cv.text(x0, yb + 50, "7.9M weights", 28, mix(INK, PAPER, .3), 1, "Bold", "lm")
    cv.text(x1, yb + 50, "930M", 28, mix(INK, PAPER, .3), 1, "Bold", "rm")
    cv.text(540, yb + 50, "model size", 28, mix(INK, PAPER, .3), 1, "SemiBold")
    f = lambda u: 1 - 1.76 * u + 1.6 * u * u
    P = eio(pr(t, .4, 3.4)); N = 60
    pts = [(lerp(x0 + 10, x1, i / N * P), lerp(yb - 30, yt, (f(i / N * P) - .5) / .5)) for i in range(N + 1)]
    pts = [(x, min(yb - 20, max(yt, y))) for x, y in pts]
    for k in range(N):
        u = (k / N * P)
        cv.line([pts[k], pts[k + 1]], RED if u < .55 else SAGE, 10)
    ex, ey = pts[-1]; cv.circ(ex, ey, 17, fill=SHAD, a=.4); cv.circ(ex, ey, 15, fill=COP, outline=PAPER, w=4)
    um = .55; mx = x0 + 10 + (x1 - x0 - 10) * um
    q = eo(pr(t, 2.0, 2.5))
    if P > .55:
        cv.text(mx, yb - 105 + 0, "dips", 38, RED, q, "Black")
    q2 = eo(pr(t, 3.6, 4.2))
    cv.text(660, 770, "then", 34, SAGE, q2, "SemiBold", "mm"); cv.text(660, 818, "recovers", 46, SAGE, q2, "Black")
    cv.text(540, 1340, "schematic of the paper's finding", 26, mix(INK, PAPER, .3), 1, "Bold")
def dial(cv, cx, cy, r, per, ang, col, jit=0, a=1):
    cv.circ(cx + 4, cy + 8, r, fill=SHAD, a=.45 * a)
    cv.circ(cx, cy, r, fill=PAPER2, outline=mix(INK, PAPER, .2), w=5, a=a)
    for k in range(per):
        th = math.radians(k / per * 360 - 90)
        cv.line([(cx + (r - 24) * math.cos(th), cy + (r - 24) * math.sin(th)), (cx + (r - 6) * math.cos(th), cy + (r - 6) * math.sin(th))], mix(INK, PAPER, .2), 5, a)
    th = math.radians(ang + jit - 90)
    cv.line([(cx, cy), (cx + (r - 30) * math.cos(th), cy + (r - 30) * math.sin(th))], col, 9, a)
    cv.circ(cx, cy, 11, fill=col, a=a)
def s5(cv, t, D):
    head(cv, t, "GOOD CODES, NOT COPIES", "how grid cells keep your place", COP)
    card(cv, 100, 540, 980, 1400, 34)
    pos = 0.9 + t * 0.35
    pers = [3, 4, 5]
    for k, per in enumerate(pers):
        cx = 260 + k * 280
        ang = (pos / per % 1) * 360
        noisy = (k == 1) and t > 2.2
        jit = (math.sin(t * 23) * 55 + math.sin(t * 41) * 25) if noisy else 0
        col = RED if noisy else INK
        qa = eo(pr(t, .1 + k * .2, .6 + k * .2))
        dial(cv, cx, 800, 108, per * 3, ang, col, jit, qa)
        cv.text(cx, 950, "module %d" % (k + 1), 28, mix(INK, PAPER, .3), qa, "Bold")
    q = eo(pr(t, 2.2, 2.8))
    cv.text(540, 1060, "one module drifts", 40, RED, q, "Black")
    q = eo(pr(t, 3.2, 3.8))
    cv.text(540, 1130, "the others disagree with it", 36, INK, q, "Bold")
    q = eo(pr(t, 4.4, 5.0))
    cv.rrect(220, 1200, 860, 1320, 30, fill=SAGE, a=q)
    cv.text(540, 1260, "error caught", 54, INK, q, "Black")
def s6(cv, t, D):
    head(cv, t, "JUST A PREPRINT", "not peer reviewed yet", COP)
    card(cv, 100, 540, 980, 1400, 34)
    x0, x1, y = 170, 910, 880
    lg = lambda n: (math.log10(n) - 7) / 5
    cv.line([(x0, y), (x1, y)], mix(INK, PAPER, .25), 6)
    for n, lab in [(1e7, "10M"), (1e8, "100M"), (1e9, "1B"), (1e10, "10B"), (1e11, "100B"), (1e12, "1T")]:
        x = lerp(x0, x1, lg(n)); cv.line([(x, y - 14), (x, y + 14)], mix(INK, PAPER, .25), 4)
        cv.text(x, y + 50, lab, 28, mix(INK, PAPER, .25), 1, "Bold")
    cv.text(540, y + 110, "weights per model", 28, mix(INK, PAPER, .3), 1, "SemiBold")
    pa = eo(pr(t, .4, 1.6))
    xa = lerp(x0, x1, lg(7.9e6)); xb = lerp(x0, x1, lg(9.3e8))
    cv.rrect(xa, y - 36, lerp(xa, xb, pa), y + 0, 12, fill=SAGE)
    cv.text((xa + xb) / 2, y - 100, "TESTED", 44, SAGE, eo(pr(t, 1.4, 2.0)), "Black")
    q = eo(pr(t, 2.6, 3.2))
    xc = lerp(x0, x1, lg(1e11))
    for i in range(0, 8):
        xx = lerp(xb + 30, x1, i / 8)
        cv.line([(xx, y - 4), (xx + 24, y - 36)], RED, 5, .7 * q)
    cv.text(xc + 20, y - 130, "FRONTIER SCALE", 36, RED, q, "Black")
    cv.text(xc + 20, y - 85, "untested", 32, RED, q, "SemiBold")
    q = eo(pr(t, 3.8, 4.4))
    cv.rrect(180, 1130, 900, 1320, 30, fill=PAPER2, a=q)
    cv.text(540, 1190, "next test, estimated", 30, mix(INK, PAPER, .3), q, "Bold")
    cv.text(540, 1265, "≈ 100 million GPU-hours", 48, INK, q, "Black")
def s7(cv, t, D):
    a = 1 - eio(pr(t, 3.9, 4.3))
    photo(cv, "wafer", 120, 440, 960, 940, t / 4.4, 1.5, 1.75, .5, .5, a)
    kinetic(cv, t, 1040, "CHEAP, FAULTY CHIPS", 74, INKC, .1, "Black", .02) if a > .02 else None
    if a > .02:
        cv.text(540, 1150, "FAR LESS ENERGY", 86, mix(COP, BG1, 1 - a), a, "Black")
        cv.text(540, 1250, "if it holds at scale", 36, mix(INKC, BG1, 1 - a), eo(pr(t, 2.2, 2.8)) * a, "SemiBold")
    kinetic(cv, t, 740, "LATOON", 150, INKC, 4.4, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, COP, eo(pr(t, 5.2, 5.8)), "SemiBold")
    chip(cv, 280, 990, 520, "FOLLOW", COP, eo(pr(t, 6.0, 6.6)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
