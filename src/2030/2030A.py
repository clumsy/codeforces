from math import inf


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    mi, ma = inf, -inf
    for i in a:
        mi = min(mi, i)
        ma = max(ma, i)
    res = (n - 1) * (ma - mi)
    print(res)
