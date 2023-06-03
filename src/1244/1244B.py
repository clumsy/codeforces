from math import inf

t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    mi, ma = inf, -inf
    for i, c in enumerate(s):
        mi = min(mi, i) if c == "1" else mi
        ma = max(ma, i) if c == "1" else ma
    res = 2 * n - (2 * min(mi, n - ma - 1) if mi < inf else n)
    print(res)
