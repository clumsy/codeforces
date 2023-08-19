t = int(input())
for _ in range(t):
    m = int(input())
    pst, ma = [None] * m, {}
    for k in range(m):
        n, a = int(input()), [int(i) for i in input().split()]
        pst[k] = a
        for p in a:
            ma[p] = k
    res = []
    for k in range(m):
        for p in pst[k]:
            if ma[p] == k:
                res.append(p)
                break
        else:
            res = [-1]
            break
    print(*res)
