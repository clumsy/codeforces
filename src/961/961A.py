from collections import Counter

n, m = (int(i) for i in input().split())
a = Counter(int(i) for i in input().split())
res = min(a.get(i, 0) for i in range(1, n + 1))
print(res)
