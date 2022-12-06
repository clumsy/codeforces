from collections import defaultdict

n = int(input())
h, g = defaultdict(int), defaultdict(int)
for _ in range(n):
    hi, gi = (int(i) for i in input().split())
    h[hi] += 1
    g[gi] += 1
res = sum(h[hi] * g[hi] for hi in h)
print(res)
