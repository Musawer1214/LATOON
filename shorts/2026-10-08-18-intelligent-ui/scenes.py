# Intelligent UI: peach paper, ink, orange, teal
BG0, BG1 = (240, 226, 206), (228, 208, 182)
INKC = (30, 36, 28); WHT = (252, 246, 236)
TERRA, MUST, FOR, PLUM = (210, 92, 46), (222, 164, 52), (36, 118, 112), (110, 62, 92)
PAPER, EDGE, SHAD = (252, 246, 236), (150, 120, 92), (196, 170, 140)
GOLD = TERRA; BL, BL2 = TERRA, TERRA
NOFADE_IN, NOFADE_OUT = {0}, set()
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (240, 226, 206), 0.0)
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
    if b: cv.text(540, 400, b, 40, c or TERRA, eo(pr(t, .3, .7)), "SemiBold")
def btn(cv, x, y, w, h, txt, col, a, tc=None, size=34):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or PAPER, a, "Black")
def bike(cv, cx, cy, p, hl=None):
    lw = 11
    for dx in (-150, 150):
        cv.circ(cx + dx, cy + 40, 95, outline=INKC if hl != "w" else TERRA, w=lw, oa=p)
        cv.circ(cx + dx, cy + 40, 8, fill=INKC, a=p)
    fr = FOR if hl == "f" else INKC
    pts = [(cx - 150, cy + 40), (cx - 40, cy - 70), (cx + 70, cy - 70), (cx + 150, cy + 40)]
    cv.line([pts[0], (cx - 10, cy + 40), pts[1]], fr, lw, p)
    cv.line([pts[1], pts[2], (cx - 10, cy + 40)], fr, lw, p)
    cv.line([pts[2], (cx + 60, cy - 130)], INKC if hl != "c" else MUST, lw, p)
    cv.line([(cx + 30, cy - 135), (cx + 100, cy - 135)], INKC if hl != "c" else MUST, lw, p)
    cv.line([pts[1], (cx - 55, cy - 110)], INKC, lw, p); cv.line([(cx - 90, cy - 110), (cx - 25, cy - 110)], INKC, lw + 3, p)
    cv.line([pts[3], pts[2]], fr, lw, p)
    cv.circ(cx - 10, cy + 40, 24, outline=PLUM if hl == "d" else INKC, w=lw, oa=p)
def s0(cv, t, D):
    cv.rrect(250, 380, 830, 440, 30, fill=TERRA, a=eo(pr(t, 0, .3)))
    cv.text(540, 408, "GPT-6 · INTELLIGENT UI", 30, PAPER, eo(pr(t, 0, .3)), "Black")
    kinetic(cv, t, 560, "NOT TEXT.", 130, INKC, -.2, "Black", .02)
    q = eback(pr(t, .4, 1.0), 2)
    card(cv, 150, 760, 930, 1300, 44, a=cl(q))
    cv.rrect(150, 760, 930, 840, 44, fill=INKC, a=cl(q)); cv.rrect(150, 800, 930, 840, 0, fill=INKC, a=cl(q))
    for k, c in enumerate((TERRA, MUST, FOR)): cv.circ(205 + k * 40, 800, 11, fill=c, a=cl(q))
    cv.text(540, 930, "APP", 170 * q, TERRA, cl(q), "Black")
    btn(cv, 250, 1080, 270, 80, "Tap", FOR, cl(q), size=36); btn(cv, 560, 1080, 270, 80, "Explore", PLUM, cl(q), size=36)
    cv.rrect(250, 1210, 830, 1236, 13, fill=SHAD, a=.7 * cl(q))
    cv.rrect(250, 1210, 250 + 580 * eo(pr(t, 1.2, 2.6)), 1236, 13, fill=MUST, a=cl(q))
def s1(cv, t, D):
    head(cv, t, "OCTOBER 7", "OpenAI starts the rollout")
    p = eback(pr(t, .3, .9), 2)
    card(cv, 110, 520, 970, 860, 40, a=cl(p))
    cv.text(540, 620, "GPT-6", 130 * p, INKC, cl(p), "Black")
    cv.text(540, 740, "+ Intelligent UI", 62, TERRA, eo(pr(t, .8, 1.3)), "Black")
    cv.text(540, 810, "answers as interfaces, not paragraphs", 30, PLUM, eo(pr(t, 1.2, 1.7)), "SemiBold")
    for k, (n_, c) in enumerate([("Plus", FOR), ("Pro", PLUM), ("Business", MUST), ("Free · next day", TERRA)]):
        a_ = eback(pr(t, 2.0 + k * .4, 2.5 + k * .4), 2)
        w = 300 if k < 3 else 420
        x = 110 + (k % 2) * 330 if k < 2 else None
    ys = [940, 940, 1070, 1070]; xs = [110, 560, 110, 480]; ws = [420, 410, 340, 490]
    for k, (n_, c) in enumerate([("Plus", FOR), ("Pro", PLUM), ("Business", MUST), ("Free tiers: next day", TERRA)]):
        a_ = eback(pr(t, 2.0 + k * .4, 2.5 + k * .4), 2)
        btn(cv, xs[k], ys[k], ws[k], 90, n_, c, cl(a_), tc=INKC if c == MUST else PAPER, size=34)
    cv.text(540, 1250, "rolling out in the Chat tab", 40, INKC, eo(pr(t, 3.8, 4.4)), "Bold")
