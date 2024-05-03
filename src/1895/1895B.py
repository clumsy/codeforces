t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    a = zip(a[:n], a[n:])
    x0, y0 = next(a)
    res = 0
    pts = [(x0, y0)]
    for x, y in a:
        res += x - x0 + y - y0
        pts.append((x, y))
        x0, y0 = x, y
    print(res)
    for x, y in pts:
        print(x, y)
