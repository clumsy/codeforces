t = int(input())
for _ in range(t):
    n = int(input())
    mi = 1 + (n + 1) // 2
    # any permutation is good
    res = [None] * n
    res[::2] = range(1, mi)
    res[1::2] = range(mi, n + 1)
    print(*res)
