n, a = int(input()), [int(i) for i in input().split()]
res, i = a, 0
while i < n - i - 1:
    if i & 1 == 0:
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    i += 1
print(*res)
