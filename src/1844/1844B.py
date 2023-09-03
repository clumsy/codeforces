t = int(input())
for _ in range(t):
    n = int(input())
    res = list(range(1, n + 1))
    if n > 2:
        res[2], res[-1] = res[-1], res[2]
    res[0], res[(n - 1) // 2] = res[(n - 1) // 2], res[0]
    if (n - 1) // 2 > 1:
        res[0], res[1] = res[1], res[0]
    print(*res)
