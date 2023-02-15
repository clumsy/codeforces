t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    x, y = 0, 0
    d = {
        "D": (0, -1),
        "U": (0, +1),
        "R": (+1, 0),
        "L": (-1, 0),
    }
    res = "NO"
    for c in s:
        x, y = map(sum, zip((x, y), d[c]))
        if (x, y) == (1, 1):
            res = "YES"
    print(res)
