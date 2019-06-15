from pyx import *
import random

c = canvas.canvas()
c.stroke(path.rect(0, 0, 200, 200))
for x in range(1, 100):
    start_point_x = random.randint(1, 199)
    start_point_y = random.randint(1, 199)
    end_point_x = start_point_x + random.randrange(-50, 50)
    end_point_y = start_point_y + random.randrange(-50, 50)
    print start_point_x, start_point_y, end_point_x, end_point_y
    c.stroke(path.line(start_point_x, start_point_y, end_point_x, end_point_y), [style.linewidth(0.25)])
c.writePDFfile("path/1")
