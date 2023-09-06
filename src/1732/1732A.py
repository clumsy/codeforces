from functools import reduce

t = int(input())


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, g = 0, reduce(gcd, a)
    if g > 1:
        for i in reversed(range(n)):
            a[i] = gcd(a[i], i + 1)
            g_hat = gcd(g, a[i])
            res += n - i if g_hat < g else 0
            g = g_hat
            if gcd(g, a[i]) == 1:
                break
    print(res)
