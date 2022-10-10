t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    lo, hi, res = 0, n - 1, None
    while lo < hi:
        if s[lo] != "a":
            res = s[: hi + 1] + "a" + s[hi + 1 :]
            break
        if s[hi] != "a":
            res = s[:lo] + "a" + s[lo:]
            break
        lo += 1
        hi -= 1
    if lo == hi and s[lo] != "a":
        res = s + "a"
    if res:
        print("YES")
        print(res)
    else:
        print("NO")
