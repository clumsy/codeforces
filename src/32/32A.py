n, d = (int(i) for i in input().split())
a = sorted(int(i) for i in input().split())
res = 0
for i in range(n):
    lo, hi = i + 1, n
    while lo < hi:
        mi = lo + (hi - lo) // 2
        if a[mi] - a[i] > d:
            hi = mi
        else:
            lo = mi + 1
    res += 2 * (lo - i - 1)
print(res)
