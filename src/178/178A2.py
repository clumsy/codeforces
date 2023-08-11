from math import log2, floor

n, a = int(input()), [int(i) for i in input().split()]
res = 0
for k in range(n - 1):
    p = floor(log2(n - 1 - k))
    res += a[k]
    a[k + 2**p] += a[k]
    print(res)
