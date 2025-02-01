t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    x = [int(i) for i in input().split()]
    lo, hi = 0, n - 1
    while lo < hi:
        if x[lo] >= k:
            x[lo], x[hi] = x[hi], x[lo]
            hi -= 1
        else:
            lo += 1
    x = sorted(x[: hi + 1])
    lo = res = 0
    hi = len(x) - 1
    while lo < hi:
        diff = k - (x[lo] + x[hi])
        if diff == 0:
            res += 1
            lo += 1
            hi -= 1
        elif diff > 0:
            lo += 1
        else:
            hi -= 1
    print(res)
