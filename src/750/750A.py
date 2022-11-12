from math import floor, sqrt

n, k = (int(i) for i in input().split())
# 5(n + 1)*n/2 = 240 - k = p
# 5n^2 + 5n - 2p = 0
# D = 25 + 40p
# n = (-5 + sqrt(D))/10
res = min(n, floor((-5 + sqrt(25 + 40 * (240 - k))) / 10))
print(res)
