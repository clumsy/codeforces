t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    s = next(a)
    m = max(a, default=s)
    # by pigeon-hole principle
    res = "YES" if m - s <= n + 1 else "NO"
    print(res)
