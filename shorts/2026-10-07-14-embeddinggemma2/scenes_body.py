
INK = (3, 20, 22)
CARDC = (8, 32, 38)
def ic_photo(cv, cx, cy, s, c, a=1):
    cv.rrect(cx - s * .45, cy - s * .35, cx + s * .45, cy + s * .35, s * .08, outline=c, w=max(2, s * .06), a=a)
    cv.circ(cx - s * .2, cy - s * .1, s * .08, fill=c, a=a)
    cv.poly([(cx - s * .38, cy + s * .28), (cx - s * .05, cy - s * .05), (cx + s * .15, cy + s * .14), (cx + s * .26, cy + s * .02), (cx + s * .38, cy + s * .28)], c, a * .9)
def ic_wave(cv, cx, cy, s, c, a=1, t=0):
    for i in range(7):
        h = s * (.12 + .3 * abs(math.sin(i * 1.3 + t * 5)))
        x = cx - s * .36 + i * s * .12
        cv.rrect(x - s * .04, cy - h, x + s * .04, cy + h, s * .04, fill=c, a=a)
def ic_aa(cv, cx, cy, s, c, a=1):
    cv.text(cx, cy, "Aa", s * .75, c, a, "Black")
def ic_any(k, cv, cx, cy, s, c, a=1, t=0):
    (ic_photo, lambda *x: ic_wave(*x, t=t), ic_aa)[k](cv, cx, cy, s, c, a)
def dotted(cv, p0, p1, t, n=14, col=ORG2, a=1, r=5, speed=.8):
    for i in range(n):
        u = (i / n + t * speed) % 1
        cv.circ(lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), r * (.5 + .5 * math.sin(u * math.pi)), fill=col, a=a * math.sin(u * math.pi))
def isogrid(cv, cx, cy, hw, hh, n, col, a=1, w=2):
    P = lambda u, v: (cx + (u - v) * hw / n, cy + (u + v - n) * hh / n)
    for i in range(n + 1):
        cv.line([P(i, 0), P(i, n)], col, w, a); cv.line([P(0, i), P(n, i)], col, w, a)
    return P

# ---- S0 hook: photo + song + sentence -> the same kind of number
def s0(cv, t, D):
    chip(cv, 540, 300, "GOOGLE DEEPMIND  ·  NEW OPEN MODEL", 30, INK, ORG, 1)
    kinetic(cv, t, 430, "EMBEDDING", 118, WHT, -.3, "Black", .02)
    kinetic(cv, t, 560, "GEMMA 2", 118, ORG, -.2, "Black", .02)
    xs = [200, 540, 880]
    for k in range(3):
        p = eback(pr(t, .5 + k * .15, 1.0 + k * .15), 2)
        cv.rrect(xs[k] - 110, 700, xs[k] + 110, 860, 30, fill=CARDC, a=cl(p), outline=ORG, w=4, oa=cl(p) * .9)
        ic_any(k, cv, xs[k], 780, 110, CREAM, cl(p), t)
        cv.text(xs[k], 905, ("PHOTO", "SOUND", "TEXT")[k], 28, MUT, cl(p), "Bold")
        # streams down to the shared vector
        f = pr(t, 1.3 + k * .1, 2.3 + k * .1)
        if f > 0:
            dotted(cv, (xs[k], 940), (540, 1110), t + k * .3, 9, ORG2 if k != 1 else AMB, eo(f))
    q = eback(pr(t, 1.9, 2.5), 2)
    cv.rrect(90, 1110, 990, 1250, 34, fill=CARDC, a=cl(q), outline=AMB, w=4, oa=cl(q))
    vals = ["0.21", "-0.87", "0.43", "0.09", "-0.52", "0.76"]
    sx = 150
    for i, v in enumerate(vals):
        a_ = eo(pr(t, 2.3 + i * .12, 2.6 + i * .12))
        cv.text(sx + i * 145, 1180, v, 42, mix(CREAM, AMB, .5 if i % 2 else 0), a_, "Bold")
    cv.text(540, 1300, "one shared kind of number", 36, ORG2, eo(pr(t, 2.9, 3.4)), "SemiBold")

