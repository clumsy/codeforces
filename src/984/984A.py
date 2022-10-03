n, a = int(input()), sorted(int(i) for i in input().split())
res = a[(len(a) - 1) // 2]
print(res)
