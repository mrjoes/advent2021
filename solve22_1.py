import re


with open('input22.txt') as fp:
    pos = [re.match('(\w+) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)', l).groups() for l in fp.readlines()]
    pos = [(n[0], int(n[1]), int(n[2]) + 1, int(n[3]), int(n[4]) + 1, int(n[5]), int(n[6]) + 1) for n in pos]

    def inside(a, b):
        r = (a[0] >= b[0] and a[0] <= b[1] and
             a[1] >= b[0] and a[1] <= b[1] and
             a[2] >= b[2] and a[2] <= b[3] and
             a[3] >= b[2] and a[3] <= b[3] and
             a[4] >= b[4] and a[4] <= b[5] and
             a[5] >= b[4] and a[5] <= b[5])
        #print('ins', a, b, r)
        return r

    def overlaps(a, b):
        r =  (max(a[0], b[0]) <= min(a[1], b[1]) and
              max(a[2], b[2]) <= min(a[3], b[3]) and
              max(a[4], b[4]) <= min(a[5], b[5]))
        #print('ovr', a, b, r)
        return r

    def split(c, n, v):
        if c[n * 2] >= v or c[n * 2 + 1] <= v:
            return []

        r1, r2 = list(c), list(c)
        r1[n * 2 + 1] = v
        r2[n * 2] = v

        res = set()
        if r1[n * 2] <= r1[n * 2 + 1]:
            res.add(tuple(r1))
        if r2[n * 2] <= r2[n * 2 + 1]:
            res.add(tuple(r2))

        return res

    def count(cubes):
        return sum((c[1] - c[0]) * (c[3] - c[2]) * (c[5] - c[4]) for c in cubes)

    def carve(cubes, a):
        res = set()

        for c in cubes:
            if inside(c, a):
                continue

            if overlaps(c, a):
                s = set((c,))

                n = 0

                while n < 6:
                    #print(n, s)
                    for k in s:
                        b = split(k, n // 2, a[n])
                        #print(k, n // 2, a[n], b)
                        if b:
                            s.remove(k)
                            s |= b
                            break
                    else:
                        n += 1

                b = set(k for k in s if not inside(k, a))

                res |= b
            else:
                res.add(c)

        return res

    cubes = set()

    for i, p in enumerate(pos):
        a, c = p[0], p[1:]

        #if not inside(c, (-50, 51, -50, 51, -50, 51)):
        #    continue

        cubes = carve(cubes, c)

        if a == 'on':
            cubes.add(c)

        print(i, p, count(cubes))

    l = 0
    for c in cubes:
        l += (c[1] - c[0]) * (c[3] - c[2]) * (c[5] - c[4])

    print(len(cubes), l)
