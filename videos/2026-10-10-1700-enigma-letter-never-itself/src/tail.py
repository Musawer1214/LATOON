
# ================= tail: background, grain, photos, props =================
_BG = None
def background():
    global _BG
    if _BG is None:
        rng = np.random.default_rng(7)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        arr = np.ones((H, W, 3), np.float32) * np.array(PAPER, np.float32)
        d = np.sqrt(((xx - W * .5) / (W * .72)) ** 2 + ((yy - H * .46) / (H * .78)) ** 2)
        arr *= (1.035 - .13 * np.clip(d, 0, 1.3) ** 2)[..., None]
        lo = rng.normal(0, 1, (H // 48 + 2, W // 48 + 2)).astype(np.float32)
        lo = np.asarray(Image.fromarray(((lo + 3) * 40).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32) / 40 - 3
        arr += lo[..., None] * np.array([2.6, 2.2, 1.6], np.float32)
        fib = Image.new("L", (W, H), 0); dd = ImageDraw.Draw(fib)
        for i in range(3200):
            x, y = rng.uniform(0, W), rng.uniform(0, H); a = rng.uniform(0, math.pi); L = rng.uniform(5, 26)
            dd.line([(x, y), (x + L * math.cos(a), y + L * math.sin(a))], fill=int(rng.uniform(20, 60)), width=1)
        fib = np.asarray(fib.filter(ImageFilter.GaussianBlur(.6)), np.float32)
        arr -= fib[..., None] * .09
        # faint foxing spots
        for i in range(14):
            cx, cy, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(20, 70)
            m = np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * r * r)))
            arr -= m[..., None] * np.array([3, 6, 10], np.float32) * rng.uniform(.3, 1)
        _BG = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    return _BG.copy()

