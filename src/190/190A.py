n, m = (int(i) for i in input().split())
if n == 0 and m > 0:
    res = "Impossible"
    print(res)
else:
    ma = n + m - 1 if m > 0 else n
    mi = n + max(0, m - n)
    res = mi, ma
    print(*res)