def s2(cv, t, D):
    head(cv, t, "ASK: HOW A BIKE WORKS", None)
    p = eo(pr(t, .2, .8))
    card(cv, 100, 480, 980, 1380, 44, a=p)
    parts = [("Frame", "f", FOR, 1.2), ("Wheels", "w", TERRA, 2.0), ("Brakes", "d", PLUM, 2.8), ("Cockpit", "c", MUST, 3.5)]
    hl = None
    for n_, k, c, ts in parts:
        if t > ts: hl = k
    bike(cv, 540, 800, cl(p), hl)
    xs = [130, 315, 500, 700]
    for i, (n_, k, c, ts) in enumerate(parts):
        a_ = eback(pr(t, .6 + i * .15, 1.1 + i * .15), 2)
        on = (hl == k)
        btn(cv, [130, 340, 560, 765][i] - 20 * 0, 1130, [190, 190, 190, 195][i], 80, n_, c if on else SHAD, cl(a_), tc=(INKC if c == MUST and on else PAPER), size=30)
    cv.text(540, 1290, "tap a part, it explains itself", 38, INKC, eo(pr(t, 3.6, 4.2)), "Bold")
def s3(cv, t, D):
    head(cv, t, "ASK: SPLIT THE BILL", "it builds the tool for you")
    p = eback(pr(t, .3, .9), 2)
    card(cv, 150, 500, 930, 1380, 44, a=cl(p))
    cv.text(540, 580, "Bill splitter", 50, INKC, cl(p), "Black")
    cv.text(540, 700, "$ 96.00", 100, TERRA, eo(pr(t, .6, 1.1)), "Black")
    cv.text(330, 830, "People", 36, PLUM, eo(pr(t, .9, 1.3)), "Bold")
    n = 3 if t < 1.8 else 4
    btn(cv, 480, 790, 80, 80, "−", SHAD, eo(pr(t, .9, 1.3)), tc=INKC, size=48)
    cv.text(640, 830, str(n), 66, INKC, eo(pr(t, .9, 1.3)), "Black")
    btn(cv, 720, 790, 80, 80, "+", FOR, eo(pr(t, .9, 1.3)), size=48)
    q = eback(pr(t, 1.5, 2.1), 2)
    card(cv, 230, 960, 850, 1180, 36, fill=FOR, outline=FOR, a=cl(q))
    val = 32.0 if t < 1.8 else 24.0
    cv.text(540, 1030, "each pays", 36, PAPER, cl(q), "Bold")
    cv.text(540, 1110, f"$ {val:.2f}", 90, PAPER, cl(q), "Black")
    cv.text(540, 1290, "a working app, in the chat", 38, INKC, eo(pr(t, 2.8, 3.4)), "Bold")
