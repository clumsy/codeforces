t = int(input())
for _ in range(t):
    n = int(input())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    d = {}
    for r in range(n):
        for c in range(n):
            d[c - r] = min(d.get(c - r, float("inf")), a[r][c])
    res = -sum(v for v in d.values() if v < 0)
    print(res)
