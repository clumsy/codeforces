n, a = int(input()), (int(i) for i in input().split())
res = len(set(i for i in a if i != 0))
print(res)
