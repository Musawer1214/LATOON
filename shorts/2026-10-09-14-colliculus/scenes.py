# Colliculus: walnut, cream, brick, ochre, teal-sage
import random
BG0, BG1 = (36, 28, 25), (52, 41, 36)
INKC = (244, 236, 218); WHT = (244, 236, 218)
COP, AMB, SAGE, ROSE = (206, 92, 70), (232, 176, 72), (110, 170, 160), (214, 130, 110)
CARDC, LINEC, MUTE, SHAD = (62, 49, 43), (120, 98, 86), (178, 160, 146), (16, 11, 9)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (36, 28, 25), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(11)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["brain"] = L("brain_s.jpg"); IM["sag"] = L("sag_s.jpg")
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
import random
GOLD = COP; BL, BL2 = COP, COP
LAY = [AMB, mix(AMB, COP, .35), mix(AMB, COP, .7), COP, ROSE]
def slab(cv, cx, y0, w, h, p, lit=None, a=1, labels=True):
    # five stacked layers: 0-1 superficial (sight), 3-4 deep (touch)
    for i in range(5):
        pp = eback(pr(p, i * .08, .5 + i * .08), 1.5)
        y = y0 + i * (h + 10)
        on = lit is None or i in lit
        col = LAY[i]
        cv.rrect(cx - w / 2 + 6, y + 8, cx + w / 2 + 6, y + h + 8, 18, fill=SHAD, a=.5 * a * cl(pp))
        cv.rrect(cx - w / 2, y, cx + w / 2, y + h, 18, fill=col, a=a * cl(pp) * (1 if on else .28))
        cv.rrect(cx - w / 2 + 10, y + 8, cx + w / 2 - 10, y + 16, 4, fill=(255, 240, 220), a=.18 * a * cl(pp) * (1 if on else .3))
def s0(cv, t, D):
    kinetic(cv, t, 320, "BEFORE IT HAPPENS", 92, INKC, -.2, "Black", .02)
    kinetic(cv, t, 428, "YOUR BRAIN KNOWS", 80, COP, -.1, "Black", .02)
    p = eback(pr(t, .1, .8), 2)
    card(cv, 150, 640, 930, 1300, 34, a=cl(p))
    kenburns(cv, "brain", 540, 970, 740, 620, 1.0, 28, cl(p))
    r = 38 + 8 * math.sin(t * 5)
    q = eo(pr(t, .8, 1.3))
    cv.circ(520, 1010, r, outline=AMB, w=6, oa=q)
    cv.line([(560, 1050), (700, 1180)], AMB, 5, q)
    cv.rrect(560, 1170, 900, 1240, 34, fill=AMB, a=q)
    cv.text(730, 1205, "SUPERIOR COLLICULUS", 24, (40, 28, 22), q, "Black")
    cv.text(540, 1340, "Image: Life Science Databases (CC BY-SA 2.1 jp)", 20, MUTE, eo(pr(t, 1.2, 1.8)), "SemiBold")
def s1(cv, t, D):
    head(cv, t, "SUPERIOR COLLICULUS", "midbrain · target of the optic nerve", AMB)
    p = eback(pr(t, .2, .9), 2)
    card(cv, 100, 520, 980, 1080, 34, a=cl(p))
    kenburns(cv, "sag", 540, 800, 840, 520, 1.0 + .08 * pr(t, 0, D), 26, cl(p), panx=.1)
    x0 = 330; q = eio(pr(t, 1.6, 2.6))
    cv.line([(380, 1150), (380 + 300 * q, 1150)], AMB, 8)
    cv.line([(380, 1130), (380, 1170)], AMB, 8, q > 0)
    cv.line([(380 + 300 * q, 1130), (380 + 300 * q, 1170)], AMB, 8, q > .1)
    cv.text(540, 1215, "about 6 mm wide", 52, AMB, eo(pr(t, 2.0, 2.6)), "Black")
    cv.text(540, 1300, '"just a reflex relay"', 42, MUTE, eo(pr(t, 3.2, 3.8)), "Bold")
    w = cv.tw('"just a reflex relay"', 42, "Bold")
    cv.line([(540 - w / 2, 1300), (540 - w / 2 + w * eo(pr(t, 4.2, 4.8)), 1300)], COP, 7, eo(pr(t, 4.2, 4.4)))
    cv.text(540, 1380, "Photo: J. A. Beal, LSUHSC (CC BY 2.5)", 20, MUTE, eo(pr(t, 1, 1.5)), "SemiBold")
