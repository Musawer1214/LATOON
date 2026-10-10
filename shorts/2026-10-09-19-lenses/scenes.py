# Lenses: dark olive-charcoal, brass, cream, rust
import random, math
BG0, BG1 = (30, 31, 26), (44, 42, 34)
INKC = (246, 238, 220); WHT = (246, 238, 220)
COP, AMB, SAGE, ROSE = (196, 98, 58), (232, 184, 84), (140, 164, 108), (196, 84, 76)
CARDC, LINEC, MUTE, SHAD = (54, 52, 42), (112, 104, 84), (190, 182, 160), (12, 12, 9)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (30, 31, 26), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(11)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k in ("l1", "l2", "info", "col"):
        IM[k] = Image.open(os.path.join(IMGDIR, {"l1":"desi-gravitational-lens-discovered-1","l2":"desi-gravitational-lens-discovered-2","info":"noirlab2615d","col":"55-DESI-GravLenses-CC-collage-cc4"}[k] + ".jpg")).convert("RGB")
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
def credit(cv, t, txt="NSF NOIRLab · DESI Legacy Imaging Surveys"):
    cv.text(540, 1385, txt, 28, MUTE, eo(pr(t, .8, 1.4)), "SemiBold")
def s0(cv, t, D):
    kinetic(cv, t, 330, "70 NATURAL", 110, INKC, -.2, "Black", .03)
    kinetic(cv, t, 460, "TELESCOPES FOUND", 66, AMB, -.1, "Black", .02)
    p = eo(pr(t, .1, .8)); card(cv, 150, 580, 930, 1360, 34, a=p)
    kenburns(cv, "l1", 540, 970, 720, 720, 1.0 + .25 * pr(t, 0, D), 26, a=p)
    credit(cv, t)
def s1(cv, t, D):
    head(cv, t, "GRAVITATIONAL LENS", "a galaxy that bends light", AMB)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1330, 34, a=p)
    kenburns(cv, "info", 540, 945, 840, 472, 1.0 + .12 * pr(t, 0, D), 20, a=p, panx=-.3 + .6 * pr(t, 0, D))
    cv.text(540, 1230, "heavy galaxy = cosmic magnifying glass", 34, INKC, eo(pr(t, 1.6, 2.2)), "Bold")
def s2(cv, t, D):
    head(cv, t, "RINGS AND ARCS", "the same galaxy, smeared round", AMB)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1360, 34, a=p)
    kenburns(cv, "l2", 540, 960, 760, 760, 1.0 + .3 * pr(t, 0, D), 26, a=p)
    cx, cy = 540, 960
    q = eo(pr(t, 1.2, 2.4)); cv.arc(cx, cy, 150 * q + 10, 0, 360 * q, AMB, 4, .9 * q)
def s3(cv, t, D):
    head(cv, t, "4 BILLION OBJECTS", "too many to scroll by eye", ROSE)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1330, 34, a=p)
    kenburns(cv, "col", 540, 880, 840, 385, 1.0 + .15 * pr(t, 0, D), 20, a=p, panx=-.5 + pr(t, 0, D))
    n = int(3_900_000_000 * eo(pr(t, .8, 5.5)))
    cv.text(540, 1140, f"{n:,}".replace(",", " "), 84, AMB, eo(pr(t, .6, 1.2)), "Black")
    cv.text(540, 1240, "5.6-trillion-pixel sky map", 34, MUTE, eo(pr(t, 1.4, 2.0)), "Bold")
def s4(cv, t, D):
    head(cv, t, "A NEURAL NETWORK", "hunting for ring-shaped patterns", AMB)
    card(cv, 90, 560, 990, 1330, 34)
    rs = random.Random(5)
    g = 14; cell = 42; x0, y0 = 150, 660
    cx = x0 + g * cell / 2; cy = y0 + g * cell / 2
    for r in range(g):
        for c in range(g):
            d = math.hypot(c - g / 2 + .5, r - g / 2 + .5)
            ring = abs(d - 4.6) < .9
            q = eo(pr(t, .1 + (r + c) * .02, .5 + (r + c) * .02))
            col = mix(CARDC, AMB, .85) if ring and t > 2.0 else mix(CARDC, LINEC, .35 + rs.random() * .3)
            cv.rrect(x0 + c * cell + 2, y0 + r * cell + 2, x0 + (c + 1) * cell - 2, y0 + (r + 1) * cell - 2, 6, fill=col, a=q)
    sc = eo(pr(t, 2.4, 3.2))
    chip(cv, 770, 880, 190, "RING", COP, sc, INKC, 34)
    cv.line([(740, 920), (770, 920)], AMB, 4, sc)
    cv.text(540, 1290, "residual neural network", 34, MUTE, eo(pr(t, 1.0, 1.6)), "Bold")
