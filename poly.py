from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 600
HEIGHT = 50
DENSITY = 12
RADIUS = 0.5
r = path.rect(0, 0, WIDTH, HEIGHT)
c.stroke(r)

x = WIDTH
points = {}
points_list = []
connected_points = {}
var_density = 100
while x > 1:
    used_y = 0
    while used_y < HEIGHT:
        used_y += random.randrange(DENSITY/2, DENSITY)
        rc1 = rng.choice(range(int(WIDTH)))
        rc2 = rng.choice(range(int(WIDTH)))
        if rc1 > x and rc2 > x:
            circle = path.circle(x, used_y, 0.5)
            c.fill(circle)
            points.setdefault(x, []).append(used_y)
            # over the last 10 points created
            eligible_points = filter(lambda point: point[0] < x + DENSITY * 4 and point[0] > x + DENSITY, points_list)
            points_to_connect = random.sample(eligible_points, min(len(eligible_points), min(2, len(eligible_points)/3 + 1)))
            for point in points_to_connect:
                num_inputs = connected_points.setdefault(point, 0)
                if num_inputs < 2:
                    c.stroke(
                        path.line(x, used_y, point[0], point[1]),
                        [style.linecap.round, style.linewidth(0.25)],
                   )
                connected_points[point] = num_inputs + 1
            points_list.append((x, used_y))
        #used_y += random.randrange(4, 15)
    var_density -= 1
    x -= var_density


c.writePDFfile("poly-%d-%d-%f-%f-%d" % (WIDTH, HEIGHT, DENSITY, RADIUS, seed));
