from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = [Counter() for _ in range(n)]
    for _ in range(n):
        for i, e in enumerate(int(i) for i in input().split()):
            cnt[i][e] += 1
    res = [None] * n
    for i in range(n):
        res[i] = cnt[max(0, i - 1)].most_common()[0][0]
        del cnt[i][res[i]]
    print(*res)
