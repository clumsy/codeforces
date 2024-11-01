def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    g, ma = None, -float("inf")
    for i in a:
        ma = max(ma, i)
        g = gcd(g, i) if g is not None else i
    res = ma // g
    print(res)
