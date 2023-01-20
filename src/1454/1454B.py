t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    sort = sorted(range(n), key=a.__getitem__)
    res = -1
    for i, e in enumerate(sort):
        if (i == n - 1 or a[e] < a[sort[i + 1]]) and (i == 0 or a[e] > a[sort[i - 1]]):
            res = e + 1
            break
    print(res)
