t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res, v = [0] * n, 1
    for i in range(k - 1, n, k):
        res[i] = v
        v += 1
    for i in range(n):
        res[i] = res[i] or v
        v += v == res[i]
    print(*res)
