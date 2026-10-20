# ===== scenes.py: topic Short "Can One Word Change What You Remember?" (Loftus & Palmer 1974). The Hidden Mind.
# PLAYBOOK v2 s5.1/s5.4, Map Warm. Colour meaning held through the video: SMASHED = SIGNAL RED / OXBLOOD text,
# HIT = TEAL / DEEP TEAL text, no-question control = INK2, what you SAW = TEAL strand, what you were TOLD = RED strand.
# Real material: 1960s staged crash-test film (Prelinger, public domain), Elizabeth Loftus photo, crash-test car photo,
# broken windscreen photo (all credited). One canvas + guided camera in the verb/speed scene (s5.1).
# Cue times: cues.json (EN word starts in scene time; scene 0 adds HOOK_PRE 0.3). Language-neutral labels only.
retime(gap=.3, tail=.6, extra=[0, 0, 0, 0, 0, 0, 0, 2.2])   # end card hold on the last scene (s5.4)
IMG = lambda f: os.path.join(HERE, "img", f)
import footage as FT
from PIL import Image as _PI, ImageDraw as _PD, ImageOps as _PO
import random as _rnd
DEEP_TEAL = (47, 95, 99); OCHRE = (201, 149, 47); WALNUT = (106, 74, 50)
CLIP = {}
def load_imgs():
    CLIP["c"] = FT.Clip(os.path.join(HERE, "footage", "crash_640.mp4"))

_WARM = {}
def film(t):
    """warm-toned frame of the staged crash film at clip time t (B&W film printed on warm stock)."""
    k = int(t * 30)
    if k not in _WARM:
        if len(_WARM) > 60: _WARM.clear()
        g = _PO.autocontrast(CLIP["c"].frame(t).convert("L"), cutoff=1)
        _WARM[k] = _PO.colorize(g, black=(34, 26, 20), white=(246, 236, 214), mid=(150, 132, 108))
    return _WARM[k]

FILM_CREDIT = "Safety Through Seat Belts (film): Prelinger Archives, public domain"

def crack_fn(p, cx=.55, cy=.42, seed=3, a=1.0):
    """frame callable for photo_print: radiating windscreen cracks drawn on to p (0..1) from (cx, cy)."""
    def f(im):
        if p <= 0: return im
        im = im.convert("RGB"); w, h = im.size
        ov = _PI.new("RGBA", im.size, (0, 0, 0, 0)); d = _PD.Draw(ov)
        r = _rnd.Random(seed); x0, y0 = cx * w, cy * h
        for i in range(13):
            ang = i / 13 * 6.283 + r.uniform(-.2, .2); L = r.uniform(.35, .75) * max(w, h) * eo(p)
            pts = [(x0, y0)]; x, y = x0, y0
            for s in range(6):
                a_ = ang + r.uniform(-.35, .35); x += math.cos(a_) * L / 6; y += math.sin(a_) * L / 6; pts.append((x, y))
            d.line(pts, fill=(22, 18, 14, int(150 * a)), width=5); d.line(pts, fill=(255, 250, 238, int(235 * a)), width=2)
        for rr in (.06, .13):
            R = rr * w * eo(cl(p * 1.4))
            d.ellipse((x0 - R, y0 - R * .8, x0 + R, y0 + R * .8), outline=(255, 250, 238, int(200 * a)), width=2)
        im.paste(ov, (0, 0), ov); return im
    return f

def car(cv, x, y, s, col, a=1.0, flip=False, dent=0.0):
    """side-view saloon pictogram (shaded body, cabin, windows, wheels); dent squashes the front end."""
    if a <= .01: return
    d = -1 if flip else 1
    fx = 92 * s * (1 - .28 * dent)                     # front overhang shrinks when dented
    X = lambda u: x + d * u
    cv.rrect(x - 96 * s + 6, y + 10 * s + 8, x + 96 * s + 6, y + 30 * s + 8, 10 * s, fill=SHADOW, a=a * .12)
    body = [(X(-92 * s), y - 18 * s), (X(fx), y - 18 * s + dent * 8 * s), (X(fx + 4 * s), y + 14 * s), (X(-96 * s), y + 14 * s)]
    cv.poly(body, col, a=a, outline=INK, w=3)
    cab = [(X(-52 * s), y - 18 * s), (X(-30 * s), y - 50 * s), (X(30 * s), y - 50 * s), (X(56 * s), y - 18 * s)]
    cv.poly(cab, col, a=a, outline=INK, w=3)
    cv.poly([(X(-44 * s), y - 21 * s), (X(-27 * s), y - 45 * s), (X(-2 * s), y - 45 * s), (X(-2 * s), y - 21 * s)], SNOW, a=a * .95)
    cv.poly([(X(4 * s), y - 21 * s), (X(4 * s), y - 45 * s), (X(27 * s), y - 45 * s), (X(47 * s), y - 21 * s)], SNOW, a=a * .95)
    cv.line([(X(-88 * s), y - 2 * s), (X(fx - 2 * s), y - 2 * s)], mix(col, INK, .35), 2, a)
    for u in (-58, 58):
        cv.circ(X(u * s), y + 16 * s, 17 * s, fill=INK, a=a)
        cv.circ(X(u * s), y + 16 * s, 7 * s, fill=PAPER2, a=a)