def s4(cv, t, D):
    head(cv, t, "THE UNSEEN PART", "no pixels are drawn")
    p = eo(pr(t, .3, .9))
    card(cv, 90, 500, 990, 1340, 44, a=p)
    cv.text(540, 570, "COMPONENT LIBRARY", 36, PLUM, p, "Black")
    items = [("Button", FOR), ("Chart", TERRA), ("Form", PLUM), ("Diagram", MUST), ("Map", FOR), ("Table", TERRA)]
    for k, (n_, c) in enumerate(items):
        a_ = eback(pr(t, 1.0 + k * .3, 1.5 + k * .3), 2)
        x = 130 + (k % 2) * 440; y = 640 + (k // 2) * 200
        cv.rrect(x + 6, y + 10, x + 400, y + 170, 24, fill=SHAD, a=.6 * cl(a_))
        cv.rrect(x, y, x + 394, y + 160, 24, fill=c, a=cl(a_))
        cv.text(x + 197, y + 80, n_, 50, INKC if c == MUST else PAPER, cl(a_), "Black")
    cv.text(540, 1260, "ready-made, picked by the model", 36, INKC, eo(pr(t, 3.6, 4.2)), "Bold")
def s5(cv, t, D):
    head(cv, t, "THE MODEL IS THE DESIGNER", "it chooses and arranges")
    card(cv, 90, 500, 990, 1340, 44, a=eo(pr(t, .2, .6)))
    slots = [(140, 560, 940, 700, "Chart", TERRA), (140, 740, 520, 900, "Form", PLUM), (560, 740, 940, 900, "Button", FOR), (140, 940, 940, 1100, "Diagram", MUST)]
    for k, (x0, y0, x1, y1, n_, c) in enumerate(slots):
        ts = .6 + k * .9
        a_ = eback(pr(t, ts, ts + .5), 2)
        yy = (1 - cl(a_)) * -60
        cv.rrect(x0 + 6, y0 + 10 + yy, x1 + 6, y1 + 10 + yy, 26, fill=SHAD, a=.6 * cl(a_))
        cv.rrect(x0, y0 + yy, x1, y1 + yy, 26, fill=c, a=cl(a_))
        cv.text((x0 + x1) / 2, (y0 + y1) / 2 + yy, n_, 50, INKC if c == MUST else PAPER, cl(a_), "Black")
    cv.text(540, 1230, "layout decided per question", 38, INKC, eo(pr(t, 4.0, 4.6)), "Bold")
def s6(cv, t, D):
    head(cv, t, "THE COMPILER", "plan in, live interface out")
    p = eo(pr(t, .3, .9))
    card(cv, 70, 500, 500, 1300, 36, a=p)
    cv.text(285, 560, "PLAN", 36, PLUM, p, "Black")
    for k in range(7):
        a_ = eo(pr(t, .8 + k * .25, 1.2 + k * .25))
        w = [300, 220, 260, 180, 300, 240, 200][k]
        cv.rrect(110, 620 + k * 90, 110 + w, 660 + k * 90, 14, fill=[TERRA, FOR, PLUM, MUST][k % 4], a=a_)
    q = eo(pr(t, 1.0, 1.5))
    cv.line([(520, 900), (560, 900)], INKC, 8, q); cv.line([(535, 870), (565, 900), (535, 930)], INKC, 8, q)
    card(cv, 580, 500, 1010, 1300, 36, a=q)
    cv.text(795, 560, "LIVE UI", 36, FOR, q, "Black")
    for k in range(5):
        a_ = eback(pr(t, 1.6 + k * .55, 2.0 + k * .55), 2)
        cv.rrect(620, 620 + k * 125, 620 + [330, 250, 330, 200, 300][k], 710 + k * 125, 20, fill=[FOR, MUST, TERRA, PLUM, FOR][k], a=cl(a_))
    cv.text(540, 1380, "appears while it writes", 38, INKC, eo(pr(t, 3.8, 4.4)), "Bold")
def s7(cv, t, D):
    head(cv, t, "TEXT STILL WINS SOMETIMES", "plain text when text is best")
    p = eback(pr(t, .4, 1.0), 2)
    card(cv, 120, 520, 960, 840, 40, a=cl(p))
    cv.text(540, 600, "Q: What's the capital of France?", 36, PLUM, cl(p), "Bold")
    cv.text(540, 720, "Paris.", 120 * p, INKC, cl(p), "Black")
    q = eo(pr(t, 1.6, 2.2))
    cv.text(540, 930, "no chart. no form. no buttons.", 40, TERRA, q, "Bold")
    r = eback(pr(t, 2.6, 3.2), 2)
    card(cv, 170, 1030, 910, 1250, 40, fill=FOR, outline=FOR, a=cl(r))
    cv.text(540, 1110, "design judgment", 56, PAPER, cl(r), "Black")
    cv.text(540, 1180, "trained, and still improving", 32, PAPER, cl(r), "SemiBold")
def s8(cv, t, D):
    head(cv, t, "THE BIG IDEA", None)
    p = eback(pr(t, .3, .9), 2); q = eback(pr(t, 1.6, 2.2), 2)
    cv.text(300, 640, "BEFORE", 44, PLUM, cl(p), "Black")
    card(cv, 110, 690, 490, 1000, 34, a=cl(p))
    cv.text(300, 760, "YOU", 56, INKC, cl(p), "Black"); cv.text(300, 830, "learn the", 34, INKC, cl(p), "Bold"); cv.text(300, 880, "software", 44, TERRA, cl(p), "Black")
    cv.text(780, 640, "NOW", 44, FOR, cl(q), "Black")
    card(cv, 590, 690, 970, 1000, 34, a=cl(q))
    cv.text(780, 760, "SOFTWARE", 46, INKC, cl(q), "Black"); cv.text(780, 830, "shapes itself", 34, INKC, cl(q), "Bold"); cv.text(780, 880, "around you", 44, FOR, cl(q), "Black")
    kinetic(cv, t, 1180, "ASK. IT BUILDS.", 90, TERRA, 2.8, "Black", .03)
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=TERRA, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=TERRA, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, TERRA, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
