from collections import Counter

n, k = (int(i) for i in input().split())
cnt = Counter()
for _ in range(n):
    t = int(input())
    cnt[t] += 1
x = sum(v // 2 for v in cnt.values())
res = 2 * x + (n + 1) // 2 - x
print(res)
