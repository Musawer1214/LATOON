# Diffie-Hellman explainer: charcoal-green, cream paper cards, ink, paint colours
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (30, 40, 37), (22, 30, 28)
INKC = (244, 236, 218); WHT = (244, 236, 218)
PAPER, PAPER2, INK = (236, 224, 198), (222, 208, 178), (38, 32, 28)
YEL, RED, TEA = (238, 180, 42), (196, 54, 44), (32, 130, 142)
ORG, GRN, BRN = (218, 112, 44), (96, 152, 84), (124, 84, 48)
MUTE, SHAD, LINEC = (176, 170, 150), (10, 14, 12), (88, 100, 90)
GOLD = YEL; BL, BL2 = YEL, YEL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def polaroid(photo, name, sub, w, rot):
    pw, ph = w, int(w * 1.1)
    fw, fh = pw + 40, ph + 40 + 120
    f = Image.new("RGBA", (fw, fh), PAPER + (255,))
    d = ImageDraw.Draw(f)
    ph_im = ImageOps.fit(photo.convert("RGB"), (pw, ph), Image.LANCZOS, centering=(.5, .3))
    f.paste(ph_im, (20, 20))
    d.rectangle((20, 20, 20 + pw, 20 + ph), outline=(120, 110, 90), width=2)
    d.text((fw // 2, 20 + ph + 42), name, font=F(40, "Black"), fill=INK, anchor="mm")
    d.text((fw // 2, 20 + ph + 88), sub, font=F(28, "SemiBold"), fill=(110, 98, 80), anchor="mm")
    sh = Image.new("RGBA", (fw + 80, fh + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle((40 + 10, 40 + 16, 40 + fw + 10, 40 + fh + 16), fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(12)); sh.alpha_composite(f, (40, 40))
    return sh.rotate(rot, expand=True, resample=Image.BICUBIC)
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (30, 40, 37), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-8, 9, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    IM["diffie"] = Image.open(os.path.join(IMGDIR, "diffie.png")).convert("RGB")
    IM["hellman"] = Image.open(os.path.join(IMGDIR, "hellman.png")).convert("RGB")
    IM["p_diffie"] = polaroid(IM["diffie"], "Whitfield Diffie", "co-inventor, 1976", 380, -4)
    IM["p_hellman"] = polaroid(IM["hellman"].resize((480, 560), Image.LANCZOS), "Martin Hellman", "co-inventor, 1976", 380, 3.5)
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
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, a=1):
    cv.rrect(x0 + 8, y0 + 14, x1 + 8, y1 + 14, r, fill=SHAD, a=.55 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a)
    cv.rrect(x0 + 10, y0 + 10, x1 - 10, y1 - 10, max(4, r - 8), outline=mix(fill, INK, .18), w=2, oa=.7 * a)
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 62, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or YEL, eo(pr(t, .3, .7)), "SemiBold")
def chip(cv, x, y, w, txt, col, a=1, tc=None, size=34, h=72):
    cv.rrect(x, y + 6, x + w, y + h + 6, h // 2, fill=SHAD, a=.6 * a)
    cv.rrect(x, y, x + w, y + h, h // 2, fill=col, a=a)
    cv.text(x + w / 2, y + h / 2, txt, size, tc or INK, a, "Black")
def ell(cv, cx, cy, rx, ry, col, a=1):
    if rx < 1 or ry < 1: return
    cv.poly([(cx + rx * math.cos(i * math.pi / 18), cy + ry * math.sin(i * math.pi / 18)) for i in range(36)], col, a)
def bucket(cv, cx, cy, s, col, a=1, level=1.0, col2=None):
    """paint bucket, centre (cx,cy), s=scale (1 -> 200 px wide). col2 blends the paint surface (mixing)."""
    top, bot = cy - 85 * s, cy + 85 * s
    ell(cv, cx + 10 * s, bot + 14 * s, 92 * s, 20 * s, SHAD, .5 * a)
    hp = [(cx - 100 * s + 4 * s + 200 * s * (i / 20) * 0 + (i / 20) * 192 * s, top - 90 * s * math.sin(i / 20 * math.pi)) for i in range(21)]
    cv.line([(x, y + 30 * s * 0) for x, y in hp], (96, 98, 94), max(3, 6 * s), a)
    mt, ml, md = (176, 178, 170), (208, 210, 202), (112, 114, 108)
    ell(cv, cx, bot, 75 * s, 20 * s, md, a)
    cv.poly([(cx - 100 * s, top), (cx + 100 * s, top), (cx + 75 * s, bot), (cx - 75 * s, bot)], mt, a)
    cv.poly([(cx - 100 * s, top), (cx - 52 * s, top), (cx - 40 * s, bot), (cx - 75 * s, bot)], ml, a * .8)
    cv.poly([(cx + 52 * s, top), (cx + 100 * s, top), (cx + 75 * s, bot), (cx + 40 * s, bot)], md, a * .75)
    for fy in (.22, .72):
        yy = lerp(top, bot, fy); wd = lerp(100, 75, fy) * s
        cv.line([(cx - wd, yy), (cx + wd, yy)], md, max(2, 5 * s), a * .8)
    ell(cv, cx, bot, 75 * s, 20 * s, md, a * .0)
    ell(cv, cx, top, 100 * s, 28 * s, (128, 130, 124), a)
    ell(cv, cx, top + 1 * s, 90 * s, 22 * s, mix(col, (0, 0, 0), .25), a)
    ell(cv, cx, top + 3 * s, 88 * s, 20 * s, col2 if col2 else col, a)
    ell(cv, cx - 24 * s, top - 2 * s, 38 * s, 6 * s, mix(col, WHT, .45), a * .55)
    if col2:
        ell(cv, cx, top + 3 * s, 88 * s, 20 * s, col, a * (1 - level))
def eye(cv, cx, cy, s, lx, ly, a=1):
    ell(cv, cx + 3, cy + 5, 40 * s, 22 * s, SHAD, .4 * a)
    ell(cv, cx, cy, 40 * s, 24 * s, (240, 232, 214), a)
    d = math.hypot(lx - cx, ly - cy) or 1; k = min(1, 14 * s / d)
    px, py = cx + (lx - cx) * k, cy + (ly - cy) * k
    cv.circ(px, py, 13 * s, fill=(40, 90, 96), a=a); cv.circ(px, py, 6.5 * s, fill=(12, 14, 12), a=a)
    cv.circ(px - 4 * s, py - 4 * s, 3 * s, fill=WHT, a=a * .9)
    cv.line([(cx - 40 * s, cy), (cx - 20 * s, cy - 20 * s), (cx + 20 * s, cy - 20 * s), (cx + 40 * s, cy)], (30, 24, 20), max(2, 4 * s), a * .8)
def phone(cv, cx, cy, s, a=1, glow_col=YEL):
    cv.rrect(cx - 80 * s + 8, cy - 150 * s + 14, cx + 80 * s + 8, cy + 150 * s + 14, 26 * s, fill=SHAD, a=.5 * a)
    cv.rrect(cx - 80 * s, cy - 150 * s, cx + 80 * s, cy + 150 * s, 26 * s, fill=(54, 56, 52), a=a, outline=(150, 152, 144), w=3, oa=a)
    cv.rrect(cx - 68 * s, cy - 136 * s, cx + 68 * s, cy + 136 * s, 16 * s, fill=PAPER, a=a)
    cv.rrect(cx - 22 * s, cy - 132 * s, cx + 22 * s, cy - 122 * s, 5 * s, fill=(54, 56, 52), a=a)
def lock(cv, cx, cy, s, col, a=1):
    cv.arc(cx, cy - 12 * s, 14 * s, -90, 90, col, max(3, 6 * s), a)
    cv.line([(cx - 14 * s, cy - 12 * s), (cx - 14 * s, cy - 2 * s)], col, max(3, 6 * s), a)
    cv.line([(cx + 14 * s, cy - 12 * s), (cx + 14 * s, cy - 2 * s)], col, max(3, 6 * s), a)
    cv.rrect(cx - 22 * s, cy - 4 * s, cx + 22 * s, cy + 26 * s, 5 * s, fill=col, a=a)
    cv.circ(cx, cy + 9 * s, 4 * s, fill=INK, a=a)
def drop(cv, x, y, s, col, a=1):
    cv.circ(x, y + s * .25, s * .5, fill=col, a=a)
    cv.poly([(x, y - s * .85), (x - s * .47, y + s * .08), (x + s * .47, y + s * .08)], col, a)
    ell(cv, x - s * .2, y + s * .18, s * .1, s * .2, WHT, a * .5)
