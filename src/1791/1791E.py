from math import inf


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    dp = [[a[0], -inf] for _ in range(2)]
    for i in range(1, n):
        dp[i & 1][0] = max(dp[(i - 1) & 1]) + a[i]
        dp[i & 1][1] = (
            max(dp[(i - 1) & 1][0] - 2 * a[i - 1], dp[(i - 1) & 1][1] + 2 * a[i - 1])
            - a[i]
        )
    res = max(dp[(n - 1) & 1])
    print(res)