def s5(cv, t, D):
    head(cv, t, "76 CANDIDATES", "a pattern isn't proof", ROSE)
    card(cv, 90, 560, 990, 1330, 34)
    for i in range(76):
        r, c = divmod(i, 12)
        x, y = 160 + c * 66, 700 + r * 78
        q = eback(pr(t, .1 + i * .02, .5 + i * .02), 2)
        cv.circ(x, y, 24 * q, fill=mix(CARDC, AMB, .6), outline=AMB, w=2, oa=cl(q))
    kinetic(cv, t, 1285, "STILL JUST GUESSES", 56, ROSE, 2.2, "Black", .03)
def s6(cv, t, D):
    head(cv, t, "VLT · MUSE", "measure both distances", AMB)
    card(cv, 90, 560, 990, 1330, 34)
    ys = [790, 1100]
    q = eo(pr(t, .3, 1.2))
    cv.circ(540, 940, 44 * q, fill=AMB, outline=INKC, w=3)
    cv.circ(540, 790 - 120, 24 * q, fill=COP, outline=INKC, w=3)
    cv.line([(540, 670), (540, lerp(670, 1180, eo(pr(t, 1.2, 2.4))))], mix(CARDC, AMB, .5), 4, .9)
    cv.text(540, 1230, "light from each galaxy, split into a spectrum", 30, MUTE, eo(pr(t, 1.8, 2.4)), "Bold")
    for i in range(24):
        x = 200 + i * 32
        h = 30 + 90 * abs(math.sin(i * .7 + 1))
        qq = eo(pr(t, 2.4 + i * .05, 3.0 + i * .05))
        cv.line([(x, 1160), (x, 1160 - h * qq)], [AMB, COP, SAGE, ROSE][i % 4], 10, .85)
def s7(cv, t, D):
    kinetic(cv, t, 480, "70", 360, AMB, -.2, "Black", .08)
    kinetic(cv, t, 760, "CONFIRMED", 90, INKC, .2, "Black", .03)
    q = eo(pr(t, .6, 1.4)); card(cv, 150, 900, 930, 1330, 34, a=q)
    kenburns(cv, "l1", 540, 1115, 740, 380, 1.1, 22, a=q, pany=-.3)
def s8(cv, t, D):
    head(cv, t, "WHY IT MATTERS", "magnify the early universe", AMB)
    p = eo(pr(t, .1, .7)); card(cv, 90, 560, 990, 1330, 34, a=p)
    kenburns(cv, "info", 540, 940, 840, 472, 1.15, 20, a=p, panx=.4 - .8 * pr(t, 0, D))
    chip(cv, 190, 1190, 700, "DARK MATTER BENDS LIGHT TOO", COP, eo(pr(t, 2.2, 3.0)), INKC, 32)
def s9(cv, t, D):
    head(cv, t, "AI NARROWED THE SKY", "humans spend the telescope time", AMB)
    card(cv, 90, 560, 990, 1330, 34)
    cv.text(300, 760, "4 BILLION", 54, MUTE, eo(pr(t, .2, .8)), "Black")
    cv.text(780, 760, "76", 54, AMB, eo(pr(t, 1.6, 2.2)), "Black")
    cv.text(540, 760, "→", 54, INKC, eo(pr(t, 1.0, 1.6)), "Black")
    cv.text(780, 860, "→ 70", 70, SAGE, eo(pr(t, 3.0, 3.6)), "Black")
    kenburns(cv, "l2", 540, 1090, 600, 340, 1.4, 22, a=eo(pr(t, .4, 1.0)))
def s10(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, AMB, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
