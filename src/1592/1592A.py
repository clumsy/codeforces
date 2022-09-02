from functools import lru_cache
from heapq import heappush, heappop


@lru_cache
def solve(first, second):
    n, H = (int(i) for i in first.split())
    a = (int(i) for i in second.split())
    m = []
    for i in a:
        heappush(m, i)
        if len(m) > 2:
            heappop(m)
    # m1*x + m2*y >= H, x >= y
    # x = y = p => p >= H / (m1 + m2)
    p, r = divmod(H, sum(m))
    return 2 * p + (2 if r > m[1] else 1 if r > 0 else 0)


t = int(input())
for _ in range(t):
    res = solve(input(), input())
    print(res)
