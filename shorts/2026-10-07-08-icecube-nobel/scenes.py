
# ---------- scenes: Nobel Physics 2026 / IceCube ghost particles (code-drawn + real photos)
BG0, BG1 = (2, 8, 18), (4, 26, 44)
ICE, ICE2 = (120, 230, 255), (200, 248, 255)
CHER = (40, 140, 255)
GOLD, GOLD2 = (236, 192, 98), (255, 226, 150)
BL, BL2 = (60, 170, 255), (120, 230, 255)
RED = (255, 90, 100)
DEEP = (10, 34, 58)
NOFADE_IN, NOFADE_OUT = {0}, set()
IMGDIR = os.path.join(HERE, "img")
IM = {}

def _rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im = im.convert("RGBA"); im.putalpha(m); return im
def _circle(im, d):
    im = im.resize((d, d), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (d * 4, d * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=255)
    im.putalpha(m.resize((d, d), Image.LANCZOS)); return im
def _cover(im, w, h):
    s = max(w / im.width, h / im.height); im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2; return im.crop((x, y, x + w, y + h))

def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S
    GLOW_O = radial(520, (60, 200, 255), 0.16); GLOW_B = radial(560, (30, 90, 255), 0.22); GLOW_S = radial(260, (120, 230, 255), 0.6)
    L = lambda f: Image.open(os.path.join(IMGDIR, f)).convert("RGB")
    IM["icl_src"] = _cover(L("icl_night.jpg"), 1160, 1270)          # Ken Burns source for hook
    hz = L("halzen.jpg")
    IM["halzen_c"] = _circle(hz.crop((140, 700, 480, 1040)), 360)
    IM["halzen_w"] = _rounded(_cover(hz.crop((60, 600, 1000, 1360)), 860, 700), 34)
    IM["dom"] = _circle(_cover(L("dom.jpg"), 900, 900), 300)
    IM["icl_day"] = _rounded(_cover(L("icl_2023.jpg"), 900, 520), 30)

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

def kenburns(cv, key, cx, cy, w, h, zoom, r, a=1, panx=0, pany=0):
    src = IM[key]; zw, zh = w / zoom * (src.width / w if src.width / w < src.height / h else src.height / h), 0
    k = min(src.width / w, src.height / h) / zoom
    cw, ch = w * k, h * k
    x0 = (src.width - cw) / 2 + panx * (src.width - cw) / 2; y0 = (src.height - ch) / 2 + pany * (src.height - ch) / 2
    crop = src.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((int(w), int(h)), Image.BILINEAR)
    img(cv, None, cx, cy, 1, a, _rounded(crop, r))

def shadow(cv, x0, y0, x1, y1, r, a=1):
    for k in range(4):
        cv.rrect(x0 - k * 6, y0 - k * 6 + 18, x1 + k * 6, y1 + k * 6 + 18, r + k * 6, fill=(0, 0, 0), a=a * .12)

def chip(cv, x, y, txt, size, fg, bg, a=1, outline=None, w="Bold"):
    tw = cv.tw(txt, size, w); pw, ph = tw / 2 + size * .8, size * .95
    cv.rrect(x - pw, y - ph, x + pw, y + ph, ph, fill=bg, a=a, outline=outline, w=3)
    cv.text(x, y, txt, size, fg, a, w)

def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    # letter-by-letter rise (kinetic typography)
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]

def streak(cv, x, y, ang, L, c=ICE, wdt=4, a=1):
    dx, dy = math.cos(ang), math.sin(ang)
    for k in range(5):
        f0, f1 = k / 5, (k + 1) / 5
        cv.line([(x - dx * L * f0, y - dy * L * f0), (x - dx * L * f1, y - dy * L * f1)], c, wdt * (1 - f0 * .6), a * (1 - f0) ** 1.3)
    cv.circ(x, y, wdt * .9, fill=ICE2, a=a)

