from math import inf

n, a = int(input()), (int(i) for i in input().split())
res = inf
for i in a:
    res = min(res, abs(i))
print(res)
