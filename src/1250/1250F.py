from math import sqrt

n = int(input())
for a in range(int(sqrt(n)), 0, -1):
    if a * (b := n // a) == n:
        res = 2 * a + 2 * b
        break
print(res)
