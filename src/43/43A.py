from collections import Counter

n = int(input())
cnt = Counter()
for _ in range(n):
    cnt[input()] += 1
res = cnt.most_common()[0][0]
print(res)
