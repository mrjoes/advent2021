import re
from math import copysign

with open('input17t.txt') as fp:
    x1, x2, y1, y2 = [int(n) for n in re.match('target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)', fp.readline()).groups()]

    sx = int(copysign(1, x1))

    maxy = 0

    for dy in range(1, abs(y1)):
        for dx in range(1, abs(x1)):
            x, y = 0, 0

            nx, ny = dx, dy

            found = False

            my = 0

            while x < x2 and y > y2:
                x += nx * sx
                y += ny

                if y > my:
                    my = y

                if x >= x1 and x < x2 and y >= y1 and y < y2:
                    found = True
                    break

                if nx != 0:
                    nx -= 1 * sx
                ny -= 1

                #print(x, y, dx, dy)

            #print(found)

            if found and my > maxy:
                maxy = my

    print(maxy)
