# Brain-IT: warm stone paper, ink, forest, terracotta, amber
import random
BG0, BG1 = (226, 224, 208), (210, 207, 188)
INKC = (30, 32, 34); WHT = (250, 246, 234)
FOR, TERRA, AMB, SLATE = (44, 84, 72), (190, 88, 58), (226, 166, 56), (88, 92, 110)
PAPER, EDGE, SHAD = (250, 246, 234), (140, 130, 108), (188, 182, 160)
GOLD = TERRA; BL, BL2 = TERRA, TERRA
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def _grain(im, amt=10, seed=1):
    rs = np.random.RandomState(seed); a = np.asarray(im.convert("RGB")).astype(np.int16)
    n = rs.randint(-amt, amt + 1, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
def pic(variant=0, S=420):
    k = 3; im = Image.new("RGB", (S * k, S * k)); d = ImageDraw.Draw(im)
    top, bot = (244, 196, 120), (250, 232, 196)
    for y in range(S * k):
        u = y / (S * k * .7); u = min(1, u)
        d.line([(0, y), (S * k, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * u) for i in range(3)))
    sx, sy = (300, 120) if variant == 0 else (290, 135)
    d.ellipse([(sx - 52) * k, (sy - 52) * k, (sx + 52) * k, (sy + 52) * k], fill=(222, 108, 66))
    h1 = [(0, 270), (90, 220), (200, 250), (300, 215), (S, 255), (S, S), (0, S)]
    h2 = [(0, 330), (140, 290), (260, 320), (S, 285), (S, S), (0, S)]
    if variant: h1 = [(0, 275), (110, 232), (210, 246), (310, 224), (S, 262), (S, S), (0, S)]
    d.polygon([(x * k, y * k) for x, y in h1], fill=(96, 128, 98))
    d.polygon([(x * k, y * k) for x, y in h2], fill=(52, 90, 74))
    hx, hy = 110, 238
    hc = (176, 76, 52) if variant == 0 else (190, 96, 66)
    d.rectangle([hx * k, (hy + 20) * k, (hx + 78) * k, (hy + 78) * k], fill=(246, 236, 214))
    d.polygon([((hx - 12) * k, (hy + 22) * k), ((hx + 39) * k, hy * k - 28 * k), ((hx + 90) * k, (hy + 22) * k)], fill=hc)
    d.rectangle([(hx + 30) * k, (hy + 44) * k, (hx + 50) * k, (hy + 78) * k], fill=(70, 52, 44))
    tx = 330 if variant == 0 else 322
    d.rectangle([tx * k, 292 * k, (tx + 10) * k, 330 * k], fill=(80, 58, 46))
    d.ellipse([(tx - 26) * k, 244 * k, (tx + 36) * k, 304 * k], fill=(36, 74, 60))
    im = im.resize((S, S), Image.LANCZOS)
    return _grain(im, 8, 3 + variant)
def pix(src, level, S=420):
    n = int(6 + (S - 6) * level ** 2.2)
    return src.resize((max(2, n), max(2, n)), Image.BILINEAR).resize((S, S), Image.NEAREST)
def tub(animal, S=420):
    k = 3; im = Image.new("RGB", (S * k, S * k)); d = ImageDraw.Draw(im)
    for y in range(S * k):
        u = y / (S * k); d.line([(0, y), (S * k, y)], fill=(int(214 + 20 * u), int(222 + 8 * u), int(214 - 10 * u)))
    d.rectangle([0, 300 * k, S * k, S * k], fill=(168, 176, 158))
    c = (196, 150, 98) if animal == "dog" else (214, 200, 172)
    cx = 210
    d.rectangle([(cx - 14) * k, 170 * k, (cx + 14) * k, 260 * k], fill=c)  # neck/body
    d.ellipse([(cx - 70) * k, 100 * k, (cx + 70) * k, 220 * k], fill=c)       # head
    if animal == "dog":
        d.ellipse([(cx - 100) * k, 110 * k, (cx - 50) * k, 215 * k], fill=(118, 80, 52))
        d.ellipse([(cx + 50) * k, 110 * k, (cx + 100) * k, 215 * k], fill=(118, 80, 52))
        d.ellipse([(cx - 34) * k, 160 * k, (cx + 34) * k, 214 * k], fill=(228, 196, 150))
        d.ellipse([(cx - 12) * k, 166 * k, (cx + 12) * k, 182 * k], fill=(36, 30, 30))
    else:
        d.polygon([((cx - 40) * k, 108 * k), ((cx - 66) * k, 40 * k), ((cx - 22) * k, 100 * k)], fill=(70, 60, 52))
        d.polygon([((cx + 40) * k, 108 * k), ((cx + 66) * k, 40 * k), ((cx + 22) * k, 100 * k)], fill=(70, 60, 52))
        d.ellipse([(cx - 112) * k, 130 * k, (cx - 60) * k, 160 * k], fill=(190, 176, 150))
        d.ellipse([(cx + 60) * k, 130 * k, (cx + 112) * k, 160 * k], fill=(190, 176, 150))
        d.polygon([((cx - 14) * k, 205 * k), ((cx + 14) * k, 205 * k), (cx * k, 262 * k)], fill=(236, 230, 214))
        d.ellipse([(cx - 20) * k, 176 * k, (cx + 20) * k, 206 * k], fill=(232, 222, 202))
    for ex in (-30, 30):
        d.ellipse([(cx + ex - 9) * k, 136 * k, (cx + ex + 9) * k, 154 * k], fill=(246, 240, 224))
        if animal == "dog": d.ellipse([(cx + ex - 5) * k, 140 * k, (cx + ex + 5) * k, 152 * k], fill=(30, 26, 26))
        else: d.rectangle([(cx + ex - 8) * k, 143 * k, (cx + ex + 8) * k, 149 * k], fill=(30, 26, 26))
    d.rounded_rectangle([60 * k, 250 * k, 360 * k, 350 * k], 46 * k, fill=(244, 242, 232), outline=(120, 120, 120), width=3 * k)
    d.rectangle([70 * k, 262 * k, 350 * k, 276 * k], fill=(120, 168, 190))
    for fx in (96, 324): d.ellipse([(fx - 16) * k, 344 * k, (fx + 16) * k, 372 * k], fill=(190, 150, 70))
    return _grain(im.resize((S, S), Image.LANCZOS), 8, 9)
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (226, 224, 208), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["mri"] = L("mri.jpg"); IM["wz"] = L("wz.jpg")
    IM["p0"] = pic(0); IM["p1"] = pic(1); IM["dog"] = tub("dog"); IM["goat"] = tub("goat")
    rs = np.random.RandomState(5)
    nz = rs.randint(60, 220, (420, 420, 1)).repeat(3, 2) * np.array([1.0, .95, .85]) 
    IM["noise"] = Image.fromarray(np.clip(nz, 0, 255).astype(np.uint8))
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
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, outline=EDGE, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.55 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or TERRA, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or PAPER, a, "Black")
def arrow(cv, x, y, a=1, c=INKC):
    cv.line([(x - 26, y), (x + 26, y)], c, 9, a); cv.line([(x + 6, y - 20), (x + 28, y), (x + 6, y + 20)], c, 9, a)
