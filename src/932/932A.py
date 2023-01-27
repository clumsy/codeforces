a = input()
lo, hi = 0, len(a) - 1
while lo < hi:
    if a[lo] == a[hi]:
        hi -= 1
    lo += 1
res = a[:lo] + a[lo::-1]
print(res)
