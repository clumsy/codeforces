from collections import Counter

n = int(input())
cnt = Counter(input()[0] for _ in range(n))
res = 0
for v in cnt.values():
    res += sum(c * (c - 1) // 2 for c in (v // 2, v - v // 2))
print(res)