def pcard(cv, key, cx, cy, S, a=1, src=None, border=EDGE):
    h = S / 2
    cv.rrect(cx - h + 8, cy - h + 12, cx + h + 8, cy + h + 12, 22, fill=SHAD, a=.55 * a)
    s = src if src is not None else IM[key]
    s = s.resize((int(S), int(S)), Image.BILINEAR)
    img(cv, None, cx, cy, 1, a, _rounded(s, 22))
    cv.rrect(cx - h, cy - h, cx + h, cy + h, 22, outline=border, w=4, oa=a)
def vox_slice(cv, cx, cy, rx, ry, t, reveal=1.0, cell=30, a=1):
    cv.circ(cx, cy, 1, fill=INKC, a=0)
    cv.rrect(cx - rx - 14, cy - ry - 14, cx + rx + 14, cy + ry + 14, min(rx, ry) * .9, fill=PAPER, a=a, outline=INKC, w=5, oa=a)
    nx, ny = int(rx * 2 / cell), int(ry * 2 / cell)
    x0 = cx - nx * cell / 2; y0 = cy - ny * cell / 2; k = 0
    for j in range(ny):
        for i in range(nx):
            u = (i + .5) / nx * 2 - 1; v = (j + .5) / ny * 2 - 1
            if u * u + v * v > 1: continue
            k += 1
            v_ = .5 + .5 * math.sin(i * 1.1 + j * .6 + t * 2.0) * math.cos(j * .9 - i * .3 + t * 1.3)
            q = eback(pr(reveal, (i + j) / (nx + ny) * .8, (i + j) / (nx + ny) * .8 + .2), 2)
            col = mix((236, 226, 196), TERRA, v_) if v_ < .6 else mix(TERRA, AMB, (v_ - .6) / .4)
            s = cell * .86 * cl(q)
            cv.rrect(x0 + i * cell + (cell - s) / 2, y0 + j * cell + (cell - s) / 2, x0 + i * cell + (cell + s) / 2, y0 + j * cell + (cell + s) / 2, 5, fill=col, a=a)
