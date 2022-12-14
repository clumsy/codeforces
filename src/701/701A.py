n, a = int(input()), [int(i) for i in input().split()]
k = sorted(range(n), key=lambda i: a[i])
lo, hi = 0, n - 1
while lo < hi:
    res = k[lo] + 1, k[hi] + 1
    lo += 1
    hi -= 1
    print(*res)
