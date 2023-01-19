from math import inf

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    s = sum(a)
    if s & 1 == 0:
        res = 0
    else:
        res = inf
        for e in a:
            k = 0
            while e // 2 ** k and (s - e + e // 2**k) & 1 == 1:
                k += 1
            if (s - e + e // 2**k) & 1 == 0:
                res = min(res, k)
    print(res)
