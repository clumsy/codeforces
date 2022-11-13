k2, k3, k5, k6 = (int(i) for i in input().split())
num_256 = min(k2, k5, k6)
res = 256 * num_256 + 32 * min(k3, k2 - num_256)
print(res)
