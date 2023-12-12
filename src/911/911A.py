from math import inf

n = int(input())
a = [int(i) for i in input().split()]
res, mi = inf, 0
for i in range(1, n):
    if a[i] == a[mi]:
        res = min(res, i - mi)
        mi = i
    if a[i] < a[mi]:
        res, mi = inf, i
print(res)
