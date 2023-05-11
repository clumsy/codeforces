from math import log2, ceil, floor

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = 0
    for i in range(n - 2, -1, -1):
        # a[i]/2**x < a[i+1] => 2**x > a[i] / a[i + 1] => x > log2(a[i]/a[i + 1])
        if a[i] < a[i + 1]:
            continue
        if a[i + 1] == 0:
            res = -1
            break
        x = log2(a[i] / a[i + 1])
        x = floor(x + 1) if x == ceil(x) else ceil(x)
        a[i] >>= x
        if a[i] >= a[i + 1]:
            res = -1
            break
        res += x
    print(res)
