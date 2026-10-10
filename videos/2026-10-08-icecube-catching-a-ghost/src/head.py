import math, os, io, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import aggdraw
W, H, FPS = 1920, 1080, 30
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_DIR = "/workspace/latoon/template/inter/extras/ttf"
# ---------------- palette: warm editorial paper + ice
PAPER = (239, 232, 217); PAPER2 = (229, 220, 201); PAPER3 = (216, 205, 184)
INK = (40, 35, 32); INK2 = (88, 79, 70); MUT = (146, 135, 120); RULE = (205, 194, 173)
SNOW = (249, 247, 241); ICE = (219, 229, 229); ICE2 = (186, 205, 208); ICE3 = (140, 165, 172); ICE4 = (92, 116, 126)
DEEP = (58, 74, 84)
TERRA = (188, 84, 54); TERRA2 = (222, 150, 120); OCHRE = (206, 150, 56); OCHRE2 = (232, 200, 140)
OLIVE = (112, 122, 82); PLUM = (116, 74, 92); SKIN = (222, 178, 146); SKIN2 = (196, 146, 114); NAIL = (240, 206, 190)
CHER = (74, 122, 176); CHER2 = (152, 182, 212); CHER3 = (206, 222, 236)
LOGO = (255, 77, 0)
BG0 = PAPER
