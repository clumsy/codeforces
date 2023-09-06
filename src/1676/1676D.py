from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    g = [[int(i) for i in input().split()] for _ in range(n)]
    # 00 01 02
    # 10 11 12
    # 20 21 22
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for r in range(n):
        for c in range(m):
            d1[c - r] += g[r][c]
            d2[c + r] += g[r][c]
    res = 0
    for r in range(n):
        for c in range(m):
            res = max(res, d1[c - r] + d2[c + r] - g[r][c])
    print(res)
