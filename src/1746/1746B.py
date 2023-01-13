t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, lo, hi = 0, 0, n - 1
    while lo < hi:
        if a[lo] < 1:
            lo += 1
        elif a[hi] > 0:
            hi -= 1
        else:
            res += 1
            lo += 1
            hi -= 1
    print(res)
