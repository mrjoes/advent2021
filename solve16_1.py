from functools import reduce

with open('input16.txt') as fp:
    s = ''.join([format((ord(n) - ord('0')) if n <= '9' else (ord(n) - ord('A')) + 10, '04b') for n in fp.readline().strip()])

    def num(v):
        return reduce(lambda a, b: a << 1 | int(b), v, 0)

    def readn(p, n):
        return num(s[p:p+n]), p+n

    ver = 0

    def read_pack(p):
        global ver

        v, p = readn(p, 3)
        t, p = readn(p, 3)

        ver += v

        if t == 4:
            n = 0
            b = 1
            while b:
                b, p = readn(p, 1)
                k, p = readn(p, 4)
                n = n << 4 | k
            #print(n)
        else:
            lt, p = readn(p, 1)

            if lt == 0:
                # Length
                l, p = readn(p, 15)
                e = p + l

                while p < e:
                    p = read_pack(p)
            else:
                # Packet count
                l, p = readn(p, 11)
                while l > 0:
                    p = read_pack(p)
                    l -= 1

        return p

    read_pack(0)

    print(ver)
