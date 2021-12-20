def printm(img):
    minx = min(c[0] for c in img)
    maxx = max(c[0] for c in img)
    miny = min(c[1] for c in img)
    maxy = max(c[1] for c in img)

    for y in range(maxy - miny + 1):
        r = []
        for x in range(maxx - miny + 1):
            if (x + minx, y + miny) in img:
                r.append('#')
            else:
                r.append('.')

        print(''.join(r))

with open('input20.txt') as fp:
    rules = [1 if c == '#' else 0 for c in fp.readline().strip()]
    fp.readline()
    print(len(rules))

    img = set()

    y = 0
    while True:
        l = fp.readline().strip()
        if not l:
            break

        for x, c in enumerate(l):
            if c == '#':
                img.add((x, y))

        y += 1

    def enhance(g, z):
        g = set(g)

        res = set()

        minx = min(c[0] for c in g) - 1
        maxx = max(c[0] for c in g) + 1
        miny = min(c[1] for c in g) - 1
        maxy = max(c[1] for c in g) + 1

        if z:
            for x in range(minx - 1, maxx + 2):
                g.add((x, miny))
                g.add((x, miny - 1))
                g.add((x, maxy))
                g.add((x, maxy + 1))

            for y in range(miny - 1, maxy + 2):
                g.add((minx, y))
                g.add((minx - 1, y))
                g.add((maxx, y))
                g.add((maxx + 1, y))

        for j in range(miny, maxy + 1):
            for i in range(minx, maxx + 1):
                acc = 0

                for y in range(j - 1, j + 2):
                    for x in range(i - 1, i + 2):
                        acc = acc << 1

                        if (x, y) in g:
                            acc |= 1
                        else:
                            acc |= 0

                if rules[acc]:
                    res.add((i, j))

        return res, z

    k = img
    z = 0
    for n in range(50):
        k, z = enhance(k, z)

        if rules[0]:
            z = rules[0] if z != rules[0] else rules[9]

    print(len(k))
