t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    lo, hi = 0, n - 1
    low, hih = [], []
    while lo < hi:
        while lo < hi and s[lo] == "0":
            lo += 1
        while hi > lo and s[hi] == "1":
            hi -= 1
        if lo >= hi:
            break
        low.append(lo + 1)
        hih.append(hi + 1)
        lo += 1
        hi -= 1
    res = low + hih[::-1]
    print(1 if res else 0)
    if res:
        print(len(res), *res)
