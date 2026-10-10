# Bytes explainer: blush paper, ink, deep teal, coral, mustard
BG0, BG1 = (240, 222, 204), (228, 206, 186)
INKC = (38, 30, 32); WHT = (252, 246, 236)
TEAL, CORAL, MUST, PLUM = (34, 92, 100), (208, 84, 62), (222, 162, 48), (110, 62, 86)
PAPER, EDGE, SHAD = (252, 246, 236), (150, 118, 98), (200, 168, 146)
GOLD = CORAL; BL, BL2 = CORAL, CORAL
NOFADE_IN, NOFADE_OUT = {0}, set()
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (240, 222, 204), 0.0)
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
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or CORAL, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or PAPER, a, "Black")
def arrow(cv, x, y, a=1, c=INKC):
    cv.line([(x - 26, y), (x + 26, y)], c, 9, a); cv.line([(x + 6, y - 20), (x + 28, y), (x + 6, y + 20)], c, 9, a)
def ltile(cv, x, y, s, ch, col=PAPER, tc=INKC, a=1):
    cv.rrect(x + 5, y + 8, x + s + 5, y + s + 8, 14, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + s, y + s, 14, fill=col, a=a, outline=EDGE, w=3, oa=a)
    cv.text(x + s / 2, y + s / 2 + 2, ch, int(s * .6), tc, a, "Black")
WORD = "STRAWBERRY"
def word(cv, x0, y, s, gap, a=1, hi=None, cols=None):
    for i, c in enumerate(WORD):
        col = PAPER; tc = INKC
        if hi and c in hi: col = CORAL; tc = PAPER
        if cols: col = cols[i]; tc = PAPER
        ltile(cv, x0 + i * (s + gap), y, s, c, col, tc, a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "YOUR AI CAN'T", 84, INKC, -.2, "Black", .02)
    kinetic(cv, t, 430, "SEE LETTERS", 84, CORAL, -.1, "Black", .02)
    s = 86; g = 6; x0 = 540 - (10 * s + 9 * g) / 2
    for i in range(10):
        a_ = eback(pr(t, .1 + i * .06, .5 + i * .06), 2)
        ltile(cv, x0 + i * (s + g), 700 + (1 - cl(a_)) * 60, s, WORD[i], a=cl(a_))
    v = eio(pr(t, 1.3, 2.4))
    cv.rrect(x0 - 20, 680, x0 - 20 + (10 * s + 9 * g + 40) * v, 810, 20, fill=TEAL, a=1)
    if v > .5: cv.text(540, 745, "?  ?  ?  ?  ?", 80, PAPER, cl((v - .5) * 2), "Black")
    cv.text(540, 1000, "it reads chunks, not letters", 46, PLUM, eo(pr(t, 2.2, 2.8)), "Bold")
def s1(cv, t, D):
    head(cv, t, "FIRST, IT CHOPS TEXT", "into tokens: word fragments")
    parts = ["Lang", "uage", " mod", "els", " read", " tok", "ens"]
    cols = [TEAL, CORAL, MUST, PLUM, TEAL, CORAL, MUST]
    ws = [cv.tw(p, 54, "Black") + 44 for p in parts]
    rows = [[0, 1, 2], [3, 4, 5, 6]]
    k = 0
    for ri, row in enumerate(rows):
        tot = sum(ws[j] for j in row) + 20 * (len(row) - 1); x = 540 - tot / 2
        for j in row:
            a_ = eback(pr(t, .6 + j * .45, 1.1 + j * .45), 2)
            y = 640 + ri * 190 - (1 - cl(a_)) * 40
            cv.rrect(x + 5, y + 8, x + ws[j] + 5, y + 118, 20, fill=SHAD, a=.6 * cl(a_))
            cv.rrect(x, y, x + ws[j], y + 110, 20, fill=cols[j], a=cl(a_))
            cv.text(x + ws[j] / 2, y + 57, parts[j], 54, PAPER, cl(a_), "Black")
            x += ws[j] + 20
    cv.text(540, 1100, "example split, real tokenizers vary", 34, EDGE, eo(pr(t, 3.5, 4.0)), "SemiBold")
