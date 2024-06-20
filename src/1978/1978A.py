t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = 0
    for i in range(n - 1):
        res = max(res, a[i] + a[-1])
    print(res)
