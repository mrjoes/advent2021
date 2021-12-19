def rotateX(n):
    return set([(c[0], c[2], -c[1]) for c in n])

def rotateY(n):
    return set([(c[2], c[1], -c[0]) for c in n])

def rotateZ(n):
    return set([(c[1], -c[0], c[2]) for c in n])


with open('input19.txt') as fp:
    def read_scanner():
        l = fp.readline()
        if not l:
            return None

        s = set()

        while True:
            l = fp.readline().strip()
            if not l:
                break
            s.add(tuple([int(n) for n in l.split(',')]))

        return s

    scanners = []

    while True:
        s = read_scanner()
        if not s:
            break

        scanners.append(s)

    #print(scanners)

    known = set(scanners[0])

    remaining = scanners[1:]

    distances = [(0, 0, 0)]

    while remaining:
        print(len(remaining), len(known))
        for s in list(remaining):
            k = list(s)

            found = False

            for nx in range(4):
                if found:
                    break

                k = rotateX(k)

                for ny in range(4):
                    if found:
                        break

                    k = rotateY(k)

                    for nz in range(4):
                        if found:
                            break

                        k = rotateZ(k)

                        for c in set(known):
                            if found:
                                break

                            for d in k:
                                dx, dy, dz = (d[0] - c[0], d[1] - c[1], d[2] - c[2])

                                nf = set((o[0] - dx, o[1] - dy, o[2] - dz) for o in k)

                                if len(known & nf) >= 12:
                                    known |= nf
                                    distances.append((dx, dy, dz))

                                    found = True
                                    break

            if found:
                remaining.remove(s)

    print(distances)

    md = 0
    for a in distances:
        for b in distances:
            if a != b:
                d = sum(abs(a-b) for a, b in zip(a, b))
                if d > md:
                    md = d

    print(md)

    #print(sorted(known, key=lambda c: c[0]))
    print(len(known))
