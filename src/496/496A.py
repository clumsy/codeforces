from math import inf

n, a = int(input()), [int(i) for i in input().split()]
res, left = inf, 0
for i in range(1, n - 1):
    cur = max(left, a[i + 1] - a[i - 1])
    for j in range(i + 1, n - 1):
        cur = max(cur, a[j + 1] - a[j])
    res = min(res, cur)
    left = max(left, a[i] - a[i - 1])
print(res)
