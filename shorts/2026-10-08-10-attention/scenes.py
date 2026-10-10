# Attention explainer: cream paper palette, ink, terracotta
BG0, BG1 = (240, 231, 214), (226, 213, 190)
INKC = (34, 28, 24); WHT = INKC
TERRA, MUST, FOR, PLUM = (196, 74, 46), (212, 150, 36), (42, 108, 88), (112, 62, 92)
PAPER, EDGE, SHAD = (252, 247, 236), (150, 130, 104), (190, 172, 146)
GOLD = TERRA; BL, BL2 = TERRA, TERRA
NOFADE_IN, NOFADE_OUT = {0}, set()
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (240, 231, 214), 0.0)
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
SENT = ["The", "animal", "didn't", "cross", "the", "street", "because", "it", "was", "too", "tired."]
ROWS = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
FS = 54
CAPC = (252, 247, 236)
def layout(cv, words, y0=860, dy=200):
    pos = {}; wid = {}
    for r, row in enumerate(ROWS):
        ws = [cv.tw(words[i], FS, "Bold") + 56 for i in row]; tot = sum(ws) + 20 * (len(row) - 1)
        x = 540 - tot / 2
        for i, w_ in zip(row, ws):
            pos[i] = (x + w_ / 2, y0 + r * dy); wid[i] = w_; x += w_ + 20
    return pos, wid
def chips(cv, words, pos, wid, t, t0=0, step=.12, hl=None, dim=None, a=1):
    for i, w_ in enumerate(words):
        p = eback(pr(t, t0 + i * step, t0 + i * step + .3), 2)
        if p <= 0: continue
        x, y = pos[i]; h = 42 * p
        col = PAPER; tc = INKC; oc = EDGE
        if hl and i in hl: col = hl[i]; tc = PAPER; oc = hl[i]
        card(cv, x - wid[i] / 2 * p, y - h, x + wid[i] / 2 * p, y + h, 24, fill=col, outline=oc, a=cl(p) * a)
        cv.text(x, y - 2, w_, FS, tc, cl(p * 1.4) * a, "Bold")
def curve(cv, p0, p1, col, w, a, bend=1.0, k=1.0):
    (x0, y0), (x1, y1) = p0, p1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy) or 1
    cx, cy = mx - dy / L * L * .28 * bend, my + dx / L * L * .28 * bend
    n = 32; pts = []
    for j in range(int(n * k) + 1):
        u = j / n
        pts.append(((1 - u) ** 2 * x0 + 2 * u * (1 - u) * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * u * (1 - u) * cy + u * u * y1))
    if len(pts) > 1: cv.line(pts, col, w, a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 66, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or TERRA, eo(pr(t, .3, .7)), "SemiBold")
W1 = {1: .62, 5: .12, 0: .03, 2: .04, 3: .05, 4: .02, 6: .05, 8: .03, 9: .02, 10: .02}
W2 = {1: .12, 5: .62, 0: .03, 2: .04, 3: .05, 4: .04, 6: .05, 8: .03, 9: .02, 10: .02}
def s0(cv, t, D):
    cv.rrect(240, 380, 840, 440, 30, fill=TERRA, a=eo(pr(t, 0, .3)))
    cv.text(540, 408, "HOW AI READS", 32, PAPER, eo(pr(t, 0, .3)), "Black")
    kinetic(cv, t, 600, "WHAT DOES", 120, INKC, -.2, "Black", .02)
    q = eback(pr(t, .1, .6), 2)
    card(cv, 340, 760, 740, 1010, 40, fill=TERRA, outline=TERRA, a=cl(q))
    cv.text(540, 880, "“it”", 190 * q, PAPER, cl(q), "Black")
    kinetic(cv, t, 1170, "MEAN?", 130, INKC, .3, "Black", .03)
    cv.text(540, 1300, "to a machine", 44, PLUM, eo(pr(t, 1.0, 1.5)), "SemiBold")
def s1(cv, t, D):
    head(cv, t, "ONE SENTENCE", "read it like a computer would")
    pos, wid = layout(cv, SENT)
    chips(cv, SENT, pos, wid, t, .3, .2, hl={7: TERRA} if t > 3.2 else None)
def s2(cv, t, D):
    head(cv, t, "YOU vs COMPUTER", None)
    pos, wid = layout(cv, SENT, 560, 130)
    for i in pos: pass
    chips(cv, SENT, {i: (x, y) for i, (x, y) in pos.items()}, wid, 9, hl={7: TERRA})
    p = eback(pr(t, .6, 1.2), 2)
    card(cv, 90, 1040, 520, 1380, 30, a=cl(p)); card(cv, 560, 1040, 990, 1380, 30, a=cl(p))
    cv.text(305, 1100, "YOU", 44, FOR, cl(p), "Black")
    cv.text(305, 1200, "it = the animal", 38, INKC, cl(p), "Bold")
    check(cv, 305, 1295, 46, eo(pr(t, 1.3, 1.9)), FOR, 12)
    q = eo(pr(t, 2.3, 2.9))
    cv.text(775, 1100, "COMPUTER", 44, TERRA, q, "Black")
    cv.text(775, 1200, "it = 4102", 54, INKC, q, "Black")
    cv.text(775, 1290, "just a number", 32, PLUM, q, "SemiBold")
