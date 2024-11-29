t = int(input())
for _ in range(t):
    n, w = int(input()), [int(i) for i in input().split()]
    lo, hi = -1, n
    res = a = b = 0
    while hi - lo > 1:
        if a <= b:
            lo += 1
            a += w[lo]
        else:
            hi -= 1
            b += w[hi]
        if a == b:
            res = lo + 1 + n - hi
    print(res)
