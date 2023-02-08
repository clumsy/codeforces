t = int(input())
for _ in range(t):
    n = int(input())
    res = [None] * n
    mi = 1 + n // 2
    res[1::2] = range(1, mi)
    res[::2] = range(mi, n + 1)
    print(*res)