# ---- S1 release: real banner from Google + 740M
def s1(cv, t, D):
    chip(cv, 540, 310, "OCT 6, 2026", 32, INK, AMB, eo(pr(t, 0, .3)))
    p = eo(pr(t, .05, .55))
    shadow(cv, 90, 420, 990, 930, 40, p)
    zoomcard(cv, "banner", 540, 675, 900, 506, 650 + 25 * pr(t, 0, D), 365, 1.0 + .14 * pr(t, 0, D), 40, p)
    cv.rrect(90, 420, 990, 930, 40, outline=ORG, w=3, oa=.6 * p)
    cv.text(540, 962, "image: © Google", 22, MUT, .8 * p, "Medium")
    n = int(740 * eo(pr(t, .4, 1.4)))
    cv.text(540, 1110, f"{n}M", 190, ORG, eo(pr(t, .3, .7)), "Black")
    cv.text(540, 1235, "PARAMETERS", 46, CREAM, eo(pr(t, .9, 1.4)), "Bold")
    q = eo(pr(t, 1.6, 2.2))
    # tiny phone glyph + line
    cv.rrect(300, 1300, 350, 1395, 12, outline=AMB, w=5, a=q)
    cv.circ(325, 1380, 4, fill=AMB, a=q)
    cv.text(650, 1348, "small enough for a phone", 40, AMB, q, "Bold")

# ---- S2 768 numbers -> a point on a map of meaning
def s2(cv, t, D):
    cv.text(540, 310, "EMBEDDING MODEL", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 378, "input in  →  numbers out", 34, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    A = 1 - eio(pr(t, 3.5, 4.1))
    cols, rows = 4, 7
    for k in range(cols * rows):
        c, r = k % cols, k // cols
        x, y = 150 + c * 260, 480 + r * 70
        s_ = 1.5 + (k * .07)
        a_ = eo(pr(t, s_ * .9, s_ * .9 + .3)) * A
        v = (((k * 7919 + int(t * 7) * 131) % 200) - 100) / 100
        col = mix(ORG2, AMB, .6 if (k + int(t * 7)) % 5 == 0 else 0)
        move = eio(pr(t, 3.5, 4.1))
        cx_ = lerp(x, 540, move); cy_ = lerp(y, 1010, move)
        cv.text(cx_, cy_, f"{v:+.2f}", 38, col, a_, "Bold")
    n = int(768 * eo(pr(t, 1.6, 3.6)))
    cv.text(540, 1190, f"{n}", 170, ORG, eo(pr(t, 1.5, 1.9)) * A, "Black")
    cv.text(540, 1300, "NUMBERS", 42, CREAM, eo(pr(t, 2.0, 2.5)) * A, "Bold")
    # map
    B = eo(pr(t, 3.6, 4.4))
    if B > 0:
        P = isogrid(cv, 540, 1040, 430, 215, 8, DIM, B, 3)
        rng = [(1.5, 6.2), (6.5, 2.0), (2.5, 3.0), (5.5, 5.5), (7.0, 6.6), (0.8, 1.5), (4.2, 7.2)]
        for (u, v) in rng:
            x, y = P(u, v); cv.circ(x, y, 8, fill=mix(DIM, ORG2, .5), a=B * .7)
        x, y = P(4.6, 3.6)
        drop = eback(pr(t, 4.0, 4.8), 1.8)
        py = lerp(y - 500, y - 160, cl(drop))
        cv.line([(x, py), (x, y)], ORG, 3, B * .6)
        ring(cv, x, y, t, ORG2, 3, 110, B * eo(pr(t, 4.6, 5.0)))
        cv.circ(x, y, 12, fill=ORG, a=B)
        cv.circ(x, py, 46, fill=ORG, a=B * .25); cv.circ(x, py, 26, fill=ORG, a=B); cv.circ(x, py, 10, fill=WHT, a=B)
        cv.text(540, 1370, "a point on a map of meaning", 40, AMB, eo(pr(t, 4.6, 5.2)), "Black")

# ---- S3 neighbours: dog photo, the word dog, a bark
DOGP = [(360, 740), (500, 820), (430, 650)]
CARP = [(770, 1090), (690, 1170), (850, 1170)]
STRT = [(180, 1150), (900, 540), (820, 900)]
def s3(cv, t, D):
    cv.text(540, 310, "MEANING = DISTANCE", 58, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 375, "similar things land close together", 32, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .1, .5))
    cv.rrect(80, 440, 1000, 1330, 36, fill=CARDC, a=p, outline=DIM, w=3, oa=p)
    for i in range(1, 9):
        cv.line([(80 + i * 102, 440), (80 + i * 102, 1330)], DIM, 1, p * .5)
    for i in range(1, 9):
        cv.line([(80, 440 + i * 99), (1000, 440 + i * 99)], DIM, 1, p * .5)
    m = eio(pr(t, .7, 2.0))
    for k in range(3):
        x = lerp(STRT[k][0], DOGP[k][0], m); y = lerp(STRT[k][1], DOGP[k][1], m)
        xc = lerp(CARP[k][0] - 60, CARP[k][0], 1); 
        cv.circ(CARP[k][0], CARP[k][1], 20, fill=DIM, a=p * .9)
        cv.circ(x, y, 50, fill=INK, a=p, outline=ORG, w=4, oa=p)
        ic_any(k, cv, x, y, 56, CREAM, p, t)
    g = eo(pr(t, 1.9, 2.5))
    cv.circ(430, 735, 190 * g, outline=AMB, w=4, oa=.55 * g)
    for a_, b_ in [(0, 1), (1, 2), (2, 0)]:
        cv.line([DOGP[a_], DOGP[b_]], AMB, 4, g * .8)
    labels = ["photo: dog", "word: dog", "sound: bark"]
    lp = [(300, 815), (570, 895), (520, 590)]
    for k in range(3):
        chip(cv, lp[k][0], lp[k][1], labels[k], 26, INK, ORG2, eo(pr(t, 2.1 + k * .15, 2.5 + k * .15)))
    cv.text(770, 1240, "car", 36, MUT, eo(pr(t, 2.6, 3.0)), "Bold")
    cv.text(770, 1030, "far away", 28, MUT, eo(pr(t, 2.8, 3.2)), "Medium")
    cv.text(430, 1290, "NEIGHBOURS", 40, AMB, eo(pr(t, 2.9, 3.4)), "Black")

