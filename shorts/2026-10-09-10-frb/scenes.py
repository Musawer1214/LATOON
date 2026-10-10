# FRB: warm night ink, cream, copper, amber, sage
import random
BG0, BG1 = (26, 22, 21), (40, 33, 29)
INKC = (244, 236, 218); WHT = (244, 236, 218)
COP, AMB, SAGE, ROSE = (214, 112, 62), (236, 178, 70), (124, 168, 146), (190, 96, 90)
CARDC, LINEC, MUTE, SHAD = (48, 41, 37), (96, 84, 74), (160, 148, 132), (14, 11, 10)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (26, 22, 21), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(11)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["jwst"] = L("jwst.png"); IM["spec"] = L("spec.jpg"); IM["mk"] = L("meerkat.jpg")
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
def zbox(cv, key, cx, cy, w, h, b0, b1, p, r, a=1):
    src = IM[key]; q = eio(p)
    bx = [lerp(b0[i], b1[i], q) for i in range(4)]
    crop = src.crop(tuple(int(v) for v in bx)).resize((int(w), int(h)), Image.LANCZOS)
    from PIL import ImageEnhance
    if q > .02: crop = ImageEnhance.Brightness(crop).enhance(1 + 1.0 * q)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))
def stars(cv, n, x0, y0, x1, y1, t, seed=3, a=1):
    rs = random.Random(seed)
    for i in range(n):
        x = rs.uniform(x0, x1); y = rs.uniform(y0, y1); r = rs.choice([1.5, 1.5, 2, 2.5]); ph = rs.uniform(0, 6.28)
        cv.circ(x, y, r, fill=(240, 226, 196), a=a * (.45 + .4 * math.sin(t * 1.7 + ph)))
def galaxy(cv, cx, cy, s, rot, a=1, col=AMB):
    for k in range(5):
        r = s * (1 - k * .16)
        for arm in range(2):
            pts = []
            for j in range(26):
                u = j / 25; ang = rot + arm * math.pi + u * 3.6; rr = r * (.1 + .9 * u)
                pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang) * .62))
            cv.line(pts, mix(col, (250, 230, 190), k / 5), max(2, s * .09 * (1 - k * .15)), a * (.35 + .12 * k))
    cv.circ(cx, cy, s * .17, fill=(252, 232, 190), a=a)
def earth(cv, cx, cy, r, a=1):
    cv.circ(cx + 5, cy + 7, r, fill=SHAD, a=.5 * a)
    cv.circ(cx, cy, r, fill=(70, 112, 118), a=a)
    for (dx, dy, rr, c) in [(-.35, -.2, .38, (122, 150, 100)), (.3, .25, .3, (140, 160, 108)), (.1, -.5, .2, (200, 190, 150)), (-.1, .45, .22, (196, 188, 150))]:
        cv.circ(cx + dx * r, cy + dy * r, rr * r, fill=c, a=a)
    cv.circ(cx - r * .3, cy - r * .3, r * .55, fill=(255, 245, 220), a=.12 * a)
    cv.circ(cx, cy, r, outline=(236, 224, 196), w=3, oa=.6 * a)
