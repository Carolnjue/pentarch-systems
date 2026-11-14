"""Cut a full-page screenshot into readable segments. usage: python3 crop.py shot.png [segment_height]"""
import sys
from PIL import Image
f = sys.argv[1]; sh = int(sys.argv[2]) if len(sys.argv) > 2 else 1100
im = Image.open(f); W, H = im.size
n = 0
for y in range(0, H, sh):
    im.crop((0, y, W, min(H, y + sh))).save(f.replace('.png', f'-s{n}.png')); n += 1
print(n, 'segments', W, H)
