t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    left, right = input(), input()
    p = n + m
    s = left + right[::-1]
    lo, hi = 0, p - 1
    while lo < p - 1 and s[lo] != s[lo + 1]:
        lo += 1
    while hi > 0 and s[hi] != s[hi - 1]:
        hi -= 1
    res = "YES" if hi - lo in [0, 1, -(p - 1)] else "NO"
    print(res)
