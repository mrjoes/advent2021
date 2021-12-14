from functools import reduce

with open('input9.txt') as fp:
    arr = [[int(c) for c in l.strip()] for l in fp.readlines()]

    w = len(arr[0])
    h = len(arr)

    candidates = {}
    queue = []

    def get(x, y):
        if x >= 0 and x < w and y >= 0 and y < h:
            return arr[y][x]

        return 9

    def cell(c, x, y, v):
        n = get(x, y)
        if n != 9 and n > v and (x, y) not in visited:
            visited.add((x, y))
            candidates[c] += 1
            queue.append((n, (x, y)))

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            v = get(x, y)
            vals = [n for n in (get(x, y - 1), get(x + 1, y), get(x, y + 1), get(x - 1, y)) if n is not None]
            if min(vals) > v:
                c = (x, y)
                candidates[c] = 1
                queue.append((v, (x, y)))

                visited = set()

                while queue:
                    v, (nx, ny) = queue.pop()

                    cell(c, nx, ny - 1, v)
                    cell(c, nx + 1, ny, v)
                    cell(c, nx, ny + 1, v)
                    cell(c, nx - 1, ny, v)

    items = sorted((y for x, y in candidates.items()), key=lambda v: -v)[:3]
    print(reduce(lambda a, b: a * b, items))
