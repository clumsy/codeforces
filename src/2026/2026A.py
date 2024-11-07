from math import sqrt, ceil


t = int(input())
for _ in range(t):
    n, y, k = (int(i) for i in input().split())
    d = ceil(k / sqrt(2))
    res = [
        [0, 0, d, d],
        [0, d, d, 0],
    ]
    for r in res:
        print(*r)
