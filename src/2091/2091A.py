from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (i for i in input().split())
    cnt = Counter("01032025")
    res, k = 0, len(cnt)
    for i, e in enumerate(a):
        cnt[e] -= 1
        k -= cnt[e] == 0
        if k == 0:
            res = i + 1
            break
    print(res)
