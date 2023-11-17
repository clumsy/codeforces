from collections import Counter

n, w = int(input()), (int(i) for i in input().split())
cnt = Counter(w)
res = "NO" if cnt[100] & 1 == 1 or (cnt[200] & 1 == 1 and cnt[100] < 2) else "YES"
print(res)
