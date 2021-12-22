import re


#/usr/bin/env python3
with open('input22t.txt') as fp:
    pos = [re.match('(\w+) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)', l).groups() for l in fp.readlines()]
    pos = [(n[0], int(n[1]), int(n[2]) + 1, int(n[3]), int(n[4]) + 1, int(n[5]), int(n[6]) + 1) for n in pos]

    s = set()

    for p in pos:
        a, c = p[0], p[1:]

        for x in range(c[0], c[1]):
            for y in range(c[2], c[3]):
                for z in range(c[4], c[5]):
                    if a == 'on':
                        s.add((x, y, z))
                    else:
                        if (x, y, z) in s:
                            s.remove((x, y, z))

        print(p, len(s))
