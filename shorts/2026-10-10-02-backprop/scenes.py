# backprop: oxblood-charcoal, paper cards, amber/rust/sage
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (58, 34, 30), (36, 20, 20)
INKC = (246, 238, 220); WHT = (246, 238, 220)
PAPER, PAPER2, INK = (238, 226, 200), (224, 210, 180), (40, 32, 28)
YEL, RED, TEA = (230, 170, 50), (204, 92, 56), (70, 126, 112)
GRN, BRN, PLM = (112, 154, 96), (126, 84, 52), (120, 70, 110)
MUTE, SHAD, LINEC = (180, 168, 148), (12, 8, 8), (96, 84, 74)
GOLD = YEL; BL, BL2 = YEL, YEL
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (30, 18, 18), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-8, 9, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
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
LAY = [3, 4, 4, 2]
def npos(l, i):
    n = LAY[l]; return 200 + l * 227, 960 + (i - (n - 1) / 2) * 150
def net(cv, t, fw=0, bw=0, nudge=0, a=1, wts=True):
    # edges
    for l in range(3):
        for i in range(LAY[l]):
            for j in range(LAY[l + 1]):
                x0, y0 = npos(l, i); x1, y1 = npos(l + 1, j)
                cv.line([(x0, y0), (x1, y1)], mix(PAPER, INK, .55), 3, .55 * a)
                if fw > 0:
                    u = cl(fw * 3 - l); 
                    if 0 < u < 1: cv.circ(lerp(x0, x1, u), lerp(y0, y1, u), 9, fill=YEL, a=a)
                if bw > 0:
                    u = cl(bw * 3 - (2 - l))
                    w = ((i * 7 + j * 3 + l) % 5) / 4
                    if u > 0:
                        cv.line([(x1, y1), (lerp(x1, x0, u), lerp(y1, y0, u))], RED, 3 + 9 * w, .85 * a)
    for l in range(4):
        for i in range(LAY[l]):
            x, y = npos(l, i)
            lit = (fw > 0 and fw * 3 >= l - .2) 
            col = YEL if lit and bw <= 0 else PAPER
            if bw > 0 and bw * 3 >= (3 - l) - .2: col = mix(PAPER, RED, .6)
            cv.circ(x + 4, y + 8, 36, fill=SHAD, a=.5 * a)
            cv.circ(x, y, 36, fill=mix(col, INK, .35), a=a)
            cv.circ(x, y - 2, 32, fill=col, a=a)
            cv.circ(x - 10, y - 12, 9, fill=mix(col, WHT, .6), a=.6 * a)
