n, b = int(input()), (int(i) for i in input().split())
res, ma = [0] * n, 0
for i, e in enumerate(b):
    res[i] = ma + e
    ma = max(ma, res[i])
print(*res)
