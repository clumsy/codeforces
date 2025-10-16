from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(Counter(a).values())
    res, rem = 0, sum(cnt.values())
    for i in sorted(cnt.keys()):
        res = max(res, i * rem)
        rem -= cnt[i]
    print(res)
