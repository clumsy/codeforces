from math import sqrt, floor

n = int(input())
# (1 + x)*x/2 = n
# x^2 + x - 2n = 0
# D = 1 + 8n
# x = (-1 + sqrt(D))/2
x = floor((sqrt(1 + 8 * n) - 1) / 2)
res = n - ((1 + x) * x) // 2
res = res or x
print(res)