def rain(cv, t, n, seed, box, ang, speed, L, a=1):
    x0, y0, x1, y1 = box; dx, dy = math.cos(ang), math.sin(ang); span = (x1 - x0) + (y1 - y0) + L
    for k in range(n):
        u = ((k * 0.6180339 + seed) % 1)
        ph = ((t * speed / span) + (k * 0.381966 + seed * 1.7)) % 1
        sx = x0 + u * (x1 - x0) * 1.6 - (x1 - x0) * .3 - dx * span * .5
        sy = y0 - dy * span * .5
        px, py = sx + dx * ph * span, sy + dy * ph * span
        if x0 - 40 < px < x1 + 40 and y0 - 40 < py < y1 + 40:
            streak(cv, px, py, ang, L, ICE, 3 + k % 3, a * (.5 + .5 * ((k * 7) % 5) / 4))

def iso(x, y, z, cx=540, cy=760, s=1.0):
    # isometric projection: x,y ground plane, z depth (down)
    return (cx + (x - y) * .87 * s, cy + (x + y) * .5 * s + z * s)

# S0 hook: real IceCube Lab at night + ghost rain
def s0(cv, t, D):
    a = 1
    z = 1.0 + .10 * eio(pr(t, 0, D))
    shadow(cv, 110, 470, 970, 1380, 40, 1)
    kenburns(cv, "icl_src", 540, 925, 860, 910, z, 40, 1, 0, -.2)
    cv.rrect(110, 470, 970, 1380, 40, fill=None, outline=ICE, w=3, oa=.35)
    rain(cv, t, 16, .13, (120, 480, 960, 1370), math.radians(68), 1500, 160, .9)
    q = eback(pr(t, -.2, .25), 2)
    chip(cv, 540, 290, "NOBEL PRIZE IN PHYSICS 2026", 34, (30, 20, 4), GOLD, cl(q))
    kinetic(cv, t, 385, "A TELESCOPE MADE OF ICE", 64, WHT, -.3, "Black", .03)
    pa = eo(pr(t, 1.6, 2.0))
    chip(cv, 540, 1300, "IceCube  ·  South Pole", 32, WHT, (8, 20, 36), pa, outline=ICE)

# S1 fingernail
def s1(cv, t, D):
    cv.text(540, 300, "EVERY SECOND", 56, ICE, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 365, "ghost particles: neutrinos", 34, MUT, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .1, .7)); fy = lerp(1500, 0, p)
    # finger (stylised)
    cv.rrect(330, 640 + fy, 750, 1430 + fy, 210, fill=(30, 52, 78), a=p, outline=ICE, w=4, oa=.5 * p)
    cv.rrect(400, 690 + fy, 680, 980 + fy, 120, fill=(70, 110, 150), a=p, outline=ICE2, w=3, oa=.6 * p)
    cv.text(540, 1040 + fy, "your fingernail", 30, ICE2, p, "SemiBold")
    rain(cv, t, 26, .41, (150, 450, 930, 1420), math.radians(80), 1900, 130, eo(pr(t, .5, .9)))
    # counter
    q = eback(pr(t, 1.6, 2.1), 2)
    if q > 0:
        cv.rrect(220, 1180, 860, 1330, 40, fill=(6, 18, 32), a=cl(q), outline=ICE, w=3)
        cv.text(540, 1235, "BILLIONS", 74 * cl(q) + 1, WHT, cl(q), "Black")
        cv.text(540, 1300, "pass through it every second", 28, MUT, cl(q), "Medium")
    fa = eo(pr(t, 3.0, 3.4))
    chip(cv, 540, 1405, "you feel: nothing", 30, WHT, (40, 20, 30), fa, outline=RED)