def s2(cv, t, D):
    head(cv, t, "7 TESLA FMRI", "MIT · Mass General Brigham", AMB)
    for k, (cx, lab, fine) in enumerate([(290, "REGULAR MRI", False), (790, "THIS STUDY", True)]):
        p = eo(pr(t, .2 + k * .6, .9 + k * .6))
        cv.rrect(cx - 220 + 6, 560 + 8, cx + 220 + 6, 1060 + 8, 26, fill=SHAD, a=.5 * p)
        cv.rrect(cx - 220, 560, cx + 220, 1060, 26, fill=CARDC, outline=LINEC, w=3, a=p, oa=p)
        if fine:
            for i in range(5):
                y = 620 + i * 80
                cv.rrect(cx - 170, y, cx + 170, y + 64, 12, fill=LAY[i], a=eo(pr(t, 1.2 + i * .15, 1.7 + i * .15)))
            cv.text(cx, 1120, "1.1 mm voxels", 44, AMB, eo(pr(t, 2.2, 2.8)), "Black")
            cv.text(cx, 1175, "layers resolved", 30, SAGE, eo(pr(t, 2.6, 3.2)), "Bold")
        else:
            avg = mix(AMB, COP, .5)
            for i in range(2):
                cv.rrect(cx - 170, 620 + i * 190, cx + 170, 620 + i * 190 + 170, 14, fill=avg, a=p)
            cv.text(cx, 1120, "2-3 mm voxels", 44, MUTE, eo(pr(t, 1.0, 1.6)), "Black")
            cv.text(cx, 1175, "layers blur", 30, ROSE, eo(pr(t, 1.4, 2.0)), "Bold")
        cv.text(cx, 600, lab, 26, MUTE, p, "Black")
def s3(cv, t, D):
    head(cv, t, "LAYERED JOBS", "known from animal studies", AMB)
    slab(cv, 540, 540, 560, 100, pr(t, .1, 1.2))
    p1 = eo(pr(t, 1.2, 1.8)); p2 = eo(pr(t, 2.6, 3.2))
    cv.text(540, 1180, "SHALLOW = SIGHT", 54, AMB, p1, "Black")
    cv.text(540, 1260, "DEEP = TOUCH", 54, ROSE, p2, "Black")
    cv.circ(150, 640, 44 * p1, outline=AMB, w=7, oa=p1); cv.circ(150, 640, 14 * p1, fill=AMB, a=p1)
    cv.circ(930, 1040, 40 * p2, fill=ROSE, a=p2); cv.text(930, 1040, "T", 40, (40, 28, 22), p2, "Black")
    cv.line([(210, 640), (250, 640)], AMB, 5, p1); cv.line([(870, 1040), (830, 1040)], ROSE, 5, p2)
def s4(cv, t, D):
    head(cv, t, "80 PEOPLE", "human layers confirmed", AMB)
    for k, (cx, lab, lit, col, sub) in enumerate([(290, "PICTURES", [0, 1], AMB, "shallow lit"), (790, "THUMB PRESSURE", [3, 4], ROSE, "deep lit")]):
        p = eo(pr(t, .3 + k * 1.6, .9 + k * 1.6))
        slab(cv, cx, 600, 380, 80, pr(t, .2 + k * 1.6, 1.0 + k * 1.6), lit if p > .3 else None, 1)
        cv.text(cx, 1070, lab, 34, INKC, p, "Black")
        cv.text(cx, 1125, sub, 34, col, p, "Bold")
    cv.text(540, 1300, "matches the animal map", 42, INKC, eo(pr(t, 3.6, 4.2)), "Bold")
