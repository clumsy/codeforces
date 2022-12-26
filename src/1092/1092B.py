n, a = int(input()), sorted(int(i) for i in input().split())
res = 0
for i in range(0, n, 2):
    res += a[i + 1] - a[i]
print(res)
