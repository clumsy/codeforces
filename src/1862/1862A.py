from math import inf

t = int(input())


def find(n, m, f, s, g, c1, c2):
    mi, ma = inf, -inf
    for r in range(n):
        for c in range(c1, c2):
            if g[r][c] == f:
                mi = min(mi, c)
            if g[r][c] == s:
                ma = max(ma, c)
    return mi, ma


for _ in range(t):
    n, m = (int(i) for i in input().split())
    c = [input() for _ in range(n)]
    res = "NO"
    v, a = find(n, m, "v", "a", c, 0, m)
    if 0 <= v < m and 0 <= a < m:
        i, k = find(n, m, "i", "k", c, v + 1, a)
        if v < i < k < a:
            res = "YES"
    print(res)
