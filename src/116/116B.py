n, m = (int(i) for i in input().split())
g = [list(input()) for i in range(n)]
res, cur = -1, 0
while cur > res:
    res = cur
    for r in range(n):
        for c in range(m):
            if g[r][c] != ".":
                p = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (
                        0 <= r + dr < n
                        and 0 <= c + dc < m
                        and g[r + dr][c + dc] not in {g[r][c], "."}
                    ):
                        p += 1
                        pr, pc = r + dr, c + dc
                if p == 1:
                    g[r][c] = g[pr][pc] = "."
                    cur += 1
print(res)
