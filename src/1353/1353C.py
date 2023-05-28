t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for i in range(3, n + 1, 2):
        res += 4 * (i - 1) * (i // 2)
    print(res)
