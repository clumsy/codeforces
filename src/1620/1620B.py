from math import inf

t = int(input())
for _ in range(t):
    w, h = (int(i) for i in input().split())
    res = 0
    for k in range(4):
        mi, ma = inf, 0
        for i, e in enumerate(int(i) for i in input().split()):
            if i > 0:
                mi = min(mi, e)
                ma = max(ma, e)
        res = max(res, (h if k < 2 else w) * (ma - mi))
    print(res)
