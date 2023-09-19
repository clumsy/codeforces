n, d = (int(i) for i in input().split())
p = sorted(int(i) for i in input().split())
res, lo, hi = 0, 0, n - 1
while lo <= hi:
    x = d - p[hi]
    while lo < hi and x >= 0:
        x -= p[hi]
        lo += 1
    res += x < 0
    hi -= 1
print(res)