# S2 straight through planets and people
def s2(cv, t, D):
    cv.text(540, 300, "STRAIGHT THROUGH", 58, WHT, eo(pr(t, .05, .4)), "Black")
    p = eback(pr(t, .1, .6), 1.6); R = 270 * p; cx, cy = 470, 820
    if R > 2:
        glow(cv.im, GLOW_S, cx, cy, .35 * cl(p)); cv.done()
        cv.circ(cx, cy, R, fill=(16, 60, 110), a=cl(p))
        for k in range(-2, 3):
            ry = R * math.cos(k * .55); yy = cy + R * math.sin(k * .55)
            cv.line([(cx - ry, yy), (cx + ry, yy)], (60, 130, 200), 2, .6 * cl(p))
        for k in range(3):
            ph = (t * .4 + k / 3) % 1; rx = R * math.cos(ph * math.pi)
            cv.arc(cx, cy, R, 0, 360, (60, 130, 200), 2, 0)
            pts = [(cx + rx * math.sin(a2), cy - R * math.cos(a2)) for a2 in np.linspace(0, math.pi, 30)]
            cv.line(pts, (60, 130, 200), 2, .5 * cl(p))
        cv.circ(cx, cy, R, outline=ICE, w=3, a=cl(p) * .7)
        cv.text(cx, cy + R + 50, "EARTH", 30, MUT, cl(p), "Bold")
    # person
    pa = eo(pr(t, .6, 1.0))
    icon_person(cv, 870, 760, 190, (70, 110, 150), pa)
    cv.text(870, 900, "YOU", 30, MUT, pa, "Bold")
    # straight lines passing through everything
    for k in range(6):
        st = .8 + k * .35
        u = pr(t, st, st + 1.0)
        if u <= 0 or u >= 1: continue
        y0 = 560 + k * 75
        x = lerp(-80, 1160, eio(u) * .2 + u * .8)
        streak(cv, x, y0 + (x - 540) * .12, math.atan2(.12, 1), 220, ICE, 5, 1)
    q = eback(pr(t, 2.6, 3.0), 2)
    if q > 0:
        cv.rrect(250, 1220, 830, 1350, 36, fill=(6, 18, 32), a=cl(q), outline=LINE, w=3)
        cv.text(540, 1262, "atoms touched", 30, MUT, cl(q), "Medium")
        cv.text(540, 1312, "almost never", 46 * cl(q) + 1, ICE2, cl(q), "Black")

# S3 Halzen 1988 idea
def s3(cv, t, D):
    yr = int(lerp(1960, 1988, eo(pr(t, .05, 1.0))))
    cv.text(540, 330, str(yr), 120, GOLD, eo(pr(t, 0, .3)), "Black")
    q = eback(pr(t, .4, 1.0), 1.7)
    if q > 0:
        glow(cv.im, GLOW_S, 300, 720, .5 * cl(q)); cv.done()
        cv.circ(300, 720, 190 * q, fill=GOLD, a=cl(q))
        img(cv, "halzen_c", 300, 720, .98 * q, cl(q))
    na = eo(pr(t, .9, 1.3))
    cv.text(530, 650, "Francis", 52, WHT, na, "ExtraBold", anchor="lm")
    cv.text(530, 715, "Halzen", 52, WHT, na, "ExtraBold", anchor="lm")
    cv.text(530, 775, "Univ. of Wisconsin–Madison", 28, MUT, eo(pr(t, 1.1, 1.5)), "Medium", anchor="lm")
    # idea -> south pole ice
    ia = eo(pr(t, 1.9, 2.3))
    # bulb
    bx, by = 260, 1110
    cv.circ(bx, by, 70, fill=GOLD2, a=ia); cv.rrect(bx - 32, by + 58, bx + 32, by + 110, 10, fill=MUT, a=ia)
    for k in range(7):
        ang = math.radians(-90 + (k - 3) * 30); rr = 95 + 10 * math.sin(t * 6)
        cv.line([(bx + math.cos(ang) * rr, by + math.sin(ang) * rr), (bx + math.cos(ang) * (rr + 28), by + math.sin(ang) * (rr + 28))], GOLD, 6, ia)
    ap = eio(pr(t, 2.4, 3.1))
    if ap > 0:
        cv.line([(370, 1110), (lerp(370, 640, ap), 1110)], ICE, 7, 1)
        if ap > .95: cv.poly([(640, 1090), (676, 1110), (640, 1130)], ICE, 1)
    cq = eback(pr(t, 3.0, 3.5), 2)
    if cq > 0:
        # ice block (isometric)
        s = 90 * cq; cx, cy = 820, 1100
        top = [(cx, cy - s), (cx + s * 1.1, cy - s * .45), (cx, cy + s * .1), (cx - s * 1.1, cy - s * .45)]
        cv.poly(top, ICE2, cl(cq))
        cv.poly([(cx - s * 1.1, cy - s * .45), (cx, cy + s * .1), (cx, cy + s * 1.1), (cx - s * 1.1, cy + s * .55)], (90, 190, 230), cl(cq))
        cv.poly([(cx + s * 1.1, cy - s * .45), (cx, cy + s * .1), (cx, cy + s * 1.1), (cx + s * 1.1, cy + s * .55)], (50, 140, 200), cl(cq))
        cv.text(cx, 1270, "South Pole ice", 32, ICE2, cl(cq), "Bold")
    cv.text(260, 1270, "catch them", 32, GOLD2, ia, "Bold")

