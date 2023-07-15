n, a = int(input()), [int(i) for i in input().split()]
d = a[1] - a[0]
for i in range(2, n):
    if a[i] - a[i - 1] != d:
        res = a[-1]
        break
else:
    res = a[-1] + d
print(res)
