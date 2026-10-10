# ---------- scenes: EmbeddingGemma 2 (code-drawn + Google's own banner image)
BG0, BG1 = (5, 10, 9), (10, 30, 24)
ORG, ORG2 = (140, 250, 90), (200, 255, 150)
AMB, CREAM = (255, 170, 40), (232, 250, 236)
PUR = (176, 132, 255)
DIM = (30, 62, 50)
RED = (255, 80, 80)
GOLD = (255, 170, 40)
BL, BL2 = (140, 250, 90), (210, 255, 160)
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}

def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im

LENS = []
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S
    GLOW_O = radial(520, (255, 160, 30), 0.14); GLOW_B = radial(560, (60, 220, 90), 0.2); GLOW_S = radial(260, (200, 255, 150), 0.6)
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["smi"] = L("card-chat-smi_82.png")
    g = Image.open(os.path.join(IMGDIR, "lens-floorplan.gif"))
    for i in range(g.n_frames):
        g.seek(i); LENS.append(g.convert("RGB").copy())
    IM["lens"] = LENS[50]

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

def zoomcard(cv, key, cx, cy, w, h, fx, fy, zoom, r=40, a=1):
    # crop window centred on (fx,fy) in source px; zoom=1 fits the whole image to the card (cover)
    src = IM[key]; base = min(src.width / w, src.height / h)
    cw, ch = w * base / zoom, h * base / zoom
    x0 = min(max(fx - cw / 2, 0), src.width - cw); y0 = min(max(fy - ch / 2, 0), src.height - ch)
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BICUBIC)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
    return (x0, y0, cw, ch)

def shadow(cv, x0, y0, x1, y1, r, a=1):
    for k in range(4):
        cv.rrect(x0 - k * 6, y0 - k * 6 + 18, x1 + k * 6, y1 + k * 6 + 18, r + k * 6, fill=(0, 0, 0), a=a * .12)

def chip(cv, x, y, txt, size, fg, bg, a=1, outline=None, w="Bold"):
    tw = cv.tw(txt, size, w); pw, ph = tw / 2 + size * .8, size * .95
    cv.rrect(x - pw, y - ph, x + pw, y + ph, ph, fill=bg, a=a, outline=outline, w=3)
    cv.text(x, y, txt, size, fg, a, w)

def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]

def ring(cv, x, y, t, col=ORG2, n=3, maxr=140, a=1):
    for k in range(n):
        u = (t * .8 + k / n) % 1
        cv.circ(x, y, 12 + u * maxr, outline=col, w=4, oa=a * (1 - u) * .9)

def star(cv, cx, cy, r, c, a=1):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * .42; an = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + rr * math.cos(an), cy + rr * math.sin(an)))
    cv.poly(pts, c, a)

def padlock(cv, cx, cy, s, p, c=ORG, a=1):
    # p: 0 closed -> 1 open (shackle lifts, right leg floats free)
    lift = eo(p) * s * .22; r = s * .26; by = cy - s * .05
    acy = by - s * .2 - lift
    arcp = [(cx - r * math.cos(math.pi * i / 20), acy - r * math.sin(math.pi * i / 20)) for i in range(21)]
    cv.line([(cx - r, by)] + arcp + [(cx + r, acy + (0 if p > .05 else s * .2 + lift))], CREAM, s * .09, a)
    cv.rrect(cx - s * .42, by, cx + s * .42, cy + s * .45, s * .1, fill=c, a=a)
    cv.circ(cx, cy + s * .14, s * .07, fill=(3, 20, 22), a=a); cv.line([(cx, cy + s * .14), (cx, cy + s * .29)], (3, 20, 22), s * .06, a)
INK = (4, 18, 12)
CARDC = (10, 34, 26)
TEAL = (60, 205, 170)

def lens_at(t, off=0):
    IM["lens"] = LENS[int((t + off) * 10) % len(LENS)]

def dotted(cv, p0, p1, t, n=14, col=ORG2, a=1, r=5, speed=.8):
    for i in range(n):
        u = (i / n + t * speed) % 1
        cv.circ(lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), r * (.5 + .5 * math.sin(u * math.pi)), fill=col, a=a * math.sin(u * math.pi))