# S4 IceCube in numbers: strings, sensors, depth
def s4(cv, t, D):
    cv.text(540, 300, "ICECUBE", 64, ICE, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 365, "1 cubic kilometre of ice", 34, MUT, eo(pr(t, .3, .7)), "SemiBold")
    rot = .25 * math.sin(t * .35)
    S = 330; N = 6
    def P(x, y, z):
        xr = x * math.cos(rot) - y * math.sin(rot); yr = x * math.sin(rot) + y * math.cos(rot)
        return iso(xr, yr, z, 560, 570, 1.0)
    ca = eo(pr(t, .2, .7))
    # surface square
    corners = [(-S / 2, -S / 2), (S / 2, -S / 2), (S / 2, S / 2), (-S / 2, S / 2)]
    depth = 500 * eio(pr(t, .6, 2.6))
    for zz, al in [(0, .8), (depth, .5)]:
        pts = [P(x, y, zz) for x, y in corners] + [P(*corners[0], zz)]
        cv.line(pts, ICE, 3, ca * al)
    for x, y in corners:
        cv.line([P(x, y, 0), P(x, y, depth)], ICE, 2, ca * .4)
    # strings with DOMs
    for i in range(N):
        for j in range(N):
            x = -S / 2 + S * (i + .5) / N; y = -S / 2 + S * (j + .5) / N
            st = .7 + (i + j) * .08
            sp = eio(pr(t, st, st + 1.4))
            if sp <= 0: continue
            top = P(x, y, 0); bot = P(x, y, 500 * sp)
            cv.line([top, bot], (70, 120, 170), 2, .8)
            for k in range(8):
                zk = 160 + k * 48
                if zk < 500 * sp:
                    px, py = P(x, y, zk)
                    lit = .5 + .5 * math.sin(t * 3 + i * 1.3 + j * .7 + k)
                    cv.circ(px, py, 5, fill=mix((60, 110, 170), ICE2, lit * pr(t, 3, 4)), a=1)
    # depth gauge
    ga = eo(pr(t, 1.0, 1.4))
    gx = 95; g0, g1 = 620, 1150
    cv.line([(gx, g0), (gx, g1)], LINE, 6, ga)
    dd = 2450 * eio(pr(t, 1.2, 3.4))
    cv.line([(gx, g0), (gx, g0 + (g1 - g0) * dd / 2450)], ICE, 6, ga)
    cv.text(gx + 22, g0 + (g1 - g0) * dd / 2450, f"{int(dd):,} m", 30, WHT, ga, "Bold", anchor="lm")
    if dd > 1450:
        yy = g0 + (g1 - g0) * 1450 / 2450
        cv.line([(gx - 14, yy), (gx + 14, yy)], GOLD, 4, ga); cv.text(gx + 22, yy, "1,450 m", 24, GOLD2, ga * pr(t, 2.6, 3.0), "SemiBold", anchor="lm")
    # sensor counter
    n = int(5160 * eo(pr(t, 1.2, 3.6)))
    ka = eo(pr(t, 1.0, 1.4))
    cv.rrect(120, 1250, 620, 1410, 36, fill=(6, 18, 32), a=ka, outline=ICE, w=3)
    cv.text(370, 1308, f"{n:,}", 76, WHT, ka, "Black")
    cv.text(370, 1375, "light sensors", 28, MUT, ka, "Medium")
    dq = eback(pr(t, 4.2, 4.8), 1.8)
    if dq > 0:
        glow(cv.im, GLOW_S, 820, 1300, .4 * cl(dq)); cv.done()
        cv.circ(820, 1300, 136 * dq, fill=ICE, a=cl(dq))
        img(cv, "dom", 820, 1300, .86 * dq, cl(dq))
        cv.text(800, 1505 - 30, "", 10, WHT, 0)
    chip(cv, 820, 1130, "one real sensor", 26, (4, 20, 34), ICE2, eo(pr(t, 4.7, 5.1)))
    chip(cv, 370, 1170, "86 strings", 26, WHT, (8, 30, 52), eo(pr(t, 3.6, 4.0)), outline=ICE)

