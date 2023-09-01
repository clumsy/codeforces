t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    if a[0] == a[-1]:
        res = "YES" if a.count(a[0]) >= k else "NO"
    else:
        res = "NO"
        lo = k
        for i in range(n):
            lo -= a[i] == a[0]
            if not lo:
                break
        lo, hi = i, k
        for i in reversed(range(n)):
            hi -= a[i] == a[-1]
            if not hi:
                break
        hi = i
        res = "YES" if lo < hi else "NO"
    print(res)
