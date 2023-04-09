from math import inf

n, a = int(input()), (int(i) for i in input().split())
res, min_odd = 0, inf
for i in a:
    res += i
    if i & 1 == 1:
        min_odd = min(min_odd, i)
res = res if res & 1 == 0 else res - min_odd
print(res)
