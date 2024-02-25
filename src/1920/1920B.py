t = int(input())
for _ in range(t):
    n, k, x = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    alc = sum(a[: n - x])
    bob = sum(a[n - x :])
    res = alc - bob
    for i in range(k):
        if n - 1 - x - i >= 0:
            alc -= a[n - 1 - x - i]
            bob += a[n - 1 - x - i]
        if n - 1 - i >= 0:
            bob -= a[n - 1 - i]
        res = max(res, alc - bob)
    print(res)
