t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    x = (int(i) for i in input().split())
    neg = []
    res = s = 0
    for _ in range(n):
        ai, xi = next(a), next(x)
        if xi < 0:
            neg.append((ai, xi))
        else:
            while res >= 0 and neg and -neg[-1][1] <= xi:
                aj, xj = neg.pop()
                s += aj
                if s > -xj * k:
                    res = -1
            s += ai
            if s > xi * k:
                res = -1
                break
    while res >= 0 and neg:
        aj, xj = neg.pop()
        s += aj
        if s > -xj * k:
            res = -1
    res = "YES" if res >= 0 else "NO"
    print(res)
