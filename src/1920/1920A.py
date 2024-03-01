from math import inf


t = int(input())
for _ in range(t):
    n = int(input())
    lo, hi = -inf, inf
    bad = set()
    for _ in range(n):
        a, x = (int(i) for i in input().split())
        if a == 1:
            lo = max(lo, x)
        elif a == 2:
            hi = min(hi, x)
        else:
            bad.add(x)
    res = (hi + 1 - lo) - sum(lo <= i <= hi for i in bad) if lo <= hi else 0
    print(res)
