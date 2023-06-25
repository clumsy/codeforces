n = int(input())
g = []
for _ in range(n):
    g.append(input())
res = "YES"
for r in range(n):
    for c in range(n):
        s = g[r - 1][c] == "o" if r > 0 else 0
        s += g[r + 1][c] == "o" if r < n - 1 else 0
        s += g[r][c - 1] == "o" if c > 0 else 0
        s += g[r][c + 1] == "o" if c < n - 1 else 0
        if s & 1 == 1:
            res = "NO"
            break
print(res)
