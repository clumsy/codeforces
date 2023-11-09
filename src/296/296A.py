from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
res, cnt = None, Counter()
for i in a:
    cnt[i] += 1
    if not res or cnt[i] > cnt[res]:
        res = i
res = "YES" if cnt[res] <= (n + 1) // 2 else "NO"
print(res)