# S5 the blue flash
def s5(cv, t, D):
    cv.text(540, 300, "A FAINT BLUE FLASH", 56, WHT, eo(pr(t, .05, .4)), "Black")
    a = eo(pr(t, .1, .5))
    cv.rrect(80, 420, 1000, 1420, 40, fill=(4, 16, 30), a=a, outline=LINE, w=3)
    xs = [190, 330, 470, 610, 750, 890]
    hit = (430, 760); ang = math.radians(58)
    dirx, diry = math.cos(ang), math.sin(ang)
    for x in xs:
        cv.line([(x, 440), (x, 1400)], (50, 90, 130), 2, a)
    th = 1.0
    # incoming ghost track
    u = pr(t, .4, th)
    if u > 0:
        sx, sy = hit[0] - dirx * 420, hit[1] - diry * 420
        px, py = lerp(sx, hit[0], u), lerp(sy, hit[1], u)
        cv.line([(sx, sy), (px, py)], ICE, 3, .35)
        cv.circ(px, py, 7, fill=ICE2, a=1)
    # flash + cone
    fq = pr(t, th, th + 1.6)
    if fq > 0:
        glow(cv.im, GLOW_S, hit[0], hit[1], (1 - fq) * .9 + .15); cv.done()
        L = 650 * eo(fq)
        ex, ey = hit[0] + dirx * L, hit[1] + diry * L
        spread = math.radians(41)
        for sgn in (-1, 1):
            a2 = ang + sgn * spread
            cv.line([hit, (hit[0] + math.cos(a2) * L * .8, hit[1] + math.sin(a2) * L * .8)], CHER, 3, .6)
        cv.line([hit, (ex, ey)], ICE2, 6, 1)
    for x in xs:
        for k in range(16):
            y = 470 + k * 58
            # distance to track for lighting
            vx, vy = x - hit[0], y - hit[1]
            along = vx * dirx + vy * diry
            perp = abs(-vx * diry + vy * dirx)
            tl = th + .15 + (max(along, 0) + perp * .6) / 600
            lit = pr(t, tl, tl + .15) * (1 if along > -40 else 0) * cl(1 - perp / 260)
            c = mix((60, 100, 140), (90, 200, 255), lit)
            cv.circ(x, y, 7 + 9 * lit, fill=c, a=a)
    # reconstructed direction
    rq = eio(pr(t, 3.1, 3.9))
    if rq > 0:
        bx, by = hit[0] + dirx * 600, hit[1] + diry * 600
        tx, ty = lerp(bx, hit[0] - dirx * 330, rq), lerp(by, hit[1] - diry * 330, rq)
        cv.line([(bx, by), (tx, ty)], GOLD, 6, 1)
        if rq > .9:
            hx, hy = hit[0] - dirx * 330, hit[1] - diry * 330
            cv.poly([(hx - dirx * 30, hy - diry * 30), (hx + diry * 18, hy - dirx * 18), (hx - diry * 18, hy + dirx * 18)], GOLD, 1)
        chip(cv, 540, 1360, "path traced back", 30, (30, 20, 4), GOLD, eo(pr(t, 3.6, 4.0)))

