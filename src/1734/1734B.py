t = int(input())
for _ in range(t):
    n = int(input())
    for k in range(1, n + 1):
        res = [0] * k
        res[0] = res[-1] = 1
        print(*res)