# ---- S4 voice memo -> matching video clip
def s4(cv, t, D):
    cv.text(540, 310, "VOICE MEMO", 70, WHT, eo(pr(t, .05, .35)), "Black")
    cv.text(540, 380, "finds the right video clip", 36, ORG2, eo(pr(t, .2, .5)), "SemiBold")
    p = eo(pr(t, .05, .45))
    cv.rrect(190, 470, 890, 690, 36, fill=CARDC, a=p, outline=ORG, w=4, oa=p)
    for i in range(27):
        h = 18 + 70 * abs(math.sin(i * .9 + t * 7)) * math.sin(i / 26 * math.pi)
        x = 250 + i * 22.5
        cv.rrect(x - 5, 580 - h, x + 5, 580 + h, 5, fill=ORG2, a=p)
    beam = eo(pr(t, .3, .8))
    tx = 810
    dotted(cv, (540, 700), (tx, 985), t, 10, AMB, beam)
    dotted(cv, (540, 700), (270, 985), t + .3, 10, DIM, beam * .8)
    dotted(cv, (540, 700), (540, 985), t + .6, 10, DIM, beam * .8)
    for k in range(3):
        x = 270 + k * 270; m = (k == 2)
        f = eo(pr(t, 1.2, 1.6)) if m else 0
        cv.rrect(x - 115, 1000, x + 115, 1250, 24, fill=mix(CARDC, (40, 90, 90), f * .6), a=p, outline=mix(DIM, AMB, f), w=3 + 3 * f, oa=p)
        for j in range(2):
            cv.rrect(x - 100, 1020 + j * 200, x - 86, 1032 + j * 200, 3, fill=DIM, a=p)
            cv.rrect(x + 86, 1020 + j * 200, x + 100, 1032 + j * 200, 3, fill=DIM, a=p)
        cv.poly([(x - 60, 1200), (x - 10, 1120), (x + 20, 1170), (x + 45, 1140), (x + 75, 1200)], mix(DIM, CREAM, f * .9), p)
        cv.circ(x - 40, 1080, 16, fill=mix(DIM, AMB, f), a=p)
    c = pr(t, 1.3, 1.8)
    if c > 0: check(cv, 810, 1300, 60, c, AMB, 10)
    cv.text(540, 1385, "no captions needed", 34, CREAM, eo(pr(t, 1.6, 2.1)), "SemiBold")

