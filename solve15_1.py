import heapq

def printm(m):
    for l in m:
        print(''.join('%3d' % k for k in l))
    print()


with open('input15.txt') as fp:
    m = [[int(n) for n in k.strip()] for k in fp.readlines()]

    w = len(m[0])
    h = len(m)

    r = [[0] * w for n in range(h)]

    queue = [(0, (0, 0))]

    def add(x, y, nw):
        if x >= 0 and x < w and y >= 0 and y < h:
            if not r[y][x] or nw < r[y][x]:
                heapq.heappush(queue, (nw, (x, y)))

    c = 0

    while queue:
        v, (x, y) = heapq.heappop(queue)

        nw = v + m[y][x]
        if not r[y][x] or nw < r[y][x]:
            r[y][x] = nw

            add(x, y - 1, nw)
            add(x + 1, y, nw)
            add(x, y + 1, nw)
            add(x - 1, y, nw)

        if not (c % 100000):
            print(c, len(queue))
        c += 1

    #printm(r)
    print(r[-1][-1] - r[0][0])
