t = int(input())
for _ in range(t):
    x, y, n = (int(i) for i in input().split())
    res, d = [y], 1
    while n > 2 and res[-1] > x:
        res.append(res[-1] - d)
        d += 1
        n -= 1
    if res[-1] - d >= x:
        res.append(x)
        res.reverse()
    else:
        res = [-1]
    print(*res)
