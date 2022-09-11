t = int(input())
for _ in range(t):
    s = int(input())
    res, n = 0, 1
    # s = 1+3+5+7+...+(2n - 1)+reminder, where reminder < 2n + 1
    while s > 0:
        res += 1
        s -= n
        n += 2
    print(res)
