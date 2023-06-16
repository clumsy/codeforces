n, a = int(input()), [int(i) for i in input().split()]
mi = min(a)
res = mi if all(i % mi == 0 for i in a) else -1
print(res)
