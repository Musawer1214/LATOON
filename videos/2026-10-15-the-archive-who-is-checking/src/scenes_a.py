"""scenes_a.py (long). One function per scene name in timeline.SCENE_PARAS: scene_<name>(cv, t, S, T).
Beat(S)(i, f) = time f through paragraph i; Beat(S).kw(i, 'word') = when a word is spoken (lock visuals to it).
Long videos: no burned captions (soft SRT per language), minimal on-screen text, several real images per minute, a chapter tag
with each chapter, a cold open within 15 s, title card at ~30-40 s, end card with the lower 2/3 clear."""
from head import *
GROUND = {}                                   # {"space_scene": "night"}

def scene_hook(cv, t, S, T):
    B = Beat(S)
    # fullphoto(cv, "lab", t / S["dur"], bands=[(.75, .05)])          # 2.5D push on a real photo (img/lab.jpg)
    numeral_hook(cv, t, "1 QUESTION", y=470, edge=False, col=OXBLOOD)
    lower_third(cv, t - 2, "Name Surname", "Role, Institution", dur=5)

def scene_title(cv, t, S, T):
    chapter_card(cv, t, 1, "Chapter Title", sub="one-line promise")

def scene_body(cv, t, S, T):
    chapter_tag(cv, 1, eo(pr(t, 0, .6)), "Chapter title")
    # photo_print(cv, t, img_path("object"), credit_txt="Author, CC BY 4.0")
    timeline(cv, t - 1, [(1950, "first"), (2017, "second"), (2022, "third")], active=2)
    source_tag(cv, t - 2, "Journal, 2026")

def scene_end(cv, t, S, T):
    end_card(cv, t)
