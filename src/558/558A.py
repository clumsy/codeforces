n = int(input())
x, a = [0] * n, [0] * n
for i in range(n):
    x[i], a[i] = (int(i) for i in input().split())
order = sorted(range(n), key=x.__getitem__)
mi = 0
for i in range(n):
    if x[order[i]] >= 0:
        break
    mi = i + 1
lft = rgt = res = 0
stop = False
for i in range(n - mi + 1):
    if mi - i - 1 >= 0:
        lft += a[order[mi - i - 1]]
    else:
        stop = True
    if mi + i < n:
        rgt += a[order[mi + i]]
    else:
        stop = True
    res = lft + rgt
    if stop:
        break
print(res)