# S6 no charge -> straight back to source
def s6(cv, t, D):
    cv.text(540, 300, "NO CHARGE. NO DETOUR.", 54, WHT, eo(pr(t, .05, .4)), "Black")
    a = eo(pr(t, .1, .5))
    src = (170, 560); earth = (880, 1180)
    # source: cosmic accelerator
    glow(cv.im, GLOW_S, src[0], src[1], .55 * a); cv.done()
    for k in range(6):
        ang = t * 1.5 + k * math.pi / 3
        cv.arc(src[0], src[1], 34 + 6 * k, math.degrees(ang), math.degrees(ang) + 90, ICE2, 3, a * (1 - k / 7))
    cv.circ(src[0], src[1], 18, fill=WHT, a=a)
    cv.text(src[0] + 10, src[1] - 110, "cosmic source", 28, MUT, a, "SemiBold")
    cv.circ(earth[0], earth[1], 60, fill=(20, 80, 150), a=a, outline=ICE, w=3)
    cv.text(earth[0], earth[1] + 100, "EARTH", 28, MUT, a, "Bold")
    # magnetic field lines (wavy)
    fa = eo(pr(t, .4, .9))
    for k in range(5):
        pts = [(x, 700 + k * 110 + 22 * math.sin(x / 80 + t * 1.2 + k)) for x in range(110, 1000, 20)]
        cv.line(pts, (90, 70, 160), 3, fa * .55)
    if fa > 0: cv.text(540, 1300, "magnetic fields", 26, (150, 130, 220), fa, "SemiBold")
    # charged particle: curved, misses
    cp = eio(pr(t, .9, 2.6))
    if cp > 0:
        pts = []
        for i in range(int(40 * cp) + 1):
            u = i / 40
            x = 170 + 220 * math.sin(math.pi * u)
            y = lerp(src[1], 1350, u)
            pts.append((x, y))
        cv.line(pts, RED, 6, 1)
        if cp >= 1: chip(cv, 230, 1150, "charged: bent", 28, WHT, (60, 18, 26), eo(pr(t, 2.6, 3.0)), outline=RED)
    # neutrino: straight
    npg = eio(pr(t, 2.6, 3.8))
    if npg > 0:
        x, y = lerp(src[0], earth[0], npg), lerp(src[1], earth[1], npg)
        cv.line([src, (x, y)], ICE2, 7, 1)
        cv.circ(x, y, 9, fill=WHT, a=1)
    if npg >= 1:
        chip(cv, 620, 760, "neutrino: straight", 28, (4, 20, 34), ICE2, eo(pr(t, 3.8, 4.2)))
    bq = eio(pr(t, 4.6, 5.4))
    if bq > 0:
        x, y = lerp(earth[0], src[0], bq), lerp(earth[1], src[1], bq)
        for k in range(12):
            u = k / 12
            if u < bq:
                cv.circ(lerp(earth[0], src[0], u), lerp(earth[1], src[1], u), 6, fill=GOLD, a=1)
        cv.text(540, 1400, "points to its source", 34, GOLD2, eo(pr(t, 4.8, 5.2)), "Bold")

# S7 beyond the solar system: zoom out
def s7(cv, t, D):
    z = eio(pr(t, .1, 2.6))
    sc = lerp(1.0, .12, z)
    cx, cy = 540, 840
    # solar system shrinking
    for k, r in enumerate([70, 120, 175, 240]):
        cv.circ(cx, cy, r * sc, outline=(70, 110, 160), w=2, a=1 - z * .6)
        ang = t * (1.2 - k * .2) + k
        cv.circ(cx + math.cos(ang) * r * sc, cy + math.sin(ang) * r * sc, max(2, 10 * sc), fill=ICE2, a=1)
    cv.circ(cx, cy, max(3, 28 * sc), fill=GOLD, a=1)
    ss = eo(pr(t, 0, .4)) * (1 - pr(t, 1.6, 2.0))
    cv.text(cx, cy + 300, "our solar system", 30, MUT, ss, "SemiBold")
    # galaxy particle field fades in around
    ga = eo(pr(t, 1.2, 2.4))
    if ga > 0:
        for k in range(220):
            arm = k % 2; r = 30 + (k * 37 % 360)
            th = r / 60 + arm * math.pi + t * .08
            x = cx + math.cos(th) * r * 1.1; y = cy + math.sin(th) * r * .55
            cv.circ(x, y, 2 + k % 3, fill=mix(ICE, WHT, (k % 5) / 4), a=ga * .5)
    # far source & incoming neutrinos
    fa = eo(pr(t, 1.8, 2.3))
    fx, fy = 860, 470
    glow(cv.im, GLOW_S, fx, fy, .6 * fa); cv.done()
    cv.circ(fx, fy, 16, fill=WHT, a=fa)
    cv.line([(fx - 60, fy + 60), (fx + 60, fy - 60)], ICE2, 4, fa)
    for k in range(4):
        u = ((t - 2.2) * .6 + k * .25) % 1
        if t > 2.2:
            streak(cv, lerp(fx, cx, u), lerp(fy, cy, u), math.atan2(cy - fy, cx - fx), 90, ICE, 4, fa)
    q = eback(pr(t, 2.4, 2.9), 2)
    if q > 0:
        cv.rrect(140, 1230, 940, 1400, 40, fill=(6, 18, 32), a=cl(q), outline=ICE, w=3)
        cv.text(540, 1290, "HIGH-ENERGY NEUTRINOS", 48 * cl(q) + 1, WHT, cl(q), "Black")
        cv.text(540, 1355, "from far beyond our solar system", 30, ICE2, cl(q), "SemiBold")
    cv.text(540, 320, "FROM DEEP SPACE", 56, ICE, eo(pr(t, .05, .4)), "Black")