def chipart(cv, cx, cy, s, t, a=1, col=ORG, label="TPU"):
    # package, pins, die
    for i in range(7):
        o = -s * .38 + i * s * .127
        for (x0, y0, x1, y1) in [(cx + o, cy - s * .62, cx + o, cy - s * .5), (cx + o, cy + s * .5, cx + o, cy + s * .62),
                                 (cx - s * .62, cy + o, cx - s * .5, cy + o), (cx + s * .5, cy + o, cx + s * .62, cy + o)]:
            cv.line([(x0, y0), (x1, y1)], mix(col, DIM, .3), 6, a)
    cv.rrect(cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2, s * .08, fill=CARDC, a=a, outline=col, w=5, oa=a)
    pulse = .5 + .5 * math.sin(t * 4)
    cv.rrect(cx - s * .33, cy - s * .33, cx + s * .33, cy + s * .33, s * .05, fill=mix(CARDC, col, .12 + .12 * pulse), a=a, outline=col, w=2, oa=a * .7)
    for i in range(3):
        for j in range(3):
            cv.rrect(cx - s * .27 + i * s * .19, cy - s * .27 + j * s * .19, cx - s * .27 + i * s * .19 + s * .14, cy - s * .27 + j * s * .19 + s * .14, 4, fill=col, a=a * (.25 + .5 * (.5 + .5 * math.sin(t * 5 + i * 1.3 + j * .9))))
    cv.text(cx, cy, label, s * .17, CREAM, a * .0, "Black")

# ---- S0 hook
def s0(cv, t, D):
    chip(cv, 540, 300, "OPEN-SOURCE AI CHIP  ·  OCT 6", 28, INK, ORG, 1)
    kinetic(cv, t, 440, "openTPU", 150, WHT, -.3, "Black", .02)
    cv.text(540, 585, "an AI chip that says AI developed it", 36, ORG2, eo(pr(t, .3, .8)), "SemiBold")
    p = eo(pr(t, .2, .8))
    chipart(cv, 540, 980, 250, t, p)
    for (x, c, lab, k) in [(170, PUR, "AI AGENTS", 0), (910, AMB, "AI MODELS", 1)]:
        q = eback(pr(t, .6 + k * .3, 1.2 + k * .3), 2)
        cv.circ(x, 980, 92 * q, fill=mix(CARDC, c, .25), a=1, outline=c, w=5)
        cv.text(x, 980, lab.split()[0], 38, CREAM, cl(q * 1.4), "Black"); cv.text(x, 1020, lab.split()[1], 26, c, cl(q * 1.4), "Bold")
    f1 = eo(pr(t, 1.4, 1.9))
    dotted(cv, (270, 980), (400, 980), t, 5, PUR, f1)
    cv.text(335, 920, "designs", 28, PUR, f1, "Bold")
    dotted(cv, (680, 980), (810, 980), t, 5, AMB, f1)
    cv.text(745, 920, "runs", 28, AMB, f1, "Bold")
    f2 = eo(pr(t, 2.2, 2.9))
    pts = [(910 - 740 * u, 1090 + 200 * math.sin(math.pi * u)) for u in [i / 30 for i in range(31)]]
    cv.line(pts[:max(2, int(31 * f2))], DIM, 4, f2)
    for i in range(6):
        u = (i / 6 + t * .4) % 1
        x, y = 910 - 740 * u, 1090 + 200 * math.sin(math.pi * u)
        cv.circ(x, y, 7, fill=ORG2, a=f2 * math.sin(math.pi * u))
    cv.text(540, 1370, "AI → chip → AI", 46, WHT, eo(pr(t, 3.0, 3.6)), "Black")

# ---- S1 one repo
ROWS = [("HARDWARE", "SystemVerilog design"), ("INSTRUCTION SET", "8 words per instruction"), ("COMPILER", "Python-style kernels"),
        ("SIMULATOR", "bit-exact, runs on a laptop"), ("PROFILER", "called Lens")]
