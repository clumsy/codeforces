from collections import Counter

n, k = (int(i) for i in input().split())
s = input()
c = Counter(s)
res = min(c.values()) * k if len(c) == k else 0
print(res)
