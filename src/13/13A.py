a = int(input())


def to_base(x, b):
    res = []
    while x:
        x, r = divmod(x, b)
        res.append(r)
    return reversed(res)


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


s = sum(sum(to_base(a, b)) for b in range(2, a))
g = gcd(s, a - 2)
res = f"{s // g}/{(a - 2) // g}"
print(res)
