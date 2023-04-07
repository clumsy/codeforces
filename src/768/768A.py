n, a = int(input()), [int(i) for i in input().split()]
mi = ma = a[0]
for i in a:
    mi = min(mi, i)
    ma = max(ma, i)
res = sum(mi < i < ma for i in a)
print(res)
