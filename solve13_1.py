import re

def printm(arr):
    w = 0
    h = 0

    for x, y in arr:
        if x >= w:
            w = x + 1
        if y >= h:
            h = y + 1

    p = [[0] * w for n in range(h)]

    for x, y in arr:
        p[y][x] = 1

    for l in p:
        print(''.join('1' if k == 1 else ' ' for k in l))
    print()


with open('input13.txt') as fp:
    dots = set()

    while True:
        l = fp.readline().strip()
        if not l:
            break

        x, y = [int(n) for n in l.split(',')]
        dots.add((x, y))

    folds = []
    while True:
        l = fp.readline().strip()
        if not l:
            break

        folds.append(tuple(re.match('fold along (\w)=(\d+)', l).groups()))

    def fold_x(n):
        global dots
        coords = [p for p in dots if p[0] > n]
        flipped = [(n - (x - n), y) for x, y in coords]
        dots -= set(coords)
        dots |= set(flipped)

    def fold_y(n):
        global dots
        coords = [p for p in dots if p[1] > n]
        flipped = [(x, n - (y - n)) for x, y in coords]
        dots -= set(coords)
        dots |= set(flipped)

    for f, n in folds:
        if f[0] == 'x':
            fold_x(int(n))
        else:
            fold_y(int(n))

        #break

    printm(dots)
    print(len(dots))
