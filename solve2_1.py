with open('input2.txt') as fp:
    lines = fp.readlines()

    h, d = 0, 0

    for l in lines:
        op, n = l.split(' ')

        if op == 'forward':
            h += int(n)
        elif op == 'down':
            d += int(n)
        elif op == 'up':
            d -= int(n)

    print(h * d)
