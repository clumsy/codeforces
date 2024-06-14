from math import floor, sqrt


def solve(n):
    # 2, 2 * 2 + 1, 3 * 2 + 2
    # 2 * k + k - 1 = 3 * k - 1
    # (2 + 3k - 1) * k // 2 = n
    # 3k^2 + k - 2n = 0
    # D = 1 + 24n
    # k = (-1 + sqrt(D)) / 6
    k = floor((sqrt(24 * n + 1) - 1) / 6)
    return n - (3 * k + 1) * k // 2


t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    while n > 1:
        n = solve(n)
        res += 1
    print(res)
