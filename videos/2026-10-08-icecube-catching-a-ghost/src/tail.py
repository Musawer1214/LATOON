
# ---------------- background: paper with fibre grain + soft vignette
_BG = None
def background():
    global _BG
    if _BG is None:
        rng = np.random.default_rng(7)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        arr = np.ones((H, W, 3), np.float32) * np.array(PAPER, np.float32)
        d = np.sqrt(((xx - W * .5) / (W * .7)) ** 2 + ((yy - H * .48) / (H * .75)) ** 2)
        arr *= (1.03 - .10 * np.clip(d, 0, 1.3) ** 2)[..., None]
        # low-frequency mottling
        lo = rng.normal(0, 1, (H // 40 + 2, W // 40 + 2)).astype(np.float32)
        lo = np.asarray(Image.fromarray(((lo + 3) * 40).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32) / 40 - 3
        arr += lo[..., None] * 2.2
        # fibres
        fib = Image.new("L", (W, H), 0); dd = ImageDraw.Draw(fib)
        for i in range(2600):
            x, y = rng.uniform(0, W), rng.uniform(0, H); a = rng.uniform(0, math.pi); L = rng.uniform(6, 30)
            dd.line([(x, y), (x + L * math.cos(a), y + L * math.sin(a))], fill=int(rng.uniform(20, 60)), width=1)
        fib = np.asarray(fib.filter(ImageFilter.GaussianBlur(.6)), np.float32)
        arr -= fib[..., None] * .10
        _BG = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    return _BG.copy()

_GR = None
def grain(im, fi, amt=5.0):
    global _GR
    if _GR is None:
        rng = np.random.default_rng(11)
        _GR = [rng.normal(0, amt, (H, W, 1)).astype(np.int16) for _ in range(4)]
    a = np.asarray(im, np.int16) + _GR[(fi // 2) % 4]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

def vgrad(w, h, stops):
    """vertical gradient image; stops = [(pos, color), ...]"""
    ys = np.linspace(0, 1, h)
    out = np.zeros((h, 3), np.float32)
    ps = [p for p, _ in stops]; cs = np.array([c for _, c in stops], np.float32)
    for k in range(3): out[:, k] = np.interp(ys, ps, cs[:, k])
    return Image.fromarray(np.repeat(out[:, None, :], w, 1).astype(np.uint8), "RGB")

_IMG = {}
def photo(name):
    if name not in _IMG: _IMG[name] = Image.open(os.path.join(ROOT, "img", name)).convert("RGB")
    return _IMG[name]

def paste_card(cv, img, cx, cy, w, h, a=1.0, crop=None, rot=0.0, border=14, shadow=True, warm=0.12):
    """editorial photo print: cream border, soft shadow, slight warm grade. world coords (cam applied)."""
    if a <= .01: return
    cv.done()
    z = cv.cam.z; X, Y = cv.pt(cx, cy); Wp, Hp = int(w * z), int(h * z)
    if Wp < 8 or Hp < 8: return
    src = img if crop is None else img.crop(crop)
    # cover-fit
    sr = src.width / src.height; tr = Wp / Hp
    if sr > tr:
        nw = int(src.height * tr); x0 = (src.width - nw) // 2; src = src.crop((x0, 0, x0 + nw, src.height))
    else:
        nh = int(src.width / tr); y0 = (src.height - nh) // 2; src = src.crop((0, y0, src.width, y0 + nh))
    ph = src.resize((Wp, Hp), Image.LANCZOS)
    arr = np.asarray(ph, np.float32)
    g = arr.mean(2, keepdims=True); arr = arr * .82 + g * .18  # slight desaturate
    arr = arr * (1 - warm) + np.array([250, 236, 205], np.float32) * warm * (arr / 255)  + arr * warm * .0
    ph = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    b = int(border * z)
    card = Image.new("RGBA", (Wp + 2 * b, Hp + 2 * b), SNOW + (255,)); card.paste(ph, (b, b))
    if rot: card = card.rotate(rot, Image.BICUBIC, expand=True)
    al = card.split()[3].point(lambda v: int(v * a))
    if shadow:
        sh = Image.new("RGBA", card.size, (40, 30, 20, 0)); sh.putalpha(al.point(lambda v: int(v * .35)))
        sh = sh.filter(ImageFilter.GaussianBlur(10 * z))
        cv.im.paste(sh, (int(X - card.width / 2 + 8 * z), int(Y - card.height / 2 + 12 * z)), sh)
    cv.im.paste(card.convert("RGB"), (int(X - card.width / 2), int(Y - card.height / 2)), al)

def shadow_circ(cv, x, y, r, a=1, off=(6, 9)):
    cv.circ(x + off[0], y + off[1], r, fill=(60, 45, 30), a=a * .16)

def label(cv, x, y, txt, a=1, c=INK2, size=26, w="SemiBold", anchor="mm"):
    cv.text(x, y, txt, size, c, a, w, anchor)

def chapter_tag(cv, num, word, a=1):
    """top-left chapter marker: small number + rule + word (consistent grid, x=120,y=96)"""
    if a <= .01: return
    cv.text(120, 96, num, 26, TERRA, a, "Bold", "lm")
    cv.line([(166, 96), (166 + 60 * eo(a), 96)], INK2, 2, a)
    cv.text(244, 96, word, 24, INK2, a, "SemiBold", "lm")

def counter_text(v, fmt="{:,.0f}"): return fmt.format(v)

def dashed(cv, pts, c, w, a=1, dash=14, gap=10, phase=0.0):
    seg = []
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        L = math.hypot(x1 - x0, y1 - y0); s = -phase % (dash + gap)
        while s < L:
            e = min(L, s + dash)
            if e > 0:
                s0 = max(0, s)
                cv.line([(x0 + (x1 - x0) * s0 / L, y0 + (y1 - y0) * s0 / L), (x0 + (x1 - x0) * e / L, y0 + (y1 - y0) * e / L)], c, w, a)
            s += dash + gap

def dom(cv, x, y, r, a=1, lit=0.0, litc=None):
    """IceCube digital optical module: glass sphere, steel belt, dark PMT, optional lit face"""
    if a <= .01: return
    shadow_circ(cv, x, y, r, a, (r * .12, r * .18))
    cv.circ(x, y, r, fill=(70, 72, 74), a=a)
    cv.circ(x - r * .12, y - r * .14, r * .82, fill=(98, 102, 104), a=a)
    cv.circ(x - r * .32, y - r * .36, r * .30, fill=(176, 182, 184), a=a * .55)
    cv.rect(x - r, y - r * .12, x + r, y + r * .12, fill=(168, 170, 168), a=a)
    if lit > 0:
        col = litc or CHER2
        cv.circ(x, y + r * .4, r * .55, fill=col, a=a * lit * .95)
        cv.circ(x, y, r * 2.0, fill=col, a=a * lit * .10)
    cv.circ(x, y, r, outline=INK, w=max(1.2, r * .08), a=a)
