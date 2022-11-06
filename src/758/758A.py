n, a = int(input()), [int(i) for i in input().split()]
res = sum(max(a) - i for i in a)
print(res)
