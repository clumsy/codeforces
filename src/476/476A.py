n, m = (int(i) for i in input().split())
# 1*x + 2*y = n
# x + y = k*m
# x + 2(k*m - x) = n
# x = 2*k*m - n, x >= 0
k_min = (n + 2 * m - 1) // (2 * m)
# y = n - k * m, y >= 0
k_max = n // m
res = k_min * m if k_min <= k_max else -1
print(res)
