t = int(input())
for _ in range(t):
    n, h = int(input()), (int(i) for i in input().split())
    prv = next(h)
    res = cnt = 1
    for i in h:
        if i == prv:
            cnt += 1
        else:
            prv, cnt = i, 1
        res = max(res, cnt)
    res = n - res
    print(res)
