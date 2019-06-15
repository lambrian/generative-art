from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 600
HEIGHT = 30
INIT_M = 0.5
RATIO = .01

c.stroke(path.rect(0, 0, WIDTH, HEIGHT))

r = path.rect(1, 1, WIDTH - 1, HEIGHT - 4)
c.stroke(r,[style.linewidth(0.4)])
points_list = []
for x in range(1, WIDTH - 1, 2):
    for y in range(1, HEIGHT - 1, 2):
        #print '%d - %f' % (x, INIT_M**(x*RATIO))
        if random.random() < INIT_M**(x*RATIO):
            # circle = path.circle(x, y, 0.5)
            # c.fill(circle)
            eligible_points = filter(
                    lambda point: point[0] < x and abs(point[1] - y) > HEIGHT/3,
                    points_list
            )[-30:]
            points_to_connect = random.sample(eligible_points, min(len(eligible_points), random.choice(range(1, 2))))
            print '%d %d' % (x, y)
            print points_to_connect
            for point in points_to_connect:
                c.stroke(
                    path.line(x, y, point[0], point[1]),
                    [style.linecap.round, style.linewidth(0.4)],
               )
            points_list.append((x, y))
c.writePDFfile("poly-2-%d-%d-%d" % (WIDTH, HEIGHT, seed));
