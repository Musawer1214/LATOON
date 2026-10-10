from common import *
from scenes_b import HEX
from scenes_a import _streams

def medal(cv, x, y, r, a=1, t=0):
    shadow_circ(cv, x, y, r, a, (12, 18))
    cv.circ(x, y, r, fill=(196, 146, 60), a=a)
    cv.circ(x, y, r * .9, fill=(214, 170, 84), a=a)
    cv.circ(x - r * .05, y - r * .05, r * .82, fill=(226, 186, 104), a=a)
    # ribbon
    cv.poly([(x - r * .55, y - r * 2.1), (x - r * .1, y - r * 2.1), (x + r * .12, y - r * .92), (x - r * .3, y - r * .92)], TERRA, a, INK, 2.5)
    cv.poly([(x + r * .55, y - r * 2.1), (x + r * .1, y - r * 2.1), (x - r * .12, y - r * .92), (x + r * .3, y - r * .92)], (160, 70, 44), a, INK, 2.5)
    cv.circ(x, y, r * .62, outline=(190, 140, 58), w=4, a=a)
    for side in (-1, 1):
        for k in range(9):
            u = math.radians(200 + k * 16) if side < 0 else math.radians(-20 - k * 16)
            lx, ly = x + r * .72 * math.cos(u), y - r * .72 * math.sin(u)
            cv.poly([(lx, ly - 9), (lx + 7, ly), (lx, ly + 9), (lx - 7, ly)], (190, 140, 58), a)
    for k in range(40):
        u = k / 40 * 6.283
        cv.circ(x + r * .86 * math.cos(u), y + r * .86 * math.sin(u), r * .015, fill=(176, 128, 50), a=a)
    cv.circ(x, y, r, outline=INK, w=3, a=a)
    # glint
    g = (math.sin(t * .8) + 1) / 2
    cv.line([(x - r * .55, y - r * .35), (x - r * .35, y - r * .6)], SNOW, 6, a * .35 * g)

def scene_nobel(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0 + .01 * t)
    chapter_tag(cv, "16", "Stockholm, 6 October 2026", 1)
    tr = b.kw(0, "He called"); tc = b.kw(0, "about four hundred")
    q = eo(pr(t, 0, 1.2))
    medal(cv, 470, 600, 200 * eback(q, 1.2), q, t)
    paste_card(cv, photo("halzen.jpg"), 1080, 470, 400, 440, eo(pr(t, .6, 1.6)), crop=(150, 0, 1280, 1250), rot=1.5)
    qq = eo(pr(t, 1.0, 2.0))
    cv.text(1340, 330, "Nobel Prize", 54, INK, qq, "Black", "lm")
    cv.text(1342, 392, "in Physics 2026", 34, TERRA, qq, "Bold", "lm")
    cv.text(1342, 460, "Francis Halzen", 32, INK2, qq, "SemiBold", "lm")
    cv.line([(1342, 512), (1342 + 360 * qq, 512)], RULE, 2, qq)
    qr = eo(pr(t, tr, tr + .8))
    cv.text(1342, 560, "“recognition the whole", 28, INK, qr, "MediumItalic", "lm")
    cv.text(1342, 600, "collaboration deserves”", 28, INK, qr, "MediumItalic", "lm")
    # 450 scientists
    qs = pr(t, tc - .5, tc + 3.5)
    if qs > 0:
        n = int(450 * eo(qs))
        x0, y0 = 200, 860
        for k in range(450):
            i, j = k % 75, k // 75
            x, y = x0 + i * 17, y0 + j * 26
            if k < n:
                cv.circ(x, y - 6, 4, fill=INK2 if k % 7 else TERRA, a=1)
                cv.rrect(x - 5, y - 1, x + 5, y + 10, 4, fill=INK2 if k % 7 else TERRA, a=1)
        cv.text(1530, 930, f"≈ {n}", 56, INK, eo(qs * 3), "Black", "lm")
        cv.text(1532, 985, "scientists", 26, INK2, eo(qs * 3), "SemiBold", "lm")

