from math import sqrt, floor


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    s = sum(a)
    sq = floor(sqrt(s))
    res = "YES" if sq * sq == s else "NO"
    print(res)
