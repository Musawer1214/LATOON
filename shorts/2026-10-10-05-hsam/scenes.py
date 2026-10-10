# hsam: umber + cream paper, mustard / terracotta / muted teal
import random, math
from PIL import ImageOps, ImageFilter
BG0, BG1 = (40, 28, 23), (22, 14, 12)
INKC = (246, 238, 222); WHT = (246, 238, 222)
PAPER, PAPER2, INK = (240, 229, 205), (224, 210, 180), (40, 30, 26)
COP, RED, SAGE = (226, 166, 52), (196, 82, 56), (86, 142, 128)
YEL = COP; TEA = SAGE
MUTE, SHAD, LINEC = (170, 150, 130), (8, 4, 3), (110, 96, 82)
GOLD = COP; BL, BL2 = COP, COP
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}
_MASK = {}
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G, BG
    z = radial(40, (20, 30, 28), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
    rs = np.random.RandomState(5)
    a = np.asarray(BG.convert("RGB")).astype(np.int16)
    a = np.clip(a + rs.randint(-7, 8, a.shape[:2])[..., None], 0, 255).astype(np.uint8)
    BG = Image.fromarray(np.dstack([a, np.full(a.shape[:2], 255, np.uint8)]), "RGBA")
    for k, f in [("cal", "cal_s.jpg"), ("album", "album_s.jpg"), ("vinyl", "vinyl_s.jpg"), ("cm", "cm_s.jpg")]:
        IM[k] = Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    b = Image.open(os.path.join(IMGDIR, "brain.png")).convert("RGBA")
    bg = Image.new("RGBA", b.size, PAPER + (255,)); bg.alpha_composite(b)
    IM["brain"] = bg.convert("RGB")
def photo(cv, key, x0, y0, x1, y1, p, z0=1.0, z1=1.15, fx=.5, fy=.5, a=1.0, r=26):
    a = cl(a * cv.ga)
    if a <= .01: return
    cv.done()
    s = IM[key]; w, h = int(x1 - x0), int(y1 - y0)
    base = min(s.width / w, s.height / h); z = lerp(z0, z1, cl(p))
    cw, ch = w * base / z, h * base / z
    cx = lerp(cw / 2, s.width - cw / 2, fx); cy = lerp(ch / 2, s.height - ch / 2, fy)
    im = s.crop((int(cx - cw / 2), int(cy - ch / 2), int(cx + cw / 2), int(cy + ch / 2))).resize((w, h), Image.BILINEAR).convert("RGBA")
    k = (w, h, r)
    if k not in _MASK:
        m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255); _MASK[k] = m
    m = _MASK[k]
    if a < .99: m = m.point(lambda v: int(v * a))
    im.putalpha(m)
    X, Y = int(cv.X(x0)), int(cv.Y(y0))
    # soft shadow
    sh = Image.new("RGBA", (w, h), SHAD + (0,)); sh.putalpha(_MASK[k].point(lambda v: int(v * .5 * a)))
    cv.im.alpha_composite(sh, dest=(max(0, X + 8), max(0, Y + 14))) if X + 8 >= 0 and Y + 14 >= 0 else None
    sx0, sy0 = max(0, -X), max(0, -Y); x0_, y0_ = max(0, X), max(0, Y)
    sx1, sy1 = min(w, W - X), min(h, H - Y)
    if sx1 > sx0 and sy1 > sy0: cv.im.alpha_composite(im.crop((sx0, sy0, sx1, sy1)), dest=(x0_, y0_))
    cv.rrect(x0, y0, x1, y1, r, outline=PAPER, w=4, oa=.9 * a / max(cv.ga, .01) if cv.ga > .01 else 0)
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
def brackets(cv, x0, y0, x1, y1, col, a=1, L=46, w=5, pad=18):
    for (x, y, dx, dy) in [(x0 + pad, y0 + pad, 1, 1), (x1 - pad, y0 + pad, -1, 1), (x0 + pad, y1 - pad, 1, -1), (x1 - pad, y1 - pad, -1, -1)]:
        cv.line([(x + dx * L, y), (x, y), (x, y + dy * L)], col, w, a)
