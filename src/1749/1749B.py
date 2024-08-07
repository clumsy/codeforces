t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    lo, hi = 0, n - 1
    res = 0
    while lo <= hi:
        if b[lo] < b[hi]:
            res += a[lo] + (b[lo] if lo != hi else 0)
            lo += 1
        else:
            res += a[hi] + (b[hi] if lo != hi else 0)
            hi -= 1
    print(res)
