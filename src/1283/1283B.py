t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = k * (n // k)
    res = res + min(k // 2, n - res)
    print(res)
