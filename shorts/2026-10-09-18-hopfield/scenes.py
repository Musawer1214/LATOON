# Hopfield: umber, copper, cream, olive
import random, math
BG0, BG1 = (38, 28, 24), (52, 38, 32)
INKC = (246, 238, 220); WHT = (246, 238, 220)
COP, AMB, SAGE, ROSE = (214, 112, 66), (240, 190, 90), (150, 170, 110), (206, 92, 84)
CARDC, LINEC, MUTE, SHAD = (66, 49, 42), (120, 92, 78), (190, 172, 156), (16, 11, 9)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (38, 28, 24), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(11)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k in ("atoms", "mot", "stan"):
        IM[k] = Image.open(os.path.join(IMGDIR, k + ".png")).convert("RGB")
def img(cv, key, cx, cy, sc=1.0, a=1.0, src=None):
    a = cl(a * cv.ga)
    if a <= 0.01 or sc <= 0.02: return
    cv.done()
    s = src if src is not None else IM[key]
    s = s.convert("RGBA")
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
    src = IM[key]; k = min(src.width / w, src.height / h) / zoom
    cw, ch = w * k, h * k
    x0 = (src.width - cw) / 2 + panx * (src.width - cw) / 2; y0 = (src.height - ch) / 2 + pany * (src.height - ch) / 2
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BILINEAR)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=CARDC, outline=LINEC, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.5 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or AMB, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or (30, 24, 22), a, "Black")
T_PIX = ["#####", "..#..", "..#..", "..#..", "..#.."]
def pixgrid(cv, x0, y0, cell, noise_p, seed, a=1, col=AMB, t_p=1.0):
    rs = random.Random(seed)
    for r in range(8):
        for c in range(8):
            on = (1 <= r <= 5 and 1 <= c <= 5 and T_PIX[r - 1][c - 1] == "#")
            flip = rs.random() < .42
            if flip and noise_p > 0.5: on = not on
            x, y = x0 + c * cell, y0 + r * cell
            cv.rrect(x + 3, y + 3, x + cell - 3, y + cell - 3, 8, fill=col if on else mix(CARDC, SHAD, .4), a=a, outline=LINEC, w=1, oa=.5 * a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "AI MEMORY", 110, INKC, -.2, "Black", .03)
    kinetic(cv, t, 460, "MADE OF ATOMS + LIGHT", 54, AMB, -.1, "Black", .02)
    p = eo(pr(t, .1, .8))
    card(cv, 110, 600, 970, 1260, 34, a=p)
    kenburns(cv, "atoms", 540, 930, 800, 600, 1.0 + .12 * pr(t, 0, D), 26, a=p)
    cv.text(540, 1330, "Stanford · Science · Oct 2026", 36, MUTE, eo(pr(t, 1.2, 1.8)), "Bold")
