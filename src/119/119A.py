a, b, n = (int(i) for i in input().split())


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a - b)


res = 1
while n:
    n -= gcd(a, n)
    a, b = b, a
    res = (res + 1) % 2
print(res)
