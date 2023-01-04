n = int(input())
res = (4, n - 4) if n & 1 == 0 else (9, n - 9)
print(*res)
