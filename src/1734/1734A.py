t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = 3 * a[-1]
    for i in range(1, n - 1):
        # (a[i] - a[i - 1]) + (a[i + 1] - a[i])
        res = min(res, a[i + 1] - a[i - 1])
    print(res)
