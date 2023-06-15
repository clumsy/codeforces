n, c = (int(i) for i in input().split())
x = [int(i) for i in input().split()]
res = 0
for i in range(n - 1):
    res = max(res, x[i] - x[i + 1] - c)
print(res)
