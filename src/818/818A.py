n, k = (int(i) for i in input().split())
# d + kd = n // 2
d = (n // 2) // (k + 1)
res = d, k * d, n - d * (k + 1)
print(*res)
