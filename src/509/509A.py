from math import factorial

n = int(input())
# 1 1 1  1  1 1 1
# 1 2 3  4  5 6 7
# 1 3 6  10
# 1 4 10 20
k = 2 * (n - 1)
res = factorial(k) // (factorial(k // 2) ** 2)
print(res)
