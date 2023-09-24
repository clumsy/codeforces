t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    mi = ma = next(a)
    res = 0
    for i in a:
        mi, ma = min(mi, i), max(ma, i)
        if ma - mi > 2 * x:
            res += 1
            mi = ma = i
    print(res)
