from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
c = Counter(i for i in a if i > 0)
res = sum(v == 2 for _, v in c.items())
res = res if all(v <= 2 for _, v in c.items()) else -1
print(res)
