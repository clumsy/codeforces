a, b, c = (int(input()) for _ in range(3))
res = (1 + 2 + 4) * min(a, b // 2, c // 4)
print(res)
