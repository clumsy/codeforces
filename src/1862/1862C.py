t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    if n != a[-1]:
        res = "NO"
    else:
        res = "YES"
        lo, hi = 0, n - 1
        while lo < n:
            k = 1
            while lo + k < n and a[lo] == a[lo + k]:
                k += 1
            p = 1
            while hi - p >= 0 and a[hi] == a[hi - p]:
                p += 1
            if (
                a[hi] - (a[hi - p] if hi - p >= 0 else 0) != k
                or a[lo] - (a[lo - 1] if lo else 0) != p
            ):
                res = "NO"
                break
            lo += k
            hi -= p
    print(res)