def s1(cv, t, D):
    chip(cv, 540, 300, "GITHUB  ·  APACHE-2.0", 28, INK, AMB, eo(pr(t, 0, .3)))
    kinetic(cv, t, 400, "ONE REPO", 110, WHT, 0, "Black", .04)
    for i, (a_, b_) in enumerate(ROWS):
        s_ = .6 + i * .55
        p = eback(pr(t, s_, s_ + .5), 1.5)
        y = 520 + i * 160
        x = lerp(1300, 0, cl(p))
        cv.rrect(90 + x, y, 990 + x, y + 130, 30, fill=CARDC, a=1, outline=ORG if i % 2 == 0 else PUR, w=3)
        cv.text(135 + x, y + 48, a_, 42, WHT, 1, "Black", anchor="lm")
        cv.text(135 + x, y + 95, b_, 28, MUT, 1, "Medium", anchor="lm")
        check(cv, 920 + x, y + 65, 52, pr(t, s_ + .3, s_ + .7), ORG, 9)
    cv.text(540, 1360, "github.com/FeSens/openTPU", 34, ORG2, eo(pr(t, 3.6, 4.2)), "SemiBold")

# ---- S2 real run
def s2(cv, t, D):
    cv.text(540, 320, "REAL LANGUAGE MODELS", 56, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "running on an old FPGA card", 36, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .1, .5)); u = eio(pr(t, .8, 3.2))
    shadow(cv, 80, 460, 1000, 1060, 40, p)
    zoomcard(cv, "smi", 540, 760, 920, 600, lerp(600, 930, u), lerp(380, 110, u), lerp(1.0, 2.1, u), 40, p)
    cv.rrect(80, 460, 1000, 1060, 40, outline=ORG, w=3, oa=.6 * p)
    cv.text(540, 1090, "screenshot: © FeSens, openTPU (Apache-2.0)", 22, MUT, .8 * p, "Medium")
    for i, (txt, c) in enumerate([("KINTEX-7 FPGA", ORG), ("DDR3 MEMORY", AMB), ("PCIe CARD", PUR)]):
        q = eback(pr(t, 1.2 + i * .25, 1.7 + i * .25), 2)
        chip(cv, 200 + i * 340, 1230, txt, 30, INK, c, cl(q))
    cv.text(540, 1340, "Qwen3 · Gemma 4 · Phi-4-mini · LFM2", 34, CREAM, eo(pr(t, 2.4, 3.0)), "SemiBold")

# ---- S3 no cache, no hidden scheduling
UN = [("DMA", PUR), ("MATRIX", ORG), ("VECTOR", AMB), ("QUANT", TEAL)]
def s3(cv, t, D):
    for k, (txt, y0) in enumerate([("NO CACHE", 340), ("NO HIDDEN SCHEDULING", 440)]):
        a_ = eo(pr(t, .1 + k * .8, .5 + k * .8)); sz = 84 if k == 0 else 54
        cv.text(540, y0, txt, sz, WHT, a_, "Black")
        w_ = cv.tw(txt, sz, "Black") / 2 + 10
        s_ = eo(pr(t, .8 + k * .8, 1.2 + k * .8))
        cv.line([(540 - w_, y0), (540 - w_ + 2 * w_ * s_, y0)], RED, 10, s_)
    A = eo(pr(t, 1.9, 2.4))
    cv.text(540, 600, "SEQUENCER", 30, MUT, A, "Bold")
    seq = [0, 1, 1, 2, 3, 0, 1, 2, 1, 3, 2, 1]
    cyc = .42; T0 = 2.4
    cur = int((t - T0) / cyc) if t > T0 else -1
    for i in range(10):
        j = cur - 2 + i
        ph = ((t - T0) / cyc) - (cur - 2) if t > T0 else i - 2
        x = 140 + (i - ph + 2) * 130 - 130
        if x < 60 or x > 1020: continue
        k = seq[j % len(seq)] if j >= 0 else 0
        c = UN[k][1]; act = (j == cur)
        cv.rrect(x - 52, 640, x + 52, 740, 18, fill=mix(CARDC, c, .5 if act else .15), a=A * (1 if j >= 0 else .3), outline=c, w=4 if act else 2)
        cv.text(x, 690, "ISA", 28, CREAM, A, "Bold")
    bx = [160, 400, 680, 920]
    for k, (n, c) in enumerate(UN):
        flash = cl(1 - ((t - T0) % cyc) / cyc) if (t > T0 and seq[cur % len(seq)] == k) else 0
        cv.rrect(bx[k] - 105, 1010, bx[k] + 105, 1130, 24, fill=mix(CARDC, c, .12 + .55 * flash), a=A, outline=c, w=4)
        cv.text(bx[k], 1070, n, 34, WHT, A, "Black")
        if flash > 0:
            sx = 140 + 2 * 130 - 130 + 130
            dotted(cv, (540, 750), (bx[k], 1005), t * 3, 4, c, flash, 8, 1)
    cv.text(540, 1250, "one instruction per cycle", 44, ORG2, eo(pr(t, 3.4, 4.0)), "Black")
    cv.text(540, 1315, "every data move is written down", 32, MUT, eo(pr(t, 4.2, 4.8)), "Medium")