def s0(cv, t, D):
    kinetic(cv, t, 330, "AN AI REDRAWS", 90, INKC, -.2, "Black", .02)
    kinetic(cv, t, 440, "WHAT YOU SEE", 90, TERRA, -.1, "Black", .02)
    p = eback(pr(t, .1, .7), 2)
    pcard(cv, "p0", 290, 880, 400, cl(p))
    cv.text(290, 1120, "WHAT THEY SAW", 36, INKC, cl(p), "Black")
    arrow(cv, 540, 880, cl(eo(pr(t, .7, 1.1))))
    lvl = eio(pr(t, 1.0, 3.2))
    q = eo(pr(t, .8, 1.2))
    pcard(cv, None, 790, 880, 400, cl(q), src=pix(IM["p1"], lvl) if lvl < 1 else IM["p1"])
    cv.text(790, 1120, "DRAWN FROM THE SCAN", 36, TERRA, cl(q), "Black")
    chip(cv, 300, 1230, 480, "BRAIN-IT · NEW STUDY", FOR, eo(pr(t, 2.2, 2.8)), size=34, h=76)
def s1(cv, t, D):
    head(cv, t, "MEET BRAIN-IT", "Michal Irani's lab · Weizmann Institute")
    p = eback(pr(t, .2, .8), 2)
    zoom = 1.0 + .12 * pr(t, 0, D)
    cv.rrect(80 + 8, 560 + 12, 1000 + 8, 1180 + 12, 30, fill=SHAD, a=.55 * cl(p))
    kenburns(cv, "wz", 540, 870, 920, 620, zoom, 30, cl(p), panx=0.1 * pr(t, 0, D))
    cv.rrect(80, 560, 1000, 1180, 30, outline=EDGE, w=4, oa=cl(p))
    cv.text(540, 1230, "Photo: Hoshvilim, CC BY-SA 4.0", 28, EDGE, eo(pr(t, 1.0, 1.5)), "SemiBold")
    chip(cv, 380, 1290, 320, "ICLR 2026", FOR, eo(pr(t, 1.5, 2.1)))
def s2(cv, t, D):
    head(cv, t, "INSIDE AN fMRI SCANNER", "thousands of photos, one brain")
    p = eback(pr(t, .2, .8), 2)
    cv.rrect(70 + 8, 520 + 12, 460 + 8, 1040 + 12, 26, fill=SHAD, a=.55 * cl(p))
    kenburns(cv, "mri", 265, 780, 390, 520, 1.0 + .1 * pr(t, 0, D), 26, cl(p), pany=-.3 + .4 * pr(t, 0, D))
    cv.rrect(70, 520, 460, 1040, 26, outline=EDGE, w=4, oa=cl(p))
    cv.text(265, 1075, "Photo: NIH/NINDS, public domain", 24, EDGE, cl(p), "SemiBold")
    q = eo(pr(t, 1.2, 1.8))
    if q > .02: vox_slice(cv, 760, 780, 190, 250, t, pr(t, 2.0, 4.6), 30, cl(q))
    cv.text(760, 1100, "VOXELS · 1.8 mm cubes", 32, INKC, eo(pr(t, 3.0, 3.6)), "Black")
    n = int(9000 * eo(pr(t, 3.8, 5.8)))
    cv.text(540, 1230, f"{n:,}+", 120, TERRA, eo(pr(t, 3.6, 4.0)), "Black")
    cv.text(540, 1330, "photos per person, over a year", 40, INKC, eo(pr(t, 4.2, 4.8)), "Bold")
