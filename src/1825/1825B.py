t = int(input())
for _ in range(t):
    n, m = sorted(int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    # MAX  MIN1 ...
    # MIN2 ...
    # ...
    # OR
    # MIN  MAX1 ...
    # MAX2 ...
    # ...
    res = max(
        (n - 1) * (a[-1] - a[1]) + n * (m - 1) * (a[-1] - a[0]),
        (n - 1) * (a[-2] - a[0]) + n * (m - 1) * (a[-1] - a[0]),
    )
    print(res)
