from math import inf
from collections import Counter


t = int(input())
for _ in range(t):
    n, c, d = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    cnt, mi = Counter(), inf
    for i in a:
        cnt[i] += 1
        mi = min(mi, i)
    for _ in range(n):
        cur = mi
        for _ in range(n):
            cnt[cur] -= 1
            cur += c
        mi += d
    res = "YES" if all(v == 0 for v in cnt.values()) else "NO"
    print(res)
