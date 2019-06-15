from pyx import *
import random

NOISE = 1
c = canvas.canvas()

curr_x_pts = []
paths = []
for i in range (0, 299):
	curr_x_pts.append(random.uniform(-NOISE / 100, NOISE / 100))
min_x_pt = min(curr_x_pts)
max_x_pt = max(curr_x_pts)
while max_x_pt < 100:
    curr_path = path.path(path.moveto(curr_x_pts[0], 0))
    next_x_pts = []
    for y in range(0, 100):
    	next_x = max(curr_x_pts[y], curr_x_pts[y] + 1 + random.uniform(-NOISE, NOISE)/ 20)
    	next_x_pts.append(next_x)
        curr_path.append(path.lineto(next_x, y))
    paths.append(curr_path)
    curr_x_pts = next_x_pts
    max_x_pt = max(max_x_pt, max(next_x_pts))
    print max_x_pt
c.fill(path.rect(min_x_pt, 0, max_x_pt + 25, 50), [color.rgb.white])
for path in paths:
	c.stroke(path, [deformer.smoothed(1.0), style.linewidth(0.2), color.rgb.black])

c.writePDFfile("trace-28")