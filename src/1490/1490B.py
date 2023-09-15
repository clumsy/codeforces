from collections import Counter

M = 3
t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(i % M for i in a)
    c = [cnt[i] for i in range(0, M)]
    k, res = n // M, 0
    for i in range(-M, M):
        d = max(0, c[i] - k)
        res += d
        if i + 1 < M:
            c[i + 1] += d
        c[i] -= d
    print(res)
