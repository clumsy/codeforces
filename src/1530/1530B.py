t = int(input())
for _ in range(t):
    h, w = (int(i) for i in input().split())
    table = [["0" for _ in range(w)] for _ in range(h)]
    for r in (0, h - 1):
        for c in range(0, w, 2):
            table[r][c] = "1"
    for r in range(2, h - 2, 2):
        for c in (0, w - 1):
            table[r][c] = "1"
    for r in range(h):
        res = "".join(table[r])
        print(res)
    print()
