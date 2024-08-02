t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1 == 0:
        res = [-1]
    else:
        res = [-1] * n
        for i in range((n + 1) // 2):
            res[n // 2 - i] = 2 * i
            res[n // 2 + i] = 2 * i + 1
    print(*res)