def s1(cv, t, D):
    head(cv, t, "HOPFIELD NETWORK", "switches that recall", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    rs = random.Random(3)
    pts = [(540 + 260 * math.cos(i * 2 * math.pi / 8 + .3), 940 + 260 * math.sin(i * 2 * math.pi / 8 + .3)) for i in range(8)]
    k = 0
    for i in range(8):
        for j in range(i + 1, 8):
            q = eo(pr(t, .4 + k * .04, .8 + k * .04)); k += 1
            cv.line([pts[i], (lerp(pts[i][0], pts[j][0], q), lerp(pts[i][1], pts[j][1], q))], LINEC, 2, .8)
    for i, (x, y) in enumerate(pts):
        q = eback(pr(t, .2 + i * .1, .6 + i * .1), 2)
        cv.circ(x + 4, y + 7, 34 * q, fill=SHAD, a=.5)
        cv.circ(x, y, 34 * q, fill=AMB if i % 3 else COP, outline=INKC, w=3, oa=cl(q))
    cv.text(540, 1260, "everything connected to everything", 34, MUTE, eo(pr(t, 2.4, 3.0)), "Bold")
def s2(cv, t, D):
    head(cv, t, "BLURRY IN, CLEAN OUT", "a smudged letter recalls itself", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    n = 1 - eio(pr(t, 1.8, 3.8))
    cell = 74
    pixgrid(cv, 540 - 4 * cell, 640, cell, n, 7)
    chip(cv, 250, 1260, 580, "NOBEL PRIZE IN PHYSICS 2024", COP, eo(pr(t, 4.4, 5.0)), INKC, 32)
def s3(cv, t, D):
    head(cv, t, "TOO MANY MEMORIES", "frustration = false patterns", ROSE)
    card(cv, 100, 560, 980, 1330, 34)
    rs = random.Random(9)
    for r in range(6):
        for c in range(6):
            x, y = 220 + c * 128, 660 + r * 96
            up = rs.random() < .5
            ang = (-1 if up else 1) * 1
            q = eback(pr(t, .2 + (r + c) * .06, .6 + (r + c) * .06), 2)
            col = ROSE if (r + c) % 3 == 0 else AMB
            cv.circ(x, y, 34 * q, fill=mix(CARDC, col, .35), outline=col, w=3, oa=cl(q))
            dy = 22 * (-1 if up else 1) * q
            cv.line([(x, y - dy), (x, y + dy)], col, 8, cl(q))
            cv.circ(x, y - dy, 9 * q, fill=INKC)
    q = eo(pr(t, 3.6, 4.4))
    kinetic(cv, t, 1295, "SPIN GLASS", 80, ROSE, 3.8, "Black", .04)
def s4(cv, t, D):
    head(cv, t, "STANFORD · LEV LAB", "cold atoms + an optical cavity", AMB)
    p = eo(pr(t, .1, .7))
    card(cv, 100, 560, 980, 1260, 34, a=p)
    kenburns(cv, "mot", 540, 910, 820, 560, 1.0 + .15 * pr(t, 0, D), 26, a=p, panx=-.3 + .5 * pr(t, 0, D))
    cv.text(540, 1330, "atoms trade photons back and forth", 38, INKC, eo(pr(t, 1.6, 2.2)), "Bold")
def s5(cv, t, D):
    head(cv, t, "FALSE → TRUE", "spurious patterns become memories", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    rs = random.Random(5)
    q = eio(pr(t, 1.2, 3.0))
    for i in range(14):
        x, y = 200 + rs.random() * 680, 650 + rs.random() * 560
        col = mix(ROSE, AMB, q)
        r = 22 + 12 * q
        cv.circ(x + 3, y + 6, r, fill=SHAD, a=.45 * eo(pr(t, i * .05, .4 + i * .05)))
        cv.circ(x, y, r * eback(pr(t, i * .05, .4 + i * .05), 2), fill=col, outline=INKC, w=3, oa=eo(pr(t, i * .05, .4 + i * .05)))
    cv.text(540, 1270, "reliable memories" if q > .5 else "spurious patterns", 40, AMB if q > .5 else ROSE, 1, "Black")
def s6(cv, t, D):
    head(cv, t, "UP TO 7× MORE", "than the classic Hopfield limit", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    q = eo(pr(t, .6, 2.4))
    cv.rrect(200, 1190, 440, 1250, 14, fill=mix(CARDC, MUTE, .5))
    cv.text(320, 1280, "Hopfield", 32, MUTE, 1, "Bold")
    h = 60 + (7 * 60 - 60) * q
    cv.rrect(600, 1250 - h, 840, 1250, 14, fill=COP)
    cv.text(720, 1280, "atoms + light", 32, AMB, 1, "Bold")
    kinetic(cv, t, 760, "7×", 150, AMB, 2.4, "Black", .1)
    cv.text(540, 1370, "16-spin network", 36, MUTE, eo(pr(t, 2.8, 3.4)), "Bold")
def s7(cv, t, D):
    head(cv, t, "ATOMS MOVE", "like synapses rewiring", AMB)
    card(cv, 100, 560, 980, 1330, 34)
    for i in range(6):
        a = i * math.pi / 3
        bx, by = 540 + 250 * math.cos(a), 920 + 250 * math.sin(a)
        mv = .5 + .5 * math.sin(t * 2.2 + i)
        x, y = bx + 28 * mv * math.cos(a), by + 28 * mv * math.sin(a)
        cv.line([(540, 920), (x, y)], COP, 3 + int(5 * mv), .9)
        cv.circ(x + 3, y + 6, 36, fill=SHAD, a=.5)
        cv.circ(x, y, 36, fill=AMB, outline=INKC, w=3)
    cv.circ(540, 920, 46, fill=COP, outline=INKC, w=3)
    kinetic(cv, t, 1260, "2× MEMORY", 80, AMB, 2.6, "Black", .04)
def s8(cv, t, D):
    head(cv, t, "A PROTOTYPE", "not a product, but a hint", AMB)
    p = eo(pr(t, .1, .7))
    card(cv, 110, 560, 970, 1280, 34, a=p)
    kenburns(cv, "stan", 540, 920, 820, 620, 1.0 + .1 * pr(t, 0, D), 26, a=p, panx=.2 - .4 * pr(t, 0, D))
    cv.text(540, 1360, "memory that runs on physics itself", 38, INKC, eo(pr(t, 2.4, 3.0)), "Bold")
def s9(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, AMB, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
