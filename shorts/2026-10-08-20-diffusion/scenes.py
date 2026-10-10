# Diffusion explainer: kraft paper, ink, rust, sage, ochre
BG0, BG1 = (232, 220, 196), (218, 202, 172)
INKC = (36, 32, 28); WHT = (252, 246, 232)
RUST, OCH, SAGE, PLUM = (196, 82, 48), (214, 154, 46), (88, 120, 98), (104, 66, 84)
PAPER, EDGE, SHAD = (251, 245, 232), (140, 112, 84), (190, 164, 132)
GOLD = RUST; BL, BL2 = RUST, RUST
NOFADE_IN, NOFADE_OUT = {0}, set()
PIC = None; NZ = None; _cache = {}
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, PIC, NZ
    z = radial(40, (232, 220, 196), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    N = 640
    im = Image.new("RGB", (N, N)); d = ImageDraw.Draw(im)
    top, bot = np.array((244, 176, 96)), np.array((250, 226, 170))
    for y in range(N):
        d.line([(0, y), (N, y)], fill=tuple(int(v) for v in (top + (bot - top) * min(y, 420) / 420)))
    d.ellipse((200, 230, 400, 430), fill=(236, 92, 52))
    d.ellipse((230, 260, 370, 400), fill=(246, 130, 70))
    for k, (cy, col, amp, ph) in enumerate([(400, (150, 110, 110), 40, 0), (450, (96, 104, 112), 50, 2), (520, (52, 72, 70), 40, 4), (590, (30, 44, 44), 30, 1)]):
        pts = [(0, N)] + [(x, cy + amp * math.sin(x / 90 + ph) + 12 * math.sin(x / 31 + ph)) for x in range(0, N + 1, 8)] + [(N, N)]
        d.polygon(pts, fill=col)
    for bx, by in [(120, 330), (150, 310), (500, 300)]:
        d.arc((bx, by, bx + 30, by + 14), 200, 340, fill=(60, 40, 40), width=3); d.arc((bx + 28, by, bx + 58, by + 14), 200, 340, fill=(60, 40, 40), width=3)
    PIC = np.asarray(im).astype(np.float32)
    rng = np.random.RandomState(7)
    NZ = np.clip(rng.normal(128, 70, (N, N, 3)), 0, 255).astype(np.float32)
def tile(cv, x, y, size, lvl):
    q = round(cl(lvl) * 60) / 60
    key = (size, q)
    if key not in _cache:
        a = PIC * (1 - q) + NZ * q
        im = Image.fromarray(a.astype(np.uint8))
        if size != 640: im = im.resize((size, size), Image.LANCZOS)
        if len(_cache) > 80: _cache.clear()
        _cache[key] = im
    cv.done()
    cv.rrect(x + 8, y + 12, x + size + 8, y + size + 12, 6, fill=SHAD, a=.6); cv.done()
    cv.im.paste(_cache[key], (int(x), int(y)))
    cv.rrect(x, y, x + size, y + size, 4, outline=INKC, w=5)
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
    if b: cv.text(540, 400, b, 40, c or RUST, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or PAPER, a, "Black")
def arrow(cv, x, y, a=1, c=INKC):
    cv.line([(x - 26, y), (x + 26, y)], c, 9, a); cv.line([(x + 6, y - 20), (x + 28, y), (x + 6, y + 20)], c, 9, a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "PURE STATIC", 92, INKC, -.2, "Black", .02)
    tile(cv, 190, 500, 700, 1 - eio(pr(t, .3, D - .2)) * .9)
    cv.text(540, 1290, "to a picture. how?", 48, RUST, eo(pr(t, 1.0, 1.5)), "Black")
def s1(cv, t, D):
    head(cv, t, "IT STARTS WITH NOISE", "every image begins as static")
    tile(cv, 220, 520, 640, 1.0)
    for k, n_ in enumerate(["Stable Diffusion", "Midjourney"]):
        a_ = eback(pr(t, 1.0 + k * .6, 1.5 + k * .6), 2)
        chip(cv, [120, 560][k], 1240, [400, 400][k], n_, [SAGE, PLUM][k], cl(a_), size=32)
def s2(cv, t, D):
    head(cv, t, "TRAINING RUNS BACKWARDS", "step 1: ruin a real photo")
    lvl = .55 * eio(pr(t, 1.2, 4.6))
    tile(cv, 220, 520, 640, lvl)
    cv.text(540, 1230, f"noise added: {int(lvl / .55 * 30 + .5)}%", 48, RUST, eo(pr(t, .6, 1.0)), "Black")
    cv.rrect(240, 1290, 840, 1316, 13, fill=SHAD, a=.7); cv.rrect(240, 1290, 240 + 600 * lvl / .55 * .5, 1316, 13, fill=RUST)
def s3(cv, t, D):
    head(cv, t, "ADD MORE, STEP BY STEP", "until nothing is left")
    lv = [0, .25, .5, .75, 1.0]
    for k, l in enumerate(lv):
        a_ = eback(pr(t, .4 + k * .5, .9 + k * .5), 2)
        x = 70 + k * 190
        if a_ > .02:
            tile(cv, x, 700 - (1 - cl(a_)) * -30, 160, l)
            if k < 4: arrow(cv, x + 178, 780, cl(a_), RUST) if False else None
    for k in range(4):
        a_ = eo(pr(t, .6 + k * .5, 1.0 + k * .5)); cv.text(70 + k * 190 + 175, 900, "›", 50, RUST, a_, "Black")
    cv.text(540, 1060, "photo  →  static", 70, INKC, eo(pr(t, 3.0, 3.6)), "Black")
def s4(cv, t, D):
    head(cv, t, "THE ONE QUESTION", "asked at every step")
    p = eback(pr(t, .3, .9), 2)
    tile(cv, 90, 560, 300, .5)
    arrow(cv, 460, 710, cl(p))
    q = eback(pr(t, 1.0, 1.6), 2)
    card(cv, 520, 590, 990, 830, 36, a=cl(q))
    cv.text(755, 680, "What noise", 54, INKC, cl(q), "Black"); cv.text(755, 760, "was just added?", 54, RUST, cl(q), "Black")
    r = eo(pr(t, 2.6, 3.3))
    cv.text(540, 1000, "Only the noise.", 60, INKC, r, "Black"); cv.text(540, 1080, "Never the picture itself.", 44, PLUM, r, "Bold")
def s5(cv, t, D):
    head(cv, t, "GUESS. SCORE. REPEAT.", "millions of times")
    card(cv, 100, 520, 980, 1260, 40)
    cv.text(540, 590, "ERROR", 40, PLUM, 1, "Black")
    pts = []
    for i in range(41):
        x = 170 + i * 18; u = i / 40
        pts.append((x, 700 + 360 * (1 - math.exp(-3.2 * u)) + 14 * math.sin(i * 1.7) * (1 - u)))
    n = int(1 + 40 * eo(pr(t, .5, 4.0)))
    cv.line(pts[:n], RUST, 10, 1)
    cv.circ(pts[n - 1][0], pts[n - 1][1], 16, fill=OCH, outline=INKC, w=4)
    cv.text(540, 1200, "it learns what noise looks like", 36, INKC, eo(pr(t, 2.0, 2.6)), "Bold")
def s6(cv, t, D):
    head(cv, t, "NOW DRAW: GO FORWARD", "subtract the predicted noise")
    ls = [1.0, .75, .5, .25, 0]
    for k, l in enumerate(ls):
        a_ = eback(pr(t, .4 + k * .7, .9 + k * .7), 2)
        if a_ > .02: tile(cv, 70 + k * 190, 640 - (1 - cl(a_)) * -30, 160, l)
    for k in range(4):
        cv.text(70 + k * 190 + 175, 740, "›", 50, RUST, eo(pr(t, .6 + k * .7, 1.0 + k * .7)), "Black")
    kinetic(cv, t, 1000, "STATIC → SUNRISE", 74, INKC, 3.0, "Black", .03)
def s7(cv, t, D):
    head(cv, t, "YOUR WORDS STEER IT", None)
    card(cv, 120, 440, 960, 560, 36)
    txt = "a sunrise over hills"; n = int(len(txt) * eo(pr(t, .3, 2.2)))
    cv.text(160, 500, txt[:n] + ("|" if int(t * 3) % 2 == 0 else ""), 46, INKC, 1, "Bold", anchor="lm")
    tile(cv, 170, 640, 740, 1 - eio(pr(t, .6, 5.2)))
    cv.text(540, 1440, "", 10, INKC)
def s8(cv, t, D):
    head(cv, t, "NOT A COPY", None)
    p = eback(pr(t, .3, .9), 2); q = eback(pr(t, 1.6, 2.2), 2)
    card(cv, 100, 520, 500, 960, 34, a=cl(p))
    cv.text(300, 600, "NOT THIS", 38, PLUM, cl(p), "Black"); cv.text(300, 720, "memorising", 44, INKC, cl(p), "Black"); cv.text(300, 780, "pictures", 44, INKC, cl(p), "Black")
    cv.line([(190, 640), (410, 860)], RUST, 12, cl(p)); cv.line([(410, 640), (190, 860)], RUST, 12, cl(p))
    card(cv, 580, 520, 980, 960, 34, a=cl(q))
    cv.text(780, 600, "THIS", 38, SAGE, cl(q), "Black"); cv.text(780, 720, "learning the", 44, INKC, cl(q), "Black"); cv.text(780, 780, "way back", 44, SAGE, cl(q), "Black"); cv.text(780, 840, "from chaos", 44, INKC, cl(q), "Black")
    kinetic(cv, t, 1150, "ORDER FROM NOISE", 80, RUST, 3.0, "Black", .03)
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=RUST, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=RUST, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, RUST, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
