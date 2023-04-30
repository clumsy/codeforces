from math import sqrt

n, k = (int(i) for i in input().split())
res = 0
x0, y0 = (int(i) for i in input().split())
for _ in range(n - 1):
    x, y = (int(i) for i in input().split())
    res += sqrt((x - x0) ** 2 + (y - y0) ** 2) / 50
    x0, y0 = x, y
res *= k
print(res)
