k, n, w = (int(i) for i in input().split())
res = max(0, k * (1 + w) * w // 2 - n)
print(res)
