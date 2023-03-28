n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
mi = min(a)
res = 0
for i in a:
    d, r = divmod(i - mi, k)
    if r == 0:
        res += d
    else:
        res = -1
        break
print(res)
