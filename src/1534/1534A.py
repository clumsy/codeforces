t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res, clr = [[c for c in input()] for _ in range(n)], [set(), set()]
    for r in range(n):
        for c in range(m):
            if res[r][c] != ".":
                clr[(r + c) & 1].add(res[r][c])
    if len(clr[0]) > 1 or len(clr[1]) > 1 or len(clr[0] & clr[1]) > 0:
        print("NO")
    else:
        print("YES")
        clr[0] = "R" if "W" not in clr[0] and "R" not in clr[1] else "W"
        clr[1] = "R" if clr[0] == "W" else "W"
        for r in range(n):
            for c in range(m):
                print(clr[(r + c) & 1], end="")
            print()
