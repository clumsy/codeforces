t = int(input())
for _ in range(t):
    n = int(input())
    res = [0] * n
    for i in range(n):
        res[i] = 2 * (i + 1) - 1
    print(*res)
