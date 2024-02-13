t = int(input())
for _ in range(t):
    n, T = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, h = [], 1
    for i in a:
        if 2 * i == T:
            h += 1
            res.append(h & 1)
        else:
            res.append(1 if i >= T / 2 else 0)
    print(*res)
