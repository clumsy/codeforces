from math import sqrt, floor

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = "YES" if any(i != floor(sqrt(i)) ** 2 for i in a) else "NO"
    print(res)
