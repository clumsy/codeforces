from collections import Counter

n, m = (int(i) for i in input().split())
a = Counter(int(i) for i in input().split())
res = 0
for i, cnt in a.items():
    n -= cnt
    res += cnt * n
print(res)