_GR = None
def grain(im, fi, amt=3.0):
    global _GR
    if _GR is None:
        rng = np.random.default_rng(11)
        _GR = [rng.normal(0, amt, (H, W, 1)).astype(np.int16) for _ in range(3)]
    a = np.asarray(im, np.int16) + _GR[(fi // 3) % 3]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

def vgrad(w, h, stops):
    ys = np.linspace(0, 1, h); out = np.zeros((h, 3), np.float32)
    ps = [p for p, _ in stops]; cs = np.array([c for _, c in stops], np.float32)
    for k in range(3): out[:, k] = np.interp(ys, ps, cs[:, k])
    return Image.fromarray(np.repeat(out[:, None, :], w, 1).astype(np.uint8), "RGB")

def hgrad(w, h, stops):
    return vgrad(h, w, stops).transpose(Image.TRANSPOSE)

def grade(img, warm=.10, desat=.15, contrast=1.0):
    arr = np.asarray(img.convert("RGB"), np.float32)
    g = arr.mean(2, keepdims=True); arr = arr * (1 - desat) + g * desat
    arr = (arr - 128) * contrast + 128
    arr = arr * (1 - warm) + np.array([255, 232, 196], np.float32) * (arr / 255) * warm
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

_IMG = {}
def photo(name, maxw=2400):
    if name not in _IMG:
        im = Image.open(os.path.join(ROOT, "img", name + ".jpg")).convert("RGB")
        if im.width > maxw: im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
        _IMG[name] = grade(im)
    return _IMG[name]

_VIG = None
def vignette_mask():
    global _VIG
    if _VIG is None:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((xx - W / 2) / (W * .62)) ** 2 + ((yy - H / 2) / (H * .62)) ** 2)
        _VIG = Image.fromarray((np.clip(d - .55, 0, 1) * 200).astype(np.uint8), "L")
    return _VIG

def fullphoto(cv, name, u, a=1.0, z0=1.0, z1=1.12, c0=(.5, .5), c1=(.5, .5), crop=None, dark=0.0):
    """Ken Burns full-frame photo. u in [0,1] progress. c = focus point in normalized coords of the image."""
    if a <= .01: return
    cv.done()
    src = photo(name)
    if crop: src = src.crop(crop)
    sw, sh = src.size
    base = max(W / sw, H / sh)
    z = base * lerp(z0, z1, esm(u))
    cx = lerp(c0[0], c1[0], esm(u)) * sw; cy = lerp(c0[1], c1[1], esm(u)) * sh
    vw, vh = W / z, H / z
    cx = min(max(cx, vw / 2), sw - vw / 2); cy = min(max(cy, vh / 2), sh - vh / 2)
    x0, y0 = cx - vw / 2, cy - vh / 2
    out = src.transform((W, H), Image.AFFINE, (1 / z, 0, x0, 0, 1 / z, y0), Image.BILINEAR)
    if dark > 0: out = Image.blend(out, Image.new("RGB", (W, H), (20, 17, 15)), dark)
    out.paste((22, 18, 15), (0, 0), vignette_mask())
    if a >= .999: cv.im.paste(out)
    else: cv.im.paste(Image.blend(cv.im, out, a))

_CARD = {}
def paste_card(cv, name, cx, cy, w, h, a=1.0, crop=None, rot=0.0, border=14, shadow=True, img=None, q=6):
    """editorial photo print with cream border + soft shadow (world coords). Cached per quantized size."""
    if a <= .01: return
    cv.done()
    z = cv.cam.z; X, Y = cv.pt(cx, cy)
    Wp, Hp = int(w * z) // q * q, int(h * z) // q * q
    if Wp < 8 or Hp < 8: return
    key = (name if img is None else id(img), Wp, Hp, crop, round(rot, 1), border)
    if key not in _CARD:
        if len(_CARD) > 120: _CARD.clear()
        src = photo(name) if img is None else img
        if crop: src = src.crop(crop)
        sr = src.width / src.height; tr = Wp / Hp
        if sr > tr:
            nw = int(src.height * tr); x0 = (src.width - nw) // 2; src = src.crop((x0, 0, x0 + nw, src.height))
        else:
            nh = int(src.width / tr); y0 = (src.height - nh) // 2; src = src.crop((0, y0, src.width, y0 + nh))
        ph = src.resize((Wp, Hp), Image.LANCZOS)
        b = int(border * z)
        card = Image.new("RGBA", (Wp + 2 * b, Hp + 2 * b), SNOW + (255,)); card.paste(ph, (b, b))
        if rot: card = card.rotate(rot, Image.BICUBIC, expand=True)
        sh = None
        if shadow:
            sh = Image.new("RGBA", (card.width + 60, card.height + 60), (40, 30, 20, 0))
            m = Image.new("L", sh.size, 0); m.paste(card.split()[3].point(lambda v: int(v * .38)), (30, 30))
            sh.putalpha(m.filter(ImageFilter.GaussianBlur(12)))
        _CARD[key] = (card, sh)
    card, sh = _CARD[key]
    if sh is not None:
        sa = sh if a >= .999 else Image.merge("RGBA", sh.split()[:3] + (sh.split()[3].point(lambda v: int(v * a)),))
        cv.im.paste(sa, (int(X - sh.width / 2 + 8 * z), int(Y - sh.height / 2 + 12 * z)), sa)
    al = card.split()[3] if a >= .999 else card.split()[3].point(lambda v: int(v * a))
    cv.im.paste(card.convert("RGB"), (int(X - card.width / 2), int(Y - card.height / 2)), al)

def shadow_circ(cv, x, y, r, a=1, off=(6, 9)):
    cv.circ(x + off[0], y + off[1], r, fill=(50, 38, 26), a=a * .18)

def dashed(cv, pts, c, w, a=1, dash=14, gap=10, phase=0.0):
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        L = math.hypot(x1 - x0, y1 - y0)
        if L < 1: continue
        s = -phase % (dash + gap) - (dash + gap)
        while s < L:
            e = min(L, s + dash); s0 = max(0, s)
            if e > s0:
                cv.line([(x0 + (x1 - x0) * s0 / L, y0 + (y1 - y0) * s0 / L), (x0 + (x1 - x0) * e / L, y0 + (y1 - y0) * e / L)], c, w, a)
            s += dash + gap

def bez(p0, p1, p2, p3, n=28):
    out = []
    for i in range(n + 1):
        u = i / n; v = 1 - u
        out.append((v ** 3 * p0[0] + 3 * v * v * u * p1[0] + 3 * v * u * u * p2[0] + u ** 3 * p3[0],
                    v ** 3 * p0[1] + 3 * v * v * u * p1[1] + 3 * v * u * u * p2[1] + u ** 3 * p3[1]))
    return out

def partial(pts, f):
    """first fraction f of a polyline"""
    if f >= 1: return pts
    if f <= 0: return pts[:1]
    L = [0]
    for (a, b), (c, d) in zip(pts[:-1], pts[1:]): L.append(L[-1] + math.hypot(c - a, d - b))
    tgt = L[-1] * f; out = [pts[0]]
    for i in range(1, len(pts)):
        if L[i] <= tgt: out.append(pts[i])
        else:
            u = (tgt - L[i - 1]) / max(1e-6, L[i] - L[i - 1])
            out.append((lerp(pts[i - 1][0], pts[i][0], u), lerp(pts[i - 1][1], pts[i][1], u))); break
    return out

def chapter_tag(cv, num, a=1):
    if a <= .01: return
    cv.text(96, 84, num, 26, OX, a, "Bold", "lm")
    cv.line([(138, 84), (138 + 56 * eo(a), 84)], INK2, 2, a)

def panel(cv, x0, y0, x1, y1, a=1, r=10, fill=SNOW, outline=RULE):
    if a <= .01: return
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=(60, 45, 30), a=a * .10)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a * .97, outline=outline, w=2)

