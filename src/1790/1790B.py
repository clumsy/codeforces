t = int(input())
for _ in range(t):
    n, s, r = (int(i) for i in input().split())
    res = [1] * n
    i = n - 1
    res[i] = s - r
    s -= sum(res)
    while s > 0 and i > 0:
        i -= 1
        diff = min(s, res[n - 1] - res[i])
        res[i] += diff
        s -= diff
    print(*res)
