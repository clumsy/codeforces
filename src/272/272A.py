n, a = int(input()), (int(i) for i in input().split())
s = sum(a)
res = sum((s - 1 + i) % (n + 1) > 0 for i in range(1, 6))
print(res)
