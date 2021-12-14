with open('input2.txt') as fp:
    lines = fp.readlines()

    h, d, a = 0, 0, 0

    for l in lines:
        op, n = l.split(' ')

        if op == 'forward':
            h += int(n)
            d += int(n) * a
        elif op == 'down':
            a += int(n)
        elif op == 'up':
            a -= int(n)

    print(h * d)
