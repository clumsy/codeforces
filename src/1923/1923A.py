t = int(input())
for _ in range(t):
    n, s = int(input()), [int(i) for i in input().split()]
    lo, hi = 0, n - 1
    while lo < hi and s[lo] == 0:
        lo += 1
    while lo < hi and s[hi] == 0:
        hi -= 1
    res = sum(s[i] == 0 for i in range(lo, hi + 1))
    print(res)
