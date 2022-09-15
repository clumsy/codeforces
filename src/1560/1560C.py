from math import sqrt, floor

t = int(input())
for _ in range(t):
    k = int(input())
    prev = floor(sqrt(k))
    if k == prev**2:
        r, c = prev, 1
    else:
        n, i = (prev + 1) ** 2 - prev**2, k - prev**2
        r, c = (prev + 1, n - i + 1) if i > prev else (i, prev + 1)
    print(r, c)
