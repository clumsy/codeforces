t = int(input())
for _ in range(t):
    a, b, n = (int(i) for i in input().split())
    # 5 4
    # 5 45
    # 554 45
    # 554 44555
    # 55555444 44555
    # 55555444 44444455555555
    # hence min * Fib(n-1) + max * Fib(n) > n
    a, b = min(a, b), max(a, b)
    f1, f2, res = 0, 1, 0
    while a * f1 + b * f2 <= n:
        f1, f2 = f2, f1 + f2
        res += 1
    print(res)
