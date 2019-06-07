from pyx import *
import random

c = canvas.canvas()
c.stroke(path.rect(0, 0, 300, 300))
for x in range(1, 300, 5):
    curr_path = path.path(path.moveto(x, 0))
    for y in range(1, 300):
        curr_path.append(path.lineto(x + random.randrange(-5, 5), y))
    c.stroke(curr_path, [deformer.smoothed(1.0)])
c.writePDFfile("waves-41")