from math import ceil, sqrt

n = int(input())
# n = x*(x + 1)//2
# x^2 + x - 2n = 0
# D = 1 + 8n
# x = (-1 + sqrt(D))/2
d = ceil(sqrt(1 + 8 * n))
x = (d - 1) // 2
res = "YES" if x * (x + 1) // 2 == n else "NO"
print(res)
