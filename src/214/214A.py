from math import sqrt, ceil

n, m = (int(i) for i in input().split())
# b = sqrt(m - a)
# b = n - a^2
res = 0
for a in range(min(ceil(sqrt(n)), m) + 1):
    res += 1 if n - a**2 == sqrt(m - a) else 0
print(res)