def s2(cv, t, D):
    head(cv, t, "A WORD ARRIVES IN CHUNKS", "so counting letters is a guess")
    parts = [("STR", 3, TEAL), ("AW", 2, CORAL), ("BERRY", 5, MUST)]
    s = 86; g = 6; x0 = 540 - (10 * s + 9 * g) / 2
    i0 = 0
    for p, n, col in parts:
        a_ = eback(pr(t, .4 + i0 * .1, .9 + i0 * .1), 2)
        w = n * s + (n - 1) * g
        cv.rrect(x0 + i0 * (s + g) - 12 + 6, 600 + 8, x0 + i0 * (s + g) + w + 12 + 6, 740 + 8, 24, fill=SHAD, a=.6 * cl(a_))
        cv.rrect(x0 + i0 * (s + g) - 12, 600, x0 + i0 * (s + g) + w + 12, 740, 24, fill=col, a=cl(a_))
        for j in range(n):
            cv.text(x0 + (i0 + j) * (s + g) + s / 2, 670, WORD[i0 + j], 64, PAPER, cl(a_), "Black")
        i0 += n
    q = eback(pr(t, 2.2, 2.8), 2)
    card(cv, 150, 860, 930, 1100, 40, a=cl(q))
    cv.text(540, 940, "How many R's?", 66, INKC, cl(q), "Black")
    cv.text(540, 1035, "the model never saw them one by one", 36, PLUM, cl(q), "SemiBold")
def s3(cv, t, D):
    head(cv, t, "OCTOBER 7: A NEW PAPER", "published in Nature")
    q = eback(pr(t, .3, .9), 2)
    card(cv, 100, 520, 980, 1000, 40, a=cl(q))
    cv.rrect(100, 520, 980, 600, 40, fill=TEAL, a=cl(q)); cv.rect(100, 570, 980, 600, fill=TEAL, a=cl(q)) if hasattr(cv, "rect") else None
    cv.text(540, 562, "NATURE  ·  7 OCT 2026", 34, PAPER, cl(q), "Black")
    txt = "Retrofitting language models to operate over bytes"
    lines = ["Retrofitting language", "models to operate", "over bytes"]
    n = int(len(txt) * eo(pr(t, 1.0, 3.2))); used = 0
    for i, ln in enumerate(lines):
        m = max(0, min(len(ln), n - used)); used += len(ln) + 1
        cv.text(150, 690 + i * 90, ln[:m], 58, INKC, 1, "Black", anchor="lm")
    chip(cv, 290, 1130, 500, "READ RAW BYTES", CORAL, eback(pr(t, 3.4, 4.0), 2), size=40, h=86)
def s4(cv, t, D):
    head(cv, t, "A BYTE: 8 SWITCHES", "every letter is a pattern of 0s and 1s")
    data = [("S", "01010011"), ("T", "01010100"), ("R", "01010010")]
    for r, (ch, bits) in enumerate(data):
        a_ = eback(pr(t, .4 + r * .9, .9 + r * .9), 2)
        y = 560 + r * 220
        ltile(cv, 90, y, 120, ch, a=cl(a_))
        arrow(cv, 250, y + 60, cl(a_), CORAL)
        for i, b in enumerate(bits):
            on = b == "1"
            x = 310 + i * 80
            cv.rrect(x + 4, y + 10, x + 70 + 4, y + 110 + 4, 14, fill=SHAD, a=.6 * cl(a_))
            cv.rrect(x, y + 6, x + 70, y + 106, 14, fill=TEAL if on else PAPER, a=cl(a_), outline=EDGE, w=3, oa=cl(a_))
            cv.text(x + 35, y + 58, b, 48, PAPER if on else EDGE, cl(a_), "Black")
    cv.text(540, 1290, "no chunks: just the raw letters", 42, PLUM, eo(pr(t, 3.6, 4.2)), "Bold")
