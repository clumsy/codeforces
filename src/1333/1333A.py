t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = [["B"] * m for _ in range(n)]
    res[0][0] = "W"
    for r in res:
        print("".join(r))
