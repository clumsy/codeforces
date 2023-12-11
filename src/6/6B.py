n, m, p = input().split()
n, m = (int(i) for i in (n, m))
g = [input() for _ in range(n)]
res = set()
for r in range(n):
    for c in range(m):
        if g[r][c] != p:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < n and 0 <= c + dc < m:
                res.add(g[r + dr][c + dc])
for c in [".", p]:
    if c in res:
        res.remove(c)
res = len(res)
print(res)