# ---- S4 Lens profiler
def s4(cv, t, D):
    lens_at(t)
    cv.text(540, 320, "LENS PROFILER", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "every clock cycle, colour-coded", 36, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .1, .5)); z = 1 + .12 * eo(pr(t, .6, D))
    shadow(cv, 60, 470, 1020, 960, 36, p)
    zoomcard(cv, "lens", 540, 715, 960, 490, 480 - 20 * pr(t, 0, D), 235, z, 36, p)
    cv.rrect(60, 470, 1020, 960, 36, outline=ORG, w=3, oa=.6 * p)
    cv.text(540, 990, "screen capture: © FeSens, openTPU (Apache-2.0)", 22, MUT, .8 * p, "Medium")
    ys = 470 + 490 * ((t * .6) % 1)
    cv.line([(70, ys), (1010, ys)], ORG2, 3, .35 * p)
    for i, (txt, c) in enumerate([("BUSY", TEAL), ("WAITING", AMB), ("BLOCKED", PUR)]):
        q = eo(pr(t, 1.2 + i * .25, 1.6 + i * .25))
        chip(cv, 220 + i * 320, 1120, txt, 30, INK, c, q)
    cv.text(540, 1250, "see where time is spent", 40, CREAM, eo(pr(t, 1.9, 2.4)), "Bold")

# ---- S5 waiting on memory
def s5(cv, t, D):
    lens_at(t, 3.0)
    kinetic(cv, t, 330, "NOT SLOW AT MATH", 66, WHT, 0, "Black", .025)
    kinetic(cv, t, 420, "WAITING ON MEMORY", 66, AMB, .5, "Black", .025)
    p = eo(pr(t, .1, .5)); u = eio(pr(t, .6, 3.5))
    shadow(cv, 100, 500, 980, 940, 36, p)
    zoomcard(cv, "lens", 540, 720, 880, 440, lerp(330, 300, u), lerp(230, 190, u), lerp(1.0, 2.0, u), 36, p)
    cv.rrect(100, 500, 980, 940, 36, outline=AMB, w=3, oa=.7 * p)
    # memory -> math pipe
    q = eo(pr(t, 1.8, 2.4))
    cv.rrect(110, 1060, 380, 1200, 28, fill=mix(CARDC, AMB, .25), a=q, outline=AMB, w=4)
    cv.text(245, 1130, "MEMORY", 36, WHT, q, "Black")
    cv.rrect(700, 1060, 970, 1200, 28, fill=CARDC, a=q, outline=ORG, w=4)
    cv.text(835, 1100, "MATH", 36, WHT, q, "Black")
    fill = .25 + .12 * math.sin(t * 3)
    cv.rrect(722, 1155, 722 + 226 * fill, 1180, 8, fill=ORG, a=q)
    dotted(cv, (385, 1130), (695, 1130), t, 6, AMB, q, 8, .5)
    cv.text(540, 1290, "it waits for data to arrive", 42, CREAM, eo(pr(t, 2.8, 3.4)), "Bold")