def s3(cv, t, D):
    head(cv, t, "EVERY WORD LOOKS", "at every other word")
    pos, wid = layout(cv, SENT)
    ks = list(pos)
    n = 0
    for i in ks:
        for j in ks:
            if i < j:
                f = pr(t, .4 + n * .035, .9 + n * .035); n += 1
                if f > 0: curve(cv, pos[i], pos[j], PLUM, 2.5, .35 * min(1, f * 3), 1 if (i + j) % 2 else -1, f)
    chips(cv, SENT, pos, wid, 9, a=.96)
    cv.text(540, 1385, "who matters to me?", 52, TERRA, eo(pr(t, 3.0, 3.6)), "Black")
def s4(cv, t, D):
    head(cv, t, "ATTENTION", "a score for every pair")
    names = [("animal", .62), ("street", .12), ("cross", .05), ("tired.", .02)]
    card(cv, 120, 560, 960, 1340, 36, a=eo(pr(t, 0, .4)))
    cv.text(540, 640, "how much “it” looks at…", 40, INKC, eo(pr(t, .2, .6)), "Bold")
    for k, (n_, v) in enumerate(names):
        y = 780 + k * 130; p = eo(pr(t, .6 + k * .35, 1.4 + k * .35))
        cv.text(250, y, n_, 40, INKC, p, "Bold")
        cv.rrect(400, y - 26, 900, y + 26, 26, fill=(232, 220, 196), a=p)
        if p > .05: cv.rrect(400, y - 26, 400 + 500 * v * p / .62 * .9 if False else 400 + 60 + 440 * v / .62 * p, y + 26, 26, fill=TERRA if k == 0 else MUST, a=p)
        cv.text(930, y, f"{v * p:.2f}", 32, INKC, p, "Black", anchor="rm") if False else cv.text(850, y, f"{v * p:.2f}", 30, PAPER if k == 0 else INKC, p, "Black")
def s5(cv, t, D):
    head(cv, t, "“IT” LOOKS AT…", "the animal, not the street")
    pos, wid = layout(cv, SENT)
    for i, v in W1.items():
        f = eo(pr(t, .5, 1.3 if i in (1, 5) else 1.6))
        curve(cv, pos[7], pos[i], TERRA if i == 1 else PLUM, 3 + v * 30, (.95 if v > .1 else .3) * f, 1.0 if i != 1 else -1.0, f)
    chips(cv, SENT, pos, wid, 9, hl={7: TERRA, 1: FOR})
    cv.text(540, 1385, "0.62  vs  0.12", 64, INKC, eo(pr(t, 1.4, 2.0)), "Black")
def s6(cv, t, D):
    head(cv, t, "CHANGE ONE WORD", None)
    flip = eio(pr(t, 1.0, 1.8))
    words = SENT[:10] + ["wide." if t > 1.4 else "tired."]
    pos, wid = layout(cv, words)
    if t > 1.4:
        pos, wid = layout(cv, words)
    for i, v in W1.items():
        v2 = W1[i] * (1 - flip) + W2[i] * flip
        col = TERRA if (i == 5 and flip > .5) or (i == 1 and flip <= .5) else PLUM
        curve(cv, pos[7], pos[i], col, 3 + v2 * 30, (.95 if v2 > .1 else .3), 1.0 if i != 1 else -1.0)
    chips(cv, words, pos, wid, 9, hl={7: TERRA, (5 if flip > .5 else 1): FOR})
    cv.text(540, 1385, "tired → wide:  “it” = the street", 40, INKC, eo(pr(t, 2.0, 2.6)), "Black")
def s7(cv, t, D):
    head(cv, t, "DOZENS OF LAYERS", "invisible links, stacked")
    n = 6
    for k in range(n):
        p = eback(pr(t, .3 + k * .3, .8 + k * .3), 1.5)
        y = 1180 - k * 120 - (1 - p) * 120; x = 540 + (k - 2.5) * 22
        card(cv, x - 380, y - 36, x + 380, y + 36, 20, fill=(252 - k * 4, 247 - k * 6, 236 - k * 10), a=cl(p))
        for j in range(5):
            u0 = x - 300 + j * 125
            curve(cv, (u0, y), (u0 + 120, y), TERRA if (j + k) % 3 == 0 else PLUM, 3, .8 * cl(p), 1, 1)
        cv.text(x - 340, y, f"{k + 1}", 24, EDGE, cl(p), "Black")
    cv.text(540, 1330, "meaning builds layer by layer", 40, INKC, eo(pr(t, 2.6, 3.2)), "Bold")
def s8(cv, t, D):
    head(cv, t, "ONE IDEA INSIDE", "the transformer")
    for k, (n_, c) in enumerate([("ChatGPT", FOR), ("Gemini", PLUM), ("Claude", MUST)]):
        p = eback(pr(t, .6 + k * .5, 1.1 + k * .5), 2); y = 700 + k * 190
        card(cv, 220, y - 70, 860, y + 70, 36, fill=c, outline=c, a=cl(p))
        cv.text(540, y - 3, n_, 70, PAPER, cl(p), "Black")
    cv.text(540, 1320, "all built on attention", 42, TERRA, eo(pr(t, 2.4, 3.0)), "Black")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=TERRA, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=TERRA, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, TERRA, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
