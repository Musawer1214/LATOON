# ---------- scenes: Claustrum / Yale Nature Neuroscience (code-drawn + public-domain anatomy + Crick photo)
BG0, BG1 = (10, 4, 24), (30, 10, 50)
VIO, VIO2 = (170, 110, 255), (225, 195, 255)
PINK = (255, 90, 170)
GOLD, GOLD2 = (255, 205, 110), (255, 232, 170)
BL, BL2 = (150, 100, 255), (230, 200, 255)
RED = (255, 90, 110)
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}

def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def _circle(im, d):
    im = im.resize((d, d), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (d * 4, d * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=255)
    im.putalpha(m.resize((d, d), Image.LANCZOS)); return im

def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S
    GLOW_O = radial(520, (190, 90, 255), 0.18); GLOW_B = radial(560, (110, 60, 255), 0.22); GLOW_S = radial(260, (225, 195, 255), 0.6)
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["g718"] = L("g718.png"); IM["g742"] = L("g742.png")
    cr = L("crick.jpg"); IM["crick"] = _circle(cr.crop((100, 250, 1500, 1650)), 420)

def zoomcard(cv, key, cx, cy, w, h, fx, fy, zoom, r=40, a=1):
    # crop window of the source centred on focus (fx,fy) in source px; zoom=1 shows the whole image fitted
    src = IM[key]; base = max(src.width / w, src.height / h) if False else min(src.width / w, src.height / h)
    cw, ch = w * base / zoom, h * base / zoom
    x0 = min(max(fx - cw / 2, 0), src.width - cw); y0 = min(max(fy - ch / 2, 0), src.height - ch)
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BICUBIC)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
    return (x0, y0, cw, ch)

def img(cv, key, cx, cy, sc=1.0, a=1.0, src=None):
    a = cl(a * cv.ga)
    if a <= 0.01 or sc <= 0.02: return
    cv.done()
    s = src if src is not None else IM[key]
    if abs(sc - 1) > 0.003:
        s = s.resize((max(1, int(s.width * sc)), max(1, int(s.height * sc))), Image.BILINEAR)
    if a < 0.99:
        s = s.copy(); s.putalpha(s.getchannel("A").point(lambda v: int(v * a)))
    x, y = int(cv.X(cx) - s.width / 2), int(cv.Y(cy) - s.height / 2)
    sx0, sy0 = max(0, -x), max(0, -y); x0, y0 = max(0, x), max(0, y)
    sx1, sy1 = min(s.width, W - x), min(s.height, H - y)
    if sx1 <= sx0 or sy1 <= sy0: return
    cv.im.alpha_composite(s.crop((sx0, sy0, sx1, sy1)), dest=(x0, y0))

def kenburns(cv, key, cx, cy, w, h, zoom, r, a=1, panx=0, pany=0):
    src = IM[key]; zw, zh = w / zoom * (src.width / w if src.width / w < src.height / h else src.height / h), 0
    k = min(src.width / w, src.height / h) / zoom
    cw, ch = w * k, h * k
    x0 = (src.width - cw) / 2 + panx * (src.width - cw) / 2; y0 = (src.height - ch) / 2 + pany * (src.height - ch) / 2
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BILINEAR)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))

def shadow(cv, x0, y0, x1, y1, r, a=1):
    for k in range(4):
        cv.rrect(x0 - k * 6, y0 - k * 6 + 18, x1 + k * 6, y1 + k * 6 + 18, r + k * 6, fill=(0, 0, 0), a=a * .12)

def chip(cv, x, y, txt, size, fg, bg, a=1, outline=None, w="Bold"):
    tw = cv.tw(txt, size, w); pw, ph = tw / 2 + size * .8, size * .95
    cv.rrect(x - pw, y - ph, x + pw, y + ph, ph, fill=bg, a=a, outline=outline, w=3)
    cv.text(x, y, txt, size, fg, a, w)

def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    # letter-by-letter rise (kinetic typography)
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]


def ring(cv, x, y, t, col=VIO2, n=3, maxr=140, a=1):
    for k in range(n):
        u = (t * .8 + k / n) % 1
        cv.circ(x, y, 12 + u * maxr, outline=col, w=4, oa=a * (1 - u) * .9)

def net(cv, t, cx, cy, n, R, p, a=1, hub=True):
    pts = [(cx + R * math.cos(i * 2 * math.pi / n + .3), cy + R * math.sin(i * 2 * math.pi / n + .3) * 1.05) for i in range(n)]
    for i, (x, y) in enumerate(pts):
        q = eo(pr(p, i * .03, i * .03 + .35))
        cv.line([(cx, cy), (lerp(cx, x, q), lerp(cy, y, q))], VIO, 3, a * .55)
        if q > .95:
            pulse = (t * 1.2 + i * .13) % 1
            cv.circ(lerp(cx, x, pulse), lerp(cy, y, pulse), 6, fill=GOLD2, a=a * .9)
        cv.circ(x, y, 15 * q, fill=VIO2, a=a * q)
    cv.circ(cx, cy, 34, fill=GOLD, a=a); cv.circ(cx, cy, 58 + 6 * math.sin(t * 4), outline=GOLD2, w=4, oa=a * .6)

