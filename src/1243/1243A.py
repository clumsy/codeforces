k = int(input())
for _ in range(k):
    n, a = int(input()), sorted(int(i) for i in input().split())
    lo, hi, mi = 0, n - 1, 0
    while lo < hi:
        mi = lo + (hi - lo) // 2
        if a[mi] >= n - mi:
            hi = mi
        else:
            lo = mi + 1
    res = n - lo
    print(res)
