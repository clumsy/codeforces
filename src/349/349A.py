from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
res, cnt = "YES", Counter()
for i in a:
    cnt[i] += 1
    i -= 25
    for c in [50, 25]:
        d = min(cnt[c], i // c)
        i -= c * d
        cnt[c] -= d
    if i:
        res = "NO"
        break
print(res)
