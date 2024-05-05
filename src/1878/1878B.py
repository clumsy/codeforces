t = int(input())
for _ in range(t):
    n = int(input())
    res = list(range(1, 2 * n + 1, 2))
    print(*res)