def burst(cv, x, y, r, p, col=SIGNAL_RED, a=1.0):
    if p <= 0: return
    q = eback(cl(p), 1.4); pts = []
    for i in range(18):
        rr = r * q * (1 if i % 2 == 0 else .48)
        ang = math.radians(i * 20 - 90); pts.append((x + rr * math.cos(ang), y + rr * math.sin(ang)))
    cv.poly(pts, HILITE, a=a, outline=col, w=4)

def gauge(cv, cx, cy, r, val, col, p=1.0, a=1.0, vmax=60):
    """speedometer: SNOW dial, ticks every 10 mph (0-60), coloured arc + INK needle to val*p."""
    if a <= .01: return
    cv.circ(cx + 8, cy + 12, r, fill=SHADOW, a=a * .12)
    cv.circ(cx, cy, r, fill=SNOW, a=a, outline=RULE, w=3)
    A0, A1 = -125, 125
    ang = lambda v: A0 + (A1 - A0) * v / vmax
    cv.arc(cx, cy, r * .80, A0, A1, PAPER3, 16, a)
    v = val * eio(cl(p))
    if v > 0.2: cv.arc(cx, cy, r * .80, A0, ang(v), col, 16, a)
    for k in range(0, vmax + 1, 10):
        g = math.radians(ang(k) - 90)
        cv.line([(cx + r * .64 * math.cos(g), cy + r * .64 * math.sin(g)), (cx + r * .70 * math.cos(g), cy + r * .70 * math.sin(g))], INK2, 3, a)
        cv.text(cx + r * .50 * math.cos(g), cy + r * .50 * math.sin(g), str(k), r * .15, INK2, a, "SemiBold", role="diag")
    g = math.radians(ang(v) - 90)
    cv.line([(cx, cy), (cx + r * .78 * math.cos(g), cy + r * .78 * math.sin(g))], INK, 7, a)
    cv.circ(cx, cy, r * .09, fill=INK, a=a); cv.circ(cx, cy, r * .04, fill=col, a=a)
    cv.text(cx, cy + r * .42, "mph", r * .14, INK2, a, "SemiBold", role="diag")

from PIL import ImageFilter as _IF, ImageChops as _IC
_M3D = {}
def _m3d_frame(path, w, h):
    im = _PI.open(path).convert("RGBA")
    if im.size != (w, h): im = im.resize((w, h), _PI.LANCZOS)
    a = im.getchannel("A")
    solid = a.point(lambda v: 255 if v > 200 else 0).filter(_IF.MinFilter(7)).filter(_IF.MaxFilter(7))
    grow = solid.filter(_IF.MaxFilter(5)).filter(_IF.GaussianBlur(1.1))
    line = _IC.subtract(grow, solid.filter(_IF.GaussianBlur(.6)))
    sh = solid.filter(_IF.GaussianBlur(14)).point(lambda v: int(v * .22))
    out = _PI.new("RGBA", (w, h), (0, 0, 0, 0))
    shadow = _PI.new("RGBA", (w, h), tuple(SHADOW) + (0,)); shadow.putalpha(sh)
    out.alpha_composite(shadow, (8, 12))
    ink = _PI.new("RGBA", (w, h), tuple(INK2) + (0,)); ink.putalpha(line.point(lambda v: int(min(255, v * 1.15))))
    out.alpha_composite(ink); out.alpha_composite(im)
    return out
def m3d_layer(cv, t, name, box, a=1.0, fin=.35):
    """Manim 3D PNG sequence (m3d/frames/<name>) composited into an engine box; holds its last frame."""
    if t < 0 or a <= .003: return
    a = a * eo(pr(t, 0, fin))
    d = os.path.join(HERE, "m3d", "frames", name)
    if name not in _M3D: _M3D[name] = len([f for f in os.listdir(d) if f.endswith(".png")])
    k = max(1, min(_M3D[name], int(t * 30) + 1))
    im = _m3d_frame(os.path.join(d, f"f_{k:05d}.png"), int(box[2] - box[0]), int(box[3] - box[1]))
    cv.paste(im, box[0], box[1], a, "lt")
    qa_log("photo", box)

