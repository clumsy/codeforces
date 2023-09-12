from collections import Counter

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    res, cnt = 0, Counter(s)
    for c in list(cnt.keys()):
        C = c.upper() if c.islower() else c.lower()
        # existing pairs
        d = min(cnt[c], cnt[C])
        res += d
        cnt[c] -= d
        cnt[C] -= d
        # grouping in pairs
        for i in (c, C):
            d_ = min(k, cnt[i] // 2)
            k -= d_
            res += d_
            cnt[i] -= 2 * d_
    print(res)
