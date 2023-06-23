a, b, c = (int(input()) for _ in range(3))
res = max((a + b) * c, a * (b + c), a * b * c, a + b + c)
print(res)
