s = input()
lo, hi = 0, len(s) - 1
res = "NA"
while lo < hi:
    if s[lo] != s[hi]:
        half = (len(s) + 1) // 2
        res = s[:lo] + s[hi] + s[lo:]
        if res[:half] == res[-half:][::-1]:
            break
        res = s[: hi + 1] + s[lo] + s[hi + 1 :]
        if res[:half] == res[-half:][::-1]:
            break
        res = "NA"
        break
    lo += 1
    hi -= 1
if res == "NA" and lo >= hi:
    half = len(s) // 2
    res = s[:half] + s[half] + s[half:]
print(res)
