n, a = int(input()), input()
res, lo, hi = 0, 0, n - 1
while lo < n and a[lo] == "<":
    res += 1
    lo += 1
while hi >= 0 and a[hi] == ">":
    res += 1
    hi -= 1
print(res)
