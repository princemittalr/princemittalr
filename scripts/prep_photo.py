"""
Prepare the profile photo for a clean ink-on-paper ASCII portrait:
  1. cut the subject out of the plain backdrop (OpenCV GrabCut, no model download)
  2. bilateral-smooth skin and shirt texture while keeping edges sharp
  3. stretch tones so skin lands light and hair / beard stay dark
  4. darken the outlines (difference-of-gaussians ridges + Canny edges): eyes,
     glasses frame, brows, jaw and collar are thin strokes that plain luminance
     averaging washes out at ASCII resolution
  5. composite onto white and crop square around the head

Output: source-prepped.png (grayscale), consumed by make_ascii_svg.py.
Needs opencv-python, numpy and Pillow (run locally only when the photo changes).

    python scripts/prep_photo.py [input.png] [output.png]
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.png")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

LINE_WEIGHT = 0.7   # how hard soft ridges are pushed toward black
EDGE_WEIGHT = 0.6   # how hard crisp edges (glasses, eyes, collar) are pushed

rgb = np.array(Image.open(INP).convert("RGB"))
H, W = rgb.shape[:2]
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

# 1. GrabCut seeded with a box around the person (photo is a centred head-and-shoulders shot)
mask = np.zeros((H, W), np.uint8)
rect = (int(W * 0.08), int(H * 0.08), int(W * 0.84), int(H * 0.92))
bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(bgr, mask, rect, bgd, fgd, 6, cv2.GC_INIT_WITH_RECT)
alpha = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
alpha = cv2.morphologyEx(alpha, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
# keep the largest blob only
n, lab, stats, _ = cv2.connectedComponentsWithStats(alpha)
if n > 1:
    big = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    alpha = np.where(lab == big, 255, 0).astype(np.uint8)

gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
# local contrast so hair keeps its strands instead of collapsing to one dark block
gray = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8)).apply(gray)

# 2. smooth texture, keep edges
smooth = gray
for _ in range(3):
    smooth = cv2.bilateralFilter(smooth, 9, 40, 9)

# 3. tone stretch over the subject only
lo, hi = np.percentile(smooth[alpha > 128], [6, 70])
tone = np.clip((smooth.astype(np.float32) - lo) / (hi - lo), 0, 1)

# 4. outlines
fine = cv2.GaussianBlur(smooth, (0, 0), 1.6).astype(np.float32)
coarse = cv2.GaussianBlur(smooth, (0, 0), 6).astype(np.float32)
ridges = np.clip((coarse - fine) / 30.0, 0, 1)
edges = cv2.Canny(cv2.GaussianBlur(smooth, (0, 0), 1.2), 30, 80)
edges = cv2.GaussianBlur(cv2.dilate(edges, np.ones((2, 2), np.uint8)).astype(np.float32) / 255.0, (0, 0), 1.2)
out = np.clip(tone - LINE_WEIGHT * ridges - EDGE_WEIGHT * edges, 0, 1)

# silhouette outline so the head and shoulders read as a shape
sil = cv2.morphologyEx(alpha, cv2.MORPH_GRADIENT, np.ones((5, 5), np.uint8)).astype(np.float32) / 255.0
out = np.clip(out - 0.8 * cv2.GaussianBlur(sil, (0, 0), 1.0), 0, 1) * 255

# 5. paste onto white, square crop around the head (top of hair to just under the collar)
m = cv2.GaussianBlur(alpha.astype(np.float32) / 255.0, (0, 0), 1.0)
out = out * m + 255.0 * (1.0 - m)

ys, xs = np.where(alpha > 20)
top = ys.min()
side = int(H * 0.60)
cx = int(np.median(xs[ys < top + side * 0.6]))
y0, x0 = max(top - int(side * 0.05), 0), cx - side // 2
canvas = np.full((side, side), 255, np.uint8)
sx0, sy0 = max(x0, 0), y0
sx1, sy1 = min(x0 + side, W), min(y0 + side, H)
canvas[sy0 - y0:sy1 - y0, sx0 - x0:sx1 - x0] = out[sy0:sy1, sx0:sx1].astype(np.uint8)

Image.fromarray(canvas, mode="L").save(OUT)
print("wrote", OUT, canvas.shape)
