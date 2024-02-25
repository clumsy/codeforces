t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    b = sorted(int(i) for i in input().split())
    lo1, hi1 = 0, n - 1
    lo2, hi2 = 0, m - 1
    res = 0
    while lo1 <= hi1:
        d1 = abs(a[hi1] - b[lo2])
        d2 = abs(a[lo1] - b[lo2])
        d3 = abs(a[hi1] - b[hi2])
        d4 = abs(a[lo1] - b[hi2])
        ma = max(d1, d2, d3, d4)
        if d1 == ma:
            hi1 -= 1
            lo2 += 1
        elif d2 == ma:
            lo1 += 1
            lo2 += 1
        elif d3 == ma:
            hi1 -= 1
            hi2 -= 1
        else:
            lo1 += 1
            hi2 -= 1
        res += ma
    print(res)
