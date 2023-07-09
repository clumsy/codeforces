n, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = 1, 0
ma = 0
for i, e in enumerate(a):
    cur = e * (n // e)
    if cur > ma:
        res = i + 1, n // e
        ma = cur
print(*res)
