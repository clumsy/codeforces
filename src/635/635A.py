r, c, n, k = (int(i) for i in input().split())
g = [[0] * c for _ in range(r)]
for _ in range(n):
    x, y = (int(i) for i in input().split())
    g[x - 1][y - 1] = 1
for x in range(r):
    for y in range(c):
        g[x][y] += (
            (g[x - 1][y] if x - 1 >= 0 else 0)
            + (g[x][y - 1] if y - 1 >= 0 else 0)
            - (g[x - 1][y - 1] if x - 1 >= 0 and y - 1 >= 0 else 0)
        )
res = 0
for x1 in range(r):
    for y1 in range(c):
        for x2 in range(x1, r):
            for y2 in range(y1, c):
                s = (
                    g[x2][y2]
                    - (g[x1 - 1][y2] if x1 - 1 >= 0 else 0)
                    - (g[x2][y1 - 1] if y1 - 1 >= 0 else 0)
                    + (g[x1 - 1][y1 - 1] if x1 - 1 >= 0 and y1 - 1 >= 0 else 0)
                )
                res += s >= k
print(res)
