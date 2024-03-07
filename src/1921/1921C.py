t = int(input())
for k in range(t):
    n, f, a, b = (int(i) for i in input().split())
    m = (int(i) for i in input().split())
    res, prv = "YES", 0
    for i in m:
        f -= min(b, (i - prv) * a)
        prv = i
        if f <= 0:
            res = "NO"
    print(res)
