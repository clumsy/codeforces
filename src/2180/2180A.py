from math import gcd


t = int(input())
for i in range(t):
    l, a, b = (int(i) for i in input().split())
    b = b if b < l else b % l
    g = gcd(l, b)
    res = l - (g - (a % g))
    print(res)