def s0(cv, t, D):
    kinetic(cv, t, 300, "WHICH DIAL", 128, INKC, -.2, "Black", .03)
    kinetic(cv, t, 430, "TO BLAME?", 100, YEL, -.1, "Black", .03)
    card(cv, 100, 560, 980, 1380, 34)
    import random
    rr = random.Random(3)
    for k in range(40):
        x, y = 190 + (k % 8) * 100, 640 + (k // 8) * 120
        ang = rr.random() * 6.28 + math.sin(t * 1.5 + k) * .3
        cv.circ(x, y, 36, fill=mix(PAPER2, INK, .3), a=1)
        cv.circ(x, y - 2, 32, fill=PAPER2)
        cv.line([(x, y), (x + 26 * math.cos(ang), y + 26 * math.sin(ang))], INK, 6)
    cv.text(540, 1320, "1,000,000,000 dials", 40, RED, eo(pr(t, 1, 1.6)), "Black")
def s1(cv, t, D):
    head(cv, t, "ONE BY ONE?", "longer than the universe", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cv.text(540, 800, "10", 120, INK, eo(pr(t, .3, .8)), "Black")
    cv.text(540, 930, "tries per second...", 40, mix(INK, PAPER, .3), eo(pr(t, .8, 1.3)), "Bold")
    for k in range(18):
        q = eo(pr(t, 1.2 + k * .12, 1.6 + k * .12))
        cv.circ(190 + k * 40, 1060, 12, fill=mix(PAPER2, INK, .4), a=q)
    cv.text(540, 1200, "still not done", 70, RED, eo(pr(t, 3.4, 4.0)), "Black")
    cv.text(540, 1290, "a smarter way exists", 36, INK, eo(pr(t, 4.6, 5.2)), "Bold")
def s2(cv, t, D):
    head(cv, t, "FORWARD PASS", "input flows to a guess", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    net(cv, t, fw=pr(t, .5, 3.8))
    cv.text(190, 1290, "input", 34, INK, 1, "Bold"); cv.text(890, 1290, "guess", 34, INK, 1, "Bold")
def s3(cv, t, D):
    head(cv, t, "THE ERROR", "guess vs truth", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cv.rrect(160, 700, 500, 1000, 28, fill=PAPER2)
    cv.text(330, 770, "GUESS", 34, mix(INK, PAPER, .3), 1, "Bold")
    cv.text(330, 880, "CAT", 100, TEA, eo(pr(t, .3, .8)), "Black")
    cv.rrect(580, 700, 920, 1000, 28, fill=PAPER2)
    cv.text(750, 770, "TRUTH", 34, mix(INK, PAPER, .3), 1, "Bold")
    cv.text(750, 880, "DOG", 100, YEL, eo(pr(t, .9, 1.4)), "Black")
    q = eo(pr(t, 1.6, 2.2))
    cv.text(540, 1130, "≠", 160, RED, q, "Black")
    cv.text(540, 1270, "error = the gap", 48, INK, eo(pr(t, 2.2, 2.8)), "Black")
def s4(cv, t, D):
    head(cv, t, "BACKPROPAGATION", "error flows backward", RED)
    card(cv, 100, 560, 980, 1380, 34)
    net(cv, t, fw=1, bw=pr(t, .4, 4))
    cv.text(890, 1290, "error", 34, RED, 1, "Black"); cv.text(190, 1290, "dials", 34, INK, 1, "Bold")
    q = eo(pr(t, .2, .8))
    cv.text(540, 640, "<<<  <<<  <<<", 52, RED, q, "Black")
def s5(cv, t, D):
    head(cv, t, "THE CHAIN RULE", "blame, layer by layer", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    for k in range(4):
        x = 190 + k * 200; q = eo(pr(t, .3 + k * .5, .8 + k * .5))
        cv.rrect(x - 70, 760, x + 70, 900, 24, fill=PAPER2, a=q)
        cv.text(x, 830, "ƒ%d" % (4 - k), 64, INK, q, "Black")
        if k < 3: cv.text(x + 100, 830, "×", 56, RED, q, "Black")
    cv.text(540, 1020, "each layer asks:", 40, mix(INK, PAPER, .3), eo(pr(t, 2.3, 2.9)), "Bold")
    cv.text(540, 1120, "how much did I add", 56, INK, eo(pr(t, 2.6, 3.2)), "Black")
    cv.text(540, 1195, "to the mistake?", 56, RED, eo(pr(t, 3.0, 3.6)), "Black")
def s6(cv, t, D):
    head(cv, t, "WHO GETS BLAME", "by how much they mattered", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    vals = [.95, .12, .7, .05, .5, .02]
    for k, v in enumerate(vals):
        y = 700 + k * 105; q = eo(pr(t, .3 + k * .35, .9 + k * .35))
        cv.text(210, y, "dial %d" % (k + 1), 34, INK, q, "Bold")
        cv.rrect(310, y - 30, 900, y + 30, 20, fill=PAPER2, a=q)
        cv.rrect(310, y - 30, 310 + max(30, 590 * v * q), y + 30, 20, fill=mix(YEL, RED, v), a=q)
    cv.text(540, 1345, "big blame  .  almost none", 32, mix(INK, PAPER, .3), eo(pr(t, 3, 3.6)), "Bold")
def s7(cv, t, D):
    head(cv, t, "ONE SWEEP", "all billion dials scored", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    import random
    rr = random.Random(9)
    p = eo(pr(t, .6, 3.2))
    for k in range(40):
        x, y = 190 + (k % 8) * 100, 650 + (k // 8) * 100
        q = cl(p * 1.6 - (k % 8 + k // 8) * .06)
        base = rr.random() * 6.28
        ang = base + q * (rr.random() - .5) * 1.2
        c = mix(PAPER2, TEA, q * .7)
        cv.circ(x, y, 34, fill=mix(c, INK, .3)); cv.circ(x, y - 2, 30, fill=c)
        cv.line([(x, y), (x + 24 * math.cos(ang), y + 24 * math.sin(ang))], INK, 6)
    cv.text(540, 1260, "a tiny nudge each", 54, INK, eo(pr(t, 2.4, 3.0)), "Black")
    cv.text(540, 1330, "error shrinks", 40, TEA, eo(pr(t, 3.4, 4.0)), "Black")
def s8(cv, t, D):
    kinetic(cv, t, 560, "RANDOM NUMBERS", 84, INKC, 0, "Black", .03)
    kinetic(cv, t, 680, "LEARN TO SEE", 100, YEL, .4, "Black", .04)
    kinetic(cv, t, 920, "LATOON", 130, INKC, 3.2, "Black", .05)
    cv.text(540, 1060, "Voyaging the unseen", 48, YEL, eo(pr(t, 4.2, 4.8)), "SemiBold")
    chip(cv, 280, 1160, 520, "FOLLOW", YEL, eo(pr(t, 5.0, 5.6)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
