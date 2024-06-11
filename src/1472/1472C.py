t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()] + [0]
    res = 0
    for i in reversed(range(n)):
        a[i] += a[min(n, i + a[i])]
        res = max(res, a[i])
    print(res)
