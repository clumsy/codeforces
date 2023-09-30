t = int(input())
for _ in range(t):
    g = [input() for _ in range(10)]
    res = 0
    for r in range(10):
        for c in range(10):
            if g[r][c] == "X":
                res += min(min(r, 9 - r), min(c, 9 - c)) + 1
    print(res)