def with_cam(cv, cam, fn):
    old = cv.cam; cv.cam = cam
    try: fn()
    finally: cv.cam = old

def guided(t, keys):
    if t <= keys[0][0]: _, x, y, z = keys[0]; return Cam(x, y, z)
    for (t0, x0, y0, z0), (t1, x1, y1, z1) in zip(keys[:-1], keys[1:]):
        if t <= t1:
            u = eio(pr(t, t0, t1)); return Cam(lerp(x0, x1, u), lerp(y0, y1, u), z0 * (z1 / z0) ** u)
    _, x, y, z = keys[-1]; return Cam(x, y, z)

TRANS = {1: "rise", 2: "mask", 3: "page", 4: "mask", 5: "rise", 6: "page", 7: "fade"}
TRANS_CENTER = {2: (540, 640), 4: (540, 700)}
GROUND = {}
AUTO_WHOOSH = False          # three-layer sound (owner 2026-10-20): bed + timed UI/motion SFX + voice
# (scene, local t, name[, dB]) - every cue sits on an on-screen event; bigger swooshes only on scene changes (voice gaps)
SFX = [
    (0, 1.95, "ui_pop_hard", -17),        # crash impact in the film
    (0, 3.10, "ui_pop_dry"),              # "1 WORD" chip
    (0, 5.62, "ui_select"),               # cracks draw over the print
    (0, 6.55, "ui_tick"),                 # NEVER THERE stamp
    (1, -.12, "swoosh_short"),            # scene change
    (1, .40, "ui_pop_light"),             # 1974 headline
    (1, 2.04, "ui_pop_dry"),              # Loftus name card
    (1, 3.30, "ui_pop_light"),            # Palmer name card
    (1, 3.50, "ui_select"),               # locator map draws in
    (1, 4.80, "ui_tick"),                 # 45 counter
    (1, 4.96, "swoosh_short", -19),       # film strip slides in
    (1, 6.40, "ui_select"),               # MPH? chip
    (2, -.12, "sweep_air"),               # scene change (mask)
    (2, .40, "ui_pop_light"),             # verb slot card
    (2, 2.26, "ui_pop_hard"),             # SMASHED card
    (2, 3.55, "ui_tick"),                 # left needle sweeps
    (2, 5.74, "ui_pop_dry"),              # HIT card
    (2, 5.95, "ui_tick"),                 # right needle sweeps
    (3, -.12, "swoosh_fast"),             # scene change (page)
    (3, .30, "ui_pop_light"),             # crash-test photo
    (3, 1.30, "ui_pop_light"),            # KNOWN SPEED chip
    (3, 2.32, "ui_pop_hard", -16),        # 3D test car hits the barrier
    (3, 2.75, "ui_tick"),                 # real-speed bars
    (3, 3.38, "ui_tick"),                 # guess bars
    (3, 4.60, "ui_select"),               # WORD > SPEED chip
    (4, -.12, "swoosh_short"),            # scene change (mask)
    (4, .50, "ui_pop_dry"),               # 150 dots
    (4, 1.52, "paper_rustle", -24),       # calendar pages flip
    (4, 2.45, "ui_select"),               # dots split into three groups
    (4, 4.85, "ui_pop_light"),            # glass photo
    (5, -.12, "sweep_air"),               # scene change
    (5, .30, "stamp", -19),               # NO BROKEN GLASS stamp
    (5, 1.40, "ui_tick"),                 # red YES dots fill
    (5, 2.30, "ui_pop_hard"),             # 16/50
    (5, 5.03, "ui_pop_dry"),              # teal YES dots + 7/50
    (5, 5.40, "ui_tick"),                 # control 6/50
    (6, -.12, "swoosh_short"),            # scene change (page)
    (6, 2.20, "ui_pop_light"),            # SEEN strand
    (6, 3.12, "ui_pop_light"),            # TOLD strand
    (6, 4.44, "swoosh_short", -21),       # strands twist together
    (6, 5.04, "ui_select"),               # ONE MEMORY card
    (7, -.12, "swoosh_fast"),             # scene change (fade)
    (7, .90, "ui_pop_dry"),               # RECORDING strike
    (7, 1.55, "ui_pop_light"),            # WITNESSES chip
    (7, 1.85, "ui_pop_light"),            # COURTS chip
    (7, 2.45, "ui_pop_dry"),              # question mark
    (7, 4.90, "chime", -26),              # end card
]

