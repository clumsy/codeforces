n = int(input())
g = [input() for _ in range(n)]
res = "YES" if g[0][0] != g[1][0] else "NO"
for r in range(n):
    for c in range(n):
        if r == c or n - 1 - r == c:
            if g[r][c] == g[0][0]:
                continue
        elif g[r][c] == g[1][0]:
            continue
        res = "NO"
        break
print(res)
