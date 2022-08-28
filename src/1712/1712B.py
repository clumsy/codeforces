t = int(input())
for _ in range(t):
    n = int(input())
    res = [1] * n
    for i in range(n, 1, -2):
        res[i - 2 : i] = i, i - 1
    print(*res)