def stamp_plate(cv, x, y, txt, size, rot, a):
    """OXBLOOD rubber stamp on a SNOW paper slip so it reads over photos (contrast >= 4.5:1)."""
    w = cv.tw(txt, size, "Black") + size * 1.5; h = size * 2.0
    c, s_ = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    pts = [(x + dx * c - dy * s_, y + dx * s_ + dy * c) for dx, dy in ((-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2))]
    cv.poly([(px + 6, py + 10) for px, py in pts], SHADOW, a=.18 * a)
    cv.poly(pts, SNOW, a=a * .97)
    stamp(cv, x, y, txt, size, rot, a, OXBLOOD)

# ---------------------------------------------------------------- 0 hook
def s_hook(cv, t, D):
    # frame 1 moving: the staged crash plays, big keyword readable muted within 2 s
    kinetic(cv, t, 330, "SAME CRASH", 96, INK, -.25, "Black", .03, role="head")
    ct = 3.8 + min(t - .3, 3.1) if t < 3.4 else 6.9          # film runs to the impact, then holds the frame
    pc = eo(pr(t, 5.55, 6.4)) if t < 6.85 else 1.0
    photo_print(cv, t + .7, film(ct), box=(110, 470, 970, 1115), rot=-1.2, push=(1.0, 1.10), dur=D, tape=True,
                frame=crack_fn(pc, a=1 - .55 * eo(pr(t, 6.85, 7.3))), credit_txt=FILM_CREDIT)
    chip(cv, W / 2, 1265, "1 WORD", OXBLOOD, eback(pr(t, 3.05, 3.45), 1.3), tc=SNOW, size=46)
    q = eo(pr(t, 5.6, 6.0))
    if q > 0: label_card(cv, W / 2, 1390, "BROKEN GLASS?", q * (1 - eo(pr(t, 6.45, 6.6))), size=38, tc=INK)
    q2 = eo(pr(t, 6.5, 6.8))
    if q2 > 0: stamp_plate(cv, W / 2, 1390, "NEVER THERE", 46, -4, q2)
    maker_mark(cv, W - 64, 1560, .8)

# ---------------------------------------------------------------- 1 who + the films
MAPV = MapView(-125.0, -119.0, 45.6, 49.2, box=(590, 790, 990, 1040))
def s_who(cv, t, D):
    kinetic(cv, t, 330, "1974", 120, INK, 0, "Black", .04, role="head")
    photo_print(cv, t - 1.7, IMG("loftus.jpg"), box=(110, 470, 500, 990), rot=-1.8, push=(1.0, 1.07), dur=D, fy=.3,
                credit_txt="Photo: BDEngler, CC BY-SA 3.0", treat="muted")
    q = eo(pr(t, 2.0, 2.4))
    cv.text(780, 560, "ELIZABETH", 46, INK, q, "Black", role="label")
    cv.text(780, 615, "LOFTUS", 46, INK, q, "Black", role="label")
    label_card(cv, 780, 715, "& JOHN PALMER", eback(pr(t, 3.28, 3.65), 1.3), size=32)
    am = eo(pr(t, 3.45, 3.9)) * (1 - eo(pr(t, 4.7, 5.0)))
    if am > 0:
        map_route(cv, t - 3.45, MAPV, places=[(-122.30, 47.65, "SEATTLE", "l")], a=am, col=TEAL, graticule=2)
    counter(cv, t, 45, x=780, y=900, size=96, dur=.8, t0=4.8, col=INK, unit="STUDENTS")
    # film strip of the crash film slides in on "films"
    p = eo(pr(t, 4.9, 5.7))
    if p > 0:
        y0, y1 = 1125, 1330; off = (1 - p) * 700 - (t - 4.9) * 40
        cv.rect(60, y0, 1020, y1, fill=WALNUT, a=p * .96)
        for i in range(-1, 24):
            hx = 60 + ((i * 46 - (t - 4.9) * 40) % 1104) - 40
            if 64 < hx < 996:
                cv.rrect(hx, y0 + 10, hx + 22, y0 + 26, 4, fill=PAPER, a=p * .9)
                cv.rrect(hx, y1 - 26, hx + 22, y1 - 10, 4, fill=PAPER, a=p * .9)
        for i in range(6):
            fxp = 80 + i * 220 + off
            if fxp > 1000 or fxp + 200 < 70: continue
            fr = film(1.0 + i * 5.2).resize((200, 150), _PI.BILINEAR)
            x0 = int(max(fxp, 66)); x1 = int(min(fxp + 200, 1014))
            if x1 - x0 < 4: continue
            crop = fr.crop((x0 - int(fxp), 0, x1 - int(fxp), 150))
            cv.paste(crop.convert("RGBA"), x0, y0 + 28, p, "lt")
        chip(cv, 780, 1080, "7 FILMS", DEEP_TEAL, eback(pr(t, 5.4, 5.8), 1.3), tc=SNOW, size=34)
    label_card(cv, W / 2, 1420, "HOW FAST?", eback(pr(t, 6.4, 6.8), 1.3), size=40, tc=INK)
    source_tag(cv, t - 2.6, "Loftus & Palmer, 1974", y=1530)

