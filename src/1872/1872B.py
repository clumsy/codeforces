from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    res = inf
    for _ in range(n):
        d, s = (int(i) for i in input().split())
        # 2k + 1 = s
        res = min(res, d + max(0, (s - 1) // 2))
    print(res)
