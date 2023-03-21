n, a, b, c = (int(input()) for _ in range(4))
res = max(0, min(min(a, b) + (n - 2) * c, (n - 1) * min(a, b)))
print(res)
