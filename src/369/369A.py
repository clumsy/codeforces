from collections import Counter

n, m, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
cnt = Counter(a)
m -= cnt[1]
k -= cnt[2]
k += max(0, m)
res = max(-m, 0) + max(-k, 0)
print(res)
