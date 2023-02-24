from math import inf

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = -inf
    for i, e in enumerate(a):
        res = max(res, a[-1] - e, e - a[0])
        if i > 0:
            res = max(res, a[i - 1] - e)
        if i < n - 1:
            res = max(res, e - a[i + 1])
    print(res)
