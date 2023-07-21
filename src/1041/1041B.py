a, b, x, y = (int(i) for i in input().split())


def gcd(a, b):
    return gcd(b, a % b) if b else a


g = gcd(x, y)
x, y = x // g, y // g
res = min(a // x, b // y)
print(res)
