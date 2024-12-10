from math import gcd


t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = (a * b) // gcd(a, b)
    print(res)
