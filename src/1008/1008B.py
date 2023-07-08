from math import inf

n = int(input())
res, prv = True, inf
for _ in range(n):
    w, h = sorted(int(i) for i in input().split())
    res &= prv >= w
    prv = h if prv >= h else w
res = "YES" if res else "NO"
print(res)
