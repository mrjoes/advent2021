from functools import reduce

with open('input16.txt') as fp:
    s = ''.join([format((ord(n) - ord('0')) if n <= '9' else (ord(n) - ord('A')) + 10, '04b') for n in fp.readline().strip()])

    def num(v):
        return reduce(lambda a, b: a << 1 | int(b), v, 0)

    def readn(p, n):
        return num(s[p:p+n]), p+n

    def run_pack(p):
        v, p = readn(p, 3)
        t, p = readn(p, 3)

        if t == 4:
            n = 0
            b = 1
            while b:
                b, p = readn(p, 1)
                k, p = readn(p, 4)
                n = n << 4 | k
            #print(n)

            return p, n
        else:
            lt, p = readn(p, 1)

            res = []

            if lt == 0:
                # Length
                l, p = readn(p, 15)
                e = p + l

                while p < e:
                    p, k = run_pack(p)
                    res.append(k)
            else:
                # Packet count
                l, p = readn(p, 11)
                while l > 0:
                    p, k = run_pack(p)
                    res.append(k)
                    l -= 1

            if t == 0:
                return p, reduce(lambda a, b: a + b, res)
            elif t == 1:
                return p, reduce(lambda a, b: a * b, res)
            elif t == 2:
                return p, min(res)
            elif t == 3:
                return p, max(res)
            elif t == 5:
                return p, 1 if res[0] > res[1] else 0
            elif t == 6:
                return p, 1 if res[0] < res[1] else 0
            elif t == 7:
                return p, 1 if res[0] == res[1] else 0

    print(run_pack(0))
