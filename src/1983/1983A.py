t = int(input())
for _ in range(t):
    n = int(input())
    res = [0] * n
    for i in reversed(range(n)):
        res[i] = sum(res[j] for j in range(i, n, i + 1))
        res[i] = (i + 1) - (res[i] % (i + 1))
    print(*res)
