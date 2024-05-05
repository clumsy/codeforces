from math import sqrt, floor

t = int(input())
for _ in range(t):
    n, k, x = (int(i) for i in input().split())
    # (k + 1)k=2x
    # k^2 + k - 2x = 0
    # D = 1 + 8x
    # k = (sqrt(D) - 1)/2
    k_ = floor((sqrt(1 + 8 * x) - 1) / 2)
    res = "YES" if n >= k <= k_ and ((n - k + 1 + n) * k) // 2 >= x else "NO"
    print(res)
