# Embeddings: forest green, cream, coral, mustard
import random
BG0, BG1 = (24, 40, 34), (34, 54, 46)
INKC = (244, 236, 218); WHT = (244, 236, 218)
COP, AMB, SAGE, ROSE = (226, 106, 78), (236, 188, 80), (140, 190, 150), (236, 150, 130)
CARDC, LINEC, MUTE, SHAD = (44, 66, 57), (96, 128, 112), (168, 188, 172), (10, 18, 14)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (24, 40, 34), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(11)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
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
ANI = {"dog": (300, 760), "puppy": (400, 700), "wolf": (260, 860), "cat": (440, 830)}
FOOD = {"pizza": (700, 1020), "pasta": (800, 1100), "bread": (660, 1130)}
def dot(cv, x, y, w, col, p, big=False, lab=True):
    r = 20 if big else 15
    q = eback(p, 2)
    cv.circ(x + 4, y + 7, r * q, fill=SHAD, a=.5 * cl(q))
    cv.circ(x, y, r * q, fill=col, a=cl(q * 1.5), outline=INKC, w=3, oa=cl(q))
    if lab: cv.text(x, y - 38, w, 34, INKC, cl(q * 1.5), "Black")
def mapcard(cv, a=1):
    card(cv, 100, 520, 980, 1300, 34, a=a)
    for i in range(1, 8):
        cv.line([(100 + i * 110, 540), (100 + i * 110, 1280)], LINEC, 1, .25 * a)
    for j in range(1, 7):
        cv.line([(120, 520 + j * 111), (960, 520 + j * 111)], LINEC, 1, .25 * a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "PUPPY = DOG?", 100, INKC, -.2, "Black", .03)
    kinetic(cv, t, 450, "HOW DOES AI KNOW", 62, AMB, -.1, "Black", .02)
    p = eo(pr(t, .1, .8))
    card(cv, 120, 640, 960, 1260, 34, a=p)
    x = 330 + 80 * (1 - eo(pr(t, .3, 1.4))); x2 = 750 - 80 * (1 - eo(pr(t, .3, 1.4)))
    cv.text(x, 880, "puppy", 80, COP, eo(pr(t, .3, .8)), "Black")
    cv.text(x2, 1050, "dog", 80, AMB, eo(pr(t, .6, 1.1)), "Black")
    q = eio(pr(t, 1.4, 2.4))
    cv.line([(x + 60, 940), (x + 60 + (x2 - x - 120) * q, 1000)], INKC, 5, q)
    cv.text(540, 1180, "same meaning, different letters", 40, MUTE, eo(pr(t, 1.8, 2.4)), "Bold")
def s1(cv, t, D):
    head(cv, t, "WORD → NUMBERS", "every word becomes a list", AMB)
    card(cv, 100, 560, 980, 1250, 34)
    cv.text(540, 680, "dog", 130, INKC, eo(pr(t, .3, .9)), "Black")
    q = eo(pr(t, 1.2, 1.8))
    cv.text(540, 790, "↓", 70, AMB, q, "Black")
    nums = ["0.82", "-0.14", "0.57", "0.03", "-0.91", "0.40"]
    for i, n in enumerate(nums):
        pp = eback(pr(t, 1.8 + i * .25, 2.3 + i * .25), 2)
        x = 160 + i * 128
        cv.rrect(x, 850, x + 118, 950, 16, fill=mix(CARDC, AMB, .25), outline=AMB, w=2, a=cl(pp), oa=cl(pp))
        cv.text(x + 59, 900, n, 32, INKC, cl(pp * 1.4), "Black")
    cv.text(540, 1050, "… hundreds more", 40, MUTE, eo(pr(t, 3.6, 4.2)), "Bold")
    cv.text(540, 1160, "an EMBEDDING", 72, COP, eo(pr(t, 4.4, 5.0)), "Black")
def s2(cv, t, D):
    head(cv, t, "THE MAP", "each word gets an address", AMB)
    mapcard(cv, eo(pr(t, .1, .6)))
    pts = [("dog", 300, 760, AMB), ("pizza", 720, 1060, COP), ("king", 640, 640, SAGE), ("cloud", 240, 1150, ROSE)]
    for i, (w, x, y, c) in enumerate(pts):
        dot(cv, x, y, w, c, pr(t, .8 + i * .5, 1.3 + i * .5), True)
    q = eo(pr(t, 2.2, 2.8))
    cv.text(300, 815, "(0.3, 0.8)", 28, MUTE, q, "SemiBold")
def s3(cv, t, D):
    head(cv, t, "CLOSE = SIMILAR", "meaning becomes distance", AMB)
    mapcard(cv)
    for i, (w, (x, y)) in enumerate(ANI.items()):
        dot(cv, x, y, w, AMB, pr(t, .2 + i * .35, .7 + i * .35))
    for i, (w, (x, y)) in enumerate(FOOD.items()):
        dot(cv, x, y, w, COP, pr(t, 2.0 + i * .35, 2.5 + i * .35))
    q = eo(pr(t, 1.6, 2.2))
    cv.circ(340, 785, 150, outline=AMB, w=4, oa=q * .8)
    q2 = eo(pr(t, 3.4, 4.0))
    cv.circ(720, 1090, 130, outline=COP, w=4, oa=q2 * .8)
    cv.text(540, 1370, "animals here · food there", 42, INKC, eo(pr(t, 4.4, 5.0)), "Bold")