# ---- S5 Matryoshka: 768 -> 256
NEST = [(768, 470, CREAM), (512, 370, ORG2), (256, 265, ORG), (128, 160, (150, 140, 230))]
def s5(cv, t, D):
    kinetic(cv, t, 320, "MATRYOSHKA", 92, WHT, .0, "Black", .035)
    cv.text(540, 400, "cut the vector shorter, keep the meaning", 32, ORG2, eo(pr(t, .4, .9)), "SemiBold")
    cy = 820
    for i, (n, sz, col) in enumerate(NEST):
        p = eback(pr(t, .5 + i * .35, 1.1 + i * .35), 1.8)
        hl = eo(pr(t, 5.0, 5.5)) if n == 256 else 0
        dim = 1 - .55 * eo(pr(t, 5.0, 5.5)) if n != 256 else 1
        if n == 128: dim *= 0.0 + 1
        s_ = sz * cl(p)
        cv.rrect(540 - s_, cy - s_ * .62, 540 + s_, cy + s_ * .62, 36, fill=mix(CARDC, col, .10 + .25 * hl), a=cl(p) * dim, outline=col, w=4 + 3 * hl, oa=cl(p) * dim)
        cv.text(540, cy - s_ * .62 + 34, str(n), 40 if n > 128 else 34, col, cl(p) * dim, "Black")
    # cut strip
    sx0, sy = 100, 1250
    N = 48
    keep = 16 / 48
    cutp = eio(pr(t, 2.8, 4.0))
    for k in range(N):
        x = sx0 + k * 18.75
        lit = k < N * keep
        a_ = 1 if lit else 1 - cutp * .88
        col = mix(ORG, AMB, k / N) if lit else DIM
        cv.rrect(x, sy, x + 15, sy + 70, 4, fill=col, a=eo(pr(t, 1.6 + k * .01, 2.0 + k * .01)) * a_)
    cx = sx0 + N * keep * 18.75 - 2
    sc = eo(pr(t, 3.0, 3.6))
    cv.line([(cx, sy - 30), (cx, sy + 100)], WHT, 4, sc)
    cv.text(cx - 20, sy + 125, "256", 36, ORG, sc, "Black", anchor="rm")
    cv.text(cx + 50, sy + 125, "768", 36, MUT, sc, "Bold", anchor="lm")
    q = eback(pr(t, 5.3, 5.9), 2)
    chip(cv, 540, 1385, "≈ LOSSLESS  ·  3× LESS STORAGE", 34, INK, AMB, cl(q))

