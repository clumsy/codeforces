from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    mi, ma, s = inf, inf, 0
    for _ in range(n):
        m, a = int(input()), (int(i) for i in input().split())
        mi1 = mi2 = inf
        for i in a:
            if i <= mi1:
                mi1, mi2 = i, mi1
            elif i < mi2:
                mi2 = i
        mi2 = mi2 if mi2 < inf else mi1
        s += mi2
        ma = min(ma, mi2)
        mi = min(mi, mi1)
    res = s - ma + mi
    print(res)
