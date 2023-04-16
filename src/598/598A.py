from math import floor, log2

t = int(input())
for _ in range(t):
    n = int(input())
    pow2 = floor(log2(n)) + 1
    # sum from 1 to n, then first remove pow2 using geometric series
    # then subtract using the same series
    res = (1 + n) * n // 2 - 2 * (2**pow2 - 1)
    print(res)
