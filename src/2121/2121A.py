t = int(input())
for _ in range(t):
    n, s = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    mi = ma = next(a)
    for i in a:
        mi = min(mi, i)
        ma = max(ma, i)
    res = (ma - mi) + abs(min(s - mi, ma - s))
    print(res)
