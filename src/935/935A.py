n = int(input())
res = sum(n % i == 0 for i in range(1, 1 + n // 2))
print(res)
