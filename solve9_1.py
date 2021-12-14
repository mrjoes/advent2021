with open('input9t.txt') as fp:
    arr = [[int(c) for c in l.strip()] for l in fp.readlines()]

    w = len(arr[0])
    h = len(arr)

    candidates = []

    def get(x, y):
        if x >= 0 and x < w and y >= 0 and y < h:
            return arr[y][x]

        return None

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            v = get(x, y)
            vals = [n for n in (get(x, y - 1), get(x + 1, y), get(x, y + 1), get(x - 1, y)) if n is not None]
            if min(vals) > v:
                candidates.append(v)

    print(sum(n + 1 for n in candidates))
