from math import sqrt, floor

n = int(input())
s = floor(sqrt(n))
r = n - s**2
res = 4 * s + (0 if r == 0 else 2 if r <= s else 4)
print(res)
