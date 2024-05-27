t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    prv, dup = {}, []
    for i, e in enumerate(a):
        if len(dup) < 2 and e in prv:
            if len(dup) == 0 or dup[0] != e:
                dup.append(e)
        prv[e] = i
    if len(dup) > 1:
        res = [3] * n
        for i, e in enumerate(a):
            if e == dup[0]:
                res[i] = 1
            elif e == dup[1]:
                res[i] = 2
        res[prv[dup[0]]] = 2
        res[prv[dup[1]]] = 3
    else:
        res = [-1]
    print(*res)
