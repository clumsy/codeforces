# 55157581939688863366
# 54943329752812629795

# 550
# 549
t = int(input())
for _ in range(t):
    L, R = input().split()
    L = "0" * (len(R) - len(L)) + L
    res = lo = hi = L_ = R_ = 0
    for ll, r in zip(L, R):
        ll, r = (int(i) for i in (ll, r))
        _r, r_ = ll if lo == R_ else 0, r if hi == R_ else 9
        _l, l_ = ll if lo == L_ else 0, r if lo == R_ else 9
        d1, d2 = abs(r_ - _l), abs(l_ - _r)
        if d1 >= d2:
            L_ = 10 * L_ + _l
            R_ = 10 * R_ + r_
            res += d1
        else:
            L_ = 10 * L_ + l_
            R_ = 10 * R_ + _r
            res += d2
        lo, hi = 10 * lo + ll, 10 * hi + r
    print(res)
