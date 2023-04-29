n, m = (int(i) for i in input().split())
a, b = [None] * m, [None] * m
for i in range(m):
    a[i], b[i] = (int(i) for i in input().split())
res = 0
for i in sorted(range(m), key=b.__getitem__, reverse=True):
    get = min(n, a[i])
    res += get * b[i]
    n -= get
    if n == 0:
        break
print(res)
