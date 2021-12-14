with open('input7.txt') as fp:
    nums = [int(n) for n in fp.readline().split(',')]

    m = None

    for n in range(min(nums), max(nums)):
        k = sum(sum(range(abs(s - n) + 1)) for s in nums)
        if m is None or k < m:
            m = k

    print(m)
