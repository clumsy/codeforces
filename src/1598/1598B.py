from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    cnt = defaultdict(set)
    for i in range(n):
        con = (int(c) for c in input().split())
        for k, e in enumerate(con):
            if e > 0:
                cnt[1 << k].add(i)
    res = "NO"
    for i in range(5):
        for j in range(i + 1, 5):
            oi = len(cnt[1 << i] - cnt[1 << j])
            oj = len(cnt[1 << j] - cnt[1 << i])
            ij = len(cnt[1 << i] & cnt[1 << j])
            if ij >= max(0, n // 2 - oi) + max(0, n // 2 - oj):
                res = "YES"
                break
    print(res)
