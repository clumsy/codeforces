n, a = (int(i) for i in input().split())
t = [int(i) for i in input().split()]
res, lo, hi = 0, a - 1, a - 1
while lo >= 0 or hi < n:
    if lo >= 0 and hi < n:
        res += 1 + (lo != hi) if t[lo] == t[hi] == 1 else 0
        lo, hi = lo - 1, hi + 1
    elif lo >= 0:
        res += t[lo] == 1
        lo -= 1
    else:
        res += t[hi] == 1
        hi += 1
print(res)
