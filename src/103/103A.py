n, a = int(input()), (int(i) for i in input().split())
res = 0
for i, e in enumerate(a):
    res += (e - 1) * (i + 1) + 1
print(res)
