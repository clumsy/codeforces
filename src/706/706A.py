from math import inf, sqrt

a, b = (int(i) for i in input().split())
n = int(input())
res = inf
for _ in range(n):
    x, y, v = (int(i) for i in input().split())
    res = min(res, sqrt((x - a) ** 2 + (y - b) ** 2) / v)
print(res)
