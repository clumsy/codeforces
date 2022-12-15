n, a = int(input()), (int(i) for i in input().split())
res = (i - (not i & 1) for i in a)
print(*res)
