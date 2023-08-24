t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    ma = mi = a[0]
    ma_cnt = 0
    for i in a:
        if i > ma:
            ma_cnt = 0
        ma = max(ma, i)
        mi = min(mi, i)
        ma_cnt += i == ma
    if ma == mi:
        print(-1)
    else:
        c, b = [ma] * ma_cnt, [i for i in a if i != ma]
        print(len(b), len(c))
        print(*b)
        print(*c)
