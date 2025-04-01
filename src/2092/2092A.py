t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    mi = ma = next(a)
    for i in a:
        mi = min(mi, i)
        ma = max(ma, i)
    res = ma - mi
    print(res)