# ---------------------------------------------------------------- 2 one verb, two speeds (one canvas, guided camera)
def s_verb(cv, t, D):
    headline(cv, t, "ONE VERB", t0=-.05)
    cam = guided(t, [(0, 540, 560, 1.45), (1.6, 540, 600, 1.30), (2.3, 330, 880, 1.04), (5.1, 330, 880, 1.04),
                     (5.9, 540, 930, .97)])
    def draw():
        # the verb slot the question turned on
        qn = 1 - eo(pr(t, 1.9, 2.4))                       # two cars, unknown speed: the question
        if qn > 0:
            car(cv, 440, 460, .62, BRASS2, qn); car(cv, 640, 460, .62, BRASS2, qn, flip=True)
            cv.text(540, 395, "? mph", 34, INK2, qn * eo(pr(t, .1, .5)), "Bold", role="label")
        qs = eo(pr(t, .36, .8))
        card(cv, 340, 560, 740, 690, 16, SNOW, qs)
        slot_fill = eo(pr(t, 1.0, 1.3)) * (1 - eo(pr(t, 2.2, 2.5)))
        cv.line([(400, 650), (680, 650)], INK2, 6, qs)
        cv.text(540, 612, "?", 64, OXBLOOD, qs * (1 - eo(pr(t, 2.2, 2.5))), "Black", role="label")
        for (xx, tt, c) in ((290, 1.6, SIGNAL_RED), (790, 1.9, TEAL)):
            pa = eo(pr(t, tt, tt + .5))
            if pa > 0: cv.arrow(540 + (xx - 540) * .22, 700, 540 + (xx - 540) * .22 + (xx - 540) * .55 * pa, 700 + 50 * pa, c, 6, .9)
        # SMASHED side
        qa = eback(pr(t, 2.26, 2.66), 1.3)
        if qa > 0:
            chip(cv, 290, 790, "SMASHED", OXBLOOD, cl(qa), tc=SNOW, size=40)
            pc = eo(pr(t, 2.5, 3.2))
            car(cv, 290 - 150 + 58 * pc, 945, .78, SIGNAL_RED, cl(qa), dent=pc)
            car(cv, 290 + 150 - 58 * pc, 945, .78, BRASS2, cl(qa), flip=True, dent=pc)
            burst(cv, 290, 920, 64, pr(t, 3.05, 3.4), SIGNAL_RED, cl(qa))
            gauge(cv, 290, 1165, 150, 40.8, SIGNAL_RED, pr(t, 3.5, 4.3), cl(qa))
            v = 40.8 * eio(pr(t, 3.5, 4.3))
            cv.text(290, 1375, f"{v:.1f}", 76, OXBLOOD, eo(pr(t, 3.5, 3.9)), "Black", role="hook")
            cv.text(290, 1440, "≈ 66 km/h", 30, INK2, eo(pr(t, 4.2, 4.6)), "SemiBold", role="sub")
        # HIT side
        qb = eback(pr(t, 5.74, 6.14), 1.3)
        if qb > 0:
            chip(cv, 790, 790, "HIT", DEEP_TEAL, cl(qb), tc=SNOW, size=40)
            ph = eo(pr(t, 5.9, 6.4))
            car(cv, 790 - 160 + 50 * ph, 945, .78, TEAL, cl(qb))
            car(cv, 790 + 160 - 50 * ph, 945, .78, BRASS2, cl(qb), flip=True)
            gauge(cv, 790, 1165, 150, 34.0, TEAL, pr(t, 5.95, 6.6), cl(qb))
            v = 34.0 * eio(pr(t, 5.95, 6.6))
            cv.text(790, 1375, f"{v:.1f}", 76, DEEP_TEAL, eo(pr(t, 5.95, 6.3)), "Black", role="hook")
            cv.text(790, 1440, "≈ 55 km/h", 30, INK2, eo(pr(t, 6.4, 6.8)), "SemiBold", role="sub")
    with_cam(cv, cam, draw)
    source_tag(cv, t - 4.6, "Loftus & Palmer 1974, Table 1", y=1530)

