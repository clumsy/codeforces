t = int(input())
for _ in range(t):
    k, n = (int(i) for i in input().split())
    res = [None] * k
    for i in range(k):
        res[i] = 1 if i == 0 else min(n - (k - i - 1), res[i - 1] + i)
    print(*res)
