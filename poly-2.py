from pyx import *
import random
import sys

SEED = 3805268403075380010

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(SEED or seed)

WIDTH = 600
HEIGHT = 30
INIT_M = 0.65
RATIO = .009
PRINT_DOTS = 0
PRINT_LINES = True

c.stroke(path.rect(0, 0, WIDTH, HEIGHT))

r = path.rect(1, 1, WIDTH - 1, HEIGHT - 4)
c.stroke(r,[style.linewidth(0.4)])
points_list = []
for x in range(1, WIDTH*2 - 1, 2):
    used_x = float(x) / 2
    for y in range(1, HEIGHT - 1, 2):
        if random.random() < INIT_M**(x*RATIO) or y == HEIGHT - 1:
            if PRINT_DOTS:
                circle = path.circle(used_x, y, 0.5)
                c.fill(circle)
            if PRINT_LINES:
                eligible_points = filter(
                        lambda point: (point[0] < used_x - 10 or used_x < 15) and point[0] > used_x - WIDTH / 13 and abs(point[1] - y) > 0 and abs(point[1] - y) < HEIGHT / 2,
                        points_list
                )[-30:]
                points_to_connect = random.sample(eligible_points, min(len(eligible_points), random.choice(range(1, 2))))
                for point in points_to_connect:
                    c.stroke(
                        path.line(used_x, y, point[0], point[1]),
                        [style.linecap.round, style.linewidth(0.4)],
                   )
                points_list.append((used_x, y))

for y in range(1, HEIGHT - 1, 2):
    if random.random() < INIT_M**(300*RATIO) or y == HEIGHT - 1:
        eligible_points = filter(
                lambda point: (point[0] < used_x - 10 or used_x < 15) and point[0] > used_x - WIDTH / 15 and abs(point[1] - y) > 0 and abs(point[1] - y) < HEIGHT / 2,
                points_list
        )[-30:]
        points_to_connect = random.sample(eligible_points, min(len(eligible_points), random.choice(range(1, 2))))
        for point in points_to_connect:
            c.stroke(
                path.line(WIDTH, y, point[0], point[1]),
                [style.linecap.round, style.linewidth(0.4)],
           )

c.writePDFfile("output/poly-2/poly-2-%d-%d-%d" % (WIDTH, HEIGHT, seed));