def s5(cv, t, D):
    head(cv, t, "WHY IT LAGGED BEHIND", "more pieces means more work")
    card(cv, 70, 520, 1010, 760, 34)
    cv.text(120, 560, "TOKENS", 34, TEAL, 1, "Black", anchor="lm")
    for i, (x, w, col) in enumerate([(120, 250, TEAL), (390, 170, CORAL), (580, 330, MUST)]):
        a_ = eback(pr(t, .4 + i * .25, .8 + i * .25), 2)
        cv.rrect(x, 610, x + w * cl(a_), 710, 18, fill=col)
    card(cv, 70, 820, 1010, 1120, 34)
    cv.text(120, 860, "BYTES", 34, CORAL, 1, "Black", anchor="lm")
    for i in range(10):
        a_ = eback(pr(t, 1.6 + i * .12, 2.0 + i * .12), 2)
        cv.rrect(120 + i * 88, 910, 120 + i * 88 + 76 * cl(a_), 1010, 14, fill=[TEAL, CORAL, MUST][i % 3])
    cv.text(540, 1200, "same word: 3 pieces vs 10", 46, INKC, eo(pr(t, 3.4, 4.0)), "Black")
def s6(cv, t, D):
    head(cv, t, "THE FIX: BYTEIFICATION", "retrofit what already exists")
    q = eback(pr(t, .3, .9), 2)
    card(cv, 70, 560, 380, 800, 30, fill=TEAL, a=cl(q))
    cv.text(225, 650, "TOKEN", 48, PAPER, cl(q), "Black"); cv.text(225, 715, "MODEL", 48, PAPER, cl(q), "Black")
    r = eback(pr(t, 3.6, 4.2), 2)
    card(cv, 700, 560, 1010, 800, 30, fill=CORAL, a=cl(r))
    cv.text(855, 650, "BYTE", 48, PAPER, cl(r), "Black"); cv.text(855, 715, "MODEL", 48, PAPER, cl(r), "Black")
    for k in range(2):
        a_ = eback(pr(t, 1.4 + k * 1.0, 2.0 + k * 1.0), 2)
        chip(cv, 410 if k == 0 else 410, 590 + k * 110, 260, ["STAGE 1", "STAGE 2"][k], [MUST, PLUM][k], cl(a_), size=36, h=84)
    arrow(cv, 540, 560 + 0, 0)
    v = eo(pr(t, 4.2, 5.0))
    card(cv, 130, 940, 950, 1130, 36, a=v)
    cv.text(540, 1000, "minimal extra training", 54, INKC, v, "Black")
    cv.text(540, 1075, "and the old model's ecosystem still works", 34, PLUM, v, "SemiBold")
def s7(cv, t, D):
    head(cv, t, "NEARLY AS CAPABLE", "and better at single characters")
    s = 86; g = 6; x0 = 540 - (10 * s + 9 * g) / 2
    word(cv, x0, 640, s, g, hi=None)
    rs = [i for i, c in enumerate(WORD) if c == "R"]
    for k, i in enumerate(rs):
        a_ = eback(pr(t, .8 + k * .8, 1.2 + k * .8), 2)
        if a_ > .02:
            ltile(cv, x0 + i * (s + g), 640, s, "R", CORAL, PAPER, 1)
            cv.text(x0 + i * (s + g) + s / 2, 780, str(k + 1), 56, CORAL, cl(a_), "Black")
    n = sum(1 for k in range(3) if t > .9 + k * .8)
    card(cv, 300, 900, 780, 1110, 40)
    cv.text(540, 960, "R's counted", 40, PLUM, 1, "Bold")
    cv.text(540, 1050, str(n), 90, CORAL, 1, "Black")
def s8(cv, t, D):
    head(cv, t, "ONE CHARACTER MATTERS", "in code and in DNA")
    p = eback(pr(t, .3, .9), 2); q = eback(pr(t, 1.8, 2.4), 2)
    card(cv, 90, 520, 990, 780, 34, a=cl(p))
    cv.text(540, 570, "CODE", 32, TEAL, cl(p), "Black")
    if t < 1.3: cv.text(540, 670, "if (x == 1)", 80, INKC, cl(p), "Black")
    else: cv.text(540, 670, "if (x = 1)", 80, CORAL, 1, "Black")
    card(cv, 90, 860, 990, 1120, 34, a=cl(q))
    cv.text(540, 910, "DNA", 32, TEAL, cl(q), "Black")
    if t < 3.0: cv.text(540, 1010, "G A T T A C A", 80, INKC, cl(q), "Black")
    else: cv.text(540, 1010, "G A T T T C A", 80, CORAL, 1, "Black")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=CORAL, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=CORAL, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, CORAL, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
