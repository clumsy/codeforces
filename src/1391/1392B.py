t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    g = [[c for c in input()] for _ in range(n)]
    res = sum(g[n - 1][c] != "R" for c in range(m - 1))
    res += sum(g[r][m - 1] != "D" for r in range(n - 1))
    print(res)