def cross(cv, x, y, s, col, a=1, w=7):
    cv.line([(x - s, y - s), (x + s, y + s)], col, w, a); cv.line([(x - s, y + s), (x + s, y - s)], col, w, a)
DIM = mix(INK, PAPER, .35)
def s0(cv, t, D):
    kinetic(cv, t, 300, "GIVE HIM", 100, INKC, -.2, "Black", .03)
    kinetic(cv, t, 420, "ANY DATE", 118, COP, -.1, "Black", .04)
    photo(cv, "cal", 120, 540, 960, 1150, t / D, 1.0, 1.45, .5, .8)
    brackets(cv, 120, 540, 960, 1150, PAPER, eo(pr(t, .4, .9)) * .9)
    q = eo(pr(t, 1.0, 1.5))
    chip(cv, 150, 1240, 780, "what did you do that day?", PAPER, q, INK, 36, 84)
    q2 = eback(pr(t, 2.7, 3.2), 2)
    chip(cv, 300, 1350, 480, "he knows.", RED, cl(q2 * 1.5), INKC, 44, 84)
def s1(cv, t, D):
    head(cv, t, "RANDOM-DATES QUIZ", "share of dates recalled correctly", COP)
    card(cv, 80, 540, 1000, 1400, 34)
    for k, (lab, val, col, y) in enumerate([("KCL, 16", 83, RED, 700), ("COMPARISON GROUP", 28.75, mix(INK, PAPER, .45), 1010)]):
        qa = eo(pr(t, .2 + k * .5, .7 + k * .5))
        cv.text(150, y - 70, lab, 34, INK, qa, "Black", "lm")
        cv.rrect(150, y - 40, 930, y + 100, 22, fill=PAPER2, a=qa)
        p = eio(pr(t, .8 + k * 1.0, 2.6 + k * 1.0))
        w = 780 * val / 100 * p
        if w > 30: cv.rrect(150, y - 40, 150 + w, y + 100, 22, fill=col)
        num = ("%d%%" % round(val * p)) if k == 0 else ("%d%%" % round(val * p))
        cv.text(150 + max(w, 140) - 26 if w > 190 else 150 + w + 24, y + 30, num, 72, INKC if w > 190 else INK, qa, "Black", "rm" if w > 190 else "lm")
    q = eo(pr(t, 4.4, 5.0))
    cv.text(540, 1290, "about three times the average", 38, RED, q, "Black")
def s2(cv, t, D):
    head(cv, t, "MEET KCL", "researchers in Poland", COP)
    photo(cv, "cm", 120, 520, 960, 1160, t / D, 1.0, 1.25, .45, .5)
    brackets(cv, 120, 520, 960, 1160, PAPER, eo(pr(t, .2, .7)) * .9)
    chip(cv, 270, 1240, 540, "KRAKÓW, POLAND", COP, eo(pr(t, .6, 1.1)), INK, 38, 84)
    cv.text(540, 1380, "memory tests: top 0.1%", 40, INKC, eo(pr(t, 1.3, 1.9)), "Black")
