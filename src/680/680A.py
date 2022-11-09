from collections import Counter

t = Counter(int(i) for i in input().split())
s = sum(k * v for k, v in t.items())
res = s
for e in reversed(sorted(t.keys())):
    if t[e] >= 2:
        res = min(res, s - min(3, t[e]) * e)
print(res)
