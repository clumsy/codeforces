t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, mi = [], float("inf")
    for i, e in enumerate(a):
        if e > mi:
            res.append(i + 1)
        mi = min(mi, e)
    print(len(res))
    print(*res)
