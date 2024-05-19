n, m = (int(i) for i in input().split())
g = [input() for _ in range(n)]
prv = -1
max_u = max_d = 0
for c in range(m):
    cur = next(r for r in range(n) if g[r][c] == "*")
    if prv >= 0:
        if cur - prv < 0:
            max_u = max(max_u, prv - cur)
        elif cur - prv > 0:
            max_d = max(max_d, cur - prv)
    prv = cur
res = max_u, max_d
print(*res)
