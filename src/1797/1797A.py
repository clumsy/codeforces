t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    x1, y1, x2, y2 = (int(i) for i in input().split())

    def block(x, y):
        if (
            (x == 1 and y == m)
            or (x == y == 1)
            or (x == n and y == 1)
            or (x == n and y == m)
        ):
            return 2
        if x == 1 or y == 1 or x == n or y == m:
            return 3
        return 4

    res = min(block(x1, y1), block(x2, y2))
    print(res)
