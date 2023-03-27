q = int(input())
for _ in range(q):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    mi = ma = next(a)
    for i in a:
        mi = min(mi, i)
        ma = max(ma, i)
    res = -1 if ma - mi > 2 * k else mi + k
    print(res)
