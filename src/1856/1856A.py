t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            res = max(res, a[i])
    print(res)
