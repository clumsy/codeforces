t = int(input())
for _ in range(t):
    n, k, a, b = (int(i) for i in input().split())
    xy = [tuple(int(i) for i in input().split()) for _ in range(n)]

    def dst(i, j):
        return (
            0
            if i < k and j < k
            else abs(xy[i][0] - xy[j][0]) + abs(xy[i][1] - xy[j][1])
        )

    res = dst(a - 1, b - 1)
    r1 = r2 = float("inf")
    for i in range(k):
        r1 = min(r1, dst(a - 1, i))
        r2 = min(r2, dst(i, b - 1))
    res = min(res, r1 + r2)
    print(res)
