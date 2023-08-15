n, x = (int(i) for i in input().split())
res, pe = 0, 1
for _ in range(n):
    s, e = (int(i) for i in input().split())
    res += divmod(s - pe, x)[1]
    res += e - s + 1
    pe = e + 1
print(res)
