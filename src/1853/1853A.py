from math import inf

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = inf
    for i in range(1, n):
        if a[i - 1] > a[i]:
            res = 0
            break
        res = min(res, (a[i] - a[i - 1] + 2) // 2)
    print(res)
