from math import sqrt

n, m = (int(i) for i in input().split())
nxt = None
for i in range(n + 1, m + 1):
    if all(i % j != 0 for j in range(2, int(sqrt(i)) + 1)):
        nxt = i
        break
res = "YES" if nxt == m else "NO"
print(res)
