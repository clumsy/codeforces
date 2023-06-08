n = int(input())
res = 2 ** (n // 2) if n & 1 == 0 else 0
print(res)
