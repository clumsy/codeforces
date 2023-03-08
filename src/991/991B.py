from collections import Counter
from math import ceil

n, a = int(input()), Counter(int(i) for i in input().split())

need = ceil(4.5 * n)
have = sum(k * v for k, v in a.items())

res = 0
for i in [2, 3, 4]:
    if have >= need:
        break
    delta = 5 - i
    res += min(a[i], (need - have + delta - 1) // delta)
    have += delta * a[i]

print(res)
