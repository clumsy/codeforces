n = int(input())
res = 1  # always ends with 1
while n > 1:
    res += n
    n = next(i for i in range(n // 2, 0, -1) if n % i == 0)
print(res)
