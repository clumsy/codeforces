from math import inf


t = int(input())
for _ in range(t):
    n, q = int(input()), (int(i) for i in input().split())
    f = ma = next(q)
    mi = inf
    res = [1]
    for i in q:
        if mi > ma:
            if i >= ma:
                ma = i
                res.append(1)
            elif i > f:
                res.append(0)
            else:
                mi = i
                res.append(1)
        elif i > f or i < mi:
            res.append(0)
        else:
            mi = i
            res.append(1)
    res = "".join(str(i) for i in res)
    print(res)
