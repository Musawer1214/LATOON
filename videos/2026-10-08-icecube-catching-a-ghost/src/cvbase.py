# ---------------- easing
def cl(x, a=0.0, b=1.0): return a if x < a else b if x > b else x
def pr(t, a, b): return cl((t - a) / (b - a)) if b > a else float(t >= a)
def eo(x): x = cl(x); return 1 - (1 - x) ** 3
def ei(x): x = cl(x); return x ** 3
def eio(x): x = cl(x); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def esm(x): x = cl(x); return x * x * (3 - 2 * x)
def eback(x, s=1.4):
    x = cl(x); c3 = s + 1; return 1 + c3 * (x - 1) ** 3 + s * (x - 1) ** 2
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): t = cl(t); return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))
def win(t, a, b, fi=.6, fo=.6):
    """visibility window: fades in at a, out at b"""
    return eo(pr(t, a, a + fi)) * (1 - eio(pr(t, b - fo, b)))

_fc = {}
def F(size, w="Medium"):
    k = (max(6, int(size)), w)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(os.path.join(FONT_DIR, f"Inter-{w}.ttf"), k[0])
    return _fc[k]

# ---------------- camera + canvas
class Cam:
    def __init__(s, cx=960, cy=540, z=1.0):
        s.cx, s.cy, s.z = cx, cy, z
    def P(s, x, y): return ((x - s.cx) * s.z + 960, (y - s.cy) * s.z + 540)

class Cv:
    def __init__(s, im, cam=None):
        s.im = im; s.agg = None; s.pil = None; s.ga = 1.0
        s.cam = cam or Cam()
    def A(s):
        if s.pil is not None: s.pil = None
        if s.agg is None: s.agg = aggdraw.Draw(s.im)
        return s.agg
    def P_(s):
        if s.agg is not None: s.agg.flush(); s.agg = None
        if s.pil is None: s.pil = ImageDraw.Draw(s.im, "RGBA")
        return s.pil
    def done(s):
        if s.agg is not None: s.agg.flush(); s.agg = None
        s.pil = None
    def _a(s, a): return int(cl(a * s.ga) * 255)
    def pt(s, x, y): return s.cam.P(x, y)
    def sz(s, v): return v * s.cam.z
    # primitives (world coordinates)
    def circ(s, x, y, r, fill=None, a=1, outline=None, w=2, oa=None):
        R = r * s.cam.z
        if R < .35: return
        if s._a(a) == 0 and (oa is None or s._a(oa) == 0): return
        X, Y = s.pt(x, y)
        if X + R < -50 or X - R > W + 50 or Y + R < -50 or Y - R > H + 50: return
        d = s.A(); args = []
        if outline is not None: args.append(aggdraw.Pen(outline[:3], max(.5, w * s.cam.z), s._a(a if oa is None else oa)))
        if fill is not None: args.append(aggdraw.Brush(fill[:3], s._a(a)))
        d.ellipse((X - R, Y - R, X + R, Y + R), *args)
    def line(s, pts, c, w, a=1, screen_w=False):
        if s._a(a) == 0 or len(pts) < 2: return
        flat = []
        for x, y in pts:
            X, Y = s.pt(x, y); flat += [X, Y]
        s.A().line(flat, aggdraw.Pen(c[:3], max(.4, w if screen_w else w * s.cam.z), s._a(a)))
    def poly(s, pts, fill, a=1, outline=None, w=2):
        if s._a(a) == 0: return
        flat = []
        for x, y in pts:
            X, Y = s.pt(x, y); flat += [X, Y]
        args = []
        if outline is not None: args.append(aggdraw.Pen(outline[:3], max(.5, w * s.cam.z), s._a(a)))
        if fill is not None: args.append(aggdraw.Brush(fill[:3], s._a(a)))
        s.A().polygon(flat, *args)
    def rect(s, x0, y0, x1, y1, fill=None, a=1, outline=None, w=2):
        s.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, a, outline, w)
    def rrect(s, x0, y0, x1, y1, r, fill=None, a=1, outline=None, w=2):
        if s._a(a) == 0: return
        X0, Y0 = s.pt(x0, y0); X1, Y1 = s.pt(x1, y1); R = min(r * s.cam.z, (X1 - X0) / 2, (Y1 - Y0) / 2)
        if X1 - X0 < 1 or Y1 - Y0 < 1: return
        args = []
        if outline is not None: args.append(aggdraw.Pen(outline[:3], max(.5, w * s.cam.z), s._a(a)))
        if fill is not None: args.append(aggdraw.Brush(fill[:3], s._a(a)))
        s.A().rounded_rectangle((X0, Y0, X1, Y1), max(0, R), *args)
    def arrow(s, x0, y0, x1, y1, c, w=4, a=1, head=16):
        ang = math.atan2(y1 - y0, x1 - x0); L = math.hypot(x1 - x0, y1 - y0)
        if L < 1: return
        hb = min(head, L * .6)
        bx, by = x1 - hb * .8 * math.cos(ang), y1 - hb * .8 * math.sin(ang)
        s.line([(x0, y0), (bx, by)], c, w, a)
        s.poly([(x1, y1), (x1 - hb * math.cos(ang - .45), y1 - hb * math.sin(ang - .45)),
                (x1 - hb * math.cos(ang + .45), y1 - hb * math.sin(ang + .45))], c, a)
    def text(s, x, y, txt, size, c=INK, a=1, w="Medium", anchor="mm", track=0):
        al = s._a(a); S = size * s.cam.z
        if al == 0 or S < 5: return
        X, Y = s.pt(x, y)
        s.P_().text((X, Y), txt, font=F(S, w), fill=tuple(c[:3]) + (al,), anchor=anchor)
    def math(s, x, y, tex, h, c=INK, a=1, anchor="mm"):
        al = cl(a * s.ga)
        if al <= 0.004: return
        Hh = h * s.cam.z
        if Hh < 4: return
        m = math_mask(tex, Hh)
        X, Y = s.pt(x, y)
        if anchor[0] == "m": X -= m.width / 2
        elif anchor[0] == "r": X -= m.width
        if anchor[1] == "m": Y -= m.height / 2
        elif anchor[1] == "b": Y -= m.height
        s.done()
        if al < .999: m = m.point(lambda v, al=al: int(v * al))
        s.im.paste(Image.new("RGB", m.size, tuple(c[:3])), (int(X), int(Y)), m)
    def mathw(s, tex, h):
        return math_mask(tex, h * s.cam.z).width / s.cam.z
    def image(s, img, x0, y0, x1, y1, a=1, resample=Image.NEAREST):
        """paste an RGB/L PIL image into world box"""
        al = cl(a * s.ga)
        if al <= .004: return
        X0, Y0 = s.pt(x0, y0); X1, Y1 = s.pt(x1, y1)
        w, h = int(X1 - X0), int(Y1 - Y0)
        if w < 2 or h < 2: return
        s.done()
        im2 = img.resize((w, h), resample)
        if im2.mode != "RGB": im2 = im2.convert("RGB")
        mask = Image.new("L", (w, h), int(al * 255))
        s.im.paste(im2, (int(X0), int(Y0)), mask)
    def glow(s, x, y, r, c, a=1):
        """soft radial halo (cheap: few concentric translucent circles)"""
        if a * s.ga < .01: return
        for k, (rr, aa) in enumerate([(1.0, .05), (.72, .07), (.5, .09), (.32, .12)]):
            s.circ(x, y, r * rr, fill=c, a=a * aa)