# S8 quote with real photo
def s8(cv, t, D):
    p = eo(pr(t, .05, .6))
    shadow(cv, 110, 430, 970, 1130, 34, p)
    img(cv, "halzen_w", 540, 780 + (1 - p) * 80, 1.0 + .03 * pr(t, 0, D), p)
    cv.text(540, 300, "HIS OWN WORDS", 52, GOLD, eo(pr(t, .05, .4)), "Black")
    chip(cv, 540, 1080, "with a replica of Galileo's telescope", 24, WHT, (6, 18, 32), eo(pr(t, .6, 1.0)), outline=LINE)
    words = "“Very few thought it would work, including myself.”".split()
    shown = int(len(words) * pr(t, .7, 2.4) + .999)
    lines = [" ".join(words[:4]), " ".join(words[4:])]
    cnt = 0
    for li, ln in enumerate(lines):
        ws = ln.split(); k = max(0, min(len(ws), shown - cnt)); cnt += len(ws)
        cv.text(540, 1200 + li * 70, " ".join(ws[:k]), 50, WHT, 1, "ExtraBold")
    cv.text(540, 1360, "— Francis Halzen", 30, MUT, eo(pr(t, 2.4, 2.8)), "SemiBold")

# S9 end card
def s9(cv, t, D):
    q = eback(pr(t, 0, .6), 1.6)
    s = 120 * q; cx, cy = 540, 600
    if s > 2:
        glow(cv.im, GLOW_S, cx, cy, .4 * cl(q)); cv.done()
        top = [(cx, cy - s), (cx + s * 1.1, cy - s * .45), (cx, cy + s * .1), (cx - s * 1.1, cy - s * .45)]
        cv.poly(top, ICE2, cl(q))
        cv.poly([(cx - s * 1.1, cy - s * .45), (cx, cy + s * .1), (cx, cy + s * 1.1), (cx - s * 1.1, cy + s * .55)], (90, 190, 230), cl(q))
        cv.poly([(cx + s * 1.1, cy - s * .45), (cx, cy + s * .1), (cx, cy + s * 1.1), (cx + s * 1.1, cy + s * .55)], (50, 140, 200), cl(q))
        rain(cv, t, 8, .7, (300, 380, 780, 800), math.radians(70), 900, 110, .8)
    cv.text(540, 830, "A NEW KIND OF ASTRONOMY", 54, WHT, eo(pr(t, .3, .7)), "Black")
    cv.text(540, 900, "Nobel Prize in Physics 2026", 34, GOLD, eo(pr(t, .5, .9)), "SemiBold")
    p = eback(pr(t, .9, 1.4), 1.6)
    if p > 0:
        y = 1130 + (1 - p) * 120
        cv.rrect(160, y - 85, 920, y + 85, 85, fill=CARD, a=cl(p), outline=LINE, w=3)
        play_btn(cv, 265, y, 80, cl(p))
        cv.text(345, y - 22, "LATOON", 52, WHT, cl(p), "ExtraBold", anchor="lm")
        cv.text(345, y + 30, "Voyaging the Unseen", 30, MUT, cl(p), "Medium", anchor="lm")
        pulse = 1 + .06 * math.sin(max(0, t - 1.6) * 7) * pr(t, 1.6, 1.9)
        bw, bh = 120 * pulse, 42 * pulse
        cv.rrect(790 - bw, y - bh, 790 + bw, y + bh, bh, fill=(255, 0, 51), a=cl(p))
        cv.text(790, y, "Subscribe", 34, WHT, cl(p), "Bold")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
