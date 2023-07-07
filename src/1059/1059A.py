n, L, a = (int(i) for i in input().split())
res = prv = 0
for _ in range(n):
    t, length = (int(i) for i in input().split())
    res += (t - prv) // a
    prv = t + length
res += (L - prv) // a
print(res)
