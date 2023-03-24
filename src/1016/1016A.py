n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res, ttl = [0] * n, 0
for i in range(n):
    res[i], ttl = divmod(ttl + next(a), m)
print(*res)
