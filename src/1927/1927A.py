t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    lo, hi = 0, n - 1
    while lo < hi and s[lo] == "W":
        lo += 1
    while hi > lo and s[hi] == "W":
        hi -= 1
    res = hi - lo + 1
    print(res)
