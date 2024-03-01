from math import gcd


t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    g = gcd(a, b)
    res = (a * b) // g
    if res == b:
        res *= b // g
    print(res)