def dish(cv, cx, cy, s, a=1):
    cv.line([(cx, cy), (cx, cy + s * .9)], MUTE, max(3, s * .08), a)
    cv.line([(cx - s * .4, cy + s * .9), (cx + s * .4, cy + s * .9)], MUTE, max(3, s * .08), a)
    pts = [(cx + s * .75 * math.cos(math.radians(a_)), cy - s * .1 + s * .75 * math.sin(math.radians(a_))) for a_ in range(20, 161, 10)]
    cv.line(pts, INKC, max(4, s * .1), a)
    cv.line([(cx, cy - s * .1), (cx - s * .3, cy - s * .75)], MUTE, 3, a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "10 BILLION YEARS", 92, INKC, -.2, "Black", .02)
    kinetic(cv, t, 440, "IN TRANSIT", 92, COP, -.1, "Black", .02)
    p = eo(pr(t, .0, .6))
    X0, X1, Y = 140, 940, 1150
    cv.rrect(X0 - 20, Y - 12, X1 + 20, Y + 12, 12, fill=CARDC, a=p, outline=LINEC, w=3, oa=p)
    def xp(by): return X0 + (10.6 - by) / 10.6 * (X1 - X0)
    prog = eio(pr(t, .3, 3.6))
    xe = lerp(X0, X1, prog)
    cv.rrect(X0 - 20, Y - 12, X0 - 20 + max(24, (xe - X0 + 20)), Y + 12, 12, fill=COP, a=p)
    galaxy(cv, X0 + 10, 880, 110, t * .25, eo(pr(t, .0, .5)))
    cv.text(X0 + 10, 1030, "FLASH LEAVES", 32, AMB, p, "Black"); cv.text(X0 + 10, 1210, "10.6 B yrs ago", 32, INKC, p, "Bold")
    # pulse rings from galaxy
    for k in range(3):
        u = (t * .8 + k / 3) % 1
        if t < 3.8: cv.arc(X0 + 10, 880, 120 + u * 150, 20, 160, COP, 5, (1 - u) * .8 * p)
    ex = xp(4.5)
    e_ = eback(pr(t, 2.4, 3.1), 2)
    earth(cv, ex, 880, 86 * cl(e_), cl(e_))
    cv.line([(ex, Y - 60), (ex, Y + 40)], MUTE, 4, cl(e_))
    cv.text(ex, 1030, "EARTH FORMS", 32, SAGE, cl(e_), "Black"); cv.text(ex, 1210, "~4.5 B yrs ago", 32, INKC, cl(e_), "Bold")
    dish(cv, X1 - 20, 860, 95, p)
    cv.text(X1 - 20, 1030, "WE LISTEN", 32, AMB, p, "Black"); cv.text(X1 - 20, 1210, "today", 32, INKC, p, "Bold")
    cv.circ(xe, Y, 17, fill=(255, 230, 170), a=p, outline=COP, w=5, oa=p)
def s1(cv, t, D):
    head(cv, t, "FRB 20240304B", "a fast radio burst")
    card(cv, 90, 500, 990, 1120, 34)
    cv.text(130, 548, "SIGNAL STRENGTH", 28, MUTE, eo(pr(t, .2, .6)), "Black", anchor="lm")
    base = 960; x0, x1 = 150, 930
    cv.line([(x0, base), (x1, base)], LINEC, 4, eo(pr(t, .2, .6)))
    rs = np.random.RandomState(4)
    nz = rs.uniform(-1, 1, 200)
    prog = pr(t, .5, 3.4)
    pts = []
    N = 160
    for i in range(int(N * prog) + 1):
        u = i / N; x = lerp(x0, x1, u)
        sp = math.exp(-((u - .62) / .012) ** 2) * 330
        y = base - 18 - 14 * nz[i] * 1.0 - sp
        pts.append((x, y))
    cv.line(pts, AMB, 5, 1)
    sp_ = pr(t, 2.0, 2.4)
    if sp_ > 0:
        for k in range(3):
            u = (t - 2.0) * .9 + k * .3
            if 0 < u < 1: cv.circ(lerp(x0, x1, .62), base - 340, 30 + u * 120, outline=COP, w=4, oa=(1 - u) * .6)
    cv.text(lerp(x0, x1, .62) + 150, base - 330, "milliseconds", 38, COP, eo(pr(t, 2.2, 2.7)), "Black")
    n = eo(pr(t, 3.3, 4.2))
    chip(cv, 130, 1190, 380, "ENORMOUS ENERGY", COP, n, size=28, h=74)
    chip(cv, 540, 1190, 410, "ORIGIN UNCERTAIN", SAGE, eo(pr(t, 4.5, 5.2)), size=28, h=74)
def s2(cv, t, D):
    head(cv, t, "MEERKAT CAUGHT IT", "radio telescope · South Africa")
    p = eback(pr(t, .1, .7), 2)
    cv.rrect(80 + 8, 500 + 12, 1000 + 8, 1100 + 12, 30, fill=SHAD, a=.5 * cl(p))
    kenburns(cv, "mk", 540, 800, 920, 600, 1.0 + .16 * pr(t, 0, D), 30, cl(p), panx=-.4 + .5 * pr(t, 0, D))
    cv.rrect(80, 500, 1000, 1100, 30, outline=LINEC, w=4, oa=cl(p))
    cv.text(540, 1135, "Photo: SKAO, CC BY 3.0", 26, MUTE, eo(pr(t, .8, 1.3)), "SemiBold")
    chip(cv, 100, 1200, 880, "MOST DISTANT FRB EVER DETECTED", COP, eo(pr(t, 1.6, 2.2)), size=34, h=84)
    cv.text(540, 1345, "more than double the old distance record", 34, INKC, eo(pr(t, 2.6, 3.2)), "Bold")
