a, b = (int(input()) for _ in range(2))
n = a + b + 1
res = [*range(1, a + 1), *range(n, n - b - 1, -1)]
print(*res)
