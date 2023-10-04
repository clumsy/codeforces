t = int(input())
for _ in range(t):
    n, k, x = (int(i) for i in input().split())
    res = (
        sum(i for i in range(k)) + (x if x != k else k - 1) * (n - k)
        if k <= n and k - 1 <= x
        else -1
    )
    print(res)
