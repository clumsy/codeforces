from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
res = max(Counter(a).values())
print(res)