def s3(cv, t, D):
    head(cv, t, "WHEN NOBODY ASKS", "what does his mind do?", COP)
    card(cv, 80, 540, 1000, 1400, 34)
    photo(cv, "brain", 250, 760, 830, 1250, t / D, 1.0, 1.08, .5, .5, eo(pr(t, .2, .8)), 30)
    for k, (key, cx, cy, sz, t0) in enumerate([("album", 220, 690, 150, 1.2), ("vinyl", 540, 640, 130, 1.9), ("cal", 860, 700, 150, 2.6)]):
        q = eback(pr(t, t0, t0 + .5), 2)
        s = int(sz * cl(q, 0, 1.1))
        if s > 20:
            bob = math.sin(t * 2.4 + k * 2) * 8
            photo(cv, key, cx - s // 2, cy - s // 2 + bob, cx + s // 2, cy + s // 2 + bob, 0, 1, 1, .5, .5, cl(q * 1.4), s // 2)
    cv.text(540, 1330, "?", 70, RED, eo(pr(t, 3.0, 3.5)), "Black")
def s4(cv, t, D):
    head(cv, t, "RANDOM CHECK-INS", "\"what are you thinking?\"", COP)
    card(cv, 70, 540, 1010, 1400, 34)
    qb = eo(pr(t, .1, .6)) * (1 - .55 * eo(pr(t, 3.0, 3.4)))
    cv.rrect(290, 590, 790, 670, 40, fill=PAPER2, a=qb)
    cv.text(540, 630, "?  what are you thinking?", 32, INK, qb, "Bold")
    def row(label, y, n_hit, t0, t1, col, sub):
        qa = eo(pr(t, t0 - .4, t0 + .1))
        cv.text(110, y - 64, label, 36, INK, qa, "Black", "lm")
        for i in range(15):
            x = 111 + i * 58
            cv.rrect(x, y, x + 46, y + 46, 10, fill=PAPER2, a=qa)
            ti = t0 + (t1 - t0) * (i / 14)
            if i < n_hit:
                q = eback(pr(t, ti, ti + .25), 2.4)
                if q > .02:
                    m = 46 * cl(q, 0, 1.15) / 2
                    cv.rrect(x + 23 - m, y + 23 - m, x + 23 + m, y + 23 + m, 10, fill=col)
        q = eo(pr(t, t1 + .1, t1 + .6))
        cv.text(110, y + 106, sub, 40, col if col != PAPER2 else INK, q, "Black", "lm")
    row("KCL", 790, 13, 3.0, 5.4, RED, "13 of 15: a memory of his own life")
    row("COMPARISON GROUP", 1100, 6, 6.2, 7.8, mix(INK, PAPER, .5), "about 4 in 10")
    cv.text(540, 1360, "autobiographical memories, caught mid-thought", 26, DIM, 1, "SemiBold")
def arrow(cv, x0, y0, x1, y1, col, a=1, w=6):
    cv.line([(x0, y0), (x1, y1)], col, w, a)
    ang = math.atan2(y1 - y0, x1 - x0)
    for s in (-1, 1):
        cv.line([(x1, y1), (x1 - 22 * math.cos(ang + s * .5), y1 - 22 * math.sin(ang + s * .5))], col, w, a)
def s5(cv, t, D):
    head(cv, t, "SAME WANDERING", "different direction", COP)
    card(cv, 80, 540, 1000, 1400, 34)
    nowx = 640
    rs = random.Random(7)
    for k, (lab, y, col) in enumerate([("TYPICAL MIND", 800, mix(INK, PAPER, .45)), ("KCL", 1130, RED)]):
        qa = eo(pr(t, .1 + k * .3, .6 + k * .3))
        cv.text(120, y - 130, lab, 36, INK, qa, "Black", "lm")
        cv.line([(130, y), (950, y)], mix(INK, PAPER, .3), 5, qa)
        cv.line([(nowx, y - 22), (nowx, y + 22)], INK, 7, qa)
        cv.text(nowx, y + 52, "now", 28, DIM, qa, "Bold")
        cv.text(160, y + 52, "past", 28, DIM, qa, "Bold"); cv.text(900, y + 52, "future", 28, DIM, qa, "Bold")
        for i in range(6):
            t0 = 1.0 + k * .2 + i * .4
            side = (-1 if (i % 2 == 0 or k == 1) else 1)
            if k == 0: side = -1 if i in (0, 2, 5) else 1
            dist = 90 + rs.random() * 340 if side < 0 else 60 + rs.random() * 190
            x1 = nowx + side * dist
            q = eo(pr(t, t0, t0 + .4))
            if q > 0:
                arrow(cv, nowx, y - 38 - (i % 3) * 14, lerp(nowx, x1, q), y - 38 - (i % 3) * 14, col, q, 8)
                cv.circ(x1, y, 20 * q, fill=col)
    cv.text(540, 1340, "it just wanders backward", 44, RED, eo(pr(t, 3.2, 3.8)), "Black")
def s6(cv, t, D):
    head(cv, t, "THE FAINTEST CUE", None)
    labs = ["SONG", "SMELL", "PHOTO"]
    for k in range(3):
        x0 = 100 + k * 310
        q = eback(pr(t, .2 + k * .55, .8 + k * .55), 2)
        dy = (1 - eo(pr(t, .2 + k * .55, .8 + k * .55))) * 80
        a = cl(q * 1.4)
        if k == 1:
            card(cv, x0, 520 + dy, x0 + 270, 920 + dy, 26, PAPER, a)
            # cup with steam
            cx, cy = x0 + 135, 790 + dy
            cv.rrect(cx - 60, cy - 30, cx + 50, cy + 60, 18, fill=INK, a=a)
            cv.arc(cx + 56, cy + 12, 24, -90, 90, INK, 9, a)
            for j in range(3):
                pts = [(cx - 30 + j * 30 + math.sin(t * 3 + j + yy / 22.0) * 10, cy - 50 - yy) for yy in range(0, 110, 8)]
                cv.line(pts, COP, 7, a * .9)
        else:
            photo(cv, "vinyl" if k == 0 else "album", x0, 520 + dy, x0 + 270, 920 + dy, t / D, 1.0, 1.3, .5 if k else .75, .5, a, 26)
        cv.text(x0 + 135, 980 + dy, labs[k], 40, INKC, a, "Black")
    for k in range(3):
        q = eo(pr(t, 2.0 + k * .2, 2.6 + k * .2))
        x = 235 + k * 310
        cv.line([(x, 1030), (x + (540 - x) * .5 * q, 1030 + 110 * q)], COP, 6, q)
    q = eo(pr(t, 2.4, 3.0))
    cv.rrect(110, 1170, 970, 1330, 40, fill=RED, a=q)
    cv.text(540, 1250, "the past arrives uninvited", 46, INKC, q, "Black")
def s7(cv, t, D):
    head(cv, t, "A LOWER THRESHOLD", "not a bigger memory", COP)
    card(cv, 80, 540, 1000, 1400, 34)
    heights = [.35, .72, .28, .55, .9, .42, .6, .25, .78, .5, .33, .66]
    for k, (lab, y0, th) in enumerate([("TYPICAL", 580, .7), ("KCL", 990, .3)]):
        yb = y0 + 330
        qa = eo(pr(t, .1 + k * 2.0, .5 + k * 2.0))
        cv.text(120, y0 + 20, lab, 36, INK, qa, "Black", "lm")
        cv.line([(120, yb), (960, yb)], mix(INK, PAPER, .3), 4, qa)
        ty = yb - th * 270
        base = 1.0 + k * 2.0
        for i, hh in enumerate(heights):
            q = eo(pr(t, base + i * .1, base + i * .1 + .35))
            h = hh * 270 * q
            fire = hh > th
            col = RED if (fire and pr(t, base + 1.5, base + 1.6) > 0) else mix(INK, PAPER, .5)
            x = 135 + i * 58
            cv.rrect(x, yb - h, x + 40, yb, 8, fill=col)
        lp = eo(pr(t, base + .2, base + .9))
        x_end = lerp(120, 840, lp)
        for xx in range(120, int(x_end), 36):
            cv.line([(xx, ty), (min(xx + 20, x_end), ty)], COP, 6, qa)
        cv.text(852, ty, "threshold", 26, COP, lp, "Bold", "lm")
        n = sum(1 for hh in heights if hh > th)
        cv.text(960, y0 + 20, "%d memories fire" % n, 34, RED if k else DIM, eo(pr(t, base + 1.6, base + 2.0)), "Black", "rm")
def s8(cv, t, D):
    a = 1 - eio(pr(t, 3.9, 4.3))
    if a > .02:
        card(cv, 200, 520, 880, 1180, 40, PAPER, a)
        cv.text(540, 800, "1", 360, RED, a * eo(pr(t, .1, .6)), "Black")
        cv.text(540, 1020, "CASE STUDY", 62, INK, a * eo(pr(t, .6, 1.1)), "Black")
        cv.text(540, 1100, "needs more cases to confirm", 32, DIM, a * eo(pr(t, 1.6, 2.2)), "SemiBold")
        cv.text(540, 1270, "how common is it?", 52, COP, a * eo(pr(t, 2.4, 3.0)), "Black")
    kinetic(cv, t, 740, "LATOON", 150, INKC, 4.4, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, COP, eo(pr(t, 5.2, 5.8)), "SemiBold")
    chip(cv, 280, 990, 520, "FOLLOW", COP, eo(pr(t, 6.0, 6.6)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
