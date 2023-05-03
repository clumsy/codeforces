from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
cnt = Counter(a)
res = min(cnt[1] + cnt[2], cnt[2] + cnt[3], cnt[1] + cnt[3])
print(res)
