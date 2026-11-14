"""Half-scale desktop sheet: 2 columns of 683px, each column covering 2800px of page. usage: dsheet.py shot.png"""
import sys
from PIL import Image
f = sys.argv[1]; sc = float(sys.argv[2]) if len(sys.argv) > 2 else .5; ch = int(sys.argv[3]) if len(sys.argv) > 3 else 2800
im = Image.open(f); W, H = im.size
im = im.resize((int(W * sc), int(H * sc)), Image.LANCZOS); W, H = im.size; ch = int(ch * sc)
n = (H + ch - 1) // ch; k = 0
for st in range(0, n, 2):
    sh = Image.new("RGB", (2 * W + 10, ch), (255, 0, 255))
    for c in range(2):
        i = st + c
        if i < n: sh.paste(im.crop((0, i * ch, W, min(H, (i + 1) * ch))), (c * (W + 10), 0))
    sh.save(f.replace(".png", f"-ds{k}.png")); k += 1
print(k)