def s5(cv, t, D):
    head(cv, t, "THE TWIST", "before anything arrived", AMB)
    segs = [("SHAPES", 110, 380, MUTE), ("CHOOSE · 2 s", 400, 700, AMB), ("STIMULUS", 720, 970, ROSE)]
    for i, (lab, a_, b_, c_) in enumerate(segs):
        p = eo(pr(t, .2 + i * .4, .7 + i * .4))
        cv.rrect(a_, 560, b_, 660, 20, fill=CARDC, outline=c_, w=4, a=p, oa=p)
        cv.text((a_ + b_) / 2, 610, lab, 26, c_, p, "Black")
    q = eo(pr(t, 2.2, 3.0))
    cv.line([(550, 680), (550, 760)], AMB, 6, q)
    lit = [3, 4] if t > 3.0 else None
    slab(cv, 540, 790, 640, 86, pr(t, 1.6, 2.4), lit)
    cv.text(540, 1330, "already lit for what was coming", 42, AMB, eo(pr(t, 3.6, 4.4)), "Black")
    cv.text(540, 1400, "(deep layers shown: touch group)", 26, MUTE, eo(pr(t, 4.0, 4.6)), "SemiBold")
def s6(cv, t, D):
    head(cv, t, "A DECODER", "trained on the pre-signal", AMB)
    rs = random.Random(4)
    card(cv, 100, 560, 560, 1000, 30)
    cv.text(330, 600, "PRE-SIGNAL", 26, MUTE, eo(pr(t, .2, .6)), "Black")
    for i in range(14):
        h = 40 + rs.randint(0, 220) * eo(pr(t, .3 + i * .05, .9 + i * .05))
        cv.rrect(130 + i * 31, 960 - h, 130 + i * 31 + 22, 960, 6, fill=ROSE if i % 3 else AMB, a=eo(pr(t, .3, .8)))
    q = eo(pr(t, 1.6, 2.2))
    cv.line([(580, 780), (650, 780)], INKC, 7, q); cv.poly([(650, 750), (700, 780), (650, 810)], INKC, q)
    cv.rrect(720, 700, 980, 860, 30, fill=ROSE, a=eo(pr(t, 2.2, 2.8)))
    cv.text(850, 760, "TOUCH", 50, (40, 28, 22), eo(pr(t, 2.4, 3.0)), "Black")
    cv.text(850, 815, "coming next", 28, (40, 28, 22), eo(pr(t, 2.6, 3.2)), "Bold")
    cv.text(540, 1160, "better than chance,", 44, INKC, eo(pr(t, 3.0, 3.6)), "Bold")
    cv.text(540, 1230, "before any touch", 44, AMB, eo(pr(t, 3.4, 4.0)), "Black")
def s7(cv, t, D):
    kinetic(cv, t, 330, "SAME SCREEN", 96, INKC, -.1, "Black", .02)
    kinetic(cv, t, 440, "SAME BUTTON", 96, INKC, .1, "Black", .02)
    p = eo(pr(t, .8, 1.4))
    card(cv, 120, 600, 960, 900, 34, a=p)
    cv.text(540, 700, "=", 100, MUTE, p, "Black")
    cv.text(540, 810, "identical input and movement", 36, MUTE, p, "SemiBold")
    q = eback(pr(t, 1.8, 2.6), 2)
    cv.rrect(160, 1020, 920, 1190, 40, fill=COP, a=cl(q))
    cv.text(540, 1080, "ONLY WHAT THEY", 52, (255, 244, 230), cl(q), "Black")
    cv.text(540, 1140, "EXPECTED DIFFERED", 52, (255, 244, 230), cl(q), "Black")
def s8(cv, t, D):
    head(cv, t, "ONE CAVEAT", "the touch was unpleasant", AMB)
    card(cv, 100, 560, 980, 960, 34)
    cv.text(540, 650, "may partly be", 44, MUTE, eo(pr(t, .3, .9)), "Bold")
    cv.text(540, 740, "PREPARATION", 90, ROSE, eo(pr(t, .6, 1.2)), "Black")
    cv.text(540, 840, "not a precise prediction", 40, INKC, eo(pr(t, 1.2, 1.8)), "SemiBold")
    cv.text(540, 910, "no eye tracking in the scanner", 30, MUTE, eo(pr(t, 1.8, 2.4)), "SemiBold")
    cv.text(540, 1130, "Your oldest brain", 62, INKC, eo(pr(t, 3.0, 3.6)), "Black")
    cv.text(540, 1220, "predicts.", 90, AMB, eo(pr(t, 3.5, 4.1)), "Black")
    cv.text(540, 1330, "Nature Neuroscience, 2026", 28, MUTE, eo(pr(t, 3.8, 4.4)), "SemiBold")
def s9(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, AMB, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
