t = int(input())
for _ in range(t):
    n, x1, y1, x2, y2 = (int(i) for i in input().split())
    r1 = min(min(x1, n + 1 - x1), min(y1, n + 1 - y1))
    r2 = min(min(x2, n + 1 - x2), min(y2, n + 1 - y2))
    res = abs(r1 - r2)
    print(res)