# S0 hook: real anatomical plate, zoom into the claustrum
def s0(cv, t, D):
    z = 1.0 + 1.5 * eio(pr(t, .2, 3.2))
    shadow(cv, 110, 470, 970, 1380, 40, 1)
    x0, y0, cw, ch = zoomcard(cv, "g718", 540, 925, 860, 910, 372 - 20 * pr(t, 0, 3), 370, z, 40)
    cv.rrect(110, 470, 970, 1380, 40, fill=None, outline=VIO, w=3, oa=.5)
    fx = 110 + (372 - x0) / cw * 860; fy = 470 + (370 - y0) / ch * 910
    if z > 1.6: ring(cv, fx, fy, t, PINK, 3, 130, eo(pr(t, 1.5, 2.2)))
    q = eback(pr(t, -.2, .25), 2)
    chip(cv, 540, 290, "NEUROSCIENCE  ·  NEW STUDY", 34, (20, 6, 40), GOLD, cl(q))
    kinetic(cv, t, 385, "THE BRAIN'S HIDDEN HUB", 70, WHT, -.3, "Black", .03)
    chip(cv, 540, 1300, "the claustrum", 36, WHT, (30, 10, 60), eo(pr(t, 2.0, 2.4)), outline=PINK)

# S1 thin sheet
def s1(cv, t, D):
    cv.text(540, 300, "A THIN SHEET OF NEURONS", 54, VIO2, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 365, "buried deep beneath the cortex", 34, MUT, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .1, .7))
    shadow(cv, 150, 470, 930, 1330, 40, p)
    x0, y0, cw, ch = zoomcard(cv, "g742", 540, 900, 780, 860, 292, 245, 1.0 + .35 * eio(pr(t, .6, D)), 40, p)
    fx = 150 + (292 - x0) / cw * 780; fy = 470 + (245 - y0) / ch * 860 + 0
    ring(cv, fx + 30, fy + 40, t, PINK, 3, 120, eo(pr(t, 1.0, 1.6)))
    chip(cv, 540, 1385, "CLAUSTRUM", 40, (20, 6, 40), PINK, eo(pr(t, 1.2, 1.7)))

# S2 most connected
def s2(cv, t, D):
    kinetic(cv, t, 330, "MOST CONNECTED", 72, WHT, .05, "Black", .03)
    cv.text(540, 410, "region of the entire brain", 38, VIO2, eo(pr(t, .5, .9)), "SemiBold")
    net(cv, t, 540, 880, 22, 400, pr(t, .3, 1.8))
    q = eo(pr(t, 1.9, 2.4))
    chip(cv, 540, 1345, "Dr. Yemi Damisah  ·  Yale School of Medicine", 30, WHT, (30, 10, 60), q, outline=VIO)

# S3 Crick
def s3(cv, t, D):
    cv.text(540, 300, "FRANCIS CRICK", 68, GOLD, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 370, "Nobel laureate  ·  co-discoverer of DNA's double helix", 28, MUT, eo(pr(t, .3, .7)), "SemiBold")
    s = eback(pr(t, .1, .7), 1.6)
    for k in range(3):
        cv.circ(540, 860, 240 + k * 40 + 10 * math.sin(t * 2 + k), outline=VIO, w=3, oa=.3 * s / (k + 1))
    img(cv, "crick", 540, 860, s)
    q = eback(pr(t, 1.5, 2.1), 2)
    chip(cv, 540, 1240, "consciousness?", 52, (20, 6, 40), PINK, cl(q))
    cv.text(540, 1330, "He suspected a link to conscious experience", 30, WHT, eo(pr(t, 2.2, 2.6)), "Medium")