def s3(cv, t, D):
    head(cv, t, "IT NEVER SEES A PICTURE", "only blood oxygen")
    card(cv, 90, 500, 990, 1300, 36)
    a_ = eo(pr(t, .3, .8))
    pcard(cv, "p0", 230, 650, 150, a_)
    cv.line([(150, 570), (310, 730)], TERRA, 12, a_); cv.line([(310, 570), (150, 730)], TERRA, 12, a_)
    cv.text(640, 620, "no picture reaches", 42, INKC, a_, "Black"); cv.text(640, 680, "the scanner's output", 42, INKC, a_, "Black")
    cv.text(540, 830, "BLOOD-OXYGEN SIGNAL", 34, SLATE, eo(pr(t, .8, 1.3)), "Black")
    base = 1110; amp = 250; x0, x1 = 160, 920
    cv.line([(x0, base), (x1, base)], EDGE, 5, eo(pr(t, .8, 1.3)))
    pts = []
    for i in range(61):
        u = i / 60
        y = math.exp(-((u - .32) / .13) ** 2) - .32 * math.exp(-((u - .66) / .17) ** 2)
        pts.append((x0 + u * (x1 - x0), base - y * amp))
    n = int(2 + 59 * eo(pr(t, 1.0, 3.6)))
    cv.line(pts[:n], TERRA, 11, 1)
    cv.circ(pts[n - 1][0], pts[n - 1][1], 15, fill=AMB, outline=INKC, w=4)
    cv.text(540, 1252, "oxygen use rises and falls", 32, INKC, eo(pr(t, 2.8, 3.4)), "Bold")
def s4(cv, t, D):
    head(cv, t, "THE AI MAKES TWO GUESSES", None)
    a_ = eback(pr(t, .2, .8), 2)
    card(cv, 60, 680, 300, 920, 28, a=cl(a_))
    vox_slice(cv, 180, 800, 78, 78, t, 1, 26, cl(a_) * .0 + cl(a_)) if False else None
    for j in range(5):
        for i in range(5):
            v_ = .5 + .5 * math.sin(i * 1.4 + j * .8 + t * 2)
            cv.rrect(98 + i * 26, 718 + j * 26, 98 + i * 26 + 22, 718 + j * 26 + 22, 4, fill=mix((236, 226, 196), TERRA, v_), a=cl(a_))
    cv.text(180, 960, "SCAN", 32, INKC, cl(a_), "Black")
    b1 = eio(pr(t, .9, 1.5)); b2 = eio(pr(t, 2.3, 2.9))
    cv.line([(300, 790), (360, 790), (360, 560)], INKC, 7, b1); cv.line([(360, 560), (360 + 30 * b1, 560)], INKC, 7, b1)
    cv.line([(300, 810), (360, 810), (360, 1010)], INKC, 7, b2); cv.line([(360, 1010), (360 + 30 * b2, 1010)], INKC, 7, b2)
    q = eback(pr(t, 1.3, 1.9), 2)
    card(cv, 400, 440, 1010, 700, 30, a=cl(q))
    cv.text(705, 500, "WHAT is in it?", 44, FOR, cl(q), "Black")
    for k, (w_, lab) in enumerate([(150, "house"), (130, "hills"), (110, "sun")]):
        chip(cv, 430 + [0, 170, 320][k], 560, w_ + 20, lab, FOR, eo(pr(t, 1.8 + k * .3, 2.3 + k * .3)) * cl(q), size=30, h=64)
    r = eback(pr(t, 2.8, 3.4), 2)
    card(cv, 400, 880, 1010, 1180, 30, a=cl(r))
    cv.text(705, 935, "WHERE, in what colors?", 44, TERRA, cl(r), "Black")
    pcard(cv, None, 560, 1060, 160, cl(r), src=pix(IM["p0"], 0.0))
    cv.text(820, 1040, "coarse layout", 34, INKC, cl(r), "Bold"); cv.text(820, 1090, "and outlines", 34, INKC, cl(r), "Bold")
    kinetic(cv, t, 1300, "TWO CLUES", 78, INKC, 4.2, "Black", .03)
def s5(cv, t, D):
    head(cv, t, "A DIFFUSION MODEL PAINTS IT", "noise removed, step by step")
    a_ = eback(pr(t, .2, .8), 2)
    chip(cv, 110, 500, 300, "WHAT", FOR, cl(a_)); chip(cv, 670, 500, 300, "WHERE", TERRA, cl(a_))
    lvl = eio(pr(t, 1.0, 4.4))
    src = Image.blend(IM["noise"], IM["p1"], lvl)
    src = pix(src, min(1, .15 + lvl * 1.0)) if lvl < .98 else src
    for xx in (260, 820):
        ps = (t * 1.6) % 1
        cv.line([(xx, 600 + 20 * ps), (xx + (540 - xx) * .25, 650 + 20 * ps)], INKC, 6, .5 * a_)
    pcard(cv, None, 540, 930, 520, cl(eo(pr(t, .4, 1.0))), src=src)
    cv.text(540, 1260, "static  →  a picture", 52, INKC, eo(pr(t, 2.4, 3.0)), "Black")
