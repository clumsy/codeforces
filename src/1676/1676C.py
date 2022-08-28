t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [input() for s in range(n)]

    def dist(a, b):
        d = 0
        for i in range(m):
            d += abs(ord(a[i]) - ord(b[i]))
        return d

    res = m * 30
    for i in range(n):
        for j in range(n)[i + 1 :]:
            res = min(res, dist(a[i], a[j]))
    print(res)
