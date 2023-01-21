n = int(input())
res = (1, 1, n - 2) if (n - 2) % 3 != 0 else (1, 2, n - 3)
print(*res)
