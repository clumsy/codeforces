n, a = int(input()), (int(i) for i in input().split())
res = 4 * sum(e * i for i, e in enumerate(a))
print(res)
