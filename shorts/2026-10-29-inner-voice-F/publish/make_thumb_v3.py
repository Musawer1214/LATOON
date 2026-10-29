"""Hidden Mind thumbnail v3 (owner-approved 2026-10-30): realistic full-frame background + locked template text/stamp/mark."""
import sys; sys.path.insert(0,'/workspace/latoon/branding/thumb_template')
import latoon_thumb as T
from PIL import Image, ImageChops
bg=Image.open(sys.argv[1] if len(sys.argv)>1 else 'hm_thumb_bg_real.png').convert('RGB')
s=1080/bg.height; bg=bg.resize((int(bg.width*s),1080),Image.LANCZOS)
im=Image.new('RGB',(1920,1080),(6,14,32)); im.paste(bg,(1920-bg.width,0))
im=T.pop(im).convert('RGBA')
n=Image.effect_noise((1920,1080),40).convert('RGB'); im=Image.blend(im.convert('RGB'),ImageChops.overlay(im.convert('RGB'),n),.08).convert('RGBA')
yy=T.text(im,90,250,'NO INNER',T.WHITE,180,maxw=900); T.text(im,90,yy,'VOICE?',T.MOODS['curious']['l2'],180,maxw=900)
T.stamp(im,100,700,'ARE YOU ONE?',T.MOODS['curious']['stamp'])
T.mark(im,1920-330,1080-115,58)
im.convert('RGB').resize((1280,720),Image.LANCZOS).save('HM_thumb_EN_1280_v3_real.png',optimize=True)
