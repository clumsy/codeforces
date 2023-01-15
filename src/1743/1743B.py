t = int(input())
for _ in range(t):
    n = int(input())
    res = list(range(1, n + 1))
    res[1], res[n - 1] = res[n - 1], res[1]
    print(*res)
