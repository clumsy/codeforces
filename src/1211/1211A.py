n, r = int(input()), [int(i) for i in input().split()]
mi = md = ma = 0
for i in range(n):
    if r[i] < r[mi]:
        md, mi = mi, i
    elif r[i] > r[ma]:
        md, ma = ma, i
res = (mi + 1, md + 1, ma + 1) if r[mi] < r[md] < r[ma] else (-1, -1, -1)
print(*res)
