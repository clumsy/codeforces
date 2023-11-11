g = [input() for _ in range(4)]
res = "NO"
for r in range(3):
    if res == "YES":
        break
    for c in range(3):
        s = (
            int(g[r][c] == "#")
            + int(g[r + 1][c + 1] == "#")
            + int(g[r + 1][c] == "#")
            + int(g[r][c + 1] == "#")
        )
        if s % 4 != 2:
            res = "YES"
            break
print(res)
