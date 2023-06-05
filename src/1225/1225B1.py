from collections import Counter

t = int(input())
for _ in range(t):
    n, k, d = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res, cnt = k, Counter()
    for i, e in enumerate(a):
        if i >= d:
            prev = a[i - d]
            cnt[prev] -= 1
            if cnt[prev] == 0:
                del cnt[prev]
        cnt[e] += 1
        if i + 1 >= d:
            res = min(res, len(cnt))
    print(res)
