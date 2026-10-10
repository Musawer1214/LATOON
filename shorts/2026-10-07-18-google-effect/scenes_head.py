# ---------- scenes: Google effect / cognitive offloading (code-drawn + real images)
BG0, BG1 = (9, 6, 24), (30, 14, 54)
ORG, ORG2 = (255, 112, 96), (255, 170, 150)
AMB, CREAM = (255, 205, 90), (240, 238, 255)
PUR = (150, 130, 255)
DIM = (58, 44, 96)
RED = (255, 80, 80)
GOLD = (255, 205, 90)
BL, BL2 = (255, 112, 96), (255, 205, 90)
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}

def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im

def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S
    GLOW_O = radial(520, (255, 100, 90), 0.14); GLOW_B = radial(560, (110, 90, 255), 0.22); GLOW_S = radial(260, (255, 190, 160), 0.6)
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    for k, f in [("goog", "google_s.jpg"), ("ucl", "ucl_s.jpg"), ("phone", "phone_s.jpg"), ("fmri", "fmri_s.jpg"), ("mri", "mri_s.jpg")]:
        IM[k] = L(f)

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
    if w < 4 or h < 4: return
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
INK = (12, 6, 30)
CARDC = (28, 18, 56)
ICE = (120, 225, 255)

def brain(cv, cx, cy, s, col, a=1, t=0, fillc=None):
    for dx in (-1, 1):
        for (ox, oy, r) in [(.0, -.28, .3), (.2, -.02, .34), (.0, .28, .3)]:
            cv.circ(cx + dx * (ox + .08) * s, cy + oy * s, r * s, fill=fillc or mix(CARDC, col, .18), a=a, outline=col, w=max(3, s * .03), oa=a)
    cv.line([(cx, cy - .55 * s), (cx, cy + .55 * s)], col, max(3, s * .025), a * .8)
    for k in range(3):
        u = (t * .8 + k / 3) % 1
        cv.circ(cx + (-.35 + u * .7) * s, cy + (-.2 + .4 * math.sin(u * 6.28 + k)) * s * .5, s * .035, fill=CREAM, a=a * math.sin(u * math.pi))

def cardimg(cv, key, cx, cy, w, h, fx, fy, zoom, a=1, r=36, edge=ICE):
    shadow(cv, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, r, a)
    zoomcard(cv, key, cx, cy, w, h, fx, fy, zoom, r, a)
    cv.rrect(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, r, outline=edge, w=3, oa=.55 * a)

def credit(cv, y, txt, a=1):
    cv.text(540, y, txt, 22, MUT, .85 * a, "Medium")

def dotted(cv, p0, p1, t, n=14, col=ORG2, a=1, r=5, speed=.8):
    for i in range(n):
        u = (i / n + t * speed) % 1
        cv.circ(lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), r * (.5 + .5 * math.sin(u * math.pi)), fill=col, a=a * math.sin(u * math.pi))
