from math import log2, floor


t = int(input())
for _ in range(t):
    l, r = (int(i) for i in input().split())
    res = floor(log2(r))
    print(res)
