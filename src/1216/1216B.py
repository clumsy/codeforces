n, a = int(input()), [int(i) for i in input().split()]
res, order = 0, sorted(range(n), key=a.__getitem__, reverse=True)
for i, x in enumerate(order):
    res += i * a[x] + 1
print(res)
print(*(i + 1 for i in order))
