MOD = int(1e9 + 7)
t = int(input())
for _ in range(t):
    n = int(input())
    # 1 2 | 2 1
    #   1   1   = 4
    # 2 1 | 1 2
    # 2         = 4
    #
    # 1 2 3 | 3 2 1
    #   1 2   2 1   = 6
    # 1 3 2 | 2 3 1
    #   3 1   1 1   = 6
    # 3 1 2 | 2 1 3
    # 4   1   1     = 6
    # 3 2 1 | 1 2 3
    # 4 2           = 6
    # 2 1 3 | 3 1 2
    # 2   2   2     = 6
    # 2 3 1 | 1 3 2
    # 2 3       1   = 6
    #
    # 1 3 4 2 5 | 5 2 4 3 1
    #   3 4 1 4   4 1 2 1   = 20
    #
    # 1 2 5 3 4 | 4 3 5 2 1
    #   1 6 2 3   3 2 2 1   = 20
    #
    # We see the beauty is the SAME for every permutation
    # So for n n-1 ... 1 | 1 2 ... n we get:
    # 2*(n - 1) + 2*(n - 2) ... + 2*0 | 0 ... 0
    res = 0
    for i in range(1, n):
        res += 2 * i
    while n > 1:
        res = (res * n) % MOD
        n -= 1
    print(res)
