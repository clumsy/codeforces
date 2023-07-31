from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
res, cnt = 0, Counter()
for i in a:
    cnt[i] += 1
    if cnt[i] > cnt[res]:
        res = i
print(res)
