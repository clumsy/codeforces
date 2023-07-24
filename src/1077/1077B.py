n, a = int(input()), [int(i) for i in input().split()]
res = 0
for i, e in enumerate(a):
    if 0 < i < n - 1 and a[i] == 0 and a[i - 1] == a[i + 1] == 1:
        a[i + 1] = 0
        res += 1
print(res)
