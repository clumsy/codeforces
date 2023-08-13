t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    k = max(k, k * (n + k - 1) // k)
    res = (k + n - 1) // n
    print(res)
