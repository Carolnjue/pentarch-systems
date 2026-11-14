"""Tile a tall narrow screenshot into side-by-side columns. usage: python3 sheet.py shot.png [colheight] [cols]"""
import sys
from PIL import Image
f = sys.argv[1]; ch = int(sys.argv[2]) if len(sys.argv) > 2 else 1500; cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
im = Image.open(f); W, H = im.size
n = (H + ch - 1) // ch; k = 0
for start in range(0, n, cols):
    sheet = Image.new("RGB", (cols * (W + 12), ch), (255, 0, 255))
    for c in range(cols):
        i = start + c
        if i >= n: break
        sheet.paste(im.crop((0, i * ch, W, min(H, (i + 1) * ch))), (c * (W + 12), 0))
    sheet.save(f.replace(".png", f"-sheet{k}.png")); k += 1
print(k, "sheets")
