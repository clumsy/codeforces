from math import inf

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    mi = [inf] * 2
    for i in a:
        mi[i & 1] = min(mi[i & 1], i) if mi[i & 1] is not None else i
    res = "YES" if all(i & 1 == min(mi) & 1 or i - mi[1] > 0 for i in a) else "NO"
    print(res)
