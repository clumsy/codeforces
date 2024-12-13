t = int(input())
for _ in range(t):
    n = int(input())
    dp = [float("inf")] * 5
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i % 5] = min(dp[(i - 1) % 5] + 1, dp[(i - 3) % 5], dp[(i - 5) % 5])
    res = dp[n % 5]
    print(res)
