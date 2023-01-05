n, a = int(input()), (int(i) for i in input().split())
res = (1 + n) * n // 2 - sum(a)
print(res)
