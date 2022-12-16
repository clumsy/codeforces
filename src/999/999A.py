n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res, lo, hi = 0, 0, n - 1
while lo <= hi:
    if a[lo] <= k:
        res += 1
        lo += 1
    elif a[hi] <= k:
        res += 1
        hi -= 1
    else:
        break
print(res)