# ---------------------------------------------------------------- 3 the real speed barely mattered
REAL = [20, 30, 40, 40]; GUESS = [37.7, 36.2, 39.7, 36.1]
def s_staged(cv, t, D):
    headline(cv, t, "STAGED CRASHES", t0=-.05, size=58)
    pa = 1 - eo(pr(t, 4.4, 4.9)) * .0
    photo_print(cv, t - .3, IMG("crash_de.jpg"), box=(190, 450, 890, 790), rot=1.2, push=(1.0, 1.08), dur=D, fy=.62,
                credit_txt="Crash-test car: Kalispera Dell, CC BY 3.0", treat="muted")
    a3 = 1 - eio(pr(t, 2.55, 2.95))
    if a3 > 0:
        m3d_layer(cv, t + .05, "crashtrack", (60, 880, 1020, 1300), a3)
        chip(cv, 300, 1360, "KNOWN SPEED", DEEP_TEAL, eback(pr(t, 1.3, 1.7), 1.3) * a3, tc=SNOW, size=30)
        cv.text(820, 1360, "20 · 30 · 40 mph", 30, INK2, eo(pr(t, 1.9, 2.3)) * a3, "Bold", role="label")
    base, k = 1300, 8.0
    xs = [330, 500, 670, 840]
    for i in range(4):
        pr_ = eo(pr(t, 2.7 + i * .1, 3.2 + i * .1)); pg = eo(pr(t, 3.3 + i * .1, 3.9 + i * .1))
        x = xs[i]
        if pr_ > 0:
            h = REAL[i] * k * pr_
            cv.rrect(x - 58, base - h, x - 4, base, 6, fill=PAPER2, a=pr_, outline=INK2, w=3)
            cv.text(x - 31, base + 34, str(REAL[i]), 28, INK2, pr_, "Bold", role="diag")
        if pg > 0:
            h = GUESS[i] * k * pg
            cv.rrect(x + 4, base - h, x + 58, base, 6, fill=OCHRE, a=pg, outline=WALNUT, w=2)
            cv.text(x + 31, base - h - 26, f"{GUESS[i]:.1f}", 26, WALNUT, eo(pr(t, 3.8 + i * .1, 4.1 + i * .1)), "Bold", role="diag")
    cv.line([(270, base), (900, base)], INK2, 3, eo(pr(t, 2.6, 2.9)))
    q = eo(pr(t, 2.7, 3.0)); q2 = eo(pr(t, 3.38, 3.7))
    label_card(cv, 330, 900, "REAL", q, size=28, tc=INK2)
    chip(cv, 480, 900, "GUESS", OCHRE, q2, tc=INK, size=28)
    cv.text(910, base + 34, "mph", 26, INK2, q, "SemiBold", "rm", role="diag")
    # the flat line of guesses
    pf = eo(pr(t, 4.0, 4.6))
    if pf > 0:
        yy = base - 37.4 * k
        for j in range(16):
            xa = 280 + j * 40
            if xa < 280 + 620 * pf: cv.line([(xa, yy), (xa + 22, yy)], OXBLOOD, 4, .9)
    chip(cv, W / 2, 1460, "WORD > SPEED", OXBLOOD, eback(pr(t, 4.58, 5.0), 1.3), tc=SNOW, size=40)
    maker_mark(cv, W - 64, 1585, .8)

# ---------------------------------------------------------------- 4 test 2: 150 students, one week, one question
def dots_pos(i, split):
    """150 dots: one 15x10 grid that splits into three 5x10 groups."""
    g, j = divmod(i, 50); c, r = j % 5, j // 5
    xa = 330 + (g * 5 + c) * 30; ya = 480 + r * 30                 # merged grid
    xb = [210, 465, 720][g] + c * 32; yb = 470 + r * 32            # split groups
    return lerp(xa, xb, split), lerp(ya, yb, split)
