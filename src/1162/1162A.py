n, h, m = (int(i) for i in input().split())
v = [h] * n
for k in range(m):
    l, r, x = (int(i) for i in input().split())
    for i in range(l - 1, r):
        v[i] = min(v[i], x)
res = sum(x * x for x in v)
print(res)
