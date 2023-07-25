from math import inf
from bisect import insort, bisect_right

n, s = int(input()), input()
x = (int(i) for i in input().split())
left, right = [], []
for i, d in zip(x, s):
    insort(left if d == "L" else right, i)
res = inf
for k in left:
    i = bisect_right(right, k)
    if i > 0:
        res = min(res, (k - right[i - 1]) // 2)
res = -1 if res == inf else res
print(res)
