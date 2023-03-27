t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        res = 0
    else:
        res = 0
        while n > 0:
            d, r = divmod(n, 6)
            if r != 0:
                break
            n = d
            res += 1
        while n > 0:
            d, r = divmod(n, 3)
            if r != 0:
                break
            n = d
            res += 2
    res = res if n == 1 else -1
    print(res)
