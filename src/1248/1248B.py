n, a = int(input()), sorted(int(i) for i in input().split())
res = sum(a[: n // 2]) ** 2 + sum(a[n // 2 :]) ** 2
print(res)