def s3(cv, t, D):
    head(cv, t, "A FLASH HAS NO ADDRESS", "radio gives a rough position")
    card(cv, 90, 500, 990, 1200, 34, fill=(24, 20, 19))
    stars(cv, 70, 110, 520, 970, 1180, t)
    p = eo(pr(t, .3, .9))
    pulse = .5 + .5 * math.sin(t * 3)
    cv.circ(540, 850, 190 + 8 * pulse, outline=COP, w=5, oa=p)
    cv.circ(540, 850, 190, fill=COP, a=.07 * p)
    for ang in range(0, 360, 30):
        a_ = math.radians(ang)
        cv.line([(540 + 190 * math.cos(a_), 850 + 190 * math.sin(a_)), (540 + 205 * math.cos(a_), 850 + 205 * math.sin(a_))], COP, 4, p)
    cv.text(540, 850, "?", 150, AMB, eo(pr(t, 1.2, 1.8)), "Black")
    cv.text(540, 1100, "Keck telescopes: nothing visible", 36, INKC, eo(pr(t, 1.8, 2.4)), "Bold")
    chip(cv, 200, 1260, 680, "TOO FAINT FOR THE GROUND", ROSE, eo(pr(t, 2.8, 3.4)), size=32, h=80)
def s4(cv, t, D):
    head(cv, t, "THEN CAME WEBB", "James Webb Space Telescope · NIRCam")
    p = eback(pr(t, .1, .7), 2)
    w_, h_ = 880, 766
    cv.rrect(100 + 8, 480 + 12, 980 + 8, 1246 + 12, 28, fill=SHAD, a=.5 * cl(p))
    zbox(cv, "jwst", 540, 863, w_, h_, (0, 0, 1600, 1394), (1118, 548, 1448, 836), pr(t, 1.0, 4.4), 28, cl(p))
    cv.rrect(100, 480, 980, 1246, 28, outline=LINEC, w=4, oa=cl(p))
    cv.text(540, 1282, "NASA, ESA, CSA, STScI, T. Nanayakkara (USYD), J. DePasquale (STScI) · CC BY 4.0", 21, MUTE, eo(pr(t, .8, 1.3)), "SemiBold")
    chip(cv, 130, 1330, 820, "~10 MILLION SUNS OF MASS", AMB, eo(pr(t, 3.4, 4.0)), size=36, h=84)
def s5(cv, t, D):
    head(cv, t, "LIGHT STRETCHED BY SPACE", "the universe kept expanding")
    card(cv, 90, 470, 990, 830, 30)
    L1, L2 = 120, 960
    def wave(y, lam, col, a, ph=0):
        pts = [(x, y + 52 * math.sin((x - L1) / lam * 6.283 + ph)) for x in range(L1 + 40, L2 - 40, 6)]
        cv.line(pts, col, 7, a)
    cv.text(150, 520, "AS EMITTED", 26, MUTE, eo(pr(t, .2, .6)), "Black", anchor="lm")
    wave(600, 70, SAGE, eo(pr(t, .2, .7)), -t * 3)
    s = 1 + 2.148 * eio(pr(t, 1.4, 3.6))
    cv.text(150, 685, "AS RECEIVED", 26, MUTE, eo(pr(t, .8, 1.2)), "Black", anchor="lm")
    wave(755, 70 * s, COP, eo(pr(t, .8, 1.2)), -t * 3)
    cv.text(930, 685, f"× {s:.1f} longer", 34, AMB, eo(pr(t, 1.6, 2.2)), "Black", anchor="rm")
    q = eo(pr(t, 2.8, 3.5))
    kenburns(cv, "spec", 540, 1075, 780, 439, 1.0, 22, cl(q))
    cv.rrect(150, 855, 930, 1294, 22, outline=LINEC, w=4, oa=cl(q))
    cv.text(540, 1322, "Webb spectrum: oxygen + hydrogen lines · NASA, ESA, CSA, J. Olmsted (STScI), CC BY 4.0", 20, MUTE, cl(q), "SemiBold")
    chip(cv, 130, 1360, 820, "10.6 BILLION YEARS AGO", COP, eo(pr(t, 4.0, 4.7)), size=38, h=84)