def scene_future(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 560, 1.0)
    chapter_tag(cv, "17", "What comes next", 1)
    tu = b.kw(0, "An upgrade"); tg = b.kw(0, "A proposed"); tr = b.kw(0, "radio")
    zoom = lerp(2.0, 1.0, eio(pr(t, tg - .2, tg + 2.0)))
    cx, cy = 960, 600
    sc = 35 * zoom
    # gen2 footprint
    qg = eo(pr(t, tg, tg + 2.0))
    if qg > 0:
        rng = np.random.default_rng(3)
        R = 2.8 * 5.3 * sc
        hexo = [(cx + R * math.cos(k * 1.047 + .52), cy + R * .62 * math.sin(k * 1.047 + .52)) for k in range(7)]
        cv.poly(hexo, ICE, qg * .6)
        dashed(cv, hexo, INK, 2.5, qg, 14, 9)
        for i in range(-10, 11):
            for j in range(-10, 11):
                x = (i + j * .5) * 2.4 * sc; y = j * .866 * 2.4 * sc * .62
                if abs(x) < 5.6 * sc and abs(y) < 5.6 * sc * .62: continue
                if (x / R) ** 2 + (y / (R * .62)) ** 2 < .82:
                    cv.circ(cx + x, cy + y, 5, fill=ICE4, a=qg * .8)
        cv.text(cx, cy + R * .62 + 50, "IceCube-Gen2  ·  proposed  ·  ≈ 8× the volume", 28, INK, qg, "Bold")
    qr = eo(pr(t, tr - .3, tr + 1.2))
    if qr > 0:
        rng = np.random.default_rng(8)
        for k in range(40):
            ang = rng.uniform(0, 6.28); rr = rng.uniform(520, 820)
            x, y = cx + rr * math.cos(ang), cy + rr * .45 * math.sin(ang)
            if 140 < y < 1000:
                qk = eo(pr(t, tr + k * .03, tr + .4 + k * .03)) * qr
                cv.line([(x, y), (x, y - 26)], INK, 3, qk)
                cv.line([(x - 12, y - 26), (x + 12, y - 26)], INK, 3, qk)
                cv.circ(x, y - 32, 4, fill=OCHRE, a=qk)
        chip(cv, 1560, 170, "radio antennas  ·  highest energies", qr, size=24)
    # current IceCube
    cv.ga = 1
    for k, (x, y) in enumerate(HEX):
        cv.circ(cx + x * sc, cy + y * sc * .62, max(3, 8 * zoom), fill=INK, a=1)
    qu = eo(pr(t, tu - .2, tu + 1.0))
    for k in range(7):
        ang = k * .9
        x, y = .7 * math.cos(ang) * (k > 0), .7 * math.sin(ang) * (k > 0)
        cv.circ(cx + x * sc, cy + y * sc * .62, max(4, 10 * zoom) * eback(qu), fill=TERRA, a=qu)
    chip(cv, cx, 300 + 200 * (1 - zoom) * 0, "IceCube today  ·  86 strings", 1 - qg, size=24)
    panel(cv, 110, 160, 640, 300, qu)
    cv.circ(150, 230, 11, fill=TERRA, a=qu)
    cv.text(180, 210, "IceCube Upgrade", 32, INK, qu, "Black", "lm")
    cv.text(182, 260, "7 new strings  ·  2025–2026", 24, INK2, qu, "SemiBold", "lm")

def scene_close(cv, t, S, T):
    b = Beat(S)
    te = b(1); td = b.kw(0, "in total darkness")
    if t < te:
        # back to the fingernail, then pull back to the ice in the dark
        u = eio(pr(t, b.kw(0, "For almost") - 1, td + 1.5))
        cv.cam = Cam(lerp(1520, 900, u), lerp(470, 640, u), lerp(2.3, 1.5, u))
        from scenes_a import scene_hook as _h
        from common import sun, earth_layers, finger
        sun(cv, 230, 420, 105, t)
        earth_layers(cv, 860, 470, 250)
        _streams(cv, t, 1)
        px, py = 860, 720
        cv.poly([(px - 46, py - 4), (px + 46, py - 4), (px + 40, py + 40), (px - 40, py + 40)], ICE, 1, INK, 2.5)
        cv.poly([(px - 46, py - 4), (px - 30, py - 18), (px + 62, py - 18), (px + 46, py - 4)], SNOW, 1, INK, 2.5)
        finger(cv, 1520, 720)
        _streams(cv, t, 1, over=True)
        dk = eo(pr(t, td - .3, td + 2.0))
        if dk > 0:
            cv.done()
            ov = Image.new("RGB", (W, H), (34, 30, 34))
            cv.im.paste(ov, (0, 0), Image.new("L", (W, H), int(238 * dk)))
            cv.cam = Cam(960, 540, 1.0 + .02 * (t - td))
            L = 260; ox, oy = 960, 560
            def P(x, y, z): return iso(x, y, z, ox, oy, 1.0)
            top = [P(0, 0, L), P(L, 0, L), P(L, L, L), P(0, L, L)]
            left = [P(0, L, L), P(L, L, L), P(L, L, 0), P(0, L, 0)]
            right = [P(L, 0, L), P(L, L, L), P(L, L, 0), P(L, 0, 0)]
            cv.poly(left, (96, 112, 120), dk, ICE3, 2); cv.poly(right, (76, 90, 98), dk, ICE3, 2); cv.poly(top, (150, 164, 168), dk, ICE2, 2)
            for k in range(1, 5):
                x0, y0 = P(k * L / 5, L, L); x1, y1 = P(k * L / 5, L, 0)
                for j in range(1, 8): cv.circ(lerp(x0, x1, j / 8), lerp(y0, y1, j / 8), 3, fill=(30, 30, 32), a=dk * .8)
            fl = max(0, math.sin((t - td) * 1.1)) ** 12
            fx, fy = P(L * .6, L, L * .45)
            cv.circ(fx, fy, 6 + 30 * fl, fill=CHER2, a=dk * fl * .5)
            cv.circ(fx, fy, 4 + 8 * fl, fill=CHER3, a=dk * fl)
    else:
        # end card: left column brand, right side left clear for YouTube end-screen elements
        cv.cam = Cam(960, 540, 1.0)
        tt = t - te
        q = eo(pr(tt, 0, 1.0))
        cv.done()
        ov = Image.new("RGB", (W, H), (34, 30, 34))
        cv.im.paste(ov, (0, 0), Image.new("L", (W, H), int(205 * (1 - q))))
        cv.text(120, 420, "LATOON", 150, INK, q, "Black", "lm")
        cv.text(124, 520, "Voyaging the Unseen", 40, TERRA, q, "Bold", "lm")
        cv.line([(124, 580), (124 + 420 * q, 580)], INK, 3, q)
        cv.text(124, 630, "AI  ·  technology  ·  science  ·  psychology  ·  philosophy", 24, INK2, q, "SemiBold", "lm")
        qq = eo(pr(tt, .8, 1.6))
        cv.text(124, 760, "What invisible thing should we catch next?", 30, INK, qq, "MediumItalic", "lm")
        # gentle stream across the bottom
        stream(cv, -50, 960, 1980, 930, t, .6 * q, TERRA, 2.5, 160)
        # faint placeholders where YouTube end-screen cards sit (right)
