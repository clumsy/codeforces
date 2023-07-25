from itertools import accumulate
from bisect import bisect_right

n, a, b = (int(i) for i in input().split())
s = (int(i) for i in input().split())
x, s = next(s), list(accumulate(sorted(s)))
# (a * x)/z' >= b
# a * x >= b * z'
# z' = z + x
# z <= (a * x) / b - x
z = (a * x) / b - x
res = len(s) - bisect_right(s, z)
print(res)
