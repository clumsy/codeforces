t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    while n:
        d, r = divmod(n, 10)
        res += d * 10
        if d:
            n = d + r
        else:
            res += r
            break
    print(res)
