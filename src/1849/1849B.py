t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, q = [], []
    for i, e in enumerate(a):
        r = e % k
        if r == 0:
            res.append(i + 1)
        else:
            q.append((-r, i + 1))
    q.sort()
    res.extend(i for _, i in q)
    print(*res)
