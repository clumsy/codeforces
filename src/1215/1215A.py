a1, a2, k1, k2, n = (int(input()) for _ in range(5))
if k1 > k2:
    a1, k1, a2, k2 = a2, k2, a1, k1
ma = min(a1, n // k1)
n1 = n - ma * k1
ma += min(a2, n1 // k2)
mi = max(0, n - a1 * (k1 - 1) - a2 * (k2 - 1))
res = mi, ma
print(*res)
