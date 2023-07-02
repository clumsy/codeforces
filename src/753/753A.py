from math import sqrt, floor

n = int(input())
# (1 + x)*x/2 = n
# x^2 + x - 2n = 0
# D = 1 + 8n
res = floor((-1 + sqrt(1 + 8 * n)) / 2)
print(res)
x = res
res = [i for i in range(1, res + 1)]
res[-1] += n - (1 + x) * x // 2
print(*res)
