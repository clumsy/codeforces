def _gcd(a, b):
    return a if b == 0 else _gcd(b, a % b)


def gcd(*v):
    g = v[0]
    for i in v[1:]:
        g = _gcd(g, i)
    return g


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    if n == 1:
        res = 0 if a[0] == 1 else 1
    elif n == 2:
        if gcd(*a) == 1:
            res = 0
        elif gcd(a[0], gcd(2, a[1])) == 1:
            res = 1
        else:
            res = 2
    else:
        g = gcd(*a[:-2])
        if gcd(g, a[-2], a[-1]) == 1:
            res = 0
        elif gcd(g, a[-2], gcd(a[-1], n)) == 1:
            res = 1
        elif gcd(g, gcd(n - 1, a[-2]), a[-1]) == 1:
            res = 2
        else:
            res = 3
    print(res)
