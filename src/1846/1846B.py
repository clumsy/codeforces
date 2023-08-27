t = int(input())


def solve(g):
    for r in range(3):
        if g[r][0] == g[r][1] == g[r][2] and g[r][1] != ".":
            return g[r][0]
    for c in range(3):
        if g[0][c] == g[1][c] == g[2][c] and g[1][c] != ".":
            return g[0][c]
    if g[0][0] == g[1][1] == g[2][2] and g[1][1] != ".":
        return g[1][1]
    if g[0][2] == g[1][1] == g[2][0] and g[1][1] != ".":
        return g[1][1]
    return "DRAW"


for _ in range(t):
    g = [input() for _ in range(3)]
    res = solve(g)
    print(res)