_STAMP = {}
def stamp(cv, x, y, txt, size=64, rot=-8, a=1.0, c=OX, box=True, font="Black"):
    """rubber stamp: inked text with worn texture, rotated."""
    if a <= .01: return
    cv.done()
    key = (txt, size, rot, c, box, font)
    if key not in _STAMP:
        f = F(size, font); tw = int(f.getlength(txt)); th = int(size * 1.25)
        pad = int(size * .45)
        m = Image.new("L", (tw + 2 * pad, th + 2 * pad), 0); d = ImageDraw.Draw(m)
        d.text((pad + tw / 2, pad + th / 2), txt, font=f, fill=255, anchor="mm")
        if box: d.rounded_rectangle((6, 6, m.width - 6, m.height - 6), int(size * .18), outline=255, width=max(3, size // 14))
        rng = np.random.default_rng(len(txt) * 7 + size)
        noise = rng.random((m.height, m.width))
        blot = np.asarray(Image.fromarray((rng.random((m.height // 6 + 1, m.width // 6 + 1)) * 255).astype(np.uint8)).resize(m.size, Image.BICUBIC), np.float32) / 255
        arr = np.asarray(m, np.float32) / 255 * np.where(noise < .13, .25, 1.0) * (.62 + .38 * blot)
        m = Image.fromarray((arr * 235).astype(np.uint8)).rotate(rot, Image.BICUBIC, expand=True)
        _STAMP[key] = m
    m = _STAMP[key]
    z = cv.cam.z
    if abs(z - 1) > .01: m = m.resize((max(2, int(m.width * z)), max(2, int(m.height * z))), Image.BILINEAR)
    X, Y = cv.pt(x, y)
    if a < .999: m = m.point(lambda v: int(v * a))
    cv.im.paste(Image.new("RGB", m.size, c), (int(X - m.width / 2), int(Y - m.height / 2)), m)

# ---------- props ----------
def key_cap(cv, x, y, r, letter, press=0.0, a=1.0, hi=0.0):
    """round Enigma typewriter key: steel rim, black cap, white letter. press 0..1 sinks it."""
    if a <= .01: return
    dy = press * r * .18
    shadow_circ(cv, x, y + r * .25, r * 1.02, a * (1 - press * .5), (r * .10, r * .18))
    cv.circ(x, y + r * .22, r * .98, fill=(26, 24, 22), a=a)                     # stem shadow
    cv.circ(x, y + dy, r, fill=STEEL2, a=a)                                       # rim
    cv.circ(x - r * .05, y + dy - r * .06, r * .96, fill=STEEL3, a=a * .7)
    cv.circ(x, y + dy, r * .84, fill=mix(BAKE, OX, hi * .7), a=a)                # cap
    cv.circ(x - r * .2, y + dy - r * .26, r * .36, fill=(110, 104, 100), a=a * .22)
    cv.text(x, y + dy + r * .02, letter, r * .78, SNOW, a, "SemiBold")
    cv.circ(x, y + dy, r, outline=(20, 18, 16), w=max(1, r * .06), a=a * .9)

def lamp(cv, x, y, r, letter, lit=0.0, a=1.0):
    """lampboard window: dark plate hole, frosted glass with stencil letter; lit = warm filament glow."""
    if a <= .01: return
    cv.circ(x, y, r * 1.12, fill=(24, 22, 20), a=a)
    cv.circ(x, y, r, fill=mix((176, 170, 156), LAMP, lit), a=a)
    if lit > 0:
        cv.circ(x, y, r * .78, fill=mix(LAMP, (255, 240, 200), .6), a=a * lit)
        cv.circ(x, y, r * 1.9, fill=LAMP2, a=a * lit * .10)
        cv.circ(x, y, r * 1.45, fill=LAMP2, a=a * lit * .12)
    cv.circ(x - r * .3, y - r * .35, r * .3, fill=SNOW, a=a * (.25 + .2 * lit))
    cv.text(x, y + r * .03, letter, r * .95, mix((70, 64, 58), (120, 50, 20), lit), a, "Bold")
    cv.circ(x, y, r, outline=(18, 16, 14), w=max(1, r * .08), a=a)

QWERTZ = ["QWERTZUIO", "ASDFGHJK", "PYXCVBNML"]

def keyboard_layout(x0, y0, dx, dy):
    pos = {}
    for ri, row in enumerate(QWERTZ):
        off = (9 - len(row)) * dx / 2
        for ci, ch in enumerate(row): pos[ch] = (x0 + off + ci * dx, y0 + ri * dy)
    return pos

def machine_face(cv, cx, cy, s, t, typed="", lit_letter=None, lit=0.0, press_letter=None, press=0.0, a=1.0, rotors="AAA"):
    """detailed top-down Enigma: wooden case, bakelite plate, rotor windows, lampboard, keyboard."""
    if a <= .01: return
    Wd, Hd = 1180 * s, 820 * s
    x0, y0 = cx - Wd / 2, cy - Hd / 2
    cv.rrect(x0 + 14 * s, y0 + 22 * s, x0 + Wd + 14 * s, y0 + Hd + 22 * s, 26 * s, fill=(40, 28, 16), a=a * .22)
    # wooden case with grain
    cv.rrect(x0, y0, x0 + Wd, y0 + Hd, 26 * s, fill=(122, 82, 46), a=a)
    for k in range(22):
        yy = y0 + 14 * s + k * (Hd - 28 * s) / 22
        cv.line([(x0 + 10 * s, yy), (x0 + Wd * .4, yy + 3 * s * math.sin(k)), (x0 + Wd - 10 * s, yy + 2 * s)], (98, 64, 34), 2 * s, a * .35)
    cv.rrect(x0, y0, x0 + Wd, y0 + Hd, 26 * s, outline=(70, 46, 24), w=4 * s, a=a)
    # bakelite top plate
    px0, py0, px1, py1 = x0 + 40 * s, y0 + 40 * s, x0 + Wd - 40 * s, y0 + Hd - 40 * s
    cv.rrect(px0, py0, px1, py1, 14 * s, fill=BAKE, a=a)
    cv.rrect(px0 + 6 * s, py0 + 6 * s, px1 - 6 * s, py0 + 40 * s, 10 * s, fill=BAKE2, a=a * .5)
    # screws
    for sx, sy in [(px0 + 22 * s, py0 + 22 * s), (px1 - 22 * s, py0 + 22 * s), (px0 + 22 * s, py1 - 22 * s), (px1 - 22 * s, py1 - 22 * s)]:
        cv.circ(sx, sy, 8 * s, fill=STEEL2, a=a); cv.line([(sx - 6 * s, sy), (sx + 6 * s, sy)], BAKE, 2 * s, a)
    # rotor windows with letters
    for k in range(3):
        wx = cx - 110 * s + k * 110 * s; wy = py0 + 80 * s
        cv.rrect(wx - 34 * s, wy - 40 * s, wx + 34 * s, wy + 40 * s, 8 * s, fill=(20, 18, 16), a=a)
        cv.rrect(wx - 24 * s, wy - 30 * s, wx + 24 * s, wy + 30 * s, 5 * s, fill=(232, 222, 196), a=a)
        cv.text(wx, wy, rotors[k], 40 * s, INK, a, "Bold")
        # thumbwheel edge
        tx = wx + 46 * s
        cv.rrect(tx - 7 * s, wy - 46 * s, tx + 7 * s, wy + 46 * s, 5 * s, fill=STEEL, a=a)
        for j in range(9):
            yy = wy - 40 * s + j * 10 * s + (t * 0) % 10
            cv.line([(tx - 6 * s, yy), (tx + 6 * s, yy)], STEEL3, 2 * s, a * .7)
    # lampboard
    lp = keyboard_layout(cx - 4 * 92 * s, py0 + 200 * s, 92 * s, 82 * s)
    for ch, (lx, ly) in lp.items():
        lamp(cv, lx, ly, 30 * s, ch, lit if ch == lit_letter else 0.0, a)
    # keyboard
    kp = keyboard_layout(cx - 4 * 96 * s, py0 + 470 * s, 96 * s, 86 * s)
    for ch, (kx, ky) in kp.items():
        key_cap(cv, kx, ky, 33 * s, ch, press if ch == press_letter else 0.0, a)
    return lp, kp

def rotor_band(cv, x, y, w, h, offset, a=1.0, ring=STEEL3, label=None, n_vis=7):
    """rotor seen edge-on: cylindrical body, alphabet ring with scrolling letters, serrated thumb wheel."""
    if a <= .01: return
    cv.done()
    cv.rrect(x - w / 2 + 10, y - h / 2 + 14, x + w / 2 + 10, y + h / 2 + 14, 12, fill=(40, 30, 20), a=a * .2)
    # thumb wheel (serrated) on left
    tw = w * .22
    cv.rrect(x - w / 2, y - h / 2 - 16, x - w / 2 + tw, y + h / 2 + 16, 8, fill=(56, 54, 52), a=a)
    nt = 18
    for j in range(nt):
        ph = ((j + offset * 1.0) % nt) / nt
        yy = y - h / 2 - 10 + ph * (h + 20)
        sh = math.sin(ph * math.pi)
        cv.line([(x - w / 2 + 3, yy), (x - w / 2 + tw - 3, yy)], mix((30, 28, 26), STEEL3, sh), 3, a * sh)
    # alphabet ring body: cylindrical gradient
    bx0 = x - w / 2 + tw + 4; bx1 = x + w / 2
    X0, Y0 = cv.pt(bx0, y - h / 2); X1, Y1 = cv.pt(bx1, y + h / 2)
    gw, gh = int(X1 - X0), int(Y1 - Y0)
    if gw > 2 and gh > 2:
        g = vgrad(gw, gh, [(0, (60, 58, 54)), (.18, (200, 194, 178)), (.5, (240, 234, 216)), (.82, (190, 184, 168)), (1, (56, 54, 50))])
        cv.im.paste(g, (int(X0), int(Y0)), Image.new("L", (gw, gh), int(255 * a)))
    # scrolling letters
    step = h / (n_vis - 1.6)
    base = offset % 26
    for j in range(-4, 5):
        idx = int(math.floor(base)) + j; frac = base - math.floor(base)
        yy = y + (j - frac) * step
        if abs(yy - y) > h / 2 - 6: continue
        u = (yy - y) / (h / 2)
        squash = math.cos(u * math.pi / 2)
        col = mix((120, 112, 100), INK, squash)
        cv.text((bx0 + bx1) / 2, yy, chr(65 + idx % 26), max(6, h * .2 * (.55 + .45 * squash)), col, a * squash, "Bold")
    cv.rrect(bx0, y - h / 2, bx1, y + h / 2, 6, outline=(40, 36, 32), w=2, a=a)
    if label: cv.text(x, y + h / 2 + 46, label, 28, INK2, a, "SemiBold")

def contact_col(cv, x, y0, y1, a=1, c=BRASS, r=5, hi=None, hic=OX):
    for i in range(26):
        yy = lerp(y0, y1, i / 25)
        cv.circ(x, yy, r * (1.5 if hi == i else 1), fill=hic if hi == i else c, a=a)

def cable(cv, p0, p1, a=1.0, sag=120, c=(30, 28, 26), f=1.0):
    pts = bez(p0, (p0[0], p0[1] + sag), (p1[0], p1[1] + sag), p1, 30)
    pts = partial(pts, f)
    cv.line([(x + 4, y + 6) for x, y in pts], (40, 30, 20), 12, a * .18)
    cv.line(pts, c, 10, a)
    cv.line([(x - 2, y - 2) for x, y in pts], (90, 86, 80), 2.4, a * .7)
    for p in (p0, pts[-1]):
        cv.circ(p[0], p[1], 13, fill=BRASS, a=a); cv.circ(p[0] - 3, p[1] - 4, 5, fill=BRASS2, a=a)
        cv.circ(p[0], p[1], 13, outline=BRASS3, w=2, a=a)

def typed_row(cv, x, y, txt, size, a=1.0, c=INK, spacing=None, reveal=None, font="monob", hl=None, hlc=OX):
    """monospace letters at fixed pitch; hl = dict index->color/box"""
    sp = spacing or size * .62
    n = len(txt) if reveal is None else int(reveal)
    for i, ch in enumerate(txt[:n]):
        col = c
        if hl and i in hl: col = hl[i]
        cv.text(x + i * sp, y, ch, size, col, a, font)

def message_sheet(cv, cx, cy, w, h, a=1.0, rot=0.0):
    """aged message form: off-white paper, header rules, faint printed boxes (no readable English)."""
    if a <= .01: return
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    cv.rect(x0 + 10, y0 + 16, x1 + 10, y1 + 16, fill=(50, 36, 22), a=a * .16)
    cv.rect(x0, y0, x1, y1, fill=(244, 238, 222), a=a)
    cv.rect(x0, y0, x1, y0 + 70, fill=(232, 224, 204), a=a)
    for k in range(6):
        cv.rect(x0 + 24 + k * (w - 48) / 6, y0 + 18, x0 + 24 + (k + 1) * (w - 48) / 6 - 10, y0 + 52, outline=MUT, w=1.5, a=a * .6)
    for k in range(9):
        yy = y0 + 110 + k * (h - 140) / 9
        cv.line([(x0 + 24, yy + 34), (x1 - 24, yy + 34)], RULE, 1.4, a * .8)
    cv.rect(x0, y0, x1, y1, outline=(190, 176, 150), w=2, a=a)

def portrait(cv, name, cx, cy, w, h, a=1, rot=0, crop=None):
    paste_card(cv, name, cx, cy, w, h, a, crop=crop, rot=rot, border=12)

def paperclip(cv, x, y, a=1, s=1.0):
    pts = [(x, y + 60 * s), (x, y - 20 * s), (x + 10 * s, y - 32 * s), (x + 20 * s, y - 20 * s), (x + 20 * s, y + 48 * s), (x + 10 * s, y + 56 * s), (x + 5 * s, y + 48 * s), (x + 5 * s, y - 8 * s)]
    cv.line(pts, STEEL, 3.4 * s, a); cv.line([(px - 1, py - 1) for px, py in pts], STEEL3, 1.2 * s, a * .8)

def brass_key(cv, x, y, s=1.0, a=1.0, rot=0.0):
    if a <= .01: return
    ca, sa = math.cos(rot), math.sin(rot)
    def P(px, py): return (x + (px * ca - py * sa) * s, y + (px * sa + py * ca) * s)
    # shadow
    sx, sy = 8 * s, 12 * s
    cv.circ(P(-120, 0)[0] + sx, P(-120, 0)[1] + sy, 70 * s, fill=(50, 36, 22), a=a * .16)
    cv.poly([(px + sx, py + sy) for px, py in [P(-60, -14), P(170, -14), P(170, 14), P(-60, 14)]], (50, 36, 22), a * .16)
    # bow
    cv.circ(*P(-120, 0), 70 * s, fill=BRASS, a=a); cv.circ(*P(-128, -8), 58 * s, fill=BRASS2, a=a * .5)
    cv.circ(*P(-120, 0), 32 * s, fill=PAPER, a=a); cv.circ(*P(-120, 0), 32 * s, outline=BRASS3, w=3 * s, a=a)
    cv.circ(*P(-120, 0), 70 * s, outline=BRASS3, w=3 * s, a=a)
    # shaft
    cv.poly([P(-56, -13), P(170, -13), P(170, 13), P(-56, 13)], BRASS, a, outline=BRASS3, w=2.5 * s)
    cv.poly([P(-56, -11), P(170, -11), P(170, -4), P(-56, -4)], BRASS2, a * .6)
    # bit
    cv.poly([P(120, 13), P(170, 13), P(170, 62), P(156, 62), P(156, 44), P(142, 44), P(142, 56), P(120, 56)], BRASS, a, outline=BRASS3, w=2.5 * s)

# ---------- captions (fixed colours: cream, dark outline, amber active word) ----------
CAP_FILL = (255, 250, 238); CAP_HI = (255, 196, 64); CAP_EDGE = (22, 18, 14)
def build_caps():
    import timeline as TL
    chunks = []
    by_p = {}
    for (p, w, a, b) in TL.WORDS: by_p.setdefault(p, []).append((w, a, b))
    for p, ws in by_p.items():
        cur = []; L = 0
        for i, (w, a, b) in enumerate(ws):
            brk = cur and (L + len(w) + 1 > 44 or (cur[-1][0][-1] in ".?!:" and L > 14) or (a - cur[-1][2] > .45 and L > 10))
            if brk: chunks.append(cur); cur = []; L = 0
            cur.append((w, a, b)); L += len(w) + 1
        if cur: chunks.append(cur)
    out = []
    for i, ch in enumerate(chunks):
        s = ch[0][1] - .12; e = ch[-1][2] + .35
        if i + 1 < len(chunks): e = min(e, chunks[i + 1][0][1] - .12)
        out.append((s, e, ch))
    return out
CAPS = None
def captions(im, T, y=1000, size=44):
    global CAPS
    if CAPS is None: CAPS = build_caps()
    for s, e, ch in CAPS:
        if s <= T < e:
            d = ImageDraw.Draw(im); f = F(size, "Bold")
            words = [w for w, _, _ in ch]; sp = f.getlength(" ")
            ws = [f.getlength(w) for w in words]; tot = sum(ws) + sp * (len(ws) - 1)
            x = W / 2 - tot / 2
            ap = eo(pr(T, s, s + .18)) * (1 - pr(T, e - .1, e))
            # soft shadow band
            for (w, a, b), wl in zip(ch, ws):
                col = CAP_HI if a - .03 <= T < b + .08 else CAP_FILL
                d.text((x + 3, y + 4), w, font=f, fill=(10, 8, 6), anchor="lm", stroke_width=8, stroke_fill=(10, 8, 6))
                d.text((x, y), w, font=f, fill=col, anchor="lm", stroke_width=6, stroke_fill=CAP_EDGE)
                x += wl + sp
            return
