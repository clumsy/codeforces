from math import sqrt, floor

n, k = (int(i) for i in input().split())
# (1 + x) * x // 2 - y = k
# x + y = n
# x + x^2 = 2 * (k + n - x)
# x^2 + x - 2 * (k + n) = 0
# D = 1 + 8 * (k + n)
# x = (sqrt(D) - 1) // 2
D = 1 + 8 * (k + n)
x = floor((sqrt(D) - 1) / 2)
res = n - x
print(res)
