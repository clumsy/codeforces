n, a = int(input()), [int(i) for i in input().split()]
res, ma = "YES", 0
for i in range(1, n):
    if ma and (a[i] > a[i - 1] or a[i] == a[i - 1] != ma):
        res = "NO"
        break
    if a[i] <= a[i - 1] and not ma:
        ma = a[i - 1]
print(res)
