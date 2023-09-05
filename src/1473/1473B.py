t = int(input())


def fact(s):
    n = len(s)
    for k in range(1, n + 1):  # length
        invalid = n % k != 0
        for j in range(k):  # chunks
            if invalid:
                break
            for i in range(1, n // k):  # times
                if s[j] != s[j + i * k]:
                    invalid = True
                    break
        if not invalid:
            return s[:k], n // k
    return s, 1


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


for _ in range(t):
    s, t = (input() for _ in range(2))
    s_, cs = fact(s)
    t_, ct = fact(t)
    res = -1 if s_ != t_ else s_ * lcm(cs, ct)
    print(res)
