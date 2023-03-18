from collections import Counter

n, k = (int(i) for i in input().split())
u = Counter(int(i) for i in input().split())
res = 0
d = max((u[i] + k - 1) // k for i in u)
res = k * d * len(u) - n
print(res)
