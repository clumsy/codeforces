l1, r1, l2, r2, k = (int(i) for i in input().split())
r, lo = min(r1, r2), max(l1, l2)
res = max(0, r - lo + 1 - (lo <= k <= r))
print(res)