GROUP_COL = [SIGNAL_RED, TEAL, MUT]
def s_test2(cv, t, D):
    headline(cv, t, "TEST 2", t0=-.05)
    sp = eio(pr(t, 2.4, 3.1))
    for i in range(150):
        q = eo(pr(t, .45 + i * .006, .75 + i * .006))
        if q <= 0: continue
        x, y = dots_pos(i, sp)
        cv.circ(x + 12, y + 12, 11, fill=mix(INK2, GROUP_COL[i // 50], sp), a=q)
    counter(cv, t, 150, x=W / 2, y=830, size=70, dur=.7, t0=.5, col=INK, a=1 - eo(pr(t, 2.3, 2.6)), unit="STUDENTS")
    for g, (txt, col, tc) in enumerate((("SMASHED", OXBLOOD, SNOW), ("HIT", DEEP_TEAL, SNOW), ("NO QUESTION", INK2, SNOW))):
        chip(cv, [286, 541, 796][g], 830, txt, col, eback(pr(t, 2.6 + g * .12, 3.0 + g * .12), 1.3), tc=tc, size=26)
    # one week later: calendar pages flip
    qc = eo(pr(t, 1.4, 1.8)) * (1 - eo(pr(t, 4.5, 4.9)))
    if qc > 0:
        x0, y0, x1, y1 = 400, 960, 680, 1250
        card(cv, x0, y0, x1, y1, 14, SNOW, qc)
        cv.rect(x0, y0, x1, y0 + 64, fill=OXBLOOD, a=qc)
        day = 1 + int(7 * eio(pr(t, 1.6, 2.6)))
        cv.text((x0 + x1) / 2, y0 + 34, "DAY", 30, SNOW, qc, "Black", track=.1, role="label")
        cv.text((x0 + x1) / 2, (y0 + y1) / 2 + 40, str(day), 120, INK, qc, "Black", role="hook")
        fl = (t * 7) % 1 if 1.6 < t < 2.6 else 0
        if fl > 0: cv.rect(x0, y0 + 64, x1, y0 + 64 + (y1 - y0 - 64) * (1 - fl), fill=PAPER2, a=qc * .6)
        chip(cv, W / 2, 1320, "+7 DAYS", OXBLOOD, eback(pr(t, 2.2, 2.6), 1.3) * qc, tc=SNOW, size=34)
    photo_print(cv, t - 4.8, IMG("glass.jpg"), box=(290, 990, 790, 1320), rot=-1.4, push=(1.0, 1.08), dur=D, fy=.45,
                credit_txt="Photo: Shixart1985, CC BY 2.0", treat="muted")
    label_card(cv, W / 2, 1470, "BROKEN GLASS?", eback(pr(t, 5.5, 5.9), 1.3), size=38, tc=INK)

# ---------------------------------------------------------------- 5 the answer: 16 / 7 / 6 of 50
YES = [16, 7, 6]
def s_answer(cv, t, D):
    headline(cv, t, "SAID YES", t0=-.05)
    photo_print(cv, t + .3, film(6.9), box=(330, 440, 750, 755), rot=1.0, push=(1.0, 1.06), dur=D, tape=False,
                credit_txt="Prelinger Archives, public domain")
    if t > .28: stamp_plate(cv, W / 2, 610, "NO BROKEN GLASS", 40, -5, eo(pr(t, .3, .55)))
    cam5 = guided(t, [(1.2, 540, 960, 1.0), (2.0, 470, 950, 1.07), (4.5, 470, 950, 1.07), (5.2, 540, 960, 1.0)])
    old_cam = cv.cam; cv.cam = cam5
    xs = [300, 540, 780]; fills = [(1.39, 2.3), (4.95, 5.4), (5.35, 5.75)]
    for g in range(3):
        qg = eo(pr(t, .9 + g * .1, 1.3 + g * .1))
        if qg <= 0: continue
        cv.text(xs[g], 850, ["SMASHED", "HIT", "NO QUESTION"][g], 26 if g < 2 else 22, [OXBLOOD, DEEP_TEAL, INK2][g], qg, "Black", role="label")
        n_on = int(YES[g] * eo(pr(t, *fills[g])) + .999) if t > fills[g][0] else 0
        for j in range(50):
            c, r = j % 5, j // 5
            x = xs[g] - 64 + c * 32; y = 890 + r * 34
            on = j < n_on
            cv.circ(x, y, 12, fill=GROUP_COL[g] if on else PAPER2, a=qg, outline=None if on else RULE, w=2)
        qn = eback(pr(t, fills[g][1] - .1, fills[g][1] + .3), 1.3)
        if qn > 0:
            cv.text(xs[g], 1285, f"{YES[g]}/50", 58 if g == 0 else 50, [OXBLOOD, DEEP_TEAL, INK2][g], cl(qn), "Black", role="hook")
    cv.cam = old_cam
    source_tag(cv, t - 3.9, "Loftus & Palmer 1974, Table 2", y=1480)

# ---------------------------------------------------------------- 6 why: two sources become one memory
def eye(cv, x, y, s, a):
    pts_top = [(x - 46 * s + 92 * s * i / 16, y - 30 * s * math.sin(math.pi * i / 16)) for i in range(17)]
    pts_bot = [(x + 46 * s - 92 * s * i / 16, y + 30 * s * math.sin(math.pi * i / 16)) for i in range(17)]
    cv.poly(pts_top + pts_bot, SNOW, a=a, outline=INK, w=4)
    cv.circ(x, y, 19 * s, fill=TEAL, a=a); cv.circ(x, y, 8 * s, fill=INK, a=a)
def bubble(cv, x, y, s, a):
    cv.rrect(x - 50 * s, y - 34 * s, x + 50 * s, y + 30 * s, 22 * s, fill=SNOW, a=a, outline=INK, w=4)
    cv.poly([(x - 18 * s, y + 28 * s), (x - 34 * s, y + 52 * s), (x - 2 * s, y + 29 * s)], SNOW, a=a, outline=INK, w=4)
    cv.rect(x - 16 * s, y + 25 * s, x - 2 * s, y + 30 * s, fill=SNOW, a=a)
    for k in (-1, 0, 1): cv.circ(x + k * 24 * s, y - 2 * s, 6 * s, fill=SIGNAL_RED, a=a)
def s_why(cv, t, D):
    headline(cv, t, "TWO SOURCES", t0=-.05)
    bl = eio(pr(t, 4.4, 5.1)); N = 60
    def strand(k, p):
        pts = []
        for i in range(int(N * p) + 1):
            u = i / N
            if k == 0: xs_, ys_ = lerp(170, 540, u), 700 + 90 * u * u
            else: xs_, ys_ = lerp(910, 540, u), 960 - 170 * u * u
            xt = lerp(170, 910, u); yt = 1090 + 34 * math.sin(2 * math.pi * 3.5 * u + (0 if k == 0 else math.pi))
            pts.append((lerp(xs_, xt, bl), lerp(ys_, yt, bl)))
        return pts
    cam6 = guided(t, [(4.3, 540, 960, 1.0), (5.3, 540, 1030, 1.08)])
    old_cam = cv.cam; cv.cam = cam6
    for k, (tt, col) in enumerate(((2.2, TEAL), (3.12, SIGNAL_RED))):
        p = eo(pr(t, tt, tt + .8)) if bl <= 0 else 1.0
        if p > 0:
            pts = strand(k, p)
            if len(pts) > 1:
                cv.line([(x + 4, y + 8) for x, y in pts], SHADOW, 14, .10)
                cv.line(pts, col, 14, 1)
    a1 = eo(pr(t, 2.0, 2.4)) * (1 - bl); a2 = eo(pr(t, 2.95, 3.35)) * (1 - bl)
    eye(cv, 170, 600, 1.0, a1); chip(cv, 170, 520, "SEEN", DEEP_TEAL, a1, tc=SNOW, size=30)
    bubble(cv, 910, 860, 1.0, a2); chip(cv, 910, 770, "TOLD", OXBLOOD, a2, tc=SNOW, size=30)
    if bl > 0:
        eye(cv, 230, 960, .7, bl); bubble(cv, 850, 950, .7, bl)
    cv.cam = old_cam
    label_card(cv, W / 2, 1260, "ONE MEMORY", eback(pr(t, 5.04, 5.45), 1.3), size=46, tc=INK)
    source_tag(cv, t - 1.0, "Loftus & Palmer 1974, p. 588", y=1480)
    maker_mark(cv, W - 64, 1585, .8)

# ---------------------------------------------------------------- 7 payoff + end card
def s_payoff(cv, t, D):
    E = D - 2.6                                   # end card starts here; scene content is gone by then
    fo = 1 - eio(pr(t, E - .75, E - .1))
    pc = eo(pr(t, 2.45, 3.4))
    photo_print(cv, t, film(6.9), box=(150, 470, 930, 1055), rot=-1.0, push=(1.0, 1.06), dur=D, a=fo,
                frame=crack_fn(pc, seed=5), credit_txt=FILM_CREDIT)
    q = eo(pr(t, .7, 1.0)) * fo
    if q > 0:
        cv.text(W / 2, 1200, "RECORDING", 64, INK, q, "Black", role="label")
        ps = eo(pr(t, .95, 1.4))
        if ps > 0: cv.line([(330, 1215), (330 + 420 * ps, 1180)], SIGNAL_RED, 9, q)
    for j, (txt, tt) in enumerate((("WITNESSES", 1.55), ("COURTS", 1.85))):
        chip(cv, 380 + j * 330, 1305, txt, [DEEP_TEAL, OXBLOOD][j], eback(pr(t, tt, tt + .4), 1.3) * fo, tc=SNOW, size=32)
    kinetic(cv, t, 1450, "?", 120, OXBLOOD, 2.42, "Black", .03, role="label") if fo > .5 else None
    if t > E: end_card(cv, t - E)

SCENES = [s_hook, s_who, s_verb, s_staged, s_test2, s_answer, s_why, s_payoff]
