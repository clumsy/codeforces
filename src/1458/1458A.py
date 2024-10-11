from functools import reduce


def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


def gcd(*a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return gcd2(*a)
    return reduce(gcd2, a)


n, m = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = (int(i) for i in input().split())
x = max(range(n), key=a.__getitem__)
a[0], a[x] = a[x], a[0]
d = gcd(*(a[0] - i for i in a[1:]))
res = (gcd(a[0] + j, d) for j in b)
print(*res)
