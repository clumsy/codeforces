t = int(input())
for _ in range(t):
    x0, n = (int(i) for i in input().split())
    # 10 10
    # 10 -1> 9 -2> 11 -3> 14 -4> 10 -5> 5 -6> 11 -7> 18 -8> 10 -9> 1 -10-> 11
    # 9 10
    # 9 -1> 10 -2> 8 -3> 5 -4> 9 -5> 14 -6> 8 -7> 1 -8> 9 -9> 18 -10> 8
    d, r = divmod(n, 4)
    if r == 0:
        res = x0
    elif r == 2:
        res = x0 + (-1) ** (x0 & 1)
    elif r == 1:
        res = x0 + (4 * d + 1) * (-1) ** (1 - x0 & 1)
    elif r == 3:
        res = x0 + 4 * (d + 1) * (-1) ** (x0 & 1)
    print(res)
