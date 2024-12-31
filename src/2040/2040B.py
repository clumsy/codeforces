from math import log2, floor


t = int(input())
for _ in range(t):
    n = int(input())
    res = n if n < 3 else 2 + floor(log2((n + 1) // 3))
    print(res)
