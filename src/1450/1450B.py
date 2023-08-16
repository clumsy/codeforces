t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    pts = [[int(i) for i in input().split()] for _ in range(n)]
    res = -1
    for i in range(n):
        if all(
            abs(pts[i][0] - pts[j][0]) + abs(pts[i][1] - pts[j][1]) <= k
            for j in range(n)
        ):
            res = 1
            break
    print(res)
