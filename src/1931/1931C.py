t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    lo, hi = 0, n - 1
    while lo < hi and a[lo] == a[lo + 1]:
        lo += 1
    while hi > lo and a[hi] == a[hi - 1]:
        hi -= 1
    res = max(0, hi - lo - 1) if a[lo] == a[hi] else min(n - 1 - lo, hi)
    print(res)
