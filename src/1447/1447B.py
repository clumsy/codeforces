from math import inf

t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    s, np, mi = 0, 0, inf
    for r in range(n):
        for c in range(m):
            e = a[r][c]
            mi = min(mi, abs(e))
            np += e <= 0
            s += abs(e)
    res = s - 2 * mi * (np & 1)
    print(res)
