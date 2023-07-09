t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    x = (int(i) for i in input().split())
    prv, res = None, 0
    for i in x:
        d = (i + 1 - prv + 1) // 2 if prv else i
        res = max(res, d)
        prv = i
    res = max(res, n + 1 - prv)
    print(res)
