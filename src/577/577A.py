from math import sqrt, floor

n, x = (int(i) for i in input().split())
res = sum(
    1 if x == i**2 else 2 if x % i == 0 and x // i <= n else 0
    for i in range(1, min(n, floor(sqrt(x))) + 1)
)
print(res)
