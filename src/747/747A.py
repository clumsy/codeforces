from math import sqrt, floor

n = int(input())
for i in reversed(range(1, floor(sqrt(n)) + 1)):
    if i * (n // i) == n:
        res = i, n // i
        break
print(*res)
