t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = 0 if n == m == 1 else min(n, m) + (n - 1 + m - 1)
    print(res)
