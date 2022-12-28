from math import inf

n, m = (int(i) for i in input().split())
res = inf
for _ in range(n):
    a, b = (int(i) for i in input().split())
    res = min(res, (a * m) / b)
print(res)
