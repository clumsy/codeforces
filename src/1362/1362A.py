t = int(input())
for _ in range(t):
    a, b = sorted(int(i) for i in input().split())
    d, r = divmod(b, a)
    if r > 0 or d & -d != d:
        res = -1
    else:
        res = 0
        while d >= 8:
            d //= 8
            res += 1
        res += d > 1
    print(res)
