t = int(input())
for _ in range(t):
    n = int(input())
    res = (i for i in range(2 * n, 4 * n, 2))
    print(*res)
