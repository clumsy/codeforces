t = int(input())
for _ in range(t):
    n, k, b, s = (int(i) for i in input().split())
    a = k * b  # sum of all n elements
    ma = a + k - 1  # max element we can have
    if s > ma + (n - 1) * (k - 1) or s < a:
        res = [-1]
    else:
        res = [0] * n
        res[0], i = min(s, a + k - 1), 1
        s -= res[0]
        while s:
            res[i] = min(s, k - 1)
            s -= res[i]
            i += 1
    print(*res)
