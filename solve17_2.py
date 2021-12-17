import re
from math import copysign

with open('input17.txt') as fp:
    x1, x2, y1, y2 = [int(n) for n in re.match('target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)', fp.readline()).groups()]

    if y1 > y2:
        y1, y2 = y2, y1

    sx = int(copysign(1, x1))

    velocities = set()

    for dy in range(-abs(y1) * 3, abs(y1) * 3):
        for dx in range(1, abs(x2) * 2):
            x, y = 0, 0

            nx, ny = dx, dy

            found = False

            my = 0

            while x < x2 and y > y1:
                x += nx * sx
                y += ny

                if y > my:
                    my = y

                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    velocities.add((dx, dy))
                    break

                if nx != 0:
                    nx -= 1 * sx
                ny -= 1

    print(len(velocities))