def s4(cv, t, D):
    head(cv, t, "NOBODY PLACED THEM", "the model learned each spot", AMB)
    card(cv, 100, 560, 980, 1250, 34)
    sents = [("the ", "puppy", " chased the ball"), ("the ", "dog", " chased the ball"), ("a ", "puppy", " slept on the couch"), ("a ", "dog", " slept on the couch")]
    for i, (a, b, c) in enumerate(sents):
        y = 660 + i * 110; p = eo(pr(t, .3 + i * .6, .9 + i * .6))
        full = a + b + c; w = cv.tw(full, 42, "Bold"); x0 = 540 - w / 2
        cv.text(x0 + cv.tw(a, 42, "Bold") + cv.tw(b, 42, "Bold") / 2, y, b, 42, AMB if b == "dog" else COP, p, "Black")
        cv.text(x0 + cv.tw(a, 42, "Bold") / 2, y, a, 42, INKC, p, "Bold")
        cv.text(x0 + cv.tw(a + b, 42, "Bold") + cv.tw(c, 42, "Bold") / 2, y, c, 42, INKC, p, "Bold")
    q = eo(pr(t, 3.0, 3.6))
    cv.text(540, 1140, "same neighbours", 60, INKC, q, "Black")
    cv.text(540, 1210, "→ same neighbourhood", 44, AMB, eo(pr(t, 3.5, 4.1)), "Bold")
def s5(cv, t, D):
    head(cv, t, "REAL MAPS", "thousands of dimensions", AMB)
    card(cv, 100, 560, 980, 1250, 34)
    n = int(2 + 1534 * eio(pr(t, 1.0, 4.0)) ** 2)
    cv.text(540, 700, "2 axes on screen", 40, MUTE, eo(pr(t, .2, .8)), "Bold")
    cv.text(540, 880, f"{n:,}", 170, COP, eo(pr(t, .8, 1.2)), "Black")
    cv.text(540, 1010, "axes in a real model", 48, INKC, eo(pr(t, 1.2, 1.8)), "Bold")
    rs = random.Random(3)
    for i in range(28):
        p = eo(pr(t, 1.0 + i * .08, 1.6 + i * .08))
        x = 150 + rs.random() * 780; y = 1090 + rs.random() * 120
        cv.line([(x, y), (x, y + 30 + rs.random() * 30)], mix(AMB, COP, rs.random()), 5, p)
    cv.text(540, 1330, "distance = meaning", 64, AMB, eo(pr(t, 4.4, 5.0)), "Black")
def s6(cv, t, D):
    head(cv, t, "DIRECTIONS TOO", "king − man + woman", AMB)
    mapcard(cv)
    K, M, Wm, Q = (360, 700), (360, 1060), (700, 1100), (700, 740)
    dot(cv, *M, "man", SAGE, pr(t, .3, .8), True); dot(cv, *K, "king", AMB, pr(t, .6, 1.1), True)
    q = eio(pr(t, 1.3, 2.3))
    cv.line([(M[0], M[1] - 28), (M[0], M[1] - 28 - (M[1] - K[1] - 56) * q)], COP, 6, q)
    cv.text(250, 880, "royal", 36, COP, q, "Black")
    dot(cv, *Wm, "woman", SAGE, pr(t, 2.4, 2.9), True)
    q = eio(pr(t, 3.0, 4.2))
    cv.line([(Wm[0], Wm[1] - 28), (Wm[0], Wm[1] - 28 - (Wm[1] - Q[1] - 56) * q)], COP, 6, q)
    dot(cv, *Q, "queen", AMB, pr(t, 4.2, 4.7), True)
    cv.circ(*Q, 46, outline=INKC, w=4, oa=eo(pr(t, 4.5, 5.0)))
    cv.text(540, 1370, "same arrow, new spot", 42, INKC, eo(pr(t, 4.6, 5.2)), "Bold")
def s7(cv, t, D):
    head(cv, t, "WHY IT MATTERS", "search by meaning", AMB)
    card(cv, 100, 560, 980, 1250, 34)
    cv.rrect(160, 620, 920, 710, 45, fill=(24, 40, 34), outline=LINEC, w=3)
    txt = "something to cheer up a sad dog"
    n = int(len(txt) * pr(t, .2, 1.4)); cv.text(200, 665, txt[:n], 36, INKC, 1, "SemiBold", anchor="lm")
    res = [("puppy toys that comfort anxious pets", AMB), ("how to help a lonely dog", AMB), ("calming treats for stressed dogs", AMB)]
    for i, (r, c) in enumerate(res):
        p = eo(pr(t, 1.5 + i * .4, 2.1 + i * .4))
        cv.rrect(160, 770 + i * 130, 920, 880 + i * 130, 20, fill=mix(CARDC, c, .22), outline=c, w=2, a=p, oa=p)
        cv.text(200, 825 + i * 130, r, 34, INKC, p, "Bold", anchor="lm")
    cv.text(540, 1190, "no shared keywords needed", 38, MUTE, eo(pr(t, 3.0, 3.6)), "Bold")
def s8(cv, t, D):
    kinetic(cv, t, 560, "MEANING", 130, AMB, 0, "Black", .05)
    cv.text(540, 700, "turned into", 60, INKC, eo(pr(t, .5, 1.0)), "Bold")
    kinetic(cv, t, 800, "GEOMETRY", 130, COP, .8, "Black", .05)
    rs = random.Random(5)
    pts = [(200 + rs.random() * 680, 1030 + rs.random() * 300) for _ in range(14)]
    for i, (x, y) in enumerate(pts):
        dot(cv, x, y, "", AMB if i % 2 else COP, pr(t, 1.6 + i * .1, 2.1 + i * .1), lab=False)
    cv.text(540, 1400, "the unseen layer under modern AI", 40, MUTE, eo(pr(t, 2.8, 3.4)), "Bold")
def s9(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, AMB, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
