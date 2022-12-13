n, a = int(input()), [int(i) for i in input().split()]
res, s, i = 0, 0, 1
while i < n:
    if a[i] <= a[i - 1]:
        res, s = max(res, i - s), i
    i += 1
res = max(res, i - s)
print(res)
