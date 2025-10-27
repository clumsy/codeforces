t = int(input())
for _ in range(t):
    n = int(input())

    # Solution 1
    # u, d, res = n, 0, 1  # (final game)
    # while u > 1 or d > 1:
    #     res += u // 2 + d // 2
    #     d += u // 2 - d // 2
    #     u -= u // 2

    # Solution 2
    res = 2 * n - 2

    print(res)
