t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    g = [[int(i) for i in input().split()] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            ma = float("-inf")
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= r + dr < n and 0 <= c + dc < m and not (dr == dc == 0):
                    ma = max(ma, g[r + dr][c + dc])
            if g[r][c] > ma:
                g[r][c] = ma
    for res in g:
        print(*res)
