from collections import Counter

t = int(input())
for _ in range(t):
    cnt = Counter(input())
    res = sum(v > 1 for v in cnt.values()) + sum(v == 1 for v in cnt.values()) // 2
    print(res)
