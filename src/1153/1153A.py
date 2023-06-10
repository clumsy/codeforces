from math import inf

n, t = (int(i) for i in input().split())
res, mi = 0, inf
for i in range(n):
    s, d = (int(i) for i in input().split())
    s += d * ((t - s + d - 1) // d) if s < t else 0
    if s - t < mi:
        res = i + 1
        mi = s - t
print(res)
