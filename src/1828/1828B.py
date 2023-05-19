t = int(input())
for _ in range(t):
    n, p = int(input()), (int(i) for i in input().split())

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    res = 0
    for i, e in enumerate(p):
        res = gcd(res, abs(e - i - 1))
    print(res)
