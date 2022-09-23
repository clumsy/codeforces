n, a = int(input()), [int(i) for i in input().split()]
ma, mi = 1, 1
for i, x in enumerate(a):
    mi = i + 1 if x == 1 else mi
    ma = i + 1 if x == n else ma
res = max(n - mi, n - ma, ma - 1, mi - 1)
print(res)
