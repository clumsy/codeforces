from collections import defaultdict
from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    b = defaultdict(lambda: inf)
    for _ in range(n):
        m, s = input().split()
        b[s] = min(b[s], int(m))
    res = min(b["01"] + b["10"], b["11"])
    res = res if res != inf else -1
    print(res)
