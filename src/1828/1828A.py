t = int(input())
for _ in range(t):
    n = int(input())
    # n - sum(a[1:]) % n, 2, 3, ...
    res = [n - ((2 + n) * (n - 1) // 2) % n] + [i for i in range(2, n + 1)]
    print(*res)
