t = int(input())
for _ in range(t):
    n = int(input())
    res = 4 * n + 1 + n - 1 + 2 * (1 + n - 2) * (n - 2) // 2
    print(res)
