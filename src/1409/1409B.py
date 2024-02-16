t = int(input())
for _ in range(t):
    a, b, x, y, n = (int(i) for i in input().split())
    # (a - i) * (b - j), i + j <= n
    # ab - ib - ja + ij
    if max(a - n, x) > max(b - n, y):
        a, b, x, y = b, a, y, x
    i = min(n, a - x)
    j = min(n - i, b - y)
    res = (a - i) * (b - j)
    print(res)