# S4 electrodes missed
def s4(cv, t, D):
    cv.text(540, 300, "TOO TINY. TOO DEEP.", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.rrect(140, 800, 940, 1100, 30, fill=(24, 12, 48), outline=VIO, w=3, oa=.5)
    cv.line([(140, 940), (330, 920), (540, 975), (760, 925), (940, 950)], PINK, 9, .95)
    cv.text(540, 1160, "claustrum: a sliver of cells", 30, VIO2, eo(pr(t, .4, .8)), "SemiBold")
    ex = lerp(-300, 1300, eio(pr(t, .4, 3.4)))
    cv.rrect(ex - 70, 700, ex + 70, 1220, 30, fill=(150, 150, 170), a=.9, outline=WHT, w=3)
    cv.text(ex, 1260, "standard electrode", 28, MUT, eo(pr(t, .6, 1.0)), "Medium")
    m = eback(pr(t, 2.0, 2.5), 2)
    chip(cv, 540, 560, "MISSED", 64, WHT, RED, cl(m))

# S5 Yale first recordings
def s5(cv, t, D):
    chip(cv, 540, 290, "NATURE NEUROSCIENCE  ·  OCT 6, 2026", 30, (20, 6, 40), GOLD, eo(pr(t, 0, .3)))
    kinetic(cv, t, 400, "A HUMAN FIRST", 80, WHT, .1, "Black", .04)
    cv.text(540, 480, "single-neuron recordings from the claustrum", 30, VIO2, eo(pr(t, .6, 1.0)), "SemiBold")
    for i in range(7):
        q = eback(pr(t, 1.8 + i * .22, 2.2 + i * .22), 2)
        x = 540 + (i - 3) * 118
        cv.circ(x, 900, 46 * cl(q), fill=VIO, a=cl(q)); cv.circ(x, 900, 46 * cl(q) + 8, outline=VIO2, w=3, oa=.5 * cl(q))
        icon_person(cv, x, 900, 40 * cl(q), WHT, cl(q))
    cv.text(540, 1130, "7", 260, GOLD, eo(pr(t, 3.6, 4.1)), "Black")
    cv.text(540, 1320, "epilepsy patients with implanted electrodes", 32, WHT, eo(pr(t, 4.0, 4.5)), "SemiBold")

# S6 microwire + game
def s6(cv, t, D):
    cv.text(540, 300, "40 MICROMETRES", 74, GOLD, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 370, "microwires fine enough to hear one neuron", 30, MUT, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .3, 1.2))
    cv.rrect(500, 480, 580, 900, 20, fill=(120, 120, 140), a=p)
    cv.line([(540, 900), (540, 900 + 160 * p)], WHT, 3, p)
    cv.circ(540, 1060, 10 * p, fill=PINK, a=p); ring(cv, 540, 1060, t, PINK, 2, 70, p)
    g = eo(pr(t, 2.2, 2.8))
    cv.rrect(180, 1130, 900, 1400, 30, fill=(10, 4, 28), a=g, outline=VIO, w=3, oa=g)
    cv.text(540, 1160, "spaceship game", 26, MUT, g, "Medium")
    for k in range(6):
        ay = 1180 + ((t * 170 + k * 90) % 210); ax = 230 + k * 120 + 20 * math.sin(t * 2 + k)
        cv.circ(ax, ay, 22, fill=(90, 70, 120), a=g * .9, outline=VIO2, w=2)
    sx = 540 + 250 * math.sin(t * 2.4)
    cv.poly([(sx, 1330), (sx - 26, 1385), (sx + 26, 1385)], GOLD, g)

# S7 uncertainty & prediction error
def s7(cv, t, D):
    cv.text(540, 300, "UNCERTAINTY", 74, VIO2, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "+ PREDICTION ERROR", 60, PINK, eo(pr(t, .3, .7)), "Black")
    cv.rrect(110, 560, 970, 1260, 36, fill=(14, 6, 34), outline=VIO, w=3, oa=.5)
    for row, (y, col, ph) in enumerate([(780, VIO2, 0), (1040, PINK, 1.7)]):
        pts = []; n = 90; L = eo(pr(t, .6, 3.2)) * n
        for i in range(int(L)):
            x = 150 + i * 8.0
            u = i / n
            spike = sum(math.exp(-((u - c) / .018) ** 2) for c in ([.25, .5, .78] if row == 0 else [.32, .62, .86]))
            pts.append((x, y - 130 * spike - 10 * math.sin(i * .9 + ph) * 0.6))
        if len(pts) > 1: cv.line(pts, col, 6, .95)
        if pts: cv.circ(pts[-1][0], pts[-1][1], 12, fill=WHT)
    cv.text(150, 640, "neuron firing: how unsure am I?", 26, MUT, 1, "Medium", anchor="lm")
    cv.text(150, 900, "neuron firing: I got it wrong", 26, MUT, 1, "Medium", anchor="lm")
    cv.text(540, 1360, "the signals of a brain learning to predict", 32, WHT, eo(pr(t, 3.4, 3.9)), "SemiBold")

# S8 filter -> driver
def s8(cv, t, D):
    cv.text(540, 300, "NOT JUST A FILTER", 66, WHT, eo(pr(t, .05, .4)), "Black")
    boxes = [(540, 620, "SENSES", VIO), (540, 930, "CLAUSTRUM", PINK), (540, 1240, "BEHAVIOUR", GOLD)]
    for i, (x, y, lab, col) in enumerate(boxes):
        q = eback(pr(t, .4 + i * .7, .9 + i * .7), 1.8)
        cv.rrect(x - 260, y - 70, x + 260, y + 70, 40, fill=(24, 10, 52), a=cl(q), outline=col, w=4, oa=cl(q))
        cv.text(x, y, lab, 50, col, cl(q), "Black")
        if i < 2:
            a = eo(pr(t, .8 + i * .7, 1.3 + i * .7))
            cv.line([(540, y + 80), (540, y + 80 + 150 * a)], VIO2, 6, a)
            if a > .9: cv.poly([(540, y + 245), (515, y + 205), (565, y + 205)], VIO2, 1)
    cv.text(540, 1400, "it tracks the signals that drive choices", 30, MUT, eo(pr(t, 3.0, 3.5)), "SemiBold")

# S9 outro
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    net(cv, t, 540, 760, 16, 300, p, .5)
    kinetic(cv, t, 1000, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1130, "Voyaging the Unseen", 46, GOLD, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1230, "what part of the mind should we map next?", 30, VIO2, eo(pr(t, 1.8, 2.3)), "Medium")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
