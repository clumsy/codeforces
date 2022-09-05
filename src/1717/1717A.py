t = int(input())
for _ in range(t):
    n = int(input())
    # a*b <= 3*gcd(a,b)^2
    # for each gcd G in [1; n] we get at most 5 pairs: (G, G), (G, 2G), (G, 3G), (2G, G), (3G, G)
    res = 2 * (n // 3) + 2 * (n // 2) + n
    print(res)
