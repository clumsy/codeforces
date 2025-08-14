t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(int(i) for i in input().split())
    res = min(
        next((i for i in range(n - 1) if (a[i] & 1) == (a[-1] & 1)), n - 1),
        next((n - 1 - i for i in reversed(range(n)) if (a[i] & 1) == (a[0] & 1)), n - 1)
    )
    print(res)
