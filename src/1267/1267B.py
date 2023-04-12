s = input()
n = len(s)
lo, hi = 0, n - 1
res = 0
while lo < hi:
    if s[lo] != s[hi]:
        break
    i = j = 0
    while lo + i + 1 <= hi and s[lo] == s[lo + i + 1]:
        i += 1
    while hi - j - 1 >= lo and s[hi] == s[hi - j - 1]:
        j += 1
    if lo + i >= hi - j:
        res = hi - lo + 2
    elif i + j + 2 < 3:
        break
    lo += i + 1
    hi -= j + 1
print(res)
