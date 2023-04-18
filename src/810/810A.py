n, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
# (sum + xk)/(n + x) = k - 0.5
# sum + xk = (k - 0.5) * (n + x)
# sum + xk = kn + xk - 0.5x - 0.5n
# 0.5x = kn - 0.5n - sum
# x = 2kn - n - 2sum = n(2k - 1) - 2sum
res = max(0, n * (2 * k - 1) - 2 * sum(a))
print(res)
