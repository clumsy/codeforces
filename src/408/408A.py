from math import inf

n, k = int(input()), (int(i) for i in input().split())
res = inf
for _ in range(n):
    m = (int(i) for i in input().split())
    s = 15 * next(k) + 5 * sum(m)
    res = min(res, s)
print(res)
