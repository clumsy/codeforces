from bisect import bisect_left
from math import floor


t = int(input())
for _ in range(t):
    n, m, q = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    q = (int(i) for i in input().split())
    a = sorted(a)
    for s in q:
        if s > a[-1]:
            res = n - a[-1]
        elif s < a[0]:
            res = a[0] - 1
        else:
            i = bisect_left(a, s)
            res = floor((a[i] + a[i - 1]) / 2 - a[i - 1])
        print(res)
