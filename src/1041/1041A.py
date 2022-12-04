n, a = int(input()), [int(i) for i in input().split()]
res = max(a) - min(a) - n + 1
print(res)
