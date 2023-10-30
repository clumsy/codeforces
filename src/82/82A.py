from math import floor, log2

n = int(input())
n -= 1
# Sn = a1 * (1-rn) / (1-r) = n
# 5 * (1 - 2^k) / (1 - 2) = n
# 2^k - 1 = n / 5
# k = log2(n / 5 + 1)
k = floor(log2(n / 5 + 1))
n -= 5 * (1 - 2**k) // (1 - 2)
res = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][n // (2**k)]
print(res)
