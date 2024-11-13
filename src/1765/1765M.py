from math import isqrt

t = int(input())
for _ in range(t):
    n = int(input())
    # a + b = n
    # gcd(a,b) -> max => lcm = (a*b)/gcd(a,b) -> min
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            res = [n // i, n - n // i]
            break
    else:
        res = [1, n - 1]
    print(*res)
