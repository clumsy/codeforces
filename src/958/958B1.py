from collections import Counter

n = int(input())
cnt = Counter()
for _ in range(n - 1):
    a, b = (int(i) for i in input().split())
    cnt[a] += 1
    cnt[b] += 1
res = sum(v == 1 for v in cnt.values())
print(res)
