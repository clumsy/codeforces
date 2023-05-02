n, m = (int(i) for i in input().split())
b = (int(i) for i in input().split())
res, last = [None] * n, n
for i, v in enumerate(b):
    for j in range(v - 1, last):
        res[j] = v
    last = min(last, v - 1)
print(*res)
