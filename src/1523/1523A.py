t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    s = [int(i) for i in input()]
    le, ri, res = 0, 0, s
    while ri < n:
        while ri < n - 1 and res[ri] == 0:
            ri += 1
        lo, hi, rem = le, ri, min(m, n)
        while rem > 0 and (hi - lo > 2 or res[lo] == 0 or res[hi] == 0):
            if res[lo] == 1:
                res[lo + 1] = 1
                lo += 1
            if res[hi] == 1:
                res[hi - 1] = 1
                hi -= 1
            rem -= 1
        le, ri = ri, ri + 1
    res = "".join(str(i) for i in res)
    print(res)
