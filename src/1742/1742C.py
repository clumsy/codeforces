from collections import Counter

t = int(input())
n = 8
for j in range(t):
    input()  # empty line
    g = [[i for i in input()] for _ in range(n)]

    def single(s, c):
        if len(s) == 1 and c in s:
            return next(iter(s.keys()))
        return None

    res = None
    for r in range(n):
        v = Counter(g[r][c] for c in range(n))
        if res := single(v, "R"):
            break
    if not res:
        for c in range(n):
            v = Counter(g[r][c] for r in range(n))
            if res := single(v, "B"):
                break
    print(res)
