n, m = (int(i) for i in input().split())
d, r = divmod(m, n)
if r != 0:
    res = -1
else:
    res = 0
    while d % 2 == 0:
        d //= 2
        res += 1
    while d % 3 == 0:
        d //= 3
        res += 1
    res = res if d == 1 else -1
print(res)
