t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    ttl = 4 * n - 2
    res = min(k + 1, ttl - 2) // 2 + max(k - (ttl - 2), 0)
    print(res)
