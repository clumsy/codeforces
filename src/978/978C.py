n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
b = (int(i) for i in input().split())
ma = sz = next(a)
res, j = [], 1
for i in b:
    while i > ma:
        sz = next(a)
        ma += sz
        j += 1
    res.append((j, i - (ma - sz)))
for r in res:
    print(*r)
