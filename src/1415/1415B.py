from math import inf

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    c = [int(i) for i in input().split()]
    res = inf
    for x in set(c):
        cur = i = 0
        while i < n:
            if c[i] != x:
                cur += 1
                i += k
            else:
                i += 1
        res = min(res, cur)
    print(res)
