t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    lo, hi = 0, n - 1
    while lo < hi and s[lo] == s[hi]:
        lo += 1
        hi -= 1
    res = "YES"
    if lo != hi:
        while lo < hi and s[lo] != s[hi]:
            lo += 1
            hi -= 1
        while lo < hi and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        if lo < hi:
            res = "NO"
    print(res)
