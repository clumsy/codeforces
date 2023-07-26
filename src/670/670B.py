from math import sqrt, floor

n, k = (int(i) for i in input().split())
id = [int(i) for i in input().split()]
# (1 + x) * x // 2 = k
# x^2 + x - 2k = 0
# D = 1 + 8k
# x = (sqrt(D) - 1) / 2
x = (sqrt(1 + 8 * k) - 1) / 2
# check the position in the last segment
x = int(x) - 1 if x == floor(x) else floor(x)
i = k - (1 + x) * x // 2
res = id[i - 1]
print(res)
