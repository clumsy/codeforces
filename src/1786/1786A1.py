from math import sqrt, floor

t = int(input())
for _ in range(t):
    n = int(input())
    # (1 + 1 + 8x - 8)*x/2 + (5 + 5 + 8x - 8)*x/2 = n =>
    # 2n = -6x + 8x^2 + 2x + 8x^2 =>
    # 16x^2 - 4x - 2n = 0
    # D = 4 + 32n
    # x = (2 + sqrt(4 + 32n)) / 16
    x = floor(2 + sqrt(4 + 32 * n)) // 16
    a, b = (1 + 1 + 8 * x - 8) * x // 2, (5 + 5 + 8 * x - 8) * x // 2
    n -= a + b
    while n:
        nxt = min(n, 1 + 8 * x)
        a += nxt
        n -= nxt
        if not n:
            break
        nxt = min(n, 5 + 8 * x)
        b += nxt
        n -= nxt
        x += 1
    print(a, b)