def s6(cv, t, D):
    head(cv, t, "A YOUNG, BUSY GALAXY", "small · metal-poor · forming stars")
    card(cv, 90, 480, 990, 1000, 34, fill=(24, 20, 19))
    stars(cv, 40, 110, 500, 970, 980, t, 8)
    cx, cy = 540, 730
    # dipole field loops
    for k, (rx, ry) in enumerate([(70, 110), (115, 165), (160, 220)]):
        a_ = eo(pr(t, .3 + k * .3, .9 + k * .3))
        for sgn in (-1, 1):
            pts = [(cx + sgn * rx * math.sin(u), cy - ry * math.cos(u) * 0 + 0) for u in []]
            pts = []
            for j in range(41):
                u = j / 40 * math.pi
                pts.append((cx + sgn * rx * math.sin(u) * 1.0, cy + ry * 0.0 - ry * math.cos(u) * 1.0))
            cv.line(pts, mix(AMB, COP, k / 2), 4, .8 * a_)
    cv.circ(cx + 4, cy + 8, 46, fill=SHAD, a=.5)
    cv.circ(cx, cy, 46, fill=(214, 204, 186)); cv.circ(cx - 12, cy - 12, 24, fill=(250, 244, 230), a=.5)
    cv.circ(cx, cy, 46, outline=(120, 108, 92), w=3)
    for k in range(3):
        u = (t * .7 + k / 3) % 1
        if t > 2.2: cv.arc(cx, cy, 70 + u * 190, -50, 50, COP, 5, (1 - u) * .8)
    cv.text(540, 960, "MAGNETAR · a newborn neutron star", 30, INKC, eo(pr(t, 1.5, 2.1)), "Black")
    chip(cv, 110, 1060, 860, "ONE LEADING THEORY, NOT PROVEN", SAGE, eo(pr(t, 3.0, 3.7)), size=32, h=80)
    chip(cv, 110, 1180, 860, "IT FITS: A YOUNG GALAXY", COP, eo(pr(t, 4.2, 4.9)), size=32, h=80)
def s7(cv, t, D):
    head(cv, t, "THE FLASH AS A FLASHLIGHT", "colors arrive at different times")
    card(cv, 90, 480, 990, 1170, 34)
    ox, oy, wx, hy = 190, 1060, 720, 500
    cv.line([(ox, oy), (ox, oy - hy)], LINEC, 4, 1); cv.line([(ox, oy), (ox + wx, oy)], LINEC, 4, 1)
    cv.text(ox + wx / 2, oy + 45, "ARRIVAL TIME →", 26, MUTE, eo(pr(t, .2, .6)), "Black")
    cv.text(120, oy - hy / 2, "FREQ", 24, MUTE, eo(pr(t, .2, .6)), "Black")
    prog = pr(t, .5, 3.0)
    n = 36
    for i in range(int(n * prog) + 1):
        u = i / n
        x = ox + 60 + wx * 0.82 * (u ** .5 * .12 + (1 - (1 - u) ** 2) * .88) if False else ox + 50 + (wx - 100) * (u ** 1.0)
        y = oy - 40 - (hy - 100) * (1 - u) ** 1.7
        c = mix(AMB, ROSE, u)
        cv.circ(x, y, 13, fill=c, outline=(250, 240, 220), w=2)
    cv.text(ox + 120, oy - hy + 60, "high first", 30, AMB, eo(pr(t, 1.0, 1.5)), "Black", anchor="lm")
    cv.text(ox + wx - 40, oy - 150, "low later", 30, ROSE, eo(pr(t, 2.6, 3.1)), "Black", anchor="rm")
    chip(cv, 110, 1230, 860, "DELAY = HOW MUCH GAS IT CROSSED", COP, eo(pr(t, 3.6, 4.3)), size=32, h=84)
def s8(cv, t, D):
    kinetic(cv, t, 400, "ONE MILLISECOND", 84, INKC, .0, "Black", .03)
    kinetic(cv, t, 500, "OF SIGNAL", 84, COP, .2, "Black", .03)
    cx, cy = 540, 960
    p = eio(pr(t, .3, 2.2))
    cv.circ(cx, cy, 250, outline=LINEC, w=26, oa=1)
    cv.arc(cx, cy, 250, 0, 360 * .8 * p, COP, 26, 1)
    cv.text(cx, cy - 10, f"{int(80 * p)}%", 170, INKC, eo(pr(t, .2, .6)), "Black")
    cv.text(cx, cy + 110, "of cosmic history", 40, AMB, eo(pr(t, .8, 1.3)), "Bold")
    cv.text(540, 1330, "probed by a single burst", 38, INKC, eo(pr(t, 1.6, 2.2)), "Bold")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=COP, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=COP, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1140, "Voyaging the Unseen", 46, AMB, eo(pr(t, 1.2, 1.8)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
