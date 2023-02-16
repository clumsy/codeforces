t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    lo, hi = 0, n - 1
    while lo < hi:
        if s[lo] == s[hi]:
            break
        lo += 1
        hi -= 1
    res = hi - lo + 1
    print(res)
