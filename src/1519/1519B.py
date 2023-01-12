t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    # m - 1 + (n - 1) * m = n * m - 1
    # n - 1 + (m - 1) * n = n * m - 1
    res = "YES" if n * m - 1 == k else "NO"
    print(res)