# ---- S6 on a phone: 567 MB
def s6(cv, t, D):
    cv.text(540, 305, "RUNS ON A PHONE", 66, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 372, "Pixel 11 Pro  ·  quantized", 32, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    p = eback(pr(t, .2, .8), 1.6)
    cv.rrect(350, 440, 730, 1120, 56, fill=(6, 22, 26), a=cl(p), outline=CREAM, w=7, oa=cl(p))
    cv.rrect(378, 470, 702, 1090, 36, fill=(9, 40, 46), a=cl(p))
    cv.rrect(500, 452, 580, 466, 7, fill=CREAM, a=cl(p))
    # chip
    cp = eo(pr(t, 1.0, 1.6))
    cv.rrect(450, 700, 630, 880, 26, fill=INK, a=cp, outline=ORG, w=5, oa=cp)
    for k in range(5):
        cv.line([(475 + k * 32, 680), (475 + k * 32, 700)], ORG, 5, cp); cv.line([(475 + k * 32, 880), (475 + k * 32, 900)], ORG, 5, cp)
        cv.line([(430, 725 + k * 32), (450, 725 + k * 32)], ORG, 5, cp); cv.line([(630, 725 + k * 32), (650, 725 + k * 32)], ORG, 5, cp)
    cv.text(540, 790, "EG2", 64, ORG, cp, "Black")
    # files fly in
    for k in range(3):
        u = eio(pr(t, 1.2 + k * .5, 2.4 + k * .5))
        x = lerp((130, 950, 130)[k], 540, u); y = lerp((600, 760, 980)[k], 790, u)
        cv.rrect(x - 50, y - 42, x + 50, y + 42, 16, fill=INK, a=(1 - u) * cl(p), outline=AMB, w=3, oa=(1 - u) * cl(p))
        ic_any(k, cv, x, y, 60, CREAM, (1 - u) * cl(p), t)
    n = int(567 * eo(pr(t, 1.6, 3.4)))
    cv.text(540, 1215, f"{n} MB", 130, ORG, eo(pr(t, 1.5, 1.9)), "Black")
    cv.text(540, 1310, "active RAM, full model", 36, CREAM, eo(pr(t, 2.2, 2.7)), "SemiBold")
    q = eback(pr(t, 4.5, 5.1), 2)
    padlock(cv, 540, 980, 150, 0, AMB, cl(q))
    chip(cv, 540, 1400, "FILES STAY ON THE DEVICE", 32, INK, AMB, cl(q))

# ---- S7 code score + the catch
def s7(cv, t, D):
    cv.text(540, 300, "MTEB CODE", 76, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 368, "code-search score · higher is better", 30, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    base, sc = 1130, 6.8
    for i, (v, nm, col) in enumerate([(68.76, "EmbeddingGemma 1", (120, 160, 160)), (78.68, "EmbeddingGemma 2", ORG)]):
        x = 330 + i * 420
        g = eo(pr(t, .5 + i * 1.6, 1.6 + i * 1.6))
        h = v * sc * g
        cv.rrect(x - 120, base - h, x + 120, base, 22, fill=col, a=1)
        cv.text(x, base - h - 50, f"{v * g:.2f}", 64, WHT if i else CREAM, eo(pr(t, .5 + i * 1.6, .9 + i * 1.6)), "Black")
        cv.text(x, base + 50, nm, 28, CREAM, 1, "SemiBold")
    q = eback(pr(t, 3.2, 3.8), 2)
    chip(cv, 540, 435, "+9.92 POINTS", 40, INK, AMB, cl(q))
    s = eback(pr(t, 5.0, 5.7), 2)
    if s > .02:
        s = cl(s)
        cv.rrect(90, 1230, 990, 1410, 30, fill=(10, 24, 28), a=.96 * s, outline=AMB, w=5, oa=s)
        cv.text(540, 1290, "GOOGLE'S OWN SCORES", 56, AMB, s, "Black")
        cv.text(470, 1360, "independent tests still to come", 32, CREAM, s, "SemiBold")
        cv.arc(900, 1340, 26, (t * 320) % 360, (t * 320) % 360 + 250, AMB, 8, s)

# ---- S8 outro: rotating cloud of meaning
def s8(cv, t, D):
    p = eo(pr(t, .1, .9))
    N = 360
    for k in range(N):
        y = 1 - 2 * (k + .5) / N; r = math.sqrt(1 - y * y); th = k * 2.399963 + t * .6
        x, z = r * math.cos(th), r * math.sin(th)
        sx, sy = 540 + x * 300, 690 + y * 300
        d = (z + 1) / 2
        col = mix(ORG, AMB, (k % 7) / 10 if k % 9 == 0 else 0)
        cv.circ(sx, sy, 3 + 5 * d, fill=col, a=p * (.2 + .7 * d))
    kinetic(cv, t, 1090, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1200, "Voyaging the Unseen", 46, AMB, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1290, "what would you search for by sound?", 32, ORG2, eo(pr(t, 1.8, 2.3)), "Medium")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
