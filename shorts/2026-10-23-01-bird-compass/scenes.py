# ===== scenes.py (Short). One scene per script line. Replace these examples; keep the API.
# fn(cv, t, D): t = seconds into the scene, D = scene length (scene-locked: the longest of EN/UR/PS sets it).
# Language-neutral: on-screen text only numbers, years, names, units, English terms, 1-3 word labels.
# Layout (s7): headline y 280-400 (headline()), stage y 420-1440 (STAGE), nothing key below 1600 or within 60 px
# of the sides; watermark corners (64,110) (W-274,110) (64,1340) stay clear. Full API: engine/README.md.
IMG = lambda f: os.path.join(HERE, "img", f)
CAM = {}
def load_imgs():
    # heavy, per-process setup (camera layers etc.). Images used via photo_print(path) are loaded lazily.
    # CAM["lab"] = camera.Parallax(IMG("lab.jpg"), bands=[(.7, .05)])
    pass

TRANS = {1: "ink", 2: "mask"}          # transition INTO scene i: rise (default) | ink | mask | page | match | fade
GROUND = {}                            # {i: "night"} for space / deep-dark subjects
SFX = [(0, .1, "low_swell", -24)]      # (scene, local t, name, dB re voice)

def s_hook(cv, t, D):
    # frame 1 already moving (HOOK_PRE); a big number or keyword readable muted within 2 s
    headline(cv, t, "THE HOOK", t0=-.2)
    numeral_hook(cv, t, "17.5%", unit="of something", y=820, edge=False, col=OXBLOOD)
    source_tag(cv, t - 1.2, "Journal, 2026")

def s_explain(cv, t, D):
    headline(cv, t, "HOW IT WORKS")
    E = Engraving()
    E.fill(circle_pts(540, 860, 220), PAPER2).shade(circle_pts(540, 860, 220, 120, 300), 45)
    E.circle(540, 860, 220).arrow(860, 600, 700, 720).label(860, 560, "the part")
    E.draw(cv, pr(t, .2, 2.6))
    chip(cv, 540, 1300, "KEY LABEL", ACCENT, eo(pr(t, 2.4, 2.8)))

def s_payoff(cv, t, D):
    headline(cv, t, "THE PAYOFF")
    counter(cv, t, 1932, y=820, fmt=lambda v: str(v), start=1900, dur=1.4, t0=.3, unit="the year")

SCENES = [s_hook, s_explain, s_payoff]
# one function per line of script.json: extend or trim SCENES to match.
