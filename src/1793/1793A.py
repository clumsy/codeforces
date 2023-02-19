t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    n, m = (int(i) for i in input().split())
    x = n // (m + 1)
    x = x * m * a + max(0, n - x * (m + 1)) * min(a, b)
    res = min(b * n, x)
    print(res)
