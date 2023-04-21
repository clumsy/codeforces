from collections import Counter

k = int(input())
cnt = Counter()
for _ in range(4):
    cnt.update(input())
del cnt["."]
res = "YES" if all(v <= 2 * k for _, v in cnt.most_common()) else "NO"
print(res)
