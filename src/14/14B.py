from math import inf

n, x0 = (int(i) for i in input().split())
a0, b0 = -inf, inf
for _ in range(n):
    a, b = sorted(int(i) for i in input().split())
    a0, b0 = max(a0, a), min(b0, b)
res = -1 if b0 < a0 else 0 if a0 <= x0 <= b0 else min(abs(a0 - x0), abs(b0 - x0))
print(res)
