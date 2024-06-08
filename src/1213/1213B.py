from math import inf


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, mi = 0, inf
    for i in reversed(range(n)):
        res += a[i] > mi
        mi = min(mi, a[i])
    print(res)
