n, a = int(input()), [int(i) for i in input().split()]
res = 0
for i in reversed(range(n)):
    res += a[i]
    if i > 0:
        a[i - 1] = min(a[i - 1], max(0, a[i] - 1))
print(res)
