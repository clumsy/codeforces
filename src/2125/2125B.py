from math import gcd


t = int(input())
for _ in range(t):
    x, y, k = (int(i) for i in input().split())
    res = 1 if x // gcd(x, y) <= k and y // gcd(x, y) <= k else 2
    print(res)
