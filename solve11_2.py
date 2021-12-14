def printm(m):
    for l in m:
        print(''.join('%2d' % k for k in l))
    print()


with open('input11.txt') as fp:
    arr = [[int(c) for c in l.strip()] for l in fp.readlines()]

    h = len(arr)
    w = len(arr[0])

    step = 0

    for n in range(1000):
        flashes = []

        print(n)

        count = 0

        for y, l in enumerate(arr):
            for x, c in enumerate(l):
                arr[y][x] = c + 1

                if c + 1 > 9:
                    flashes.append((y, x))

        while flashes:
            printm(arr)

            y, x = flashes.pop()
            if arr[y][x] == 0:
                continue

            arr[y][x] = 0
            count += 1

            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if i >= 0 and i < h and j >= 0 and j < w:
                        if arr[i][j] != 0:
                            arr[i][j] += 1

                            if arr[i][j] > 9:
                                flashes.append((i, j))

        #printm(arr)
        if count == 100:
            step = n + 1
            break

    print(step)