# ---- S6 gauge
def s6(cv, t, D):
    cv.text(540, 320, "WHILE DECODING", 56, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "memory runs near its limit", 36, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    cx, cy, R_ = 540, 840, 270
    p = eo(pr(t, .3, 2.6)); val = 94 * p
    cv.circ(cx, cy, R_, outline=DIM, w=34, oa=1)
    cv.arc(cx, cy, R_, 0, 360 * val / 100, AMB, 34, 1)
    ang = math.radians(360 * val / 100 - 90)
    hx, hy = cx + R_ * math.cos(ang), cy + R_ * math.sin(ang)
    cv.circ(hx, hy, 22, fill=WHT, a=1)
    cv.circ(hx, hy, 52, fill=AMB, a=.25 * pr(t, .3, .6))
    cv.text(cx, cy - 10, f"{int(val)}%", 190, WHT, eo(pr(t, .3, .7)), "Black")
    cv.text(cx, cy + 110, "UP TO", 30, AMB, eo(pr(t, .5, .9)), "Bold")
    cv.text(540, 1230, "of the DDR3 peak speed", 46, CREAM, eo(pr(t, 1.2, 1.8)), "Bold")
    cv.text(540, 1305, "peak = 17.1 GB/s on this card", 32, MUT, eo(pr(t, 1.8, 2.4)), "Medium")
    for k in range(10):
        u = (k / 10 + t * .35) % 1; an = u * math.tau
        cv.circ(cx + (R_ + 55) * math.cos(an), cy + (R_ + 55) * math.sin(an), 4, fill=AMB, a=.35 * p)

# ---- S7 4-bit
def s7(cv, t, D):
    cv.text(540, 320, "4-BIT WEIGHTS", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "fewer bytes to fetch per token", 36, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    cv.text(540, 470, "Qwen3-0.6B · tokens per second", 30, MUT, eo(pr(t, .4, .8)), "Medium")
    for k, (lab, v, c, t0) in enumerate([("int8", 21.6, TEAL, .6), ("4-bit", 31.3, AMB, 1.6)]):
        y = 600 + k * 230
        a_ = eo(pr(t, t0, t0 + .4)); g = eo(pr(t, t0, t0 + 1.2))
        cv.text(110, y - 55, lab, 38, c, a_, "Black", anchor="lm")
        cv.rrect(110, y - 25, 110 + 800 * v / 31.3 * g, y + 55, 20, fill=c, a=a_)
        cv.text(110 + 800 * v / 31.3 * g - 20, y + 15, f"{v * g:.1f}", 54, INK, a_, "Black", anchor="rm")
    # weight squares
    q = eo(pr(t, 2.7, 3.2))
    cv.text(540, 1100, "bits per weight", 30, MUT, q, "Medium")
    for i in range(8):
        cv.rrect(130 + i * 100, 1140, 130 + i * 100 + 80, 1200, 10, fill=TEAL, a=q)
    for i in range(5):
        w_ = 80 if i < 4 else 20
        cv.rrect(130 + i * 100, 1220, 130 + i * 100 + w_, 1280, 10, fill=AMB, a=q)
    cv.text(110, 1170, "", 20, MUT, q)
    chip(cv, 540, 1370, "+45% DECODE SPEED", 38, INK, ORG, eback(pr(t, 3.6, 4.2), 2))

# ---- S8 outro
def s8(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(5):
        u = (t * .35 + k / 5) % 1
        cv.circ(540, 700, 40 + u * 330, outline=ORG, w=4, oa=(1 - u) * .7 * p)
    chipart(cv, 540, 700, 220, t, p)
    kinetic(cv, t, 1090, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1200, "Voyaging the Unseen", 46, AMB, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1290, "the bottleneck wasn't thinking. it was fetching.", 30, ORG2, eo(pr(t, 1.8, 2.3)), "Medium")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
