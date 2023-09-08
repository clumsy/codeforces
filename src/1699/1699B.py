t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    g = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            g[r][c] = int(((r - 1) // 2) & 1 == ((c - 1) // 2) & 1)
    for r in range(n):
        print(" ".join(str(i) for i in g[r]))
