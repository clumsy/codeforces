from math import inf

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    ma = -inf
    for i in a:
        if i < 0:
            res = i
            break
        ma = max(ma, i)
    else:
        res = ma
    print(res)
