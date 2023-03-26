n, a = int(input()), [int(i) for i in input().split()]
z = a.index(0)
a = a[z:] + a[:z]
res, cur = 0, 0
for i in range(2 * n):
    if a[i % n] == 0:
        res, cur = max(res, cur), 0
    else:
        cur += 1
print(res)
