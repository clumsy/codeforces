t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = cn = 0
    ma = None
    for i in a:
        if i == 0:
            res += 1
        elif i < 0:
            ma = i if ma is None else max(ma, i)
            cn += 1
    res += 1 - ma if cn & 1 == 1 and ma is not None else 0
    print(res)

    n