def s6(cv, t, D):
    head(cv, t, "ONE HOUR, NOT FORTY", "similar quality for a new person")
    card(cv, 70, 520, 1010, 1260, 36)
    cv.text(110, 600, "OLDER METHODS", 36, SLATE, 1, "Black", anchor="lm")
    cv.text(110, 650, "trained on 40 h per person", 32, INKC, 1, "Bold", anchor="lm")
    w1 = 860 * eio(pr(t, .5, 2.0))
    cv.rrect(110, 700, 110 + w1, 790, 16, fill=SLATE)
    cv.text(110, 890, "BRAIN-IT", 36, TERRA, eo(pr(t, 2.0, 2.4)), "Black", anchor="lm")
    cv.text(110, 940, "new person, ~1 h of scanning", 32, INKC, eo(pr(t, 2.0, 2.4)), "Bold", anchor="lm")
    w2 = max(14, 860 / 40 * eio(pr(t, 2.4, 3.2)))
    cv.rrect(110, 990, 110 + w2, 1080, 12, fill=TERRA, a=eo(pr(t, 2.2, 2.6)))
    cv.text(110 + w2 + 30, 1035, "1 h", 54, TERRA, eo(pr(t, 3.0, 3.5)), "Black", anchor="lm")
    cv.text(540, 1180, "reported as comparable results", 32, EDGE, eo(pr(t, 3.4, 3.9)), "SemiBold")
def s7(cv, t, D):
    head(cv, t, "IT STILL SLIPS", None)
    a_ = eback(pr(t, .2, .8), 2); b_ = eback(pr(t, 1.6, 2.2), 2)
    pcard(cv, "dog", 285, 760, 410, cl(a_)); cv.text(285, 1000, "SAW: dog in a bathtub", 32, INKC, cl(a_), "Black")
    arrow(cv, 540, 760, cl(eo(pr(t, 1.2, 1.6))))
    pcard(cv, "goat", 795, 760, 410, cl(b_)); cv.text(795, 1000, "DREW: a goat", 32, TERRA, cl(b_), "Black")
    c1 = eback(pr(t, 3.4, 4.0), 2); c2 = eback(pr(t, 4.4, 5.0), 2)
    chip(cv, 110, 1100, 860, "WORKS: pictures people saw", FOR, cl(c1), size=38, h=84)
    chip(cv, 110, 1220, 860, "NOT YET: dreams or thoughts", TERRA, cl(c2), size=38, h=84)
def s8(cv, t, D):
    kinetic(cv, t, 400, "WHO GETS TO", 84, INKC, .0, "Black", .03)
    kinetic(cv, t, 500, "READ A BRAIN?", 84, TERRA, .2, "Black", .03)
    cx, cy = 540, 960
    for k in range(3):
        u = (t * .35 + k / 3) % 1
        cv.circ(cx, cy, 150 + u * 260, outline=TERRA, w=4, oa=(1 - u) * .45)
    op = 1 - eio(pr(t, 1.0, 1.8))
    sh = 70 * op
    cv.arc(cx, cy - 120 - sh * .0, 100, -90 - 90, 90 + (0), INKC, 26, 1) if False else None
    cv.line([(cx - 100, cy - 80), (cx - 100, cy - 190 - sh * .6), (cx - 60, cy - 245 - sh * .6), (cx + 60, cy - 245 - sh * .6), (cx + 100, cy - 190 - sh * .6), (cx + 100, cy - 80 - sh * (1 if op > .5 else 0))], INKC, 28, 1)
    cv.rrect(cx - 170 + 8, cy - 90 + 12, cx + 170 + 8, cy + 170 + 12, 40, fill=SHAD, a=.6)
    cv.rrect(cx - 170, cy - 90, cx + 170, cy + 170, 40, fill=AMB, outline=INKC, w=6)
    cv.circ(cx, cy + 20, 32, fill=INKC); cv.rrect(cx - 12, cy + 30, cx + 12, cy + 110, 8, fill=INKC)
    cv.text(540, 1250, "mental privacy", 56, FOR, eo(pr(t, 1.8, 2.4)), "Black")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=TERRA, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=TERRA, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
