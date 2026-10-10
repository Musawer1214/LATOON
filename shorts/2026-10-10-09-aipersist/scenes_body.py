def s0(cv, t, D):
    kinetic(cv, t, 300, "10 MINUTES", 124, INKC, -.2, "Black", .03)
    kinetic(cv, t, 420, "with an AI helper", 50, MUST, .3, "Bold", .02)
    photo(cv, "computer", 90, 490, 990, 1010, t / D, 1.0, 1.2, .5, .5)
    brackets(cv, 90, 490, 990, 1010, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Michael Surran, CC BY-SA 2.0", 1040, eo(pr(t, .8, 1.3)), 100, "lm")
    sa = eo(pr(t, .3, .7))
    stopwatch(cv, 800, 1050, 150, eio(pr(t, .4, 2.6)), sa)
    q = eback(pr(t, 2.2, 2.7), 2)
    chip(cv, 110, 1290, 860, "...AND GIVE UP SOONER", CORAL, cl(q * 1.4), INKC, 52, 104)
def s1(cv, t, D):
    kinetic(cv, t, 300, "FRACTION PROBLEMS", 84, INKC, -.2, "Black", .02)
    for (x0, x1, lab, col, ts) in [(70, 520, "ON THEIR OWN", TEAL, .5), (560, 1010, "CHATGPT OPEN BESIDE", MUST, 1.0)]:
        a = eo(pr(t, ts - .3, ts + .3))
        card(cv, x0, 450, x1, 1130, 28, PAPER, a)
        cx = (x0 + x1) / 2
        cv.text(cx, 505, "PROBLEM 7 OF 15", 26, mix(INK, PAPER, .4), a, "Black")
        frac(cv, cx - 100, 640, "3", "4", 72, INK, a)
        cv.text(cx - 24, 640, "+", 58, INK, a, "Black")
        frac(cv, cx + 52, 640, "1", "6", 72, INK, a)
        cv.text(cx + 132, 640, "=", 58, INK, a, "Black")
        cv.text(cx + 188, 640, "?", 72, CORAL, a, "Black")
        for k in range(3):
            cv.line([(x0 + 40, 800 + k * 62), (x1 - 40, 800 + k * 62)], mix(PAPER2, INK, .1), 3, a * .9)
        chip(cv, x0 + 30, 1040, x1 - x0 - 60, lab, col, a, INK, 25, 64)
    # handwriting on the left card, chat bubbles on the right
    wr = eo(pr(t, 1.2, 2.8))
    if wr > .01:
        pts = [(110 + i * 8, 780 + math.sin(i * .9) * 10) for i in range(int(40 * wr))]
        if len(pts) > 1: cv.line(pts, mix(INK, TEAL, .3), 4, .9)
    ba = eo(pr(t, 2.4, 2.9)); bb = eo(pr(t, 3.5, 4.0))
    bubble(cv, 595, 770, 905, 840, ["what's 3/4 + 1/6?"], PAPER2, INK, ba, 27, 22)
    bubble(cv, 650, 880, 975, 960, ["11/12. Done."], MUST, INK, bb, 32, 22)
    cv.text(540, 1215, "15 problems  \u00b7  randomized groups", 36, MUST, eo(pr(t, 3.9, 4.4)), "Bold")
def s2(cv, t, D):
    kinetic(cv, t, 300, "AT FIRST...", 104, INKC, -.2, "Black", .03)
    base = 1260
    cv.line([(150, base), (930, base)], mix(INK, PAPER, .2), 5, eo(pr(t, 0, .3)))
    for x, h, col, lab, t0 in [(340, 360, TEAL, "NO HELP", .3), (740, 520, MUST, "WITH AI", .6)]:
        g = eo(pr(t, t0, t0 + .7))
        cv.rrect(x - 110, base - h * g + 10, x + 110, base + 10, 14, fill=SHAD, a=.45)
        cv.rrect(x - 110, base - h * g, x + 110, base, 14, fill=col)
        cv.rrect(x - 110, base - h * g, x - 60, base, 14, fill=mix(col, PAPER, .25))
        cv.text(x, base + 52, lab, 36, PAPER, g, "Black")
    ua = eback(pr(t, 1.2, 1.6), 2)
    arrow(cv, 740, 700, 740, 620, CORAL, 12, cl(ua * 1.4), 34)
    cv.text(740, 575, "ACCURACY", 34, INKC, eo(pr(t, 1.2, 1.6)), "Black")
    cv.text(540, 440, "helped group scored higher", 42, MUST, eo(pr(t, .2, .7)), "Bold")
def s3(cv, t, D):
    kinetic(cv, t, 300, "PROBLEM 12", 112, INKC, -.2, "Black", .03)
    rowsy = [720, 890]
    # 15 dots: 8 on row 1, 7 on row 2
    for i in range(15):
        row = 0 if i < 8 else 1; col_i = i if i < 8 else i - 8
        x = 150 + col_i * 111; y = rowsy[row]
        a = eo(pr(t, .1 + i * .06, .35 + i * .06))
        done = i < 12
        cv.circ(x + 4, y + 8, 40, fill=SHAD, a=.4 * a)
        cv.circ(x, y, 40, fill=PAPER if done else mix(PAPER, BG1, .55), a=a)
        cv.text(x, y, str(i + 1), 34, INK, a, "Black")
    # helper band across 1..12
    off = eio(pr(t, 1.9, 2.4))
    ba = eo(pr(t, .6, 1.0)) * (1 - off)
    cv.rrect(105, 655, 975, 785, 60, outline=MUST, w=6, oa=ba)
    cv.rrect(105, 825, 800, 955, 60, outline=MUST, w=6, oa=ba)
    chip(cv, 300, 520, 480, "AI HELPER ON", MUST, ba, INK, 36, 76)
    if off > .01:
        chip(cv, 250, 520, 580, "AI HELPER GONE", CORAL, off, INKC, 38, 80)
    cv.text(540, 1090, "the chatbot vanished", 60, INKC, eo(pr(t, 2.1, 2.6)), "Black")
    cv.text(540, 1175, "3 problems left", 38, MUST, eo(pr(t, 2.4, 2.9)), "Bold")
    # drifting chat bubble that fades out
    fx = eo(pr(t, 1.9, 3.0))
    bubble(cv, 260 - 200 * fx, 1250, 820 - 200 * fx, 1340, ["Sure! Here's the answer..."], PAPER2, INK, (1 - fx) * eo(pr(t, 1.6, 1.9)), 34, 36)
def s4(cv, t, D):
    kinetic(cv, t, 300, "THEN THE DROP", 96, INKC, -.2, "Black", .02)
    X = lambda i: 170 + (i - 1) / 14 * 760
    helped = [.70, .78, .80, .82, .80, .84, .83, .85, .84, .86, .85, .87, .46, .40, .36]
    plain = [.55, .58, .60, .62, .63, .65, .66, .67, .68, .70, .71, .72, .74, .75, .77]
    sk_h = [.04, .04, .05, .04, .05, .04, .05, .04, .05, .04, .05, .05, .22, .30, .36]
    sk_p = [.05, .04, .05, .05, .04, .05, .04, .05, .05, .04, .05, .04, .05, .05, .04]
    def draw(vals, p, base, sc, col):
        n = p * 14; pts = []
        for i in range(15):
            if i <= n: pts.append((X(i + 1), base - vals[i] * sc))
            elif i - 1 < n:
                f = n - (i - 1)
                pts.append((lerp(X(i), X(i + 1), f), base - lerp(vals[i - 1], vals[i], f) * sc))
        if len(pts) > 1:
            cv.line(pts, col, 9, 1)
            cv.circ(pts[-1][0], pts[-1][1], 12, fill=col)
    a1 = eo(pr(t, 0, .4)); a2 = eo(pr(t, 2.4, 2.8))
    card(cv, 70, 430, 1010, 880, 30, PAPER, a1)
    cv.text(120, 470, "SOLVED CORRECTLY", 28, INK, a1, "Black", "lm")
    cv.line([(150, 830), (950, 830)], mix(INK, PAPER, .3), 3, a1)
    cv.line([(X(12), 520), (X(12), 830)], CORAL, 3, a1 * .9)
    cv.text(X(12) - 10, 805, "AI REMOVED", 22, CORAL, a1, "Black", "rm")
    draw(plain, eio(pr(t, .4, 2.4)), 830, 340, TEAL)
    draw(helped, eio(pr(t, .4, 2.4)), 830, 340, CORAL)
    card(cv, 70, 920, 1010, 1380, 30, PAPER, a2)
    cv.text(120, 962, "QUESTIONS SKIPPED", 28, INK, a2, "Black", "lm")
    cv.line([(150, 1320), (950, 1320)], mix(INK, PAPER, .3), 3, a2)
    cv.line([(X(12), 1010), (X(12), 1320)], CORAL, 3, a2 * .9)
    p2 = eio(pr(t, 2.7, 4.5))
    if p2 > 0:
        draw(sk_p, p2, 1320, 600, TEAL)
        draw(sk_h, p2, 1320, 600, CORAL)
    chip(cv, 640, 1000, 190, "AI", CORAL, a1, INKC, 26, 46)
    chip(cv, 840, 1000, 140, "NO AI", TEAL, a1, INKC, 26, 46)
    cv.text(540, 1415, "schematic of the reported pattern, not measured values", 21, ASH, eo(pr(t, 1.0, 1.5)), "SemiBold")
def s5(cv, t, D):
    kinetic(cv, t, 300, "IT REPEATED", 104, INKC, -.2, "Black", .03)
    for x0, x1, lab, ts in [(70, 520, "FRACTIONS", .4), (560, 1010, "READING", .9)]:
        a = eo(pr(t, ts, ts + .4))
        card(cv, x0, 430, x1, 700, 28, PAPER, a)
        cx = (x0 + x1) / 2
        cv.text(cx, 520, lab, 42, INK, a, "Black")
        if lab == "FRACTIONS":
            frac(cv, cx, 625, "3", "4", 52, CORAL, a)
        else:
            for k in range(4): cv.line([(cx - 120, 590 + k * 28), (cx + 120 - (k == 3) * 80, 590 + k * 28)], mix(INK, PAPER, .3), 5, a)
        check(cv, x1 - 62, 478, 24, eo(pr(t, ts + .4, ts + .8)), TEAL, 8, a)
    n = int(1222 * eo(pr(t, 2.2, 3.4)))
    cv.text(540, 880, "{:,}".format(n), 170, INKC, eo(pr(t, 2.1, 2.5)), "Black")
    cv.text(540, 1012, "PEOPLE, IN RANDOMIZED TRIALS", 38, MUST, eo(pr(t, 2.6, 3.1)), "Black")
    k = int(48 * eo(pr(t, 2.3, 3.8)))
    for i in range(48):
        if i >= k: break
        icon_person(cv, 130 + (i % 16) * 55, 1115 + (i // 16) * 90, 40, PAPER if i % 5 else MUST, 1)
    cv.text(540, 1385, "adults tested online", 28, ASH, eo(pr(t, 3.4, 3.9)), "SemiBold")
def s6(cv, t, D):
    kinetic(cv, t, 300, "THE TEAM'S IDEA", 90, INKC, -.2, "Black", .02)
    nodes = [(540, 620, "ASK", TEAL), (790, 1020, "INSTANT ANSWER", MUST), (290, 1020, "EXPECT IT AGAIN", CORAL)]
    # arrows
    for k, (p0, p1) in enumerate([(0, 1), (1, 2), (2, 0)]):
        ta = .5 + k * .9
        q = eio(pr(t, ta, ta + .7))
        x0, y0, _, _ = nodes[p0]; x1, y1, _, _ = nodes[p1]
        sx, sy, ex, ey = [(600, 690, 750, 925), (600, 1020, 480, 1020), (330, 925, 480, 700)][k]
        arrow(cv, sx, sy, lerp(sx, ex, q), lerp(sy, ey, q), PAPER, 9, q if q > .05 else 0, 30)
    for k, (x, y, lab, col) in enumerate(nodes):
        a = eback(pr(t, .1 + k * .8, .5 + k * .8), 2)
        s = lerp(.7, 1, cl(a)); w = 190 if k else 130
        cv.rrect(x - w * s + 6, y - 60 * s + 12, x + w * s + 6, y + 60 * s + 12, 36, fill=SHAD, a=.45 * cl(a))
        cv.rrect(x - w * s, y - 60 * s, x + w * s, y + 60 * s, 36, fill=col, a=cl(a))
        cv.text(x, y, lab, int(36 * s) if k else int(46 * s), INK if col != CORAL else INKC, cl(a), "Black")
    # loop pulse
    pa = eo(pr(t, 3.0, 3.5))
    cv.circ(540, 880, 120, outline=MUST, w=4, oa=.45 * pa)
    cv.text(540, 862, "less time", 32, INKC, pa, "Bold"); cv.text(540, 902, "struggling", 32, INKC, pa, "Bold")
    ch = eo(pr(t, 3.7, 4.2))
    card(cv, 100, 1190, 980, 1380, 30, PAPER, ch)
    cv.text(540, 1255, "denied the experience of", 34, mix(INK, PAPER, .25), ch, "SemiBold")
    cv.text(540, 1318, "working through challenges", 46, INK, ch, "Black")
def s7(cv, t, D):
    kinetic(cv, t, 300, "BRIAN CHRISTIAN", 84, INKC, -.2, "Black", .02)
    cv.text(540, 395, "co-author  \u00b7  UC Berkeley, Center for Human-Compatible AI", 27, MUST, eo(pr(t, .3, .8)), "SemiBold")
    photo(cv, "christian", 90, 450, 480, 960, t / D, 1.0, 1.12, .5, .35)
    photo(cv, "pen", 520, 450, 990, 960, t / D, 1.05, 1.25, .35, .6)
    for (a, b, c, d) in [(90, 450, 480, 960), (520, 450, 990, 960)]:
        brackets(cv, a, b, c, d, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Brian Christian: Eileen Meny, CC BY-SA 4.0", 988, eo(pr(t, .8, 1.3)), 90, "lm")
    credit(cv, "Pen: Aaron Burden, CC0", 1016, eo(pr(t, .8, 1.3)), 90, "lm")
    nb = eback(pr(t, 1.8, 2.3), 2)
    chip(cv, 548, 868, 410, "WRITES EVERY DAY", MUST, cl(nb * 1.4), INK, 38, 70)
    photo(cv, "sather", 90, 1080, 990, 1400, t / D, 1.0, 1.15, .5, .45)
    brackets(cv, 90, 1080, 990, 1400, PAPER, eo(pr(t, .6, 1.1)) * .9)
    credit(cv, "Sather Tower, UC Berkeley: Coolcaesar, CC BY-SA 4.0", 1428, eo(pr(t, 1.0, 1.5)))
def s8(cv, t, D):
    kinetic(cv, t, 300, "NOT LESS AI", 112, INKC, -.2, "Black", .03)
    a1 = eo(pr(t, .3, .7)); a2 = eo(pr(t, 1.4, 1.8))
    card(cv, 60, 440, 520, 1060, 30, mix(PAPER, BG1, .35), a1)
    card(cv, 560, 440, 1020, 1060, 30, PAPER, a2)
    cv.text(290, 495, "ANSWER MACHINE", 30, mix(INK, PAPER, .4), a1, "Black")
    cv.text(790, 495, "TUTOR", 34, INK, a2, "Black")
    bubble(cv, 90, 560, 330, 630, ["3/4 + 1/6?"], PAPER2, INK, a1, 28, 22)
    bubble(cv, 250, 700, 490, 770, ["11/12."], mix(MUST, BG1, .45), INK, eo(pr(t, .7, 1.1)), 30, 22)
    cv.text(290, 880, "answer given,", 28, mix(INK, PAPER, .35), a1, "Bold")
    cv.text(290, 920, "nothing practised", 28, mix(INK, PAPER, .35), a1, "Bold")
    bubble(cv, 590, 560, 830, 630, ["3/4 + 1/6?"], PAPER2, INK, a2, 28, 22)
    bubble(cv, 700, 660, 1000, 770, ["What number do", "4 and 6 both fit in?"], MUST, INK, eo(pr(t, 2.0, 2.4)), 27, 22)
    bubble(cv, 790, 800, 990, 860, ["12?"], PAPER2, INK, eo(pr(t, 2.6, 3.0)), 30, 22)
    bubble(cv, 590, 890, 960, 960, ["Yes. Now convert both."], MUST, INK, eo(pr(t, 3.0, 3.4)), 27, 22)
    chip(cv, 180, 1140, 720, "SCAFFOLDS LEARNING", TEAL, eo(pr(t, 3.2, 3.7)), INK, 44, 96)
    cv.text(540, 1270, "the study's call for AI design", 26, ASH, eo(pr(t, 3.5, 4.0)), "SemiBold")
def s9(cv, t, D):
    # compass ring of ticks
    p = eio(pr(t, 0, 1.6))
    for k in range(72):
        ang = math.radians(k * 5 - 90 + 30 * p); r0 = 330; r1 = 330 + (46 if k % 6 == 0 else 24)
        cv.line([(540 + r0 * math.cos(ang), 760 + r0 * math.sin(ang)), (540 + r1 * math.cos(ang), 760 + r1 * math.sin(ang))],
                MUST if k % 6 == 0 else PAPER, 5 if k % 6 == 0 else 3, eo(pr(t, k * .01, k * .01 + .4)) * .9)
    kinetic(cv, t, 740, "LATOON", 150, INKC, -.1, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, MUST, eo(pr(t, .9, 1.5)), "SemiBold")
    chip(cv, 280, 1110, 520, "FOLLOW", MUST, eo(pr(t, 1.6, 2.2)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
