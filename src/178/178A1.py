from math import log2, floor

n, a = int(input()), [int(i) for i in input().split()]
res = [0] * (n - 1)
for k in range(n - 1):
    if k > 0:
        res[k] += res[k - 1]
    res[k] += a[k]
    p = floor(log2(n - 1 - k))
    a[k + 2**p] += a[k]
print(*res, sep="\n")
