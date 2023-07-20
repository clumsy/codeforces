n = int(input())
res = 1 if n == 0 else [8, 4, 2, 6][(n - 1) % 4]
print(res)
