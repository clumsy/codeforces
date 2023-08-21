from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    res = "YES" if cnt[0] == cnt.most_common()[0][1] else "NO"
    for i in cnt.keys():
        if i > 0 and cnt[i] > cnt[i - 1]:
            res = "NO"
            break
    print(res)
