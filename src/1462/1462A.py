t = int(input())
for _ in range(t):
    n, b = int(input()), [int(i) for i in input().split()]
    res = [0] * n
    i, lo, hi = 0, 0, n - 1
    while lo <= hi:
        res[i] = b[lo]
        if lo != hi:
            res[i + 1] = b[hi]
        i += 2
        lo += 1
        hi -= 1
    print(*res)
